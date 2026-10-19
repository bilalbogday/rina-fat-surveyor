/* RINA Marine Surveyor — Official LEONARDO TEST & RINA Rules 2026 AI Assistant */

const GEMINI_CONFIG = {
  apiKey: 'AIzaSyBkSjxPeFbMxy-KsLPFz-8TswT_WXK5evY',
  endpoint: 'https://generativelanguage.googleapis.com/v1beta/interactions',
  fastModel: 'gemini-3.5-flash-lite'
};

// Comprehensive Turkish <-> English RINA Rules 2026 Marine Surveyor Dictionary & Section Router
const MARINE_SYNONYMS = [
  { tr: ['lomboz', 'pencere', 'cam', 'ışıklık', 'kör kapak', 'sidescuttle', 'window', 'skylight', 'deadlight', 'iso 614', 'iso 21005', 'punch test'], en: ['sidescuttles', 'windows', 'skylights', 'deadlights', 'glass panes', 'punch test', '6.3.2'], sections: ['Pt D, Ch 4, Sec 1', 'Pt B, Ch 9, Sec 9'] },
  { tr: ['hava tüpü', 'ilk hareket hava', 'starting air', 'air receiver', 'hava şişesi', 'basınçlı kap', 'pressure vessel'], en: ['pressure vessels', 'air receiver', 'starting air', 'hydrostatic test', '7.3.2', '1,5 p'], sections: ['Pt C, Ch 1, Sec 3'] },
  { tr: ['kazan', 'buhar kazanı', 'boiler', 'steam generator', 'ekonomizer', 'kızdırıcı'], en: ['boilers', 'steam generators', 'safety valve', 'hydrostatic test', '7.3'], sections: ['Pt C, Ch 1, Sec 3'] },
  { tr: ['eşanjör', 'ısı değiştirici', 'heat exchanger', 'cooler', 'soğutucu', 'kondenser', 'heater'], en: ['heat exchangers', 'tube bundle', 'shell', 'hydrostatic test', '7.3.2'], sections: ['Pt C, Ch 1, Sec 3'] },
  { tr: ['valf', 'vana', 'borda valfi', 'ship side valve', 'sea valve', 'kinistin', 'emniyet valfi', 'safety valve', 'check valve', 'kelebek vana', 'globe valve', 'gate valve'], en: ['valves', 'accessories', 'shell test', 'seat tightness', 'ship side', '21.4.3', '1,5 p', '1,1 p', '5 bar'], sections: ['Pt C, Ch 1, Sec 10'] },
  { tr: ['boru', 'piping', 'pipe', 'class i', 'class ii', 'class iii', 'flanş', 'fitting', 'manşon', 'dirsek'], en: ['piping systems', 'class i', 'class ii', 'class iii', 'hydrostatic test', '21.4', 'table 30'], sections: ['Pt C, Ch 1, Sec 10'] },
  { tr: ['esnek hortum', 'flexible hose', 'expansion joint', 'kompansatör', 'körük', 'bellows'], en: ['flexible hoses', 'expansion joints', 'burst test', 'impulse test', 'hydrostatic', '2.5'], sections: ['Pt C, Ch 1, Sec 10'] },
  { tr: ['pompa', 'santrifüj pompa', 'pump', 'sintine pompası', 'yangın pompası', 'fire pump', 'bilge pump', 'ballast pump', 'transfer pump', 'hidrofor'], en: ['pumps', 'centrifugal', 'displacement', 'hydrostatic test', 'capacity test', 'NPSH', '21.4.5', '17.6'], sections: ['Pt C, Ch 1, Sec 10'] },
  { tr: ['kompresör', 'hava kompresörü', 'air compressor', 'compressor'], en: ['air compressors', 'hydrostatic test', 'capacity test', 'relief valve', '21.4.5'], sections: ['Pt C, Ch 1, Sec 10'] },
  { tr: ['dizel', 'dizel motor', 'ana makine', 'yardımcı makine', 'diesel engine', 'internal combustion', 'krank', 'crankshaft', 'karter', 'crankcase', 'enjektör', 'silindir'], en: ['internal combustion engines', 'diesel engines', 'type approval', 'works trials', 'overspeed', 'crankcase', 'safety valve'], sections: ['Pt C, Ch 1, Sec 2'] },
  { tr: ['turbo', 'turboşarj', 'turbocharger', 'egzoz türbini'], en: ['turbochargers', 'containment', 'overspeed', 'impeller', 'hydrostatic'], sections: ['Pt C, Ch 1, Sec 16'] },
  { tr: ['şaft', 'pervane şaftı', 'ara şaft', 'shaft', 'shafting', 'tailshaft', 'propeller shaft', 'stern tube', 'kaplin', 'coupling'], en: ['shafting', 'propeller shaft', 'intermediate shaft', 'liner', 'coupling', 'ultrasonic', 'magnetic'], sections: ['Pt C, Ch 1, Sec 7', 'Pt D, Ch 2, Sec 3'] },
  { tr: ['pervane', 'propeller', 'kanat', 'pitch', 'cpp', 'fpp', 'hub', 'kovan'], en: ['propellers', 'controllable pitch', 'fixed pitch', 'static balancing', 'copper alloy', 'dye penetrant'], sections: ['Pt C, Ch 1, Sec 8', 'Pt D, Ch 3, Sec 2'] },
  { tr: ['dümen', 'dümen makinesi', 'steering gear', 'rudder', 'rudder stock', 'dümen yelpazesi', 'yeke', 'tiller', 'hidrolik silindir'], en: ['steering gear', 'rudders', 'rudder stock', 'relief valves', 'overload', 'tightness', '28 s'], sections: ['Pt C, Ch 1, Sec 11', 'Pt B, Ch 10, Sec 1'] },
  { tr: ['irgat', 'vinç', 'windlass', 'winch', 'mooring', 'halat tamburu', 'fren testi', 'capstan'], en: ['windlasses', 'mooring winches', 'overload test', 'brake holding', 'continuous duty'], sections: ['Pt C, Ch 1, Sec 12', 'Pt B, Ch 10, Sec 4'] },
  { tr: ['sintine separatörü', 'ows', '15 ppm', 'oily water separator', 'oil filtering', 'alarm', 'marpol'], en: ['oil filtering equipment', '15 ppm', 'bilge', 'separator', 'stopping device'], sections: ['Pt C, Ch 1, Sec 10', 'Pt F, Ch 7, Sec 4'] },
  { tr: ['insineratör', 'incinerator', 'atık yakma', 'sewage', 'pis su'], en: ['incinerators', 'sewage', 'pollution', 'flame failure', 'alarms'], sections: ['Pt F, Ch 7, App 3', 'Pt F, Ch 7, Sec 4'] },
  { tr: ['soğutma', 'reefer', 'refrigerating', 'soğutucu akışkan', 'buzluk'], en: ['refrigerating installations', 'compressors', 'pressure vessels', 'leak test', 'pneumatic'], sections: ['Pt F, Ch 8, Sec 1'] },
  { tr: ['trafo', 'transformatör', 'transformer', 'izolasyon trafosu'], en: ['transformers', 'high voltage test', 'induced voltage', 'insulation resistance', 'temperature rise', '2 U + 1000', '1.5.3'], sections: ['Pt C, Ch 2, Sec 5'] },
  { tr: ['alternatör', 'jeneratör', 'generator', 'alternator', 'elektrik motoru', 'electric motor', 'rotating machine', 'avr', 'stator', 'rotor'], en: ['rotating machines', 'generators', 'motors', 'dielectric strength', 'overspeed', 'insulation resistance', 'table 2'], sections: ['Pt C, Ch 2, Sec 4'] },
  { tr: ['pano', 'ana pano', 'acil pano', 'switchboard', 'msb', 'esb', 'mcc', 'dağıtım panosu', 'bara', 'busbar', 'şalter', 'circuit breaker'], en: ['switchboards', 'busbars', 'high voltage test', 'insulation resistance', 'circuit-breakers', 'table 2', 'table 3'], sections: ['Pt C, Ch 2, Sec 8', 'Pt C, Ch 2, Sec 6'] },
  { tr: ['kablo', 'cable', 'deniz kablosu', 'flame retardant', 'fire resistant', 'iec 60332', 'iec 60331'], en: ['cables', 'high voltage test', 'insulation resistance', 'flame', 'fire resistant'], sections: ['Pt C, Ch 2, Sec 9'] },
  { tr: ['akü', 'batarya', 'ups', 'şarj', 'battery', 'charger', 'uninterruptible', 'redresör'], en: ['storage batteries', 'chargers', 'uninterruptible power', 'ups', 'ventilation', 'capacity test'], sections: ['Pt C, Ch 2, Sec 6'] },
  { tr: ['otomasyon', 'alarm', 'pms', 'automation', 'control console', 'plc', 'scada', 'sensör', 'bilgisayar'], en: ['automation', 'programmable electronic', 'environmental tests', 'power supply failure', 'alarm system'], sections: ['Pt C, Ch 3, Sec 6', 'Pt C, Ch 3, Sec 3'] },
  { tr: ['siber', 'siber güvenlik', 'cyber', 'ur e27', 'ur e26', 'firewall', 'network'], en: ['cyber resilience', 'security', 'software', 'computer based'], sections: ['Pt C, Ch 3, Sec 3', 'Pt C, Ch 3, Sec 6'] },
  { tr: ['yangın', 'yangın damperi', 'fire damper', 'a-60', 'yangın kapısı', 'fire door', 'co2', 'water mist', 'köpük', 'foam', 'dedektör'], en: ['fire protection', 'fire dampers', 'fire doors', 'extinguishing', 'co2', 'detection'], sections: ['Pt C, Ch 4, Sec 1', 'Pt C, Ch 4, Sec 2'] },
  { tr: ['sac', 'gemi sacı', 'çelik plaka', 'ah36', 'dh36', 'eh36', 'fh36', 'normal mukavemet', 'steel plate', 'flat bar', 'profil', 'charpy', 'darbe testi'], en: ['normal and higher strength', 'rolled steel', 'plates', 'tensile test', 'charpy v-notch', 'impact test', 'ah36', 'dh36', 'eh36'], sections: ['Pt D, Ch 2, Sec 1'] },
  { tr: ['dövme', 'çelik dövme', 'forging', 'steel forging', 'krank dövme', 'şaft dövme'], en: ['steel forgings', 'tensile', 'impact', 'ultrasonic', 'magnetic particle', 'heat treatment'], sections: ['Pt D, Ch 2, Sec 3'] },
  { tr: ['döküm', 'çelik döküm', 'casting', 'steel casting', 'stern frame', 'dümen bodoslaması'], en: ['steel castings', 'heat treatment', 'ndt', 'ultrasonic', 'magnetic', 'weld repair'], sections: ['Pt D, Ch 2, Sec 4'] },
  { tr: ['bakır', 'bronz', 'cu1', 'cu2', 'cu3', 'cu4', 'copper alloy', 'pirinç', 'pervane döküm'], en: ['copper alloy', 'propellers', 'castings', 'cu1', 'cu2', 'cu3', 'cu4', 'repair welding'], sections: ['Pt D, Ch 3, Sec 2', 'Pt D, Ch 3, Sec 1'] },
  { tr: ['çapa', 'zincir', 'anchor', 'chain cable', 'stud link', 'kilit', 'shackle', 'fırdöndü', 'swivel', 'proof load', 'breaking load'], en: ['anchors', 'chain cables', 'proof load', 'breaking load', 'drop test', 'ndt'], sections: ['Pt D, Ch 4, Sec 1'] },
  { tr: ['tel halat', 'halat', 'wire rope', 'fiber rope', 'mooring rope'], en: ['steel wire ropes', 'fibre ropes', 'breaking load', 'zinc coating', '4.4', '5.4'], sections: ['Pt D, Ch 4, Sec 1'] },
  { tr: ['kaynak', 'wpqr', 'wps', 'welding', 'kaynak prosedürü', 'elektrot', 'teli', 'alın kaynağı', 'köşe kaynağı'], en: ['welding procedure', 'wpqr', 'butt weld', 'fillet weld', 'radiographic', 'ultrasonic', 'bend test', 'macro'], sections: ['Pt D, Ch 5, Sec 4', 'Pt D, Ch 5, Sec 2'] },
  { tr: ['su geçirmez kapı', 'watertight door', 'borda kapısı', 'shell door', 'bow door', 'stern door', 'rampa', 'ramp'], en: ['watertight doors', 'bow doors', 'side doors', 'stern doors', 'hydrostatic test', 'hose test'], sections: ['Pt B, Ch 2, Sec 1', 'Pt B, Ch 9, Sec 5', 'Pt B, Ch 9, Sec 6', 'Pt B, Ch 12, Sec 3'] },
  { tr: ['ambar kapağı', 'hatch cover', 'mezerna', 'coaming', 'weathertight', 'hortum testi', 'hose test', 'tebeşir testi'], en: ['hatch covers', 'coamings', 'hose test', 'ultrasonic', 'weathertight', 'closing devices'], sections: ['Pt B, Ch 9, Sec 7', 'Pt B, Ch 12, Sec 3'] },
  { tr: ['havalandırma', 'ventilator', 'hava firar', 'air pipe', 'iskandil', 'sounding pipe', 'discharges', 'frengi', 'freeing port', 'zincirlik'], en: ['ventilators', 'discharges', 'freeing ports', 'chain lockers', 'companionway', 'skylights'], sections: ['Pt B, Ch 9, Sec 9'] },
  { tr: ['tank testi', 'tank testing', 'structural test', 'leak test', 'hava testi', 'air test', 'balast tankı'], en: ['testing', 'structural test', 'leak test', 'hose test', 'hydropneumatic', 'compartments'], sections: ['Pt B, Ch 12, Sec 3'] }
];

