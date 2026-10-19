/* RINA Marine Surveyor FAT — Leonardo TEST & RINA Rules 2026 Offline PWA */

const state = {
  equipmentList: [],
  rulesIndex: [],
  rulesFull: null, // Loaded from rina-rules-2026-sections.json
  rulesLoading: false,
  selectedEquipmentId: 'transformers-essential',
  selectedCategory: 'all',
  searchQuery: '',
  langMode: 'both', // 'both' | 'en' | 'tr'
  stepFilterMode: 'dynamic', // 'dynamic' | 'all'
  answers: {}, // { [equipId]: { [questionId]: value } }
  checklist: {}, // { [equipId]: { [stepNum]: { status: 'ok'|'fail'|'na'|'pending', note: '' } } }
  meta: {
    factory: '',
    project: '',
    serial: '',
    typeSerial: '',
    surveyor: ''
  },
  savedInspections: [],
  activeRuleSectionId: 'Pt C, Ch 2, Sec 5',
  deferredInstallPrompt: null
};

const STORAGE_KEYS = {
  STATE: 'rina_fat_pwa_active_state_v1',
  SAVED: 'rina_fat_pwa_saved_inspections_v1'
};

document.addEventListener('DOMContentLoaded', async () => {
  loadPersistedState();
  bindNavigationAndToolbar();
  setupPwaAndOfflineHandlers();
  await loadDatabases();
});

function loadPersistedState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.STATE);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed.selectedEquipmentId) state.selectedEquipmentId = parsed.selectedEquipmentId;
      if (parsed.langMode) state.langMode = parsed.langMode;
      if (parsed.stepFilterMode) state.stepFilterMode = parsed.stepFilterMode;
      if (parsed.answers) state.answers = parsed.answers;
      if (parsed.checklist) state.checklist = parsed.checklist;
      if (parsed.meta) state.meta = { ...state.meta, ...parsed.meta };
    }
    const savedRaw = localStorage.getItem(STORAGE_KEYS.SAVED);
    if (savedRaw) {
      state.savedInspections = JSON.parse(savedRaw) || [];
    }
  } catch (e) {
    console.warn('State restore warning:', e);
  }
  syncMetaInputs();
  updateSavedCountBadge();
}

function persistState() {
  try {
    localStorage.setItem(
      STORAGE_KEYS.STATE,
      JSON.stringify({
        selectedEquipmentId: state.selectedEquipmentId,
        langMode: state.langMode,
        stepFilterMode: state.stepFilterMode,
        answers: state.answers,
        checklist: state.checklist,
        meta: state.meta
      })
    );
  } catch (e) {
    console.warn('State persist warning:', e);
  }
}

async function loadDatabases() {
  try {
    const [eqRes, idxRes] = await Promise.all([
      fetch('/data/equipment-fat-db.json'),
      fetch('/data/rina-rules-index.json')
    ]);
    state.equipmentList = await eqRes.json();
    state.rulesIndex = await idxRes.json();

    // Initialize default answers for each equipment if not set
    for (const eq of state.equipmentList) {
      if (!state.answers[eq.id]) {
        state.answers[eq.id] = {};
      }
      for (const q of eq.applicationTerms || []) {
        if (state.answers[eq.id][q.id] === undefined) {
          state.answers[eq.id][q.id] = q.default;
        }
      }
    }

    renderEquipmentGrid();
    renderLeonardoSheet();
    renderRulesSidebar();
    renderSavedInspections();

    // Preload full 2026 RINA PDF sections in background for instant offline rule lookup
    ensureFullRulesLoaded();
  } catch (err) {
    console.error('Error loading databases:', err);
    showToast('Veritabanı yüklenirken hata oluştu.');
  }
}

async function ensureFullRulesLoaded() {
  if (state.rulesFull) return state.rulesFull;
  if (state.rulesLoading) {
    while (state.rulesLoading) {
      await new Promise((r) => setTimeout(r, 80));
    }
    return state.rulesFull;
  }
  state.rulesLoading = true;
  try {
    const res = await fetch('/data/rina-rules-2026-sections.json');
    state.rulesFull = await res.json();
    renderSelectedRuleSectionInTab(state.activeRuleSectionId);
  } catch (e) {
    console.warn('Full rules load error:', e);
  } finally {
    state.rulesLoading = false;
  }
  return state.rulesFull;
}

/* =====================================================
   EQUIPMENT GRID & SEARCH
   ===================================================== */
function getFilteredEquipment() {
  const q = state.searchQuery.trim().toLowerCase();
  return state.equipmentList.filter((item) => {
    if (state.selectedCategory !== 'all' && item.category !== state.selectedCategory) {
      return false;
    }
    if (!q) return true;
    const haystack = [
      item.code,
      item.titleEn,
      item.titleTr,
      item.ruleRef,
      item.sectionId,
      ...(item.keywords || []),
      ...(item.certificationActivities || []).map((a) => `${a.titleEn} ${a.titleTr} ${a.detailTr}`)
    ]
      .join(' ')
      .toLowerCase();
    return q.split(/\s+/).every((word) => haystack.includes(word));
  });
}

function renderEquipmentGrid() {
  const grid = document.getElementById('equipmentGrid');
  const filtered = getFilteredEquipment();

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 1rem; text-align: center; color: #64748b;">
        Aramanızla eşleşen ekipman bulunamadı. Tüm 2026 PDF kuralları içinde aramak için üstten <strong>"📖 RINA 2026 PDF Kuralları"</strong> sekmesine geçebilirsiniz.
      </div>
    `;
    return;
  }

  // If current selected equipment is not in filtered results and user typed a search query, auto-select first match
  if (state.searchQuery.trim() && !filtered.some((e) => e.id === state.selectedEquipmentId)) {
    state.selectedEquipmentId = filtered[0].id;
    renderLeonardoSheet();
  }

  grid.innerHTML = filtered
    .map((item) => {
      const isActive = item.id === state.selectedEquipmentId;
      return `
        <button type="button" class="equip-card ${isActive ? 'active' : ''}" data-eq-id="${escapeHtml(item.id)}">
          <div class="equip-card-top">
            <span class="equip-code">${escapeHtml(item.code)}</span>
            <span class="equip-rule">${escapeHtml(item.ruleRef)}</span>
          </div>
          <div class="equip-title-tr">${escapeHtml(item.titleTr)}</div>
          <div class="equip-title-en">${escapeHtml(item.titleEn)}</div>
        </button>
      `;
    })
    .join('');

  grid.querySelectorAll('.equip-card').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.selectedEquipmentId = btn.dataset.eqId;
      persistState();
      renderEquipmentGrid();
      renderLeonardoSheet();
    });
  });
}

/* =====================================================
   LEONARDO TEST SHEET RENDERER
   ===================================================== */
function getCurrentEquipment() {
  return (
    state.equipmentList.find((e) => e.id === state.selectedEquipmentId) ||
    state.equipmentList[0]
  );
}

function isStepApplicable(step, eqAnswers) {
  if (!step.condition || step.condition === 'always') return true;
  const { field, equals, notEquals } = step.condition;
  const currentVal = eqAnswers[field];
  if (equals !== undefined) return currentVal === equals;
  if (notEquals !== undefined) return currentVal !== notEquals;
  return true;
}

function renderLeonardoSheet() {
  const eq = getCurrentEquipment();
  if (!eq) return;

  const container = document.getElementById('leonardoSheet');
  const eqAnswers = state.answers[eq.id] || {};
  const eqChecklist = state.checklist[eq.id] || {};

  const showEn = state.langMode === 'both' || state.langMode === 'en';
  const showTr = state.langMode === 'both' || state.langMode === 'tr';

  const todayStr = new Date().toLocaleDateString('en-GB', {
    day: '2-digit',
    month: 'short',
    year: 'numeric'
  });

  // Metadata summary banner
  const hasMeta =
    state.meta.factory ||
    state.meta.project ||
    state.meta.serial ||
    state.meta.typeSerial ||
    state.meta.surveyor;

  const metaBannerHtml = hasMeta
    ? `
    <div class="leo-meta-summary">
      ${state.meta.factory ? `<div class="leo-meta-item"><strong>Manufacturer / Fabrika:</strong> ${escapeHtml(state.meta.factory)}</div>` : ''}
      ${state.meta.project ? `<div class="leo-meta-item"><strong>Project / Ship No:</strong> ${escapeHtml(state.meta.project)}</div>` : ''}
      ${state.meta.serial ? `<div class="leo-meta-item"><strong>Serial / Heat No:</strong> ${escapeHtml(state.meta.serial)}</div>` : ''}
      ${state.meta.typeSerial ? `<div class="leo-meta-item"><strong>Type-Tested Prototype S/N:</strong> ${escapeHtml(state.meta.typeSerial)}</div>` : ''}
      ${state.meta.surveyor ? `<div class="leo-meta-item"><strong>Attending Surveyor:</strong> ${escapeHtml(state.meta.surveyor)}</div>` : ''}
    </div>
  `
    : '';

  // Application Terms HTML
  const appTermsRows = (eq.applicationTerms || [])
    .map((q) => {
      const currentVal = eqAnswers[q.id] ?? q.default;
      const optionsHtml = q.options
        .map(
          (opt) => `
          <option value="${escapeHtml(opt.value)}" ${opt.value === currentVal ? 'selected' : ''}>
            ${escapeHtml(state.langMode === 'en' ? opt.labelEn : state.langMode === 'tr' ? opt.labelTr : `${opt.value} — ${opt.labelTr}`)}
          </option>
        `
        )
        .join('');

      return `
        <tr>
          <td style="width: 72%;">
            ${showEn ? `<div class="question-en">${escapeHtml(q.questionEn)}</div>` : ''}
            ${showTr ? `<div class="question-tr">🇹🇷 ${escapeHtml(q.questionTr)}</div>` : ''}
          </td>
          <td style="width: 28%;">
            <select class="answer-select" data-question-id="${escapeHtml(q.id)}">
              ${optionsHtml}
            </select>
          </td>
        </tr>
      `;
    })
    .join('');

  // Calculator Box HTML (if equipment has a calculator)
  const calcHtml = eq.calculator ? renderCalculatorHtml(eq) : '';

  // Reference Tables HTML
  const refTablesHtml =
    eq.referenceTables && eq.referenceTables.length > 0
      ? `
      <div class="ref-tables-wrap">
        ${eq.referenceTables
          .map(
            (tbl) => `
          <div class="ref-table-box">
            <div class="ref-table-caption">
              📊 ${showEn ? escapeHtml(tbl.titleEn) : ''} ${showEn && showTr ? ' / ' : ''} ${showTr ? escapeHtml(tbl.titleTr) : ''}
            </div>
            <table class="ref-data-table">
              <thead>
                <tr>
                  ${tbl.headers.map((h) => `<th>${escapeHtml(h)}</th>`).join('')}
                </tr>
              </thead>
              <tbody>
                ${tbl.rows
                  .map(
                    (row) => `
                  <tr>
                    ${row.map((cell) => `<td>${escapeHtml(cell)}</td>`).join('')}
                  </tr>
                `
                  )
                  .join('')}
              </tbody>
            </table>
          </div>
        `
          )
          .join('')}
      </div>
    `
      : '';

  // Acceptance Requirements HTML
  const accReqRows = (eq.acceptanceRequirements || [])
    .map(
      (r) => `
      <tr>
        <td style="width: 34%;">
          <button type="button" class="leo-rule-link js-open-rule" data-sec="${escapeHtml(r.sectionId)}" data-page="${r.page || eq.pdfPage}">
            📄 ${escapeHtml(r.ruleRef)}
          </button>
        </td>
        <td style="width: 66%;">
          ${showEn ? `<div style="font-weight: 600; color: #0f172a;">${escapeHtml(r.reqEn)}</div>` : ''}
          ${showTr ? `<div style="font-size: 0.84rem; color: #0369a1; margin-top: 0.2rem;">🇹🇷 ${escapeHtml(r.reqTr)}</div>` : ''}
        </td>
      </tr>
    `
    )
    .join('');

  // Certification Activities HTML
  const allSteps = eq.certificationActivities || [];
  const visibleSteps = allSteps.filter((step) => {
    const applicable = isStepApplicable(step, eqAnswers);
    if (state.stepFilterMode === 'dynamic') return applicable;
    return true;
  });

  let okCount = 0;
  visibleSteps.forEach((s) => {
    if (eqChecklist[s.num]?.status === 'ok') okCount++;
  });

  const certStepsHtml = visibleSteps
    .map((step, idx) => {
      const applicable = isStepApplicable(step, eqAnswers);
      const stepState = eqChecklist[step.num] || { status: 'pending', note: '' };
      const displayNum = state.stepFilterMode === 'dynamic' ? idx + 1 : step.num;

      return `
        <div class="cert-item status-${escapeHtml(stepState.status)} ${!applicable ? 'filtered-out' : ''}" data-step-num="${step.num}">
          <div class="cert-item-header">
            <div style="flex: 1;">
              ${
                showEn
                  ? `<div class="cert-main-title-en">
                      (${displayNum}) ${escapeHtml(step.titleEn)}
                      <button type="button" class="inline-rule-chip no-print js-open-rule" data-sec="${escapeHtml(step.sectionId || eq.sectionId)}" data-page="${step.page || eq.pdfPage}">
                        📖 ${escapeHtml(step.ruleRef)} (s.${step.page || eq.pdfPage})
                      </button>
                    </div>`
                  : `<div class="cert-main-title-en">
                      (${displayNum}) ${escapeHtml(step.titleTr)}
                      <button type="button" class="inline-rule-chip no-print js-open-rule" data-sec="${escapeHtml(step.sectionId || eq.sectionId)}" data-page="${step.page || eq.pdfPage}">
                        📖 ${escapeHtml(step.ruleRef)} (s.${step.page || eq.pdfPage})
                      </button>
                    </div>`
              }
              ${
                !applicable
                  ? `<span style="display:inline-block; margin-top:0.25rem; font-size:0.74rem; background:#fef3c7; color:#92400e; padding:0.1rem 0.45rem; border-radius:4px; font-weight:700;">
                      ℹ️ Seçili Uygulama Koşuluna (Application Terms) göre bu test muaf / opsiyoneldir
                    </span>`
                  : ''
              }
              ${showEn && step.detailEn ? `<div class="cert-sub-en">${escapeHtml(step.detailEn)}</div>` : ''}
            </div>

            <div class="status-btn-group no-print" role="group" aria-label="Test Durumu">
              <button type="button" class="status-btn ${stepState.status === 'ok' ? 'active-ok' : ''}" data-step="${step.num}" data-status="ok" title="Uygun / Doğrulandı">✓ OK</button>
              <button type="button" class="status-btn ${stepState.status === 'fail' ? 'active-fail' : ''}" data-step="${step.num}" data-status="fail" title="Uygun Değil / Ret">✗ Ret</button>
              <button type="button" class="status-btn ${stepState.status === 'na' ? 'active-na' : ''}" data-step="${step.num}" data-status="na" title="Uygulanamaz (N/A)">— N/A</button>
            </div>
          </div>

          ${
            showTr
              ? `
            <div class="cert-tr-block">
              <div class="cert-title-tr">🇹🇷 ${escapeHtml(step.titleTr)}</div>
              <div class="cert-detail-tr">${escapeHtml(step.detailTr)}</div>
              ${step.tipTr ? `<div class="cert-tip-tr">💡 <strong>Sörveyör Saha İpucu:</strong> ${escapeHtml(step.tipTr)}</div>` : ''}
            </div>
          `
              : ''
          }

          <div class="step-note-row">
            <input
              type="text"
              class="step-note-input"
              data-step-note="${step.num}"
              value="${escapeHtml(stepState.note || '')}"
              placeholder="✍️ Saha Notu / Ölçülen Değer (Örn: Megger: 250 MΩ @ 500V DC, HV: 2500V 60sn OK, Kalibrasyon No...)"
            />
          </div>
        </div>
      `;
    })
    .join('');

  container.innerHTML = `
    <!-- OFFICIAL RINA LEONARDO TEST HEADER -->
    <div class="leo-header">
      <div class="leo-left-col">
        <div class="leo-rina-logo">
          <svg viewBox="0 0 155 62" width="135" height="54" aria-label="RINA">
            <text x="2" y="46" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="42" fill="#004b87">R</text>
            <text x="36" y="46" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="42" fill="#004b87">I</text>
            <polygon points="72,2 80,26 72,22 64,26" fill="#0072bc"/>
            <polygon points="72,60 80,36 72,40 64,36" fill="#0072bc"/>
            <polygon points="50,31 66,26 62,31 66,36" fill="#38bdf8"/>
            <polygon points="94,31 78,26 82,31 78,36" fill="#38bdf8"/>
            <text x="95" y="46" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="42" fill="#004b87">A</text>
          </svg>
        </div>
        <div class="leo-date-issue">Date of issue: <strong>${todayStr}</strong></div>
      </div>

      <div class="leo-right-col">
        <div class="leo-doc-title">CERTIFICATION ACTIVITIES</div>
        <div class="leo-doc-subtitle">Leonardo TEST &bull; RINA Rules 2026</div>
        <div class="leo-cert-according">Certification according to RINA Rules for the Classification of Ships - Products</div>
        ${showEn ? `<div class="leo-product-title-en">${escapeHtml(eq.titleEn)} (See Application Terms below)</div>` : ''}
        ${showTr ? `<div class="leo-product-title-tr">🇹🇷 ${escapeHtml(eq.titleTr)}</div>` : ''}
        <div class="leo-rule-ref-row">
          <button type="button" class="leo-rule-link js-open-rule" data-sec="${escapeHtml(eq.sectionId)}" data-page="${eq.pdfPage}">
            Rule Reference: <strong>${escapeHtml(eq.ruleRef)}</strong> (PDF s.${eq.pdfPage} Aç 📖)
          </button>
        </div>
      </div>
    </div>

    ${metaBannerHtml}

    <!-- SECTION 1: APPLICATION TERMS -->
    <div class="leo-section">
      <div class="leo-section-title">APPLICATION TERMS</div>
      <div class="leo-section-desc">
        List of circumstances which affect the applicable acceptance requirements and certification activities
        ${showTr ? `<span class="leo-section-desc-tr">🇹🇷 Uygulanacak kabul gereksinimlerini ve fabrika test adımlarını belirleyen uygulama koşulları (Cevabı değiştirdiğinizde test maddeleri otomatik güncellenir)</span>` : ''}
      </div>
      <table class="leo-table">
        <thead>
          <tr>
            <th>Questions ${showTr ? '/ Sorular' : ''}</th>
            <th>Answers ${showTr ? '/ Cevaplar' : ''}</th>
          </tr>
        </thead>
        <tbody>
          ${appTermsRows}
        </tbody>
      </table>
    </div>

    <!-- QUICK TEST CALCULATOR & REFERENCE TABLES -->
    ${calcHtml}
    ${refTablesHtml}

    <!-- SECTION 2: ACCEPTANCE REQUIREMENTS -->
    <div class="leo-section">
      <div class="leo-section-title">ACCEPTANCE REQUIREMENTS</div>
      <div class="leo-section-desc">
        List of rule references of applicable design, construction and inspection requirements
        ${showTr ? `<span class="leo-section-desc-tr">🇹🇷 İlgili tasarım, imalat ve muayene kurallarının RINA 2026 kural referansları (Kurala tıklayarak orijinal PDF sayfasını açabilirsiniz)</span>` : ''}
      </div>
      <table class="leo-table">
        <thead>
          <tr>
            <th>Rule references ${showTr ? '/ Kural Referansı' : ''}</th>
            <th>Acceptance Requirement ${showTr ? '/ Kabul Gereksinimi' : ''}</th>
          </tr>
        </thead>
        <tbody>
          ${accReqRows}
        </tbody>
      </table>
    </div>

    <!-- SECTION 3: CERTIFICATION ACTIVITIES -->
    <div class="leo-section">
      <div class="leo-section-title">CERTIFICATION ACTIVITIES</div>
      <div class="leo-section-desc">
        List of documentation checks carried out by RINA Services S.p.A. and tests witnessed by the Surveyor
        ${showTr ? `<span class="leo-section-desc-tr">🇹🇷 RINA tarafından kontrol edilecek dokümanlar ve Sörveyör huzurunda (Witness) yapılacak fabrika test adımları</span>` : ''}
      </div>

      <div class="progress-bar-wrap no-print">
        <div class="progress-stats">
          ✅ Tamamlanan Test Adımı: <strong>${okCount} / ${visibleSteps.length}</strong>
        </div>
        <div class="quick-check-btns">
          <button type="button" class="btn-xs" id="markAllOkBtn">✓ Tümünü OK İşaretle</button>
          <button type="button" class="btn-xs" id="resetChecklistBtn">↺ İşaretleri Sıfırla</button>
        </div>
      </div>

      <div class="cert-activities-list">
        ${certStepsHtml}
      </div>
    </div>

    <div class="leo-footer">
      <span>RINA Rules for the Classification of Ships 2026 — ${escapeHtml(eq.ruleRef)}</span>
      <span>Page 1 of 1</span>
    </div>
  `;

  bindSheetInteractions(eq);
}

/* =====================================================
   QUICK FIELD CALCULATOR (TRAFO, ALTERNATOR, PANO, KAZAN, POMPA, VALF)
   ===================================================== */
function renderCalculatorHtml(eq) {
  const c = eq.calculator;
  if (!c) return '';

  if (c.type === 'transformer') {
    return `
      <div class="calc-box no-print">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0369a1;">Formül: HV = 2U + 1000V (min 2500V) | Endüklenen = 2U</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Sargı Anma Gerilimi U (V)</label>
            <input type="number" id="calcTrafoU" value="${c.defaultVoltage}" min="12" max="36000" />
          </div>
          <div class="calc-input-group">
            <label>Anma Frekansı fn (Hz)</label>
            <input type="number" id="calcTrafoFn" value="${c.defaultFreq}" min="50" max="60" />
          </div>
          <div class="calc-input-group">
            <label>Endüklenen Test Frekansı fp (Hz)</label>
            <input type="number" id="calcTrafoFp" value="${c.defaultFreq * 2}" min="50" max="400" />
          </div>
          <div class="calc-results" id="calcTrafoResults"></div>
        </div>
      </div>
    `;
  }

  if (c.type === 'rotating_machine') {
    return `
      <div class="calc-box no-print">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0369a1;">IEC 60034-1 &amp; Pt C, Ch 2, Sec 4 Tab. 2</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Anma Gerilimi Un (V)</label>
            <input type="number" id="calcRotU" value="${c.defaultVoltage}" min="24" max="15000" />
          </div>
          <div class="calc-input-group">
            <label>Anma Devri n (RPM)</label>
            <input type="number" id="calcRotRpm" value="${c.defaultSpeed}" min="100" max="3600" />
          </div>
          <div class="calc-results" id="calcRotResults"></div>
        </div>
      </div>
    `;
  }

  if (c.type === 'switchboard') {
    return `
      <div class="calc-box no-print">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0369a1;">Pt C, Ch 2, Sec 8 [3.3.4] Tab. 2 &amp; Tab. 3</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Ana Bara Yalıtım Gerilimi Ui (V)</label>
            <input type="number" id="calcSwbUi" value="${c.defaultVoltage}" min="24" max="1000" />
          </div>
          <div class="calc-input-group">
            <label>Kumanda Devresi Ui (V)</label>
            <input type="number" id="calcSwbAux" value="${c.defaultAuxVoltage}" min="12" max="690" />
          </div>
          <div class="calc-results" id="calcSwbResults"></div>
        </div>
      </div>
    `;
  }

  if (c.type === 'pressure_vessel' || c.type === 'pump_compressor' || c.type === 'valve_pipe') {
    return `
      <div class="calc-box no-print">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0369a1;">1 MPa = 10 bar</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Tasarım Basıncı p (bar)</label>
            <input type="number" id="calcPressBar" value="${c.defaultPressureBar}" min="0.5" max="1000" step="0.5" />
          </div>
          <div class="calc-results" id="calcPressResults" data-calc-type="${c.type}"></div>
        </div>
      </div>
    `;
  }

  return '';
}

function updateCalculatorValues(eq) {
  if (!eq.calculator) return;
  const type = eq.calculator.type;

  if (type === 'transformer') {
    const u = parseFloat(document.getElementById('calcTrafoU')?.value) || 440;
    const fn = parseFloat(document.getElementById('calcTrafoFn')?.value) || 60;
    const fp = parseFloat(document.getElementById('calcTrafoFp')?.value) || 120;
    const hv = Math.max(2500, Math.round(2 * u + 1000));
    const indV = Math.round(2 * u);
    const indTime = fp <= 2 * fn ? 60 : Math.max(15, Math.round((120 * fn) / fp));
    const el = document.getElementById('calcTrafoResults');
    if (el) {
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Yüksek Gerilim (HV) Testi [1.5.3]</span><span class="val">${hv} V AC (60 sn)</span></div>
        <div class="calc-res-card"><span class="lbl">Endüklenen Gerilim Testi [1.5.6]</span><span class="val">${indV} V @ ${fp}Hz (${indTime} sn)</span></div>
        <div class="calc-res-card"><span class="lbl">Min. İzolasyon (Megger) [1.5.5]</span><span class="val">≥ 5 MΩ (@ 500V DC)</span></div>
      `;
    }
  } else if (type === 'rotating_machine') {
    const u = parseFloat(document.getElementById('calcRotU')?.value) || 440;
    const rpm = parseFloat(document.getElementById('calcRotRpm')?.value) || 1800;
    const hv = Math.max(1500, Math.round(2 * u + 1000));
    const overspeed = Math.round(rpm * 1.2);
    let meggerV = '500 V DC';
    let minMohm = '1 MΩ';
    if (u <= 250) {
      meggerV = `${Math.round(2 * u)} V DC`;
      minMohm = '1 MΩ';
    } else if (u <= 1000) {
      meggerV = '500 V DC';
      minMohm = '1 MΩ';
    } else if (u <= 7200) {
      meggerV = '1000 V DC';
      minMohm = `${(u / 1000 + 1).toFixed(1)} MΩ`;
    } else {
      meggerV = '5000 V DC';
      minMohm = `${(u / 1000 + 1).toFixed(1)} MΩ`;
    }
    const el = document.getElementById('calcRotResults');
    if (el) {
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Dielektrik (HV) Testi [4.9]</span><span class="val">${hv} V AC (60 sn)</span></div>
        <div class="calc-res-card"><span class="lbl">Min. Megger [Tab. 2]</span><span class="val">≥ ${minMohm} (@ ${meggerV})</span></div>
        <div class="calc-res-card"><span class="lbl">Aşırı Devir (Overspeed) [4.8]</span><span class="val">${overspeed} RPM (2 dk)</span></div>
      `;
    }
  } else if (type === 'switchboard') {
    const ui = parseFloat(document.getElementById('calcSwbUi')?.value) || 440;
    const uaux = parseFloat(document.getElementById('calcSwbAux')?.value) || 230;
    let mainHv = 2500;
    if (ui <= 60) mainHv = 1000;
    else if (ui <= 300) mainHv = 2000;
    else if (ui <= 660) mainHv = 2500;
    else if (ui <= 800) mainHv = 3000;
    else mainHv = 3500;

    let auxHv = 1500;
    if (uaux <= 12) auxHv = 250;
    else if (uaux <= 60) auxHv = 500;
    else auxHv = Math.max(1500, Math.round(2 * uaux + 1000));

    const el = document.getElementById('calcSwbResults');
    if (el) {
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Ana Devre HV [Tab. 2]</span><span class="val">${mainHv} V AC (60 sn)</span></div>
        <div class="calc-res-card"><span class="lbl">Kumanda Devresi HV [Tab. 3]</span><span class="val">${auxHv} V AC (60 sn)</span></div>
        <div class="calc-res-card"><span class="lbl">HV Sonrası Megger [3.4]</span><span class="val">≥ 1 MΩ (@ ≥500V DC)</span></div>
      `;
    }
  } else {
    const pBar = parseFloat(document.getElementById('calcPressBar')?.value) || 10;
    const pMpa = pBar / 10.0;
    const el = document.getElementById('calcPressResults');
    if (!el) return;

    if (type === 'pressure_vessel') {
      let ptMpa = 1.5 * pMpa;
      if (pMpa > 4 && pMpa <= 25) ptMpa = 1.4 * pMpa + 0.4;
      else if (pMpa > 25) ptMpa = pMpa + 10.4;
      const ptBar = (ptMpa * 10).toFixed(1);
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Hidrostatik Test Basıncı pt [7.3.2]</span><span class="val">${ptBar} bar (${ptMpa.toFixed(2)} MPa)</span></div>
        <div class="calc-res-card"><span class="lbl">Aksesuar Test Basıncı [7.3.3]</span><span class="val">${(1.5 * pBar).toFixed(1)} bar</span></div>
      `;
    } else if (type === 'pump_compressor') {
      let phMpa = 1.5 * pMpa;
      if (pMpa > 4 && pMpa <= 25) phMpa = 1.4 * pMpa + 0.4;
      else if (pMpa > 25) phMpa = pMpa + 10.4;
      phMpa = Math.max(0.4, phMpa);
      const waterBar = Math.max(2.0, 1.5 * pBar).toFixed(1);
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Gövde/Silindir Hidrotest pH [21.4.5]</span><span class="val">${(phMpa * 10).toFixed(1)} bar (min 4 bar)</span></div>
        <div class="calc-res-card"><span class="lbl">Kompresör Su Ceketi [21.4.5 d]</span><span class="val">${waterBar} bar (min 2 bar)</span></div>
      `;
    } else if (type === 'valve_pipe') {
      const valveShell = (1.5 * pBar).toFixed(1);
      const shipSide = Math.max(5.0, 1.5 * pBar).toFixed(1);
      const pipeHydro = Math.max(4.0, 2.0 * pBar).toFixed(1);
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Valf Gövde (1.5×p) / Sit (1.1×p)</span><span class="val">${valveShell} bar / ${(1.1 * pBar).toFixed(1)} bar</span></div>
        <div class="calc-res-card"><span class="lbl">Borda (Ship-Side) Valfi [21.4.3b]</span><span class="val">${shipSide} bar (min 5 bar)</span></div>
        <div class="calc-res-card"><span class="lbl">Class I/II Boru Testi (2×p) [21.4.2e]</span><span class="val">${pipeHydro} bar (min 4 bar)</span></div>
      `;
    }
  }
}

function bindSheetInteractions(eq) {
  // Application Terms Selects
  document.querySelectorAll('#leonardoSheet .answer-select').forEach((sel) => {
    sel.addEventListener('change', () => {
      const qId = sel.dataset.questionId;
      if (!state.answers[eq.id]) state.answers[eq.id] = {};
      state.answers[eq.id][qId] = sel.value;
      persistState();
      renderLeonardoSheet();
    });
  });

  // Calculator inputs
  updateCalculatorValues(eq);
  document.querySelectorAll('#leonardoSheet .calc-box input').forEach((inp) => {
    inp.addEventListener('input', () => updateCalculatorValues(eq));
  });

  // Rule reference buttons -> Open Rule PDF Modal
  document.querySelectorAll('#leonardoSheet .js-open-rule').forEach((btn) => {
    btn.addEventListener('click', () => {
      const secId = btn.dataset.sec || eq.sectionId;
      const page = parseInt(btn.dataset.page, 10) || eq.pdfPage;
      openRuleModal(secId, page);
    });
  });

  // Checklist status buttons
  document.querySelectorAll('#leonardoSheet .status-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const stepNum = btn.dataset.step;
      const targetStatus = btn.dataset.status;
      if (!state.checklist[eq.id]) state.checklist[eq.id] = {};
      const curr = state.checklist[eq.id][stepNum] || { status: 'pending', note: '' };
      curr.status = curr.status === targetStatus ? 'pending' : targetStatus;
      state.checklist[eq.id][stepNum] = curr;
      persistState();
      renderLeonardoSheet();
    });
  });

  // Step note inputs
  document.querySelectorAll('#leonardoSheet .step-note-input').forEach((inp) => {
    inp.addEventListener('input', () => {
      const stepNum = inp.dataset.stepNote;
      if (!state.checklist[eq.id]) state.checklist[eq.id] = {};
      const curr = state.checklist[eq.id][stepNum] || { status: 'pending', note: '' };
      curr.note = inp.value;
      state.checklist[eq.id][stepNum] = curr;
      persistState();
    });
  });

  // Mark All OK / Reset buttons
  document.getElementById('markAllOkBtn')?.addEventListener('click', () => {
    if (!state.checklist[eq.id]) state.checklist[eq.id] = {};
    (eq.certificationActivities || []).forEach((s) => {
      const curr = state.checklist[eq.id][s.num] || { status: 'pending', note: '' };
      curr.status = 'ok';
      state.checklist[eq.id][s.num] = curr;
    });
    persistState();
    renderLeonardoSheet();
    showToast('Tüm test adımları OK olarak işaretlendi.');
  });

  document.getElementById('resetChecklistBtn')?.addEventListener('click', () => {
    state.checklist[eq.id] = {};
    persistState();
    renderLeonardoSheet();
    showToast('Kontrol listesi sıfırlandı.');
  });
}

/* =====================================================
   ORIGINAL RINA 2026 PDF RULE MODAL & FULL RULES TAB
   ===================================================== */
async function openRuleModal(sectionId, targetPage) {
  const modal = document.getElementById('ruleModal');
  const badge = document.getElementById('ruleModalBadge');
  const title = document.getElementById('ruleModalTitle');
  const body = document.getElementById('ruleModalBody');
  const pills = document.getElementById('modalArticlePills');
  const filterInput = document.getElementById('modalRuleFilterInput');

  modal.classList.remove('hidden');
  badge.textContent = sectionId;
  title.textContent = 'RINA Rules 2026 PDF Metni Yükleniyor...';
  body.innerHTML = `<div style="padding:2rem; text-align:center;">⏳ 2026 RINA Kural veritabanından ilgili bölüm yükleniyor...</div>`;

  const fullDb = await ensureFullRulesLoaded();
  if (!fullDb) {
    body.innerHTML = `<div style="padding:2rem; color:#991b1b;">Kural veritabanı yüklenemedi.</div>`;
    return;
  }

  const sec = fullDb.find((s) => s.id === sectionId) || fullDb[0];
  badge.textContent = `${sec.id} (PDF Sayfa ${sec.start_page}–${sec.end_page})`;
  title.textContent = `${sec.chapter} — ${sec.section}`;
  filterInput.value = '';

  // Render article quick jump pills
  pills.innerHTML = (sec.articles || [])
    .filter((a) => a.level === 4)
    .map(
      (a) => `
      <button type="button" class="btn-xs js-modal-page-jump" data-page="${a.page}">
        ${escapeHtml(a.title.replace('Article - ', ''))} (s.${a.page})
      </button>
    `
    )
    .join('');

  const renderPages = (query = '') => {
    const q = query.trim().toLowerCase();
    const pagesHtml = sec.pages
      .filter((p) => !q || p.text.toLowerCase().includes(q))
      .map((p) => {
        const isTarget = p.page === targetPage;
        const formattedText = highlightText(p.text, q);
        return `
          <div class="pdf-page-block" id="modal-pdf-page-${p.page}" style="${isTarget ? 'border: 2px solid #0284c7; background:#f0f9ff;' : ''}">
            <div class="pdf-page-header">
              <span>${escapeHtml(sec.id)} &bull; ${escapeHtml(sec.section)}</span>
              <span>PDF Sayfa ${p.page}</span>
            </div>
            <div class="pdf-page-text">${formattedText}</div>
          </div>
        `;
      })
      .join('');

    body.innerHTML =
      pagesHtml || `<div style="padding:1.5rem; text-align:center;">Bu bölümde "${escapeHtml(query)}" bulunamadı.</div>`;
  };

  renderPages('');

  pills.querySelectorAll('.js-modal-page-jump').forEach((btn) => {
    btn.addEventListener('click', () => {
      const pg = btn.dataset.page;
      const el = document.getElementById(`modal-pdf-page-${pg}`);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  filterInput.oninput = () => renderPages(filterInput.value);

  // Scroll to targetPage
  setTimeout(() => {
    const targetEl = document.getElementById(`modal-pdf-page-${targetPage}`);
    if (targetEl) targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 60);
}

function renderRulesSidebar() {
  const sidebar = document.getElementById('rulesSidebar');
  if (!sidebar || !state.rulesIndex.length) return;

  sidebar.innerHTML = state.rulesIndex
    .map((sec) => {
      const active = sec.id === state.activeRuleSectionId;
      return `
        <button type="button" class="sec-nav-item ${active ? 'active' : ''}" data-sec-id="${escapeHtml(sec.id)}">
          <div style="font-weight:700; font-size:0.76rem; opacity:0.85;">${escapeHtml(sec.id)} (s.${sec.start_page})</div>
          <div>${escapeHtml(sec.section)}</div>
        </button>
      `;
    })
    .join('');

  sidebar.querySelectorAll('.sec-nav-item').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.activeRuleSectionId = btn.dataset.secId;
      renderRulesSidebar();
      renderSelectedRuleSectionInTab(state.activeRuleSectionId);
    });
  });
}

async function renderSelectedRuleSectionInTab(secId, highlightQuery = '') {
  const reader = document.getElementById('rulesReader');
  if (!reader) return;

  if (!state.rulesFull) {
    reader.innerHTML = `<div style="padding:2rem; text-align:center;">⏳ RINA 2026 PDF Tam Metin Veritabanı Yükleniyor...</div>`;
    await ensureFullRulesLoaded();
  }
  if (!state.rulesFull) return;

  const sec = state.rulesFull.find((s) => s.id === secId) || state.rulesFull[0];
  reader.innerHTML = `
    <div style="margin-bottom:1rem; padding-bottom:0.75rem; border-bottom:2px solid #004b87;">
      <span class="equip-code">${escapeHtml(sec.id)}</span>
      <h3 style="margin-top:0.35rem; color:#002b54;">${escapeHtml(sec.chapter)} — ${escapeHtml(sec.section)}</h3>
      <div style="font-size:0.8rem; color:#64748b;">RINA Rules 2026 Interactive PDF Sayfa Aralığı: ${sec.start_page} – ${sec.end_page}</div>
    </div>
    ${sec.pages
      .map(
        (p) => `
      <div class="pdf-page-block" id="tab-pdf-page-${p.page}">
        <div class="pdf-page-header">
          <span>${escapeHtml(sec.id)}</span>
          <span>PDF Sayfa ${p.page}</span>
        </div>
        <div class="pdf-page-text">${highlightText(p.text, highlightQuery)}</div>
      </div>
    `
      )
      .join('')}
  `;
}

async function performFullRulesSearch() {
  const inp = document.getElementById('fullRulesSearchInput');
  const resultsBox = document.getElementById('fullRulesSearchResults');
  const q = inp.value.trim().toLowerCase();

  if (!q || q.length < 2) {
    resultsBox.classList.add('hidden');
    return;
  }

  resultsBox.classList.remove('hidden');
  resultsBox.innerHTML = `<div>🔍 1.238 sayfalık RINA 2026 Part C &amp; Part D içinde aranıyor...</div>`;

  const fullDb = await ensureFullRulesLoaded();
  if (!fullDb) return;

  const hits = [];
  for (const sec of fullDb) {
    for (const pg of sec.pages) {
      const idx = pg.text.toLowerCase().indexOf(q);
      if (idx !== -1) {
        const start = Math.max(0, idx - 70);
        const end = Math.min(pg.text.length, idx + q.length + 110);
        const snippet = pg.text.slice(start, end).replace(/\s+/g, ' ');
        hits.push({
          secId: sec.id,
          secTitle: sec.section,
          page: pg.page,
          snippet
        });
        if (hits.length >= 60) break;
      }
    }
    if (hits.length >= 60) break;
  }

  if (hits.length === 0) {
    resultsBox.innerHTML = `<div>"${escapeHtml(inp.value)}" için eşleşme bulunamadı.</div>`;
    return;
  }

  resultsBox.innerHTML = `
    <div style="font-size:0.8rem; font-weight:700; color:#004b87; margin-bottom:0.5rem;">
      Bulunan Sonuçlar (${hits.length}${hits.length === 60 ? '+' : ''}) — İlgili sayfayı açmak için tıklayın:
    </div>
    ${hits
      .map(
        (h) => `
      <div class="search-hit-item" data-sec="${escapeHtml(h.secId)}" data-page="${h.page}">
        <div style="font-weight:700; font-size:0.82rem; color:#002b54;">
          ${escapeHtml(h.secId)} — ${escapeHtml(h.secTitle)} <span style="color:#0284c7;">(PDF Sayfa ${h.page})</span>
        </div>
        <div style="font-size:0.78rem; color:#475569; margin-top:0.15rem;">
          ...${highlightText(h.snippet, q)}...
        </div>
      </div>
    `
      )
      .join('')}
  `;

  resultsBox.querySelectorAll('.search-hit-item').forEach((item) => {
    item.addEventListener('click', async () => {
      const secId = item.dataset.sec;
      const page = parseInt(item.dataset.page, 10);
      state.activeRuleSectionId = secId;
      renderRulesSidebar();
      await renderSelectedRuleSectionInTab(secId, q);
      const pageEl = document.getElementById(`tab-pdf-page-${page}`);
      if (pageEl) pageEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
}

/* =====================================================
   SAVED FACTORY INSPECTIONS (OFFLINE HISTORY)
   ===================================================== */
function saveCurrentInspection() {
  const eq = getCurrentEquipment();
  if (!eq) return;

  const record = {
    id: `fat-${Date.now()}`,
    savedAt: new Date().toLocaleString('tr-TR'),
    equipmentId: eq.id,
    equipmentCode: eq.code,
    equipmentTitleTr: eq.titleTr,
    equipmentTitleEn: eq.titleEn,
    ruleRef: eq.ruleRef,
    meta: { ...state.meta },
    answers: { ...(state.answers[eq.id] || {}) },
    checklist: JSON.parse(JSON.stringify(state.checklist[eq.id] || {}))
  };

  state.savedInspections.unshift(record);
  localStorage.setItem(STORAGE_KEYS.SAVED, JSON.stringify(state.savedInspections));
  updateSavedCountBadge();
  renderSavedInspections();
  showToast('💾 Saha testi ve kontrol listesi kaydedildi!');
}

function updateSavedCountBadge() {
  const badge = document.getElementById('savedCountBadge');
  if (badge) badge.textContent = String(state.savedInspections.length);
}

function renderSavedInspections() {
  const listEl = document.getElementById('savedInspectionsList');
  if (!listEl) return;

  if (state.savedInspections.length === 0) {
    listEl.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 2rem; text-align: center; color: #64748b;">
        Henüz kaydedilmiş bir fabrika testi bulunmuyor. Test ekranındaki <strong>"💾 Saha Testini Kaydet"</strong> butonuna basarak fabrika test kayıtlarınızı burada saklayabilirsiniz.
      </div>
    `;
    return;
  }

  listEl.innerHTML = state.savedInspections
    .map((rec) => {
      const stepsObj = rec.checklist || {};
      const okCount = Object.values(stepsObj).filter((v) => v.status === 'ok').length;
      const failCount = Object.values(stepsObj).filter((v) => v.status === 'fail').length;
      return `
        <div class="saved-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="equip-code">${escapeHtml(rec.equipmentCode || 'FAT')}</span>
            <span style="font-size:0.75rem; color:#64748b;">${escapeHtml(rec.savedAt)}</span>
          </div>
          <div style="font-weight:700; color:#002b54; font-size:0.92rem;">${escapeHtml(rec.equipmentTitleTr)}</div>
          <div style="font-size:0.78rem; color:#475569;">
            <strong>Fabrika:</strong> ${escapeHtml(rec.meta?.factory || '—')} &bull;
            <strong>Proje:</strong> ${escapeHtml(rec.meta?.project || '—')} &bull;
            <strong>Seri No:</strong> ${escapeHtml(rec.meta?.serial || '—')}
          </div>
          <div style="font-size:0.78rem; font-weight:700; color:#0f766e;">
            ✓ ${okCount} OK ${failCount > 0 ? `| ✗ ${failCount} Ret` : ''}
          </div>
          <div style="display:flex; gap:0.5rem; margin-top:0.35rem;">
            <button type="button" class="btn-primary js-load-saved" data-id="${escapeHtml(rec.id)}" style="flex:1; justify-content:center;">
              📂 Testi Aç
            </button>
            <button type="button" class="btn-secondary js-delete-saved" data-id="${escapeHtml(rec.id)}">
              🗑️ Sil
            </button>
          </div>
        </div>
      `;
    })
    .join('');

  listEl.querySelectorAll('.js-load-saved').forEach((btn) => {
    btn.addEventListener('click', () => {
      const rec = state.savedInspections.find((r) => r.id === btn.dataset.id);
      if (!rec) return;
      state.selectedEquipmentId = rec.equipmentId;
      state.meta = { ...state.meta, ...(rec.meta || {}) };
      state.answers[rec.equipmentId] = { ...(rec.answers || {}) };
      state.checklist[rec.equipmentId] = JSON.parse(JSON.stringify(rec.checklist || {}));
      syncMetaInputs();
      persistState();
      renderEquipmentGrid();
      renderLeonardoSheet();
      switchMainTab('fat');
      showToast('Kayıtlı fabrika testi yüklendi.');
    });
  });

  listEl.querySelectorAll('.js-delete-saved').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.savedInspections = state.savedInspections.filter((r) => r.id !== btn.dataset.id);
      localStorage.setItem(STORAGE_KEYS.SAVED, JSON.stringify(state.savedInspections));
      updateSavedCountBadge();
      renderSavedInspections();
      showToast('Kayıt silindi.');
    });
  });
}