const state = {
  equipmentList: [],
  rulesIndex: [],
  rulesFull: null,
  rulesLoading: false,
  selectedEquipmentId: 'sidescuttles-windows-skylights',
  activeDynamicSheet: null,
  matchedPdfPages: [],
  lastQuery: '',
  langMode: 'both', // 'both' | 'en' | 'tr'
  answers: {},
  aiCache: {},
  modalSectionId: 'Pt D, Ch 4, Sec 1',
  modalCurrentPage: 2521,
  deferredInstallPrompt: null
};

const STORAGE_KEYS = {
  STATE: 'rina_leonardo_state_v3',
  AI_CACHE: 'rina_leonardo_ai_cache_v3'
};

document.addEventListener('DOMContentLoaded', async () => {
  loadPersistedState();
  bindEvents();
  setupPwaHandlers();
  await loadDatabases();
});

function loadPersistedState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.STATE);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed.selectedEquipmentId) state.selectedEquipmentId = parsed.selectedEquipmentId;
      if (parsed.langMode) state.langMode = parsed.langMode;
      if (parsed.answers) state.answers = parsed.answers;
      if (parsed.activeDynamicSheet) state.activeDynamicSheet = parsed.activeDynamicSheet;
    }
    const cacheRaw = localStorage.getItem(STORAGE_KEYS.AI_CACHE);
    if (cacheRaw) {
      state.aiCache = JSON.parse(cacheRaw) || {};
    }
  } catch (e) {
    console.warn('State restore warning:', e);
  }
}

function persistState() {
  try {
    localStorage.setItem(
      STORAGE_KEYS.STATE,
      JSON.stringify({
        selectedEquipmentId: state.selectedEquipmentId,
        langMode: state.langMode,
        answers: state.answers,
        activeDynamicSheet: state.activeDynamicSheet
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

    for (const eq of state.equipmentList) {
      if (!state.answers[eq.id]) state.answers[eq.id] = {};
      for (const q of eq.applicationTerms || []) {
        if (state.answers[eq.id][q.id] === undefined) {
          state.answers[eq.id][q.id] = q.default;
        }
      }
    }

    populatePresetSelect();
    syncQuickPills();
    renderLeonardoSheet();

    // Load full 1,645-page RINA 2026 PDF database in background
    ensureFullRulesLoaded();
  } catch (err) {
    console.error('Database load error:', err);
  }
}

async function ensureFullRulesLoaded() {
  if (state.rulesFull) return state.rulesFull;
  if (state.rulesLoading) {
    while (state.rulesLoading) {
      await new Promise((r) => setTimeout(r, 60));
    }
    return state.rulesFull;
  }
  state.rulesLoading = true;
  try {
    const res = await fetch('/data/rina-rules-2026-sections.json');
    state.rulesFull = await res.json();
    const eq = getCurrentEquipment();
    if (eq) {
      state.matchedPdfPages = getPdfPagesForEquipment(eq);
      renderMatchedPdfPagesPanel();
    }
  } catch (e) {
    console.warn('Full rules load error:', e);
  } finally {
    state.rulesLoading = false;
  }
  return state.rulesFull;
}

function populatePresetSelect() {
  const sel = document.getElementById('presetEquipmentSelect');
  if (!sel) return;
  sel.innerHTML = state.equipmentList
    .map(
      (eq) =>
        `<option value="${escapeHtml(eq.id)}" ${!state.activeDynamicSheet && eq.id === state.selectedEquipmentId ? 'selected' : ''}>
          ${escapeHtml(eq.titleEn)} — ${escapeHtml(eq.titleTr)}
        </option>`
    )
    .join('');
}

function syncQuickPills() {
  document.querySelectorAll('#aiQuickChips .eq-pill').forEach((btn) => {
    btn.classList.toggle('active', !state.activeDynamicSheet && btn.dataset.eqId === state.selectedEquipmentId);
  });
}

function getCurrentEquipment() {
  if (state.activeDynamicSheet) return state.activeDynamicSheet;
  return (
    state.equipmentList.find((e) => e.id === state.selectedEquipmentId) ||
    state.equipmentList[0]
  );
}

/* =====================================================
   FORMAT RULE REFERENCE INTO LEONARDO STYLE:
   e.g. "Pt C, Ch 2, Sec 5, [1.5.3]" -> "Part. C - Ch. 2 - Sec. 5 - Par. 1.5.3"
   ===================================================== */
function toLeonardoRuleFormat(rawRef) {
  if (!rawRef) return '';
  if (rawRef.includes('Part.')) return rawRef;
  return rawRef
    .replace(/\bPt\s+([A-F])\b/gi, 'Part. $1')
    .replace(/,\s*Ch\s+(\d+)/gi, ' - Ch. $1')
    .replace(/,\s*Sec\s+(\d+)/gi, ' - Sec. $1')
    .replace(/,\s*App\s+(\d+)/gi, ' - App. $1')
    .replace(/,?\s*\[([\d.]+)\s*[a-z]?\]/gi, ' - Par. $1');
}

function toParenLeonardoCitation(rawRef) {
  if (!rawRef) return '';
  if (rawRef.trim().startsWith('(Part.')) return rawRef.trim();
  const clean = rawRef
    .replace(/\bPt\s+([A-F])\b/gi, 'Part. $1')
    .replace(/,\s*Ch\s+(\d+)/gi, ' Ch. $1')
    .replace(/,\s*Sec\s+(\d+)/gi, ' Sec. $1')
    .replace(/,\s*App\s+(\d+)/gi, ' App. $1')
    .replace(/,?\s*\[([\d.]+)\s*[a-z]?\]/gi, ' Par. $1')
    .replace(/,\s*Tab\.?\s*(\d+)/gi, ' Tab. $1')
    .trim();
  return `(${clean})`;
}

/* =====================================================
   OFFICIAL LEONARDO TEST SHEET RENDERER (Matches screenshot 100%)
   ===================================================== */
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

  const showEn = state.langMode === 'both' || state.langMode === 'en';
  const showTr = state.langMode === 'both' || state.langMode === 'tr';

  const todayStr = new Date().toLocaleDateString('en-GB', {
    day: '2-digit',
    month: 'short',
    year: 'numeric'
  });

  // Format top Rule References (can be split by / )
  const ruleRefLines = (eq.ruleRef || eq.sectionId || '')
    .split(/\s*\/\s*/)
    .map((r) => toLeonardoRuleFormat(r.trim()))
    .filter(Boolean);

  const ruleRefHtml = ruleRefLines
    .map((line, i) => {
      const targetSec = resolveSectionIdFromCitation(line, eq.sectionId);
      const targetPage = resolvePageFromCitation(line, targetSec, eq.pdfPage);
      return `
        <div>
          ${i === 0 ? 'Rule Reference: ' : ''}
          <button type="button" class="leo-ref-clickable js-open-rule" data-sec="${escapeHtml(targetSec)}" data-page="${targetPage}" title="Orijinal RINA 2026 PDF Sayfasını Aç (s.${targetPage})">
            ${escapeHtml(line)}
          </button>
        </div>
      `;
    })
    .join('');

  // Section 1: APPLICATION TERMS
  const appTerms = eq.applicationTerms || [];
  const appTermsSectionHtml =
    appTerms.length > 0
      ? `
    <div class="leo-block">
      <div class="leo-sec-heading">APPLICATION TERMS</div>
      <div class="leo-sec-subheading">
        List of circumstances which affect the applicable acceptance requirements and certification activities
        ${showTr ? `<span class="leo-sec-subheading-tr">🇹🇷 Uygulanacak kabul gereksinimlerini ve fabrika test adımlarını belirleyen uygulama koşulları</span>` : ''}
      </div>
      <table class="leo-clean-table">
        <thead>
          <tr>
            <th style="width: 78%;">Questions</th>
            <th style="width: 22%;">Answers</th>
          </tr>
        </thead>
        <tbody>
          ${appTerms
            .map((q) => {
              const currentVal = eqAnswers[q.id] ?? q.default;
              const optionsHtml = (q.options || [
                { value: 'Yes', labelEn: 'Yes', labelTr: 'Yes (Evet)' },
                { value: 'No', labelEn: 'No', labelTr: 'No (Hayır)' }
              ])
                .map(
                  (opt) => `
                  <option value="${escapeHtml(opt.value)}" ${opt.value === currentVal ? 'selected' : ''}>
                    ${escapeHtml(state.langMode === 'en' ? opt.labelEn : opt.labelTr || opt.value)}
                  </option>
                `
                )
                .join('');
              return `
                <tr>
                  <td>
                    ${showEn ? `<div>${escapeHtml(q.questionEn)}</div>` : ''}
                    ${showTr ? `<div class="leo-tr-subline">🇹🇷 ${escapeHtml(q.questionTr)}</div>` : ''}
                  </td>
                  <td>
                    <select class="leo-inline-select answer-select" data-question-id="${escapeHtml(q.id)}">
                      ${optionsHtml}
                    </select>
                  </td>
                </tr>
              `;
            })
            .join('')}
        </tbody>
      </table>
    </div>
  `
      : '';

  // Section 2: ACCEPTANCE REQUIREMENTS
  const accReqs = eq.acceptanceRequirements || [];
  const accReqSectionHtml =
    accReqs.length > 0
      ? `
    <div class="leo-block">
      <div class="leo-sec-heading">ACCEPTANCE REQUIREMENTS</div>
      <div class="leo-sec-subheading">
        List of rule references of applicable design, construction and inspection requirements
        ${showTr ? `<span class="leo-sec-subheading-tr">🇹🇷 İlgili tasarım, imalat ve muayene kurallarının RINA 2026 kural referansları (Tıklayarak PDF sayfasını açabilirsiniz)</span>` : ''}
      </div>
      <table class="leo-clean-table">
        <thead>
          <tr>
            <th style="width: 34%;">Rule references</th>
            <th style="width: 66%;">Acceptance Requirement</th>
          </tr>
        </thead>
        <tbody>
          ${accReqs
            .map((r) => {
              const fmtRef = toLeonardoRuleFormat(r.ruleRef).replace(/\s*-\s*/g, ' ');
              const secId = r.sectionId || resolveSectionIdFromCitation(r.ruleRef, eq.sectionId);
              const pg = r.page || eq.pdfPage;
              return `
                <tr>
                  <td>
                    <button type="button" class="leo-ref-clickable js-open-rule" data-sec="${escapeHtml(secId)}" data-page="${pg}">
                      ${escapeHtml(fmtRef)}
                    </button>
                  </td>
                  <td>
                    ${showEn ? `<div>${escapeHtml(r.reqEn)}</div>` : ''}
                    ${showTr ? `<div class="leo-tr-subline">🇹🇷 ${escapeHtml(r.reqTr)}</div>` : ''}
                  </td>
                </tr>
              `;
            })
            .join('')}
        </tbody>
      </table>
    </div>
  `
      : '';

  // Section 3: CERTIFICATION ACTIVITIES
  // Ensure step (1) is ALWAYS the standard Leonardo calibration verification step if not already present!
  const rawSteps = (eq.certificationActivities || []).filter((step) => isStepApplicable(step, eqAnswers));
  const finalSteps = [];

  const firstIsCalibration =
    rawSteps.length > 0 &&
    rawSteps[0].titleEn.toLowerCase().includes('calibration status');

  if (!firstIsCalibration) {
    finalSteps.push({
      isCalibrationStep: true,
      ruleRef: '',
      sectionId: eq.sectionId,
      page: eq.pdfPage,
      titleEn: 'The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.',
      detailEn: '',
      titleTr: 'Test ölçüm cihazlarının kalibrasyon durumu ve uygunluğu tatmin edici şekilde doğrulanmıştır.',
      detailTr: 'Fabrika testinde kullanılan tüm ölçü aletlerinin (manometre, multimetre, megger, yük hücresi, takometre, kumpas vb.) geçerli kalibrasyon sertifikaları kontrol edilir.',
      tipTr: ''
    });
  }

  for (const s of rawSteps) {
    finalSteps.push(s);
  }

  const activitiesHtml = finalSteps
    .map((step, idx) => {
      const displayNum = idx + 1;
      const secId = step.sectionId || eq.sectionId;
      const pg = step.page || eq.pdfPage;

      // Format English title in exact Leonardo style:
      // (2) Drawings approval (Part. B Ch. 1 Sec. 3 Par. 1)
      let mainTitleText = step.titleEn;
      let citationHtml = '';
      if (!step.isCalibrationStep && step.ruleRef && step.ruleRef !== 'General' && !mainTitleText.includes('(Part.')) {
        const parenCite = toParenLeonardoCitation(step.ruleRef);
        citationHtml = ` <button type="button" class="rule-cite-btn js-open-rule" data-sec="${escapeHtml(secId)}" data-page="${pg}" title="PDF Sayfa ${pg} Aç">${escapeHtml(parenCite)}</button>`;
      } else {
        // Make any embedded (Part. ...) inside mainTitleText clickable
        mainTitleText = linkifyParentheticalCitations(escapeHtml(mainTitleText), secId, pg);
      }

      const subDetailEn = step.detailEn
        ? step.detailEn.trim().startsWith('-')
          ? step.detailEn.trim()
          : `- ${step.detailEn.trim()}`
        : '';

      return `
        <div class="leo-activity-row">
          ${
            showEn
              ? `
            <div class="leo-act-main-line">
              (${displayNum}) ${citationHtml ? escapeHtml(step.titleEn) + citationHtml : mainTitleText}
            </div>
            ${subDetailEn ? `<div class="leo-act-sub-line">${escapeHtml(subDetailEn)}</div>` : ''}
          `
              : `
            <div class="leo-act-main-line">
              (${displayNum}) ${escapeHtml(step.titleTr)}
              ${!step.isCalibrationStep && step.ruleRef ? `<button type="button" class="rule-cite-btn js-open-rule" data-sec="${escapeHtml(secId)}" data-page="${pg}">(${escapeHtml(step.ruleRef)} — PDF s.${pg})</button>` : ''}
            </div>
          `
          }

          ${
            showTr
              ? `
            <div class="leo-act-tr-box">
              ${showEn ? `<div class="leo-act-tr-title">🇹🇷 (${displayNum}) ${escapeHtml(step.titleTr)}</div>` : ''}
              ${step.detailTr ? `<div class="leo-act-tr-detail">${escapeHtml(step.detailTr)}</div>` : ''}
              ${step.tipTr ? `<div class="leo-act-tr-tip">💡 <strong>Saha Notu / Kural Özeti:</strong> ${escapeHtml(step.tipTr)}</div>` : ''}
            </div>
          `
              : ''
          }
        </div>
      `;
    })
    .join('');

  // Calculator & Reference Tables (from RINA 2026 PDF)
  const calcHtml = eq.calculator ? renderCalculatorHtml(eq) : '';
  const refTablesHtml =
    eq.referenceTables && eq.referenceTables.length > 0
      ? `
      <div class="leo-ref-section">
        ${eq.referenceTables
          .map(
            (tbl) => `
          <div class="ref-table-box">
            <div class="ref-table-caption">
              📊 ${showEn ? escapeHtml(tbl.titleEn) : ''} ${showEn && showTr ? ' — ' : ''} ${showTr ? escapeHtml(tbl.titleTr) : ''}
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

  container.innerHTML = `
    <!-- Top-Right CERTIFICATION ACTIVITIES / Leonardo TEST -->
    <div class="leo-top-title-block">
      <div class="leo-top-main-title">CERTIFICATION ACTIVITIES</div>
      <div class="leo-top-sub-title">Leonardo TEST</div>
    </div>

    <!-- Split Header with Vertical Line | in Center -->
    <div class="leo-split-header">
      <div class="leo-split-left">
        <svg viewBox="0 0 155 58" width="118" height="44" aria-label="RINA">
          <text x="2" y="43" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="38" fill="#003359">R</text>
          <text x="33" y="43" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="38" fill="#003359">I</text>
          <polygon points="66,2 73,24 66,20 59,24" fill="#0072bc"/>
          <polygon points="66,56 73,34 66,38 59,34" fill="#0072bc"/>
          <polygon points="46,29 61,24 57,29 61,34" fill="#38bdf8"/>
          <polygon points="86,29 71,24 75,29 71,34" fill="#38bdf8"/>
          <text x="88" y="43" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="38" fill="#003359">A</text>
        </svg>
      </div>

      <div class="leo-split-right">
        <div class="leo-cert-according-line">Certification according to RINA Rules for the Classification of Ships - Products</div>
        ${showEn ? `<div class="leo-product-name-en">${escapeHtml(eq.titleEn)} (See Application Terms below)</div>` : ''}
        ${showTr ? `<div class="leo-product-name-tr">🇹🇷 ${escapeHtml(eq.titleTr)}</div>` : ''}
      </div>
    </div>

    <!-- Date of issue & Rule Reference Row -->
    <div class="leo-date-ruleref-row">
      <div class="leo-date-cell">
        Date of issue: <strong>${todayStr}</strong>
      </div>
      <div class="leo-ruleref-cell">
        ${ruleRefHtml}
      </div>
    </div>

    ${appTermsSectionHtml}
    ${accReqSectionHtml}

    <!-- CERTIFICATION ACTIVITIES -->
    <div class="leo-block">
      <div class="leo-sec-heading">CERTIFICATION ACTIVITIES</div>
      <div class="leo-sec-subheading">
        List of documentation checks carried out by RINA Services S.p.A. and tests witnessed by the Surveyor
        ${showTr ? `<span class="leo-sec-subheading-tr">🇹🇷 RINA tarafından yapılan doküman kontrolleri ve Sörveyör huzurunda (Witness) yapılan fabrika testleri (Kural parantezlerine tıklayarak orijinal 2026 PDF sayfasını açabilirsiniz)</span>` : ''}
      </div>

      <div class="leo-activities-list">
        ${activitiesHtml}
      </div>
    </div>

    ${calcHtml ? `<div class="leo-ref-section no-print">${calcHtml}</div>` : ''}
    ${refTablesHtml}

    <div class="leo-page-footer">
      <span>RINA Rules for the Classification of Ships 2026</span>
      <span>Page 1 of 1</span>
    </div>
  `;

  bindSheetEvents(eq);
}

function linkifyParentheticalCitations(escapedHtml, defaultSecId, defaultPage) {
  return escapedHtml.replace(/\(Part\.\s*([A-F])\s+Ch\.\s*(\d+)\s+Sec\.\s*(\d+)[^)]*\)/gi, (match, part, ch, sec) => {
    const secId = `Pt ${part.toUpperCase()}, Ch ${ch}, Sec ${sec}`;
    const pg = resolvePageFromCitation(match, secId, defaultPage);
    return `<button type="button" class="rule-cite-btn js-open-rule" data-sec="${escapeHtml(secId)}" data-page="${pg}" title="PDF Sayfa ${pg} Aç">${match}</button>`;
  });
}

function resolveSectionIdFromCitation(citationStr, fallbackSecId) {
  if (!citationStr) return fallbackSecId;
  const m = citationStr.match(/(?:Part\.|Pt)\s*([A-F])\s*[-,]?\s*Ch\.?\s*(\d+)\s*[-,]?\s*(Sec|App)\.?\s*(\d+)/i);
  if (m) {
    const kind = m[3].toLowerCase().startsWith('app') ? 'App' : 'Sec';
    const candidate = `Pt ${m[1].toUpperCase()}, Ch ${m[2]}, ${kind} ${m[4]}`;
    if (state.rulesIndex.some((s) => s.id === candidate)) return candidate;
  }
  return fallbackSecId;
}

function resolvePageFromCitation(citationStr, secId, fallbackPage) {
  const sec = state.rulesIndex.find((s) => s.id === secId);
  if (!sec) return fallbackPage || 1442;
  const mPar = citationStr.match(/Par\.?\s*(\d+)(?:\.(\d+))?/i);
  if (mPar && sec.articles) {
    const mainArt = mPar[1];
    const subArt = mPar[2] ? `${mPar[1]}.${mPar[2]}` : null;
    if (subArt) {
      const foundSub = sec.articles.find((a) => a.title.includes(`SubArticle - ${subArt} `));
      if (foundSub) return foundSub.page;
    }
    const foundArt = sec.articles.find((a) => a.title.includes(`Article - ${mainArt} `));
    if (foundArt) return foundArt.page;
  }
  return sec.start_page || fallbackPage;
}

function bindSheetEvents(eq) {
  document.querySelectorAll('#leonardoSheet .answer-select').forEach((sel) => {
    sel.addEventListener('change', () => {
      const qId = sel.dataset.questionId;
      if (!state.answers[eq.id]) state.answers[eq.id] = {};
      state.answers[eq.id][qId] = sel.value;
      persistState();
      renderLeonardoSheet();
    });
  });

  updateCalculatorValues(eq);
  document.querySelectorAll('#leonardoSheet .calc-box input').forEach((inp) => {
    inp.addEventListener('input', () => updateCalculatorValues(eq));
  });

  document.querySelectorAll('#leonardoSheet .js-open-rule').forEach((btn) => {
    btn.addEventListener('click', () => {
      const secId = btn.dataset.sec || eq.sectionId;
      const page = parseInt(btn.dataset.page, 10) || eq.pdfPage;
      openRuleModal(secId, page);
    });
  });
}

/* =====================================================
   QUICK FIELD CALCULATORS
   ===================================================== */
function renderCalculatorHtml(eq) {
  const c = eq.calculator;
  if (!c) return '';

  if (c.type === 'transformer') {
    return `
      <div class="calc-box">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0b5a7a;">HV = 2U + 1000V (min 2500V) | Endüklenen = 2U</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Anma Gerilimi U (V)</label>
            <input type="number" id="calcTrafoU" value="${c.defaultVoltage || 440}" min="12" max="36000" />
          </div>
          <div class="calc-input-group">
            <label>Anma Frekansı fn (Hz)</label>
            <input type="number" id="calcTrafoFn" value="${c.defaultFreq || 60}" min="50" max="60" />
          </div>
          <div class="calc-input-group">
            <label>Test Frekansı fp (Hz)</label>
            <input type="number" id="calcTrafoFp" value="${(c.defaultFreq || 60) * 2}" min="50" max="400" />
          </div>
          <div class="calc-results" id="calcTrafoResults"></div>
        </div>
      </div>
    `;
  }

  if (c.type === 'rotating_machine') {
    return `
      <div class="calc-box">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0b5a7a;">Part. C Ch. 2 Sec. 4 Tab. 2</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Anma Gerilimi Un (V)</label>
            <input type="number" id="calcRotU" value="${c.defaultVoltage || 440}" min="24" max="15000" />
          </div>
          <div class="calc-input-group">
            <label>Anma Devri n (RPM)</label>
            <input type="number" id="calcRotRpm" value="${c.defaultSpeed || 1800}" min="100" max="3600" />
          </div>
          <div class="calc-results" id="calcRotResults"></div>
        </div>
      </div>
    `;
  }

  if (c.type === 'switchboard') {
    return `
      <div class="calc-box">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0b5a7a;">Part. C Ch. 2 Sec. 8 Par. 3.3.4</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Ana Bara Ui (V)</label>
            <input type="number" id="calcSwbUi" value="${c.defaultVoltage || 440}" min="24" max="1000" />
          </div>
          <div class="calc-input-group">
            <label>Kumanda Ui (V)</label>
            <input type="number" id="calcSwbAux" value="${c.defaultAuxVoltage || 230}" min="12" max="690" />
          </div>
          <div class="calc-results" id="calcSwbResults"></div>
        </div>
      </div>
    `;
  }

  if (c.type === 'pressure_vessel' || c.type === 'pump_compressor' || c.type === 'valve_pipe') {
    return `
      <div class="calc-box">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0b5a7a;">1 MPa = 10 bar</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Tasarım Basıncı p (bar)</label>
            <input type="number" id="calcPressBar" value="${c.defaultPressureBar || 10}" min="0.5" max="1000" step="0.5" />
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
        <div class="calc-res-card"><span class="lbl">Yüksek Gerilim (HV) [1.5.3]</span><span class="val">${hv} V AC (60 s)</span></div>
        <div class="calc-res-card"><span class="lbl">Endüklenen Gerilim [1.5.6]</span><span class="val">${indV} V @ ${fp}Hz (${indTime} s)</span></div>
        <div class="calc-res-card"><span class="lbl">Min. Megger [1.5.5]</span><span class="val">≥ 5 MΩ (@ 500V DC)</span></div>
      `;
    }
  } else if (type === 'rotating_machine') {
    const u = parseFloat(document.getElementById('calcRotU')?.value) || 440;
    const rpm = parseFloat(document.getElementById('calcRotRpm')?.value) || 1800;
    const hv = Math.max(1500, Math.round(2 * u + 1000));
    const overspeed = Math.round(rpm * 1.2);
    const el = document.getElementById('calcRotResults');
    if (el) {
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Dielektrik (HV) [4.9]</span><span class="val">${hv} V AC (60 s)</span></div>
        <div class="calc-res-card"><span class="lbl">Min. Megger [Tab. 2]</span><span class="val">≥ 1 MΩ (@ 500V DC)</span></div>
        <div class="calc-res-card"><span class="lbl">Overspeed [4.8]</span><span class="val">${overspeed} RPM (2 min)</span></div>
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
    const auxHv = uaux <= 60 ? 500 : Math.max(1500, Math.round(2 * uaux + 1000));
    const el = document.getElementById('calcSwbResults');
    if (el) {
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Ana Bara HV [Tab. 2]</span><span class="val">${mainHv} V AC (60 s)</span></div>
        <div class="calc-res-card"><span class="lbl">Kumanda HV [Tab. 3]</span><span class="val">${auxHv} V AC (60 s)</span></div>
        <div class="calc-res-card"><span class="lbl">Min. Megger [3.4]</span><span class="val">≥ 1 MΩ (@ ≥500V DC)</span></div>
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
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Hidrostatik Test pt [7.3.2]</span><span class="val">${(ptMpa * 10).toFixed(1)} bar</span></div>
        <div class="calc-res-card"><span class="lbl">Hava Tüpü / Aksesuar (1.5×p)</span><span class="val">${(1.5 * pBar).toFixed(1)} bar</span></div>
      `;
    } else if (type === 'pump_compressor') {
      let phMpa = 1.5 * pMpa;
      if (pMpa > 4 && pMpa <= 25) phMpa = 1.4 * pMpa + 0.4;
      else if (pMpa > 25) phMpa = pMpa + 10.4;
      phMpa = Math.max(0.4, phMpa);
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Gövde Hidrotest pH [21.4.5]</span><span class="val">${(phMpa * 10).toFixed(1)} bar (min 4 bar)</span></div>
        <div class="calc-res-card"><span class="lbl">Su Ceketi (1.5×p) [21.4.5d]</span><span class="val">${Math.max(2.0, 1.5 * pBar).toFixed(1)} bar</span></div>
      `;
    } else if (type === 'valve_pipe') {
      el.innerHTML = `
        <div class="calc-res-card"><span class="lbl">Valf Gövde (1.5×p) / Sit (1.1×p)</span><span class="val">${(1.5 * pBar).toFixed(1)} bar / ${(1.1 * pBar).toFixed(1)} bar</span></div>
        <div class="calc-res-card"><span class="lbl">Borda Valfi [21.4.3b]</span><span class="val">${Math.max(5.0, 1.5 * pBar).toFixed(1)} bar (min 5 bar)</span></div>
        <div class="calc-res-card"><span class="lbl">Boru Devresi (2×p) [21.4.2e]</span><span class="val">${Math.max(4.0, 2.0 * pBar).toFixed(1)} bar</span></div>
      `;
    }
  }
}

/* =====================================================
   MATCHED VERBATIM RINA 2026 PDF PAGES PANEL
   ===================================================== */
function getPdfPagesForEquipment(eq) {
  if (!state.rulesFull || !eq) return [];
  const targetMap = new Map();

  const addPage = (secId, pgNo) => {
    const sec = state.rulesFull.find((s) => s.id === secId);
    if (!sec) return;
    const found = sec.pages.find((p) => p.page === pgNo);
    if (found) {
      targetMap.set(`${secId}-${pgNo}`, {
        secId: sec.id,
        chapter: sec.chapter,
        section: sec.section,
        page: found.page,
        text: found.text
      });
    }
  };

  addPage(eq.sectionId, eq.pdfPage);
  (eq.acceptanceRequirements || []).forEach((r) => {
    addPage(r.sectionId || eq.sectionId, r.page || eq.pdfPage);
  });
  (eq.certificationActivities || []).forEach((s) => {
    addPage(s.sectionId || eq.sectionId, s.page || eq.pdfPage);
    if (s.page) addPage(s.sectionId || eq.sectionId, s.page + 1);
  });

  return Array.from(targetMap.values()).slice(0, 6);
}

function renderMatchedPdfPagesPanel() {
  const panel = document.getElementById('matchedPdfPagesPanel');
  if (!panel) return;

  const pages = state.matchedPdfPages || [];
  if (pages.length === 0) {
    panel.innerHTML = '';
    return;
  }

  const terms = state.lastQuery
    ? expandQueryToRinaTerms(state.lastQuery).terms.filter((t) => t.length >= 3)
    : [];

  panel.innerHTML = `
    <div class="pdf-extracts-header">
      <div>
        <div style="font-size:0.75rem; font-weight:700; color:#0b5a7a;">📖 RINA RULES 2026 PDF — İLGİLİ ORİJİNAL KURAL SAYFALARI</div>
        <h3 style="font-size:1rem; color:#003359; margin-top:0.15rem;">
          Bu Leonardo TEST Sayfasının Dayandığı Orijinal RINA 2026 PDF Metinleri (${pages.length} Sayfa)
        </h3>
      </div>
      <span style="font-size:0.76rem; color:#475569;">Tam bölümü açmak için sayfa butonuna tıklayın</span>
    </div>
    ${pages
      .map(
        (p) => `
      <div class="pdf-page-block">
        <div class="pdf-page-header">
          <span>${escapeHtml(p.secId)} &bull; ${escapeHtml(p.chapter)} — ${escapeHtml(p.section)}</span>
          <button type="button" class="btn-xs js-open-matched-pdf" data-sec="${escapeHtml(p.secId)}" data-page="${p.page}">
            📄 PDF Sayfa ${p.page} Tam Görünüm Aç
          </button>
        </div>
        <div class="pdf-page-text">${highlightMultipleTerms(p.text, terms)}</div>
      </div>
    `
      )
      .join('')}
  `;

  panel.querySelectorAll('.js-open-matched-pdf').forEach((btn) => {
    btn.addEventListener('click', () => {
      openRuleModal(btn.dataset.sec, parseInt(btn.dataset.page, 10));
    });
  });
}

/* =====================================================
   HYBRID INSTANT + GEMINI AI PDF SEARCH ENGINE
   ===================================================== */
function expandQueryToRinaTerms(rawQuery) {
  const qLower = rawQuery.toLowerCase().trim();
  const expandedTerms = new Set();
  const boostedSections = new Set();

  qLower
    .replace(/[^\w\sçğıöşü.,/-]/gi, ' ')
    .split(/\s+/)
    .filter((w) => w.length >= 2)
    .forEach((w) => expandedTerms.add(w));

  for (const entry of MARINE_SYNONYMS) {
    if (entry.tr.some((term) => qLower.includes(term))) {
      entry.en.forEach((enTerm) => expandedTerms.add(enTerm.toLowerCase()));
      entry.sections.forEach((secId) => boostedSections.add(secId));
    }
  }

  return {
    terms: Array.from(expandedTerms),
    boostedSections: Array.from(boostedSections)
  };
}

function searchRinaPdfPages(rawQuery, fullDb, extraTerms = [], extraSections = [], maxPages = 6) {
  if (!fullDb || !fullDb.length) return [];
  const { terms, boostedSections } = expandQueryToRinaTerms(rawQuery);
  const allTerms = Array.from(new Set([...terms, ...extraTerms.map((t) => t.toLowerCase())]));
  const allBoostedSecs = new Set([...boostedSections, ...extraSections]);
  const fatSignalWords = ['test', 'hydrostatic', 'hydraulic', 'pressure', 'witness', 'surveyor', 'certificate', 'inspection', 'table', 'voltage', 'insulation', 'charpy', 'tensile', 'ndt', 'tightness'];

  const scoredPages = [];

  for (const sec of fullDb) {
    const isBoostedSec = allBoostedSecs.has(sec.id);
    const secHeaderLower = `${sec.id} ${sec.chapter} ${sec.section}`.toLowerCase();

    for (const pg of sec.pages) {
      const textLower = pg.text.toLowerCase();
      let score = isBoostedSec ? 18 : 0;
      let matchedTermCount = 0;

      for (const term of allTerms) {
        if (!term || term.length < 2) continue;
        if (secHeaderLower.includes(term)) score += 10;
        const idx = textLower.indexOf(term);
        if (idx !== -1) {
          matchedTermCount++;
          let count = 0;
          let pos = idx;
          while (pos !== -1 && count < 5) {
            count++;
            pos = textLower.indexOf(term, pos + term.length);
          }
          const weight = term.includes(' ') ? 12 : term.length >= 6 ? 7 : 4;
          score += weight * (1 + Math.log1p(count));
        }
      }

      if (matchedTermCount === 0 && !isBoostedSec) continue;

      if (matchedTermCount > 0) {
        for (const sig of fatSignalWords) {
          if (textLower.includes(sig)) score += 2.5;
        }
      }

      if (score > 8) {
        scoredPages.push({
          secId: sec.id,
          part: sec.part,
          chapter: sec.chapter,
          section: sec.section,
          page: pg.page,
          text: pg.text,
          score
        });
      }
    }
  }

  scoredPages.sort((a, b) => b.score - a.score);
  return scoredPages.slice(0, maxPages);
}

function findMatchingPreset(query) {
  const q = query.toLowerCase().trim();
  if (!q) return null;

  let best = null;
  let bestScore = 0;

  for (const eq of state.equipmentList) {
    let sc = 0;
    const tTr = eq.titleTr.toLowerCase();
    const tEn = eq.titleEn.toLowerCase();
    if (tTr === q || tEn === q) sc += 100;
    if (tTr.includes(q) || tEn.includes(q)) sc += 35;

    const words = q.split(/\s+/).filter((w) => w.length >= 2);
    const hay = `${tTr} ${tEn} ${(eq.keywords || []).join(' ')} ${eq.ruleRef}`.toLowerCase();
    const matchedWords = words.filter((w) => hay.includes(w));
    if (words.length > 0 && matchedWords.length === words.length) {
      sc += 40;
    } else {
      sc += matchedWords.length * 12;
    }

    if (sc > bestScore) {
      bestScore = sc;
      best = eq;
    }
  }

  return bestScore >= 24 ? best : null;
}

async function callGeminiInteraction({ model, systemInstruction, input, responseFormat }) {
  const body = {
    model: model || GEMINI_CONFIG.fastModel,
    input,
    store: false
  };
  if (systemInstruction) body.system_instruction = systemInstruction;
  if (responseFormat) body.response_format = responseFormat;

  const res = await fetch(`${GEMINI_CONFIG.endpoint}?key=${GEMINI_CONFIG.apiKey}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });

  if (!res.ok) {
    throw new Error(`Gemini HTTP ${res.status}`);
  }

  const data = await res.json();
  return (data.steps || [])
    .filter((s) => s.type === 'model_output')
    .flatMap((s) => s.content || [])
    .map((c) => c.text || '')
    .join('')
    .trim();
}

async function handleSearchSubmit(rawQuery) {
  const query = rawQuery.trim();
  if (!query) return;
  state.lastQuery = query;

  // 1. Check if it directly matches one of our 24 verified Leonardo TEST sheets — if so, show it INSTANTLY (<5ms)!
  const directPreset = findMatchingPreset(query);
  if (directPreset) {
    state.activeDynamicSheet = null;
    state.selectedEquipmentId = directPreset.id;
    persistState();
    populatePresetSelect();
    syncQuickPills();
    renderLeonardoSheet();
    if (state.rulesFull) {
      state.matchedPdfPages = getPdfPagesForEquipment(directPreset);
      renderMatchedPdfPagesPanel();
    }
    showToast(`✓ ${directPreset.titleEn} (${directPreset.titleTr}) Leonardo TEST sayfası açıldı.`);
    return;
  }

  // 2. Otherwise, run AI-Powered RINA 2026 PDF Search & Leonardo TEST Synthesis!
  const submitBtn = document.getElementById('aiSearchSubmitBtn');
  const progBanner = document.getElementById('aiProgressBanner');
  const progTitle = document.getElementById('aiProgressTitle');

  if (submitBtn) submitBtn.disabled = true;
  progBanner?.classList.remove('hidden');
  if (progTitle) progTitle.textContent = `"${query}" için RINA Rules 2026 PDF taranıyor ve Leonardo TEST sayfası hazırlanıyor...`;

  try {
    const fullDb = await ensureFullRulesLoaded();
    const cacheKey = query.toLowerCase();

    if (state.aiCache[cacheKey]) {
      state.activeDynamicSheet = state.aiCache[cacheKey].sheet;
      state.matchedPdfPages = searchRinaPdfPages(query, fullDb, state.aiCache[cacheKey].keywordsEn || [], [], 5);
      persistState();
      populatePresetSelect();
      syncQuickPills();
      renderLeonardoSheet();
      renderMatchedPdfPagesPanel();
      showToast('✨ RINA 2026 PDF Leonardo TEST sayfası yüklendi.');
      return;
    }

    let topPages = searchRinaPdfPages(query, fullDb, [], [], 5);

    if ((!topPages.length || topPages[0].score < 30) && navigator.onLine) {
      try {
        const expStr = await callGeminiInteraction({
          model: GEMINI_CONFIG.fastModel,
          systemInstruction:
            'Convert the marine surveyor query into English RINA Rules 2026 keywords and likely RINA section IDs (e.g. "Pt B, Ch 9, Sec 9", "Pt D, Ch 4, Sec 1", "Pt C, Ch 1, Sec 10", "Pt C, Ch 1, Sec 3", "Pt C, Ch 2, Sec 4").',
          input: `Query: "${query}"`,
          responseFormat: {
            type: 'object',
            properties: {
              keywordsEn: { type: 'array', items: { type: 'string' } },
              sectionIds: { type: 'array', items: { type: 'string' } }
            },
            required: ['keywordsEn', 'sectionIds']
          }
        });
        const exp = JSON.parse(expStr);
        const retry = searchRinaPdfPages(query, fullDb, exp.keywordsEn || [], exp.sectionIds || [], 5);
        if (retry.length > 0) topPages = retry;
      } catch (e) {
        console.warn('Query expansion fallback:', e);
      }
    }

    state.matchedPdfPages = topPages;
    renderMatchedPdfPagesPanel();

    const pdfContext = topPages
      .slice(0, 5)
      .map((p) => `=== SECTION: ${p.secId} (${p.chapter} - ${p.section}) | PDF PAGE: ${p.page} ===\n${p.text}`)
      .join('\n\n')
      .slice(0, 14000);

    const aiJsonStr = await callGeminiInteraction({
      model: GEMINI_CONFIG.fastModel,
      systemInstruction: `You are RINA's official LEONARDO TEST Certification Activities generator grounded strictly on the RINA Rules for the Classification of Ships 2026 PDF.
Given the surveyor's query and the retrieved RINA 2026 PDF pages, generate an official Leonardo TEST sheet:
- Use official Leonardo TEST Rule Reference format: e.g. "Part. B - Ch. 9 - Sec. 9 - Par. 3 / Part. D - Ch. 4 - Sec. 1 - Par. 6"
- In certificationActivities:
  - Activity (1) MUST be: "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified."
  - Subsequent activities (2), (3), (4), (5), (6) must follow official RINA Leonardo TEST naming with parenthetical rule references in the titleEn, e.g.:
    - "Drawings approval (Part. B Ch. 1 Sec. 3 Par. 1) (Part. ...)" with detailEn starting with "- "
    - "Testing of materials (Part. ...)" with exact test loads/pressures/mandrel/Charpy/tensile details from the PDF in detailEn and detailTr
    - "Visual, dimensional examination and NDT (Part. ...)"
    - "Hydraulic / Hydrostatic / Electrical / Functional test (Part. ...)" with exact test formulas/pressures from the PDF
    - "Final inspection and marking (Part. ...)"`,
      input: `SURVEYOR QUERY: "${query}"\n\nRINA RULES 2026 PDF PAGES:\n${pdfContext}`,
      responseFormat: {
        type: 'object',
        properties: {
          titleEn: { type: 'string' },
          titleTr: { type: 'string' },
          ruleRef: { type: 'string' },
          sectionId: { type: 'string' },
          pdfPage: { type: 'integer' },
          keywordsEn: { type: 'array', items: { type: 'string' } },
          applicationTerms: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                id: { type: 'string' },
                questionEn: { type: 'string' },
                questionTr: { type: 'string' },
                defaultValue: { type: 'string' }
              },
              required: ['id', 'questionEn', 'questionTr', 'defaultValue']
            }
          },
          acceptanceRequirements: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                ruleRef: { type: 'string' },
                sectionId: { type: 'string' },
                page: { type: 'integer' },
                reqEn: { type: 'string' },
                reqTr: { type: 'string' }
              },
              required: ['ruleRef', 'sectionId', 'page', 'reqEn', 'reqTr']
            }
          },
          certificationActivities: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                ruleRef: { type: 'string' },
                sectionId: { type: 'string' },
                page: { type: 'integer' },
                titleEn: { type: 'string' },
                detailEn: { type: 'string' },
                titleTr: { type: 'string' },
                detailTr: { type: 'string' },
                tipTr: { type: 'string' }
              },
              required: ['ruleRef', 'sectionId', 'page', 'titleEn', 'detailEn', 'titleTr', 'detailTr', 'tipTr']
            }
          }
        },
        required: ['titleEn', 'titleTr', 'ruleRef', 'sectionId', 'pdfPage', 'applicationTerms', 'acceptanceRequirements', 'certificationActivities']
      }
    });

    const aiData = JSON.parse(aiJsonStr);
    const primarySec = topPages[0]?.secId || resolveSectionIdFromCitation(aiData.sectionId, 'Pt C, Ch 1, Sec 10');
    const primaryPage = topPages[0]?.page || aiData.pdfPage || 1442;

    const sheet = {
      id: `ai-${Date.now()}`,
      isAiGenerated: true,
      titleEn: aiData.titleEn,
      titleTr: aiData.titleTr,
      ruleRef: aiData.ruleRef,
      sectionId: primarySec,
      pdfPage: primaryPage,
      applicationTerms: (aiData.applicationTerms || []).map((q, i) => ({
        id: q.id || `q_${i + 1}`,
        questionEn: q.questionEn,
        questionTr: q.questionTr,
        default: q.defaultValue === 'No' ? 'No' : 'Yes',
        options: [
          { value: 'Yes', labelEn: 'Yes', labelTr: 'Yes (Evet)' },
          { value: 'No', labelEn: 'No', labelTr: 'No (Hayır)' }
        ]
      })),
      acceptanceRequirements: (aiData.acceptanceRequirements || []).map((r) => ({
        ruleRef: r.ruleRef,
        sectionId: resolveSectionIdFromCitation(r.sectionId || r.ruleRef, primarySec),
        page: r.page || primaryPage,
        reqEn: r.reqEn,
        reqTr: r.reqTr
      })),
      certificationActivities: (aiData.certificationActivities || []).map((s, i) => ({
        num: i + 1,
        ruleRef: s.ruleRef,
        sectionId: resolveSectionIdFromCitation(s.sectionId || s.ruleRef, primarySec),
        page: s.page || primaryPage,
        condition: 'always',
        titleEn: s.titleEn,
        detailEn: s.detailEn,
        titleTr: s.titleTr,
        detailTr: s.detailTr,
        tipTr: s.tipTr
      }))
    };

    state.activeDynamicSheet = sheet;
    state.aiCache[cacheKey] = { sheet, keywordsEn: aiData.keywordsEn || [] };
    try {
      localStorage.setItem(STORAGE_KEYS.AI_CACHE, JSON.stringify(state.aiCache));
    } catch (e) {}

    persistState();
    populatePresetSelect();
    syncQuickPills();
    renderLeonardoSheet();
    renderMatchedPdfPagesPanel();
    showToast('✨ Yapay zeka RINA 2026 PDF kurallarından Leonardo TEST sayfasını oluşturdu.');
  } catch (err) {
    console.error('AI search error:', err);
    showToast('PDF arama tamamlandı.');
  } finally {
    progBanner?.classList.add('hidden');
    if (submitBtn) submitBtn.disabled = false;
  }
}

/* =====================================================
   FAST PAGINATED RINA 2026 PDF RULE MODAL
   ===================================================== */
async function openRuleModal(sectionId, targetPage) {
  const modal = document.getElementById('ruleModal');
  const badge = document.getElementById('ruleModalBadge');
  const title = document.getElementById('ruleModalTitle');
  const body = document.getElementById('ruleModalBody');
  const pills = document.getElementById('modalArticlePills');
  const filterInput = document.getElementById('modalRuleFilterInput');
  const secSelect = document.getElementById('modalSectionSelect');
  const pageSelect = document.getElementById('modalPageSelect');
  const prevBtn = document.getElementById('modalPrevPageBtn');
  const nextBtn = document.getElementById('modalNextPageBtn');

  modal.classList.remove('hidden');
  badge.textContent = sectionId;
  title.textContent = 'RINA Rules 2026 PDF Yükleniyor...';
  body.innerHTML = `<div style="padding:2rem; text-align:center;">⏳ 2026 RINA Kural veritabanından ilgili sayfa açılıyor...</div>`;

  const fullDb = await ensureFullRulesLoaded();
  if (!fullDb) {
    body.innerHTML = `<div style="padding:2rem; color:#991b1b;">Kural veritabanı yüklenemedi.</div>`;
    return;
  }

  let sec = fullDb.find((s) => s.id === sectionId) || fullDb[0];
  state.modalSectionId = sec.id;
  state.modalCurrentPage = sec.pages.some((p) => p.page === targetPage)
    ? targetPage
    : sec.pages[0]?.page || sec.start_page;

  // Populate section selector (all 132 sections)
  if (secSelect) {
    secSelect.innerHTML = fullDb
      .map((s) => `<option value="${escapeHtml(s.id)}" ${s.id === sec.id ? 'selected' : ''}>${escapeHtml(s.id)} — ${escapeHtml(s.section)}</option>`)
      .join('');
    secSelect.onchange = () => {
      const nextSec = fullDb.find((s) => s.id === secSelect.value);
      if (nextSec) openRuleModal(nextSec.id, nextSec.start_page);
    };
  }

  badge.textContent = `${sec.id} (PDF Sayfa ${sec.start_page}–${sec.end_page})`;
  title.textContent = `${sec.chapter} — ${sec.section}`;
  filterInput.value = '';

  pageSelect.innerHTML = sec.pages
    .map((p) => `<option value="${p.page}" ${p.page === state.modalCurrentPage ? 'selected' : ''}>PDF Sayfa ${p.page} / ${sec.end_page}</option>`)
    .join('');

  pills.innerHTML = (sec.articles || [])
    .filter((a) => a.level <= 5)
    .slice(0, 30)
    .map(
      (a) => `
      <button type="button" class="btn-xs js-modal-page-jump" data-page="${a.page}">
        ${escapeHtml(a.title.replace(/^(Sub)?Article - /, ''))} (s.${a.page})
      </button>
    `
    )
    .join('');

  const renderModalView = () => {
    const q = filterInput.value.trim().toLowerCase();
    if (q.length >= 2) {
      const matched = sec.pages.filter((p) => p.text.toLowerCase().includes(q)).slice(0, 8);
      if (matched.length === 0) {
        body.innerHTML = `<div style="padding:1.5rem; text-align:center;">Bu bölümde "${escapeHtml(filterInput.value)}" bulunamadı.</div>`;
        return;
      }
      body.innerHTML = matched
        .map(
          (p) => `
          <div class="pdf-page-block" style="border: 2px solid #0b5a7a;">
            <div class="pdf-page-header">
              <span>${escapeHtml(sec.id)} &bull; ${escapeHtml(sec.section)}</span>
              <span>PDF Sayfa ${p.page}</span>
            </div>
            <div class="pdf-page-text">${highlightText(p.text, q)}</div>
          </div>
        `
        )
        .join('');
      return;
    }

    const idx = sec.pages.findIndex((p) => p.page === state.modalCurrentPage);
    const slice = idx !== -1 ? sec.pages.slice(idx, idx + 2) : sec.pages.slice(0, 2);
    pageSelect.value = String(state.modalCurrentPage);
    prevBtn.disabled = idx <= 0;
    nextBtn.disabled = idx === -1 || idx >= sec.pages.length - 1;

    body.innerHTML = slice
      .map(
        (p, i) => `
        <div class="pdf-page-block" style="${i === 0 ? 'border: 2px solid #0b5a7a;' : ''}">
          <div class="pdf-page-header">
            <span>${escapeHtml(sec.id)} &bull; ${escapeHtml(sec.section)}</span>
            <span>PDF Sayfa ${p.page}</span>
          </div>
          <div class="pdf-page-text">${escapeHtml(p.text)}</div>
        </div>
      `
      )
      .join('');
    body.scrollTop = 0;
  };

  renderModalView();

  pageSelect.onchange = () => {
    state.modalCurrentPage = parseInt(pageSelect.value, 10);
    filterInput.value = '';
    renderModalView();
  };

  prevBtn.onclick = () => {
    const idx = sec.pages.findIndex((p) => p.page === state.modalCurrentPage);
    if (idx > 0) {
      state.modalCurrentPage = sec.pages[idx - 1].page;
      filterInput.value = '';
      renderModalView();
    }
  };

  nextBtn.onclick = () => {
    const idx = sec.pages.findIndex((p) => p.page === state.modalCurrentPage);
    if (idx !== -1 && idx < sec.pages.length - 1) {
      state.modalCurrentPage = sec.pages[idx + 1].page;
      filterInput.value = '';
      renderModalView();
    }
  };

  pills.querySelectorAll('.js-modal-page-jump').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.modalCurrentPage = parseInt(btn.dataset.page, 10);
      filterInput.value = '';
      renderModalView();
    });
  });

  let debounceTimer = null;
  filterInput.oninput = () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(renderModalView, 180);
  };
}

/* =====================================================
   EVENTS & PWA SETUP
   ===================================================== */
function bindEvents() {
  const searchForm = document.getElementById('aiSearchForm');
  const searchInp = document.getElementById('aiSearchInput');
  const clearBtn = document.getElementById('clearSearchBtn');

  searchForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    if (searchInp?.value.trim()) {
      handleSearchSubmit(searchInp.value.trim());
    }
  });

  searchInp?.addEventListener('input', () => {
    clearBtn?.classList.toggle('hidden', !searchInp.value);
  });

  clearBtn?.addEventListener('click', () => {
    if (searchInp) searchInp.value = '';
    clearBtn.classList.add('hidden');
    searchInp?.focus();
  });

  // Quick Equipment Pills (Instant zero-delay selection!)
  document.querySelectorAll('#aiQuickChips .eq-pill').forEach((btn) => {
    btn.addEventListener('click', () => {
      const eqId = btn.dataset.eqId;
      if (!eqId) return;
      state.activeDynamicSheet = null;
      state.selectedEquipmentId = eqId;
      persistState();
      populatePresetSelect();
      syncQuickPills();
      renderLeonardoSheet();
      const eq = getCurrentEquipment();
      if (eq && state.rulesFull) {
        state.matchedPdfPages = getPdfPagesForEquipment(eq);
        renderMatchedPdfPagesPanel();
      }
    });
  });

  // Preset Dropdown (Instant selection)
  const presetSel = document.getElementById('presetEquipmentSelect');
  presetSel?.addEventListener('change', () => {
    const val = presetSel.value;
    if (!val) return;
    state.activeDynamicSheet = null;
    state.selectedEquipmentId = val;
    persistState();
    syncQuickPills();
    renderLeonardoSheet();
    const eq = getCurrentEquipment();
    if (eq && state.rulesFull) {
      state.matchedPdfPages = getPdfPagesForEquipment(eq);
      renderMatchedPdfPagesPanel();
    }
  });

  // Language mode buttons
  document.querySelectorAll('#langModeControl .lang-btn').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.lang === state.langMode);
    btn.addEventListener('click', () => {
      state.langMode = btn.dataset.lang;
      document.querySelectorAll('#langModeControl .lang-btn').forEach((b) => {
        b.classList.toggle('active', b.dataset.lang === state.langMode);
      });
      persistState();
      renderLeonardoSheet();
    });
  });

  document.getElementById('openFullPdfExplorerBtn')?.addEventListener('click', () => {
    const eq = getCurrentEquipment();
    openRuleModal(eq?.sectionId || 'Pt D, Ch 4, Sec 1', eq?.pdfPage || 2521);
  });

  document.getElementById('printSheetBtn')?.addEventListener('click', () => {
    window.print();
  });

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
}

function setupPwaHandlers() {
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
      .register('/sw.js')
      .then((reg) => reg.update())
      .catch((err) => console.warn('SW error:', err));
  }

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
  return escaped.replace(new RegExp(`(${safeQ})`, 'gi'), '<mark class="hl">$1</mark>');
}

function highlightMultipleTerms(text, terms) {
  const escaped = escapeHtml(text);
  if (!terms || !terms.length) return escaped;
  const clean = terms
    .filter((t) => t && t.length >= 3)
    .slice(0, 6)
    .map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
  if (!clean.length) return escaped;
  return escaped.replace(new RegExp(`(${clean.join('|')})`, 'gi'), '<mark class="hl">$1</mark>');
}

function showToast(msg) {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const el = document.createElement('div');
  el.className = 'toast';
  el.textContent = msg;
  container.appendChild(el);
  setTimeout(() => el.remove(), 2800);
}