/* =====================================================
   NAVIGATION, TOOLBAR & PWA EVENTS
   ===================================================== */
function switchMainTab(tabName) {
  document.querySelectorAll('.main-tabs .tab-btn').forEach((b) => {
    b.classList.toggle('active', b.dataset.tab === tabName);
  });
  document.querySelectorAll('.tab-panel').forEach((p) => {
    p.classList.toggle('active', p.id === `tab-${tabName}`);
  });
}

function syncMetaInputs() {
  const map = {
    metaFactory: 'factory',
    metaProject: 'project',
    metaSerial: 'serial',
    metaTypeSerial: 'typeSerial',
    metaSurveyor: 'surveyor'
  };
  Object.entries(map).forEach(([elId, key]) => {
    const el = document.getElementById(elId);
    if (el) el.value = state.meta[key] || '';
  });
}

function bindNavigationAndToolbar() {
  // Main tabs
  document.querySelectorAll('.main-tabs .tab-btn').forEach((btn) => {
    btn.addEventListener('click', () => switchMainTab(btn.dataset.tab));
  });

  document.getElementById('brandHomeBtn')?.addEventListener('click', () => {
    switchMainTab('fat');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // Search Input
  const searchInp = document.getElementById('equipmentSearchInput');
  const clearBtn = document.getElementById('clearSearchBtn');
  searchInp?.addEventListener('input', () => {
    state.searchQuery = searchInp.value;
    clearBtn.classList.toggle('hidden', !state.searchQuery);
    renderEquipmentGrid();
  });
  clearBtn?.addEventListener('click', () => {
    searchInp.value = '';
    state.searchQuery = '';
    clearBtn.classList.add('hidden');
    renderEquipmentGrid();
  });

  // Category chips
  document.querySelectorAll('#categoryChips .chip').forEach((chip) => {
    chip.addEventListener('click', () => {
      state.selectedCategory = chip.dataset.cat;
      document.querySelectorAll('#categoryChips .chip').forEach((c) => c.classList.remove('active'));
      chip.classList.add('active');
      renderEquipmentGrid();
    });
  });

  // Language mode buttons
  document.querySelectorAll('#langModeControl .seg-btn').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.lang === state.langMode);
    btn.addEventListener('click', () => {
      state.langMode = btn.dataset.lang;
      document.querySelectorAll('#langModeControl .seg-btn').forEach((b) => {
        b.classList.toggle('active', b.dataset.lang === state.langMode);
      });
      persistState();
      renderLeonardoSheet();
    });
  });

  // Step filter buttons
  document.querySelectorAll('#stepFilterControl .seg-btn').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.filter === state.stepFilterMode);
    btn.addEventListener('click', () => {
      state.stepFilterMode = btn.dataset.filter;
      document.querySelectorAll('#stepFilterControl .seg-btn').forEach((b) => {
        b.classList.toggle('active', b.dataset.filter === state.stepFilterMode);
      });
      persistState();
      renderLeonardoSheet();
    });
  });

  // Metadata fields
  const metaMap = {
    metaFactory: 'factory',
    metaProject: 'project',
    metaSerial: 'serial',
    metaTypeSerial: 'typeSerial',
    metaSurveyor: 'surveyor'
  };
  Object.entries(metaMap).forEach(([elId, key]) => {
    const el = document.getElementById(elId);
    el?.addEventListener('input', () => {
      state.meta[key] = el.value;
      persistState();
      renderLeonardoSheet();
    });
  });

  // Toolbar action buttons
  document.getElementById('openRulePdfModalBtn')?.addEventListener('click', () => {
    const eq = getCurrentEquipment();
    if (eq) openRuleModal(eq.sectionId, eq.pdfPage);
  });

  document.getElementById('saveInspectionBtn')?.addEventListener('click', saveCurrentInspection);

  document.getElementById('printSheetBtn')?.addEventListener('click', () => {
    window.print();
  });

  // Full Rules Search
  document.getElementById('fullRulesSearchBtn')?.addEventListener('click', performFullRulesSearch);
  document.getElementById('fullRulesSearchInput')?.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') performFullRulesSearch();
  });

  // Modals close
  document.getElementById('closeRuleModalBtn')?.addEventListener('click', () => {
    document.getElementById('ruleModal').classList.add('hidden');
  });
  document.getElementById('ruleModal')?.addEventListener('click', (e) => {
    if (e.target.id === 'ruleModal') document.getElementById('ruleModal').classList.add('hidden');
  });

  document.getElementById('installPwaBtn')?.addEventListener('click', () => {
    document.getElementById('installModal').classList.remove('hidden');
  });
  document.getElementById('closeInstallModalBtn')?.addEventListener('click', () => {
    document.getElementById('installModal').classList.add('hidden');
  });
  document.getElementById('installModal')?.addEventListener('click', (e) => {
    if (e.target.id === 'installModal') document.getElementById('installModal').classList.add('hidden');
  });

  // Export & Import Saved JSON
  document.getElementById('exportSavedJsonBtn')?.addEventListener('click', () => {
    const dataStr = JSON.stringify(state.savedInspections, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `rina-fat-kayitlar-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  });

  document.getElementById('importSavedJsonInput')?.addEventListener('change', (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const imported = JSON.parse(reader.result);
        if (Array.isArray(imported)) {
          state.savedInspections = [...imported, ...state.savedInspections];
          localStorage.setItem(STORAGE_KEYS.SAVED, JSON.stringify(state.savedInspections));
          updateSavedCountBadge();
          renderSavedInspections();
          showToast('Yedek dosyası başarıyla yüklendi!');
        }
      } catch (err) {
        showToast('Geçersiz JSON dosyası.');
      }
    };
    reader.readAsText(file);
  });
}

function setupPwaAndOfflineHandlers() {
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
      .register('/sw.js')
      .then(() => console.log('RINA FAT Service Worker registered'))
      .catch((err) => console.warn('SW registration error:', err));
  }

  const updateOnlineBadge = () => {
    const badge = document.getElementById('offlineBadge');
    const txt = document.getElementById('offlineBadgeText');
    if (!badge || !txt) return;
    if (navigator.onLine) {
      badge.className = 'status-pill online';
      txt.textContent = 'Offline Hazır';
    } else {
      badge.className = 'status-pill offline';
      txt.textContent = 'Çevrimdışı Mod (Aktif)';
    }
  };
  window.addEventListener('online', updateOnlineBadge);
  window.addEventListener('offline', updateOnlineBadge);
  updateOnlineBadge();

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    state.deferredInstallPrompt = e;
    document.getElementById('nativeInstallPromptBox')?.classList.remove('hidden');
  });

  document.getElementById('triggerNativeInstallBtn')?.addEventListener('click', async () => {
    if (!state.deferredInstallPrompt) return;
    state.deferredInstallPrompt.prompt();
    await state.deferredInstallPrompt.userChoice;
    state.deferredInstallPrompt = null;
    document.getElementById('nativeInstallPromptBox')?.classList.add('hidden');
    document.getElementById('installModal')?.classList.add('hidden');
  });
}

/* =====================================================
   UTILITIES
   ===================================================== */
function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function highlightText(text, query) {
  const escaped = escapeHtml(text);
  if (!query || query.length < 2) return escaped;
  const safeQ = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const regex = new RegExp(`(${safeQ})`, 'gi');
  return escaped.replace(regex, '<mark class="hl">$1</mark>');
}

function showToast(msg) {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const el = document.createElement('div');
  el.className = 'toast';
  el.textContent = msg;
  container.appendChild(el);
  setTimeout(() => {
    el.remove();
  }, 3200);
}
