/* RINA Marine Surveyor — AI-Powered RINA Rules 2026 PDF Finder & Leonardo TEST PWA */

const GEMINI_CONFIG = {
  apiKey: 'AIzaSyBkSjxPeFbMxy-KsLPFz-8TswT_WXK5evY',
  endpoint: 'https://generativelanguage.googleapis.com/v1beta/interactions',
  fastModel: 'gemini-3.5-flash-lite',
  proModel: 'gemini-3.8-flash'
};

// Comprehensive Turkish <-> English RINA Rules 2026 Marine Surveyor Dictionary & Section Router
const MARINE_SYNONYMS = [
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
  { tr: ['tel halat', 'halat', 'wire rope', 'fiber rope', 'mooring rope'], en: ['steel wire ropes', 'fibre ropes', 'breaking load', 'zinc coating'], sections: ['Pt D, Ch 4, Sec 2'] },
  { tr: ['kaynak', 'wpqr', 'wps', 'welding', 'kaynak prosedürü', 'elektrot', 'teli', 'alın kaynağı', 'köşe kaynağı'], en: ['welding procedure', 'wpqr', 'butt weld', 'fillet weld', 'radiographic', 'ultrasonic', 'bend test', 'macro'], sections: ['Pt D, Ch 5, Sec 4', 'Pt D, Ch 5, Sec 2'] },
  { tr: ['su geçirmez kapı', 'watertight door', 'borda kapısı', 'shell door', 'bow door', 'stern door', 'rampa', 'ramp'], en: ['watertight doors', 'bow doors', 'side doors', 'stern doors', 'hydrostatic test', 'hose test'], sections: ['Pt B, Ch 2, Sec 1', 'Pt B, Ch 9, Sec 5', 'Pt B, Ch 9, Sec 6', 'Pt B, Ch 12, Sec 3'] },
  { tr: ['ambar kapağı', 'hatch cover', 'mezerna', 'coaming', 'weathertight', 'hortum testi', 'hose test', 'tebeşir testi'], en: ['hatch covers', 'coamings', 'hose test', 'ultrasonic', 'weathertight', 'closing devices'], sections: ['Pt B, Ch 9, Sec 7', 'Pt B, Ch 12, Sec 3'] },
  { tr: ['tank testi', 'tank testing', 'structural test', 'leak test', 'hava testi', 'air test', 'balast tankı'], en: ['testing', 'structural test', 'leak test', 'hose test', 'hydropneumatic', 'compartments'], sections: ['Pt B, Ch 12, Sec 3'] },
  { tr: ['boya', 'korozyon', 'katodik koruma', 'anot', 'psp', 'coating', 'corrosion', 'anode'], en: ['protection of hull', 'coating', 'cathodic protection', 'anodes'], sections: ['Pt B, Ch 11, Sec 1'] }
];

const state = {
  equipmentList: [],
  rulesIndex: [],
  rulesFull: null,
  rulesLoading: false,
  selectedEquipmentId: 'valves-piping-fittings',
  activeDynamicSheet: null, // Holds AI-generated Leonardo TEST sheet when user searches!
  aiSummary: null, // Holds AI direct rule summary & formulas
  matchedPdfPages: [], // Holds verbatim RINA 2026 PDF pages found for current query
  lastQuery: '',
  langMode: 'both', // 'both' | 'en' | 'tr'
  stepFilterMode: 'dynamic', // 'dynamic' | 'all'
  answers: {},
  checklist: {},
  meta: {
    factory: '',
    project: '',
    serial: '',
    typeSerial: '',
    surveyor: ''
  },
  savedInspections: [],
  aiCache: {}, // Cache AI search results in localStorage for instant repeat & offline access
  activeRuleSectionId: 'Pt C, Ch 1, Sec 10',
  modalSectionId: 'Pt C, Ch 1, Sec 10',
  modalCurrentPage: 1941,
  deferredInstallPrompt: null
};

const STORAGE_KEYS = {
  STATE: 'rina_fat_pwa_active_state_v2',
  SAVED: 'rina_fat_pwa_saved_inspections_v1',
  AI_CACHE: 'rina_fat_pwa_ai_search_cache_v2'
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
      if (parsed.activeDynamicSheet) state.activeDynamicSheet = parsed.activeDynamicSheet;
      if (parsed.aiSummary) state.aiSummary = parsed.aiSummary;
      if (parsed.matchedPdfPages) state.matchedPdfPages = parsed.matchedPdfPages;
      if (parsed.lastQuery) state.lastQuery = parsed.lastQuery;
    }
    const savedRaw = localStorage.getItem(STORAGE_KEYS.SAVED);
    if (savedRaw) {
      state.savedInspections = JSON.parse(savedRaw) || [];
    }
    const cacheRaw = localStorage.getItem(STORAGE_KEYS.AI_CACHE);
    if (cacheRaw) {
      state.aiCache = JSON.parse(cacheRaw) || {};
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
        meta: state.meta,
        activeDynamicSheet: state.activeDynamicSheet,
        aiSummary: state.aiSummary,
        matchedPdfPages: (state.matchedPdfPages || []).slice(0, 6),
        lastQuery: state.lastQuery
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
    if (state.lastQuery) {
      const inp = document.getElementById('aiSearchInput');
      if (inp) inp.value = state.lastQuery;
      document.getElementById('clearSearchBtn')?.classList.remove('hidden');
    }

    renderAiSummaryCard();
    renderLeonardoSheet();
    renderMatchedPdfPagesPanel();
    renderRulesSidebar();
    renderSavedInspections();

    // Load full 1,631-page RINA 2026 PDF database in background immediately
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
      await new Promise((r) => setTimeout(r, 60));
    }
    return state.rulesFull;
  }
  state.rulesLoading = true;
  try {
    const res = await fetch('/data/rina-rules-2026-sections.json');
    state.rulesFull = await res.json();
    // If Matched PDF panel is empty on initial load, populate it with current equipment's PDF pages
    if (!state.matchedPdfPages || state.matchedPdfPages.length === 0) {
      const eq = getCurrentEquipment();
      if (eq) {
        state.matchedPdfPages = getPdfPagesForEquipment(eq);
        renderMatchedPdfPagesPanel();
      }
    }
    const rulesTab = document.getElementById('tab-rules');
    if (rulesTab?.classList.contains('active')) {
      renderSelectedRuleSectionInTab(state.activeRuleSectionId);
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
  sel.innerHTML =
    `<option value="">— Hazır Leonardo TEST Şablonu Seçin (23 Ekipman/Malzeme) —</option>` +
    state.equipmentList
      .map(
        (eq) =>
          `<option value="${escapeHtml(eq.id)}" ${!state.activeDynamicSheet && eq.id === state.selectedEquipmentId ? 'selected' : ''}>
            [${escapeHtml(eq.ruleRef)}] ${escapeHtml(eq.titleTr)} (${escapeHtml(eq.titleEn)})
          </option>`
      )
      .join('');
}

/* =====================================================
   BILINGUAL RINA 2026 PDF RETRIEVAL ENGINE (BM25 + SYNONYM ROUTER)
   ===================================================== */
function expandQueryToRinaTerms(rawQuery) {
  const qLower = rawQuery.toLowerCase().trim();
  const expandedTerms = new Set();
  const boostedSections = new Set();

  // Add raw query words (>= 2 chars)
  qLower
    .replace(/[^\w\sçğıöşü.,/-]/gi, ' ')
    .split(/\s+/)
    .filter((w) => w.length >= 2)
    .forEach((w) => expandedTerms.add(w));

  // Match against Marine Surveyor TR<->EN Dictionary
  for (const entry of MARINE_SYNONYMS) {
    const matched = entry.tr.some((term) => qLower.includes(term));
    if (matched) {
      entry.en.forEach((enTerm) => expandedTerms.add(enTerm.toLowerCase()));
      entry.sections.forEach((secId) => boostedSections.add(secId));
    }
  }

  // Also check if user typed explicit section or rule numbers like "Sec 10", "21.4", "Pt C"
  const secMatch = qLower.match(/sec(?:tion)?\s*(\d+)/i);
  if (secMatch) expandedTerms.add(`section ${secMatch[1]}`);

  return {
    terms: Array.from(expandedTerms),
    boostedSections: Array.from(boostedSections)
  };
}

function searchRinaPdfPages(rawQuery, fullDb, extraTerms = [], extraSections = [], maxPages = 7) {
  if (!fullDb || !fullDb.length) return [];
  const { terms, boostedSections } = expandQueryToRinaTerms(rawQuery);
  const allTerms = Array.from(new Set([...terms, ...extraTerms.map((t) => t.toLowerCase())]));
  const allBoostedSecs = new Set([...boostedSections, ...extraSections]);

  // Test-related keywords that surveyors care about most in FAT
  const fatSignalWords = ['test', 'hydrostatic', 'hydraulic', 'pressure', 'witness', 'surveyor', 'certificate', 'inspection', 'table', 'voltage', 'insulation', 'charpy', 'tensile', 'ndt', 'tightness', 'overload'];

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
        if (secHeaderLower.includes(term)) {
          score += 10;
        }
        const idx = textLower.indexOf(term);
        if (idx !== -1) {
          matchedTermCount++;
          // Count occurrences (up to 5)
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

      // Boost pages that contain testing/certification clauses when matchedTermCount > 0
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

function getPdfPagesForEquipment(eq) {
  if (!state.rulesFull || !eq) return [];
  const sec = state.rulesFull.find((s) => s.id === eq.sectionId);
  if (!sec) return [];
  const targetPages = new Set([eq.pdfPage]);
  (eq.certificationActivities || []).forEach((s) => {
    if (s.page) targetPages.add(s.page);
  });
  (eq.acceptanceRequirements || []).forEach((r) => {
    if (r.page) targetPages.add(r.page);
  });
  const pages = sec.pages
    .filter((p) => targetPages.has(p.page))
    .slice(0, 6)
    .map((p) => ({
      secId: sec.id,
      part: sec.part,
      chapter: sec.chapter,
      section: sec.section,
      page: p.page,
      text: p.text,
      score: 100
    }));
  if (pages.length === 0 && sec.pages.length > 0) {
    return sec.pages.slice(0, 3).map((p) => ({
      secId: sec.id,
      part: sec.part,
      chapter: sec.chapter,
      section: sec.section,
      page: p.page,
      text: p.text,
      score: 50
    }));
  }
  return pages;
}

/* =====================================================
   GEMINI AI + RINA 2026 PDF SEARCH & SYNTHESIS PIPELINE
   ===================================================== */
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
    const errText = await res.text();
    throw new Error(`Gemini API HTTP ${res.status}: ${errText}`);
  }

  const data = await res.json();
  const outputText = (data.steps || [])
    .filter((s) => s.type === 'model_output')
    .flatMap((s) => s.content || [])
    .map((c) => c.text || '')
    .join('')
    .trim();

  return outputText;
}

async function runAiPdfSearch(rawQuery) {
  const query = rawQuery.trim();
  if (!query) return;

  state.lastQuery = query;
  const inp = document.getElementById('aiSearchInput');
  if (inp && inp.value !== query) inp.value = query;
  document.getElementById('clearSearchBtn')?.classList.remove('hidden');

  // Highlight matching quick chip if any
  document.querySelectorAll('#aiQuickChips .q-chip').forEach((chip) => {
    chip.classList.toggle('active', chip.dataset.query?.toLowerCase() === query.toLowerCase());
  });

  const submitBtn = document.getElementById('aiSearchSubmitBtn');
  const progBanner = document.getElementById('aiProgressBanner');
  const progTitle = document.getElementById('aiProgressTitle');
  const progSub = document.getElementById('aiProgressSub');

  if (submitBtn) submitBtn.disabled = true;
  progBanner?.classList.remove('hidden');
  if (progTitle) progTitle.textContent = `🔍 "${query}" için RINA Rules 2026 PDF (1.631 sayfa) taranıyor...`;
  if (progSub) progSub.textContent = 'İlgili bölüm, tablo ve paragraflar PDF veritabanından çıkarılıyor...';

  try {
    const fullDb = await ensureFullRulesLoaded();

    // Check cache first for instant response
    const cacheKey = query.toLowerCase();
    if (state.aiCache[cacheKey] && fullDb) {
      const cached = state.aiCache[cacheKey];
      state.activeDynamicSheet = cached.sheet;
      state.aiSummary = cached.summary;
      state.matchedPdfPages = searchRinaPdfPages(
        query,
        fullDb,
        cached.searchKeywordsEn || [],
        cached.sheet?.sectionId ? [cached.sheet.sectionId] : [],
        6
      );
      initializeSheetAnswers(state.activeDynamicSheet);
      persistState();
      populatePresetSelect();
      renderAiSummaryCard();
      renderLeonardoSheet();
      renderMatchedPdfPagesPanel();
      progBanner?.classList.add('hidden');
      if (submitBtn) submitBtn.disabled = false;
      showToast('✨ RINA 2026 PDF kural ve test sonucu yüklendi.');
      return;
    }

    // Step 1: Local retrieval from 1,631-page RINA 2026 PDF
    let topPages = searchRinaPdfPages(query, fullDb, [], [], 6);

    // Check if query also matches one of our 23 curated equipment templates (to enrich calculator/tables)
    const matchedPreset = findBestMatchingPreset(query);

    // If the user wrote an unusual Turkish query that yielded weak local matches (< 35 score),
    // ask Gemini Flash-Lite in ~500ms to translate the query into exact RINA English search terms & section ID!
    if ((!topPages.length || topPages[0].score < 32) && navigator.onLine) {
      if (progSub) progSub.textContent = '✨ Yapay zeka Türkçe aramayı RINA 2026 İngilizce kural terimlerine çeviriyor...';
      try {
        const expansionJsonStr = await callGeminiInteraction({
          model: GEMINI_CONFIG.fastModel,
          systemInstruction:
            'You are a RINA Rules 2026 marine classification search router. Convert the user query into English RINA technical search keywords and likely RINA section IDs (e.g. "Pt C, Ch 1, Sec 10", "Pt C, Ch 1, Sec 3", "Pt C, Ch 2, Sec 4", "Pt D, Ch 2, Sec 1", "Pt B, Ch 12, Sec 3", "Pt B, Ch 9, Sec 7").',
          input: `User Query: "${query}"`,
          responseFormat: {
            type: 'object',
            properties: {
              keywordsEn: { type: 'array', items: { type: 'string' } },
              sectionIds: { type: 'array', items: { type: 'string' } }
            },
            required: ['keywordsEn', 'sectionIds']
          }
        });
        const exp = JSON.parse(expansionJsonStr);
        const retryPages = searchRinaPdfPages(query, fullDb, exp.keywordsEn || [], exp.sectionIds || [], 6);
        if (retryPages.length > 0) topPages = retryPages;
      } catch (expErr) {
        console.warn('Query expansion fallback:', expErr);
      }
    }

    // Immediately show the matched verbatim PDF pages at the bottom even before AI synthesis finishes!
    state.matchedPdfPages = topPages;
    renderMatchedPdfPagesPanel();

    const matchedPageLabels = topPages.map((p) => `${p.secId} (s.${p.page})`).join(', ');
    if (progTitle) {
      progTitle.textContent = `✨ PDF'ten ilgili sayfalar bulundu: ${matchedPageLabels || 'RINA 2026 Rules'}`;
    }
    if (progSub) {
      progSub.textContent = 'Yapay zeka (Gemini) bu PDF sayfalarındaki kuralları Leonardo TEST (EN + TR) formatına dönüştürüyor...';
    }

    // Build context from retrieved RINA 2026 PDF pages
    const pdfContext = topPages
      .slice(0, 5)
      .map((p) => `=== RINA 2026 PDF | SECTION: ${p.secId} (${p.chapter} - ${p.section}) | PDF PAGE: ${p.page} ===\n${p.text}`)
      .join('\n\n')
      .slice(0, 15000);

    // Step 2: Grounded AI Synthesis via Gemini Interactions API
    const aiResponseStr = await callGeminiInteraction({
      model: GEMINI_CONFIG.fastModel,
      systemInstruction: `You are an official RINA Marine Surveyor AI Assistant and Leonardo TEST Sheet Generator.
You are strictly grounded on the provided verbatim pages from "RINA Rules for the Classification of Ships (1 July 2026)".
Given the surveyor's search query and the retrieved RINA 2026 PDF pages:
1. Extract the exact RINA 2026 rule references (e.g. "Pt C, Ch 1, Sec 10, [21.4.3]") and exact PDF page numbers from the provided pages.
2. Provide a clear, accurate direct summary in both English (directAnswerEn) and Turkish (directAnswerTr) answering the surveyor's query and stating the required test pressures, voltages, material certificates (3.2 / 3.1), NDT, or inspection criteria.
3. Extract 2 to 4 key formulas or acceptance values (keyFormulas) with their exact rule clause.
4. Generate a complete Leonardo TEST sheet with:
   - 2 or 3 Application Terms questions (Yes/No)
   - 2 to 4 Acceptance Requirements with exact ruleRef, sectionId, page, reqEn, reqTr
   - 4 to 7 detailed Certification Activities (witnessed tests, document/NDT reviews, marking) with exact ruleRef, sectionId, page, verbatim-style English rule (titleEn, detailEn), detailed Turkish explanation for the surveyor (titleTr, detailTr), and practical field tip (tipTr).`,
      input: `SURVEYOR SEARCH QUERY: "${query}"\n\nRETRIEVED RINA RULES 2026 PDF PAGES:\n${pdfContext}`,
      responseFormat: {
        type: 'object',
        properties: {
          titleEn: { type: 'string' },
          titleTr: { type: 'string' },
          ruleRef: { type: 'string' },
          sectionId: { type: 'string' },
          pdfPage: { type: 'integer' },
          directAnswerEn: { type: 'string' },
          directAnswerTr: { type: 'string' },
          searchKeywordsEn: { type: 'array', items: { type: 'string' } },
          keyFormulas: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                labelTr: { type: 'string' },
                value: { type: 'string' },
                ruleClause: { type: 'string' }
              },
              required: ['labelTr', 'value', 'ruleClause']
            }
          },
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
        required: [
          'titleEn',
          'titleTr',
          'ruleRef',
          'sectionId',
          'pdfPage',
          'directAnswerEn',
          'directAnswerTr',
          'keyFormulas',
          'applicationTerms',
          'acceptanceRequirements',
          'certificationActivities'
        ]
      }
    });

    const aiData = JSON.parse(aiResponseStr);
    const primaryPage = topPages[0]?.page || aiData.pdfPage || 1442;
    const primarySec = topPages[0]?.secId || aiData.sectionId || 'Pt C, Ch 1, Sec 10';

    const dynamicId = `ai-${Date.now()}`;
    const dynamicSheet = {
      id: dynamicId,
      isAiGenerated: true,
      code: 'AI-PDF',
      category: matchedPreset?.category || 'machinery',
      titleEn: aiData.titleEn,
      titleTr: aiData.titleTr,
      ruleRef: aiData.ruleRef || primarySec,
      sectionId: primarySec,
      pdfPage: primaryPage,
      calculator: matchedPreset?.calculator || inferCalculatorForQuery(query, primarySec),
      referenceTables: matchedPreset?.referenceTables || [],
      applicationTerms: (aiData.applicationTerms || []).map((q, idx) => ({
        id: q.id || `q_${idx + 1}`,
        questionEn: q.questionEn,
        questionTr: q.questionTr,
        default: q.defaultValue === 'No' ? 'No' : 'Yes',
        options: [
          { value: 'Yes', labelEn: 'Yes', labelTr: 'Evet (Yes)' },
          { value: 'No', labelEn: 'No', labelTr: 'Hayır (No)' }
        ]
      })),
      acceptanceRequirements: (aiData.acceptanceRequirements || []).map((r) => ({
        ruleRef: r.ruleRef,
        sectionId: normalizeSectionId(r.sectionId, primarySec),
        page: r.page || primaryPage,
        reqEn: r.reqEn,
        reqTr: r.reqTr
      })),
      certificationActivities: (aiData.certificationActivities || []).map((step, idx) => ({
        num: idx + 1,
        ruleRef: step.ruleRef,
        sectionId: normalizeSectionId(step.sectionId, primarySec),
        page: step.page || primaryPage,
        condition: 'always',
        titleEn: step.titleEn,
        detailEn: step.detailEn,
        titleTr: step.titleTr,
        detailTr: step.detailTr,
        tipTr: step.tipTr
      }))
    };

    const summaryObj = {
      query,
      titleEn: aiData.titleEn,
      titleTr: aiData.titleTr,
      ruleRef: aiData.ruleRef || primarySec,
      sectionId: primarySec,
      pdfPage: primaryPage,
      directAnswerEn: aiData.directAnswerEn,
      directAnswerTr: aiData.directAnswerTr,
      keyFormulas: aiData.keyFormulas || [],
      followupAnswer: ''
    };

    state.activeDynamicSheet = dynamicSheet;
    state.aiSummary = summaryObj;

    // Save in AI cache (keep max 25 recent queries)
    state.aiCache[cacheKey] = {
      sheet: dynamicSheet,
      summary: summaryObj,
      searchKeywordsEn: aiData.searchKeywordsEn || []
    };
    try {
      const keys = Object.keys(state.aiCache);
      if (keys.length > 25) delete state.aiCache[keys[0]];
      localStorage.setItem(STORAGE_KEYS.AI_CACHE, JSON.stringify(state.aiCache));
    } catch (e) {
      console.warn('AI cache storage limit:', e);
    }

    initializeSheetAnswers(dynamicSheet);
    persistState();
    populatePresetSelect();
    renderAiSummaryCard();
    renderLeonardoSheet();
    renderMatchedPdfPagesPanel();
    showToast('✨ Yapay zeka RINA 2026 PDF kurallarını ve Leonardo TEST adımlarını hazırladı!');
  } catch (err) {
    console.error('AI PDF search error:', err);
    // Offline or fallback: build a sheet directly from the matched PDF pages or best preset!
    handleOfflineFallbackSearch(query);
  } finally {
    progBanner?.classList.add('hidden');
    if (submitBtn) submitBtn.disabled = false;
  }
}

function normalizeSectionId(candidate, fallbackSecId) {
  if (!candidate) return fallbackSecId;
  if (state.rulesIndex.some((s) => s.id === candidate)) return candidate;
  const m = candidate.match(/(Pt\s+[A-F],\s*Ch\s+\d+,\s*(?:Sec|App)\s+\d+)/i);
  if (m && state.rulesIndex.some((s) => s.id.toLowerCase() === m[1].toLowerCase())) {
    return state.rulesIndex.find((s) => s.id.toLowerCase() === m[1].toLowerCase()).id;
  }
  return fallbackSecId;
}

function findBestMatchingPreset(query) {
  const q = query.toLowerCase();
  let best = null;
  let bestScore = 0;
  for (const eq of state.equipmentList) {
    let sc = 0;
    if (eq.titleTr.toLowerCase().includes(q) || eq.titleEn.toLowerCase().includes(q)) sc += 25;
    for (const kw of eq.keywords || []) {
      if (q.includes(kw.toLowerCase())) sc += 10;
    }
    if (sc > bestScore) {
      bestScore = sc;
      best = eq;
    }
  }
  return bestScore >= 10 ? best : null;
}

function inferCalculatorForQuery(query, secId) {
  const q = query.toLowerCase();
  if (secId === 'Pt C, Ch 2, Sec 5' || q.includes('trafo') || q.includes('transformer')) {
    return { type: 'transformer', labelTr: 'Trafo Test Gerilimi Hesaplayıcı', defaultVoltage: 440, defaultFreq: 60 };
  }
  if (secId === 'Pt C, Ch 2, Sec 4' || q.includes('alternatör') || q.includes('generator') || q.includes('motor')) {
    return { type: 'rotating_machine', labelTr: 'Döner Elektrik Makinesi HV & Overspeed Hesaplayıcı', defaultVoltage: 440, defaultSpeed: 1800 };
  }
  if (secId === 'Pt C, Ch 2, Sec 8' || q.includes('pano') || q.includes('switchboard')) {
    return { type: 'switchboard', labelTr: 'Pano (MSB/ESB) Yüksek Gerilim Hesaplayıcı', defaultVoltage: 440, defaultAuxVoltage: 230 };
  }
  if (secId === 'Pt C, Ch 1, Sec 3' || q.includes('tüp') || q.includes('kazan') || q.includes('eşanjör') || q.includes('vessel') || q.includes('boiler')) {
    return { type: 'pressure_vessel', labelTr: 'Basınçlı Kap / Hava Tüpü / Kazan Hidrotest Hesaplayıcı', defaultPressureBar: 30 };
  }
  if (q.includes('pompa') || q.includes('pump') || q.includes('kompresör') || q.includes('compressor')) {
    return { type: 'pump_compressor', labelTr: 'Pompa & Kompresör Hidrostatik Test Hesaplayıcı', defaultPressureBar: 10 };
  }
  if (secId === 'Pt C, Ch 1, Sec 10' || q.includes('valf') || q.includes('vana') || q.includes('valve') || q.includes('boru') || q.includes('pipe')) {
    return { type: 'valve_pipe', labelTr: 'Valf (Gövde/Sit) & Boru Hidrostatik Test Hesaplayıcı', defaultPressureBar: 10 };
  }
  return null;
}

function handleOfflineFallbackSearch(query) {
  const preset = findBestMatchingPreset(query);
  if (preset) {
    state.activeDynamicSheet = null;
    state.selectedEquipmentId = preset.id;
    state.aiSummary = {
      query,
      titleEn: preset.titleEn,
      titleTr: preset.titleTr,
      ruleRef: preset.ruleRef,
      sectionId: preset.sectionId,
      pdfPage: preset.pdfPage,
      directAnswerEn: `Matched RINA 2026 Section ${preset.ruleRef} (PDF p.${preset.pdfPage}). See full Leonardo TEST steps and verbatim PDF pages below.`,
      directAnswerTr: `"${query}" aramanız için RINA 2026 ${preset.ruleRef} (PDF Sayfa ${preset.pdfPage}) kuralları ve Leonardo TEST adımları aşağıda listelenmiştir.`,
      keyFormulas: []
    };
    renderAiSummaryCard();
    renderLeonardoSheet();
    renderMatchedPdfPagesPanel();
    showToast('Çevrimdışı PDF eşleşmesi yüklendi.');
    return;
  }

  if (state.matchedPdfPages && state.matchedPdfPages.length > 0) {
    const top = state.matchedPdfPages[0];
    state.aiSummary = {
      query,
      titleEn: `${top.chapter} — ${top.section}`,
      titleTr: `${top.id} — PDF Sayfa ${top.page} Kural Sonucu`,
      ruleRef: `${top.secId} (PDF s.${top.page})`,
      sectionId: top.secId,
      pdfPage: top.page,
      directAnswerEn: top.text.slice(0, 420) + '...',
      directAnswerTr: `"${query}" için RINA 2026 PDF içinde en yüksek eşleşmeye sahip bölüm: ${top.secId} (${top.section}, PDF Sayfa ${top.page}). Aşağıdaki orijinal PDF sayfalarından tüm detayları inceleyebilirsiniz.`,
      keyFormulas: []
    };
    renderAiSummaryCard();
    renderMatchedPdfPagesPanel();
  }
}

function initializeSheetAnswers(sheet) {
  if (!sheet) return;
  if (!state.answers[sheet.id]) state.answers[sheet.id] = {};
  for (const q of sheet.applicationTerms || []) {
    if (state.answers[sheet.id][q.id] === undefined) {
      state.answers[sheet.id][q.id] = q.default || 'Yes';
    }
  }
}

/* =====================================================
   RENDER AI DIRECT RULE SUMMARY & FOLLOW-UP Q&A CARD
   ===================================================== */
function renderAiSummaryCard() {
  const card = document.getElementById('aiSummaryCard');
  if (!card) return;

  if (!state.aiSummary) {
    card.classList.add('hidden');
    card.innerHTML = '';
    return;
  }

  const s = state.aiSummary;
  const showEn = state.langMode === 'both' || state.langMode === 'en';
  const showTr = state.langMode === 'both' || state.langMode === 'tr';

  const formulasHtml =
    s.keyFormulas && s.keyFormulas.length > 0
      ? `
      <div class="ai-formulas-grid">
        ${s.keyFormulas
          .map(
            (f) => `
          <div class="ai-formula-card">
            <span class="f-lbl">📐 ${escapeHtml(f.labelTr)}</span>
            <span class="f-val">${escapeHtml(f.value)}</span>
            <span class="f-ref">📖 ${escapeHtml(f.ruleClause)}</span>
          </div>
        `
          )
          .join('')}
      </div>
    `
      : '';

  card.classList.remove('hidden');
  card.innerHTML = `
    <div class="ai-sum-header">
      <div>
        <span class="ai-sum-badge">✨ YAPAY ZEKA &bull; RINA 2026 PDF KURAL ÖZETİ</span>
        <h3 style="margin-top:0.35rem; color:#002b54; font-size:1.1rem;">
          ${escapeHtml(s.titleTr)} <span style="font-weight:500; color:#475569; font-size:0.92rem;">(${escapeHtml(s.titleEn)})</span>
        </h3>
      </div>
      <button type="button" class="leo-rule-link js-open-summary-pdf" data-sec="${escapeHtml(s.sectionId)}" data-page="${s.pdfPage}">
        📖 Kaynak PDF: <strong>${escapeHtml(s.ruleRef)}</strong> (Sayfa ${s.pdfPage} Aç)
      </button>
    </div>

    ${formulasHtml}

    <div class="ai-sum-grid">
      ${
        showTr
          ? `
        <div class="ai-answer-box tr">
          <div style="font-weight:800; margin-bottom:0.25rem;">🇹🇷 Türkçe Kural &amp; Test Özeti:</div>
          <div>${escapeHtml(s.directAnswerTr)}</div>
        </div>
      `
          : ''
      }
      ${
        showEn
          ? `
        <div class="ai-answer-box en">
          <div style="font-weight:800; margin-bottom:0.25rem;">🇬🇧 RINA 2026 Rule Summary (EN):</div>
          <div>${escapeHtml(s.directAnswerEn)}</div>
        </div>
      `
          : ''
      }
    </div>

    <!-- FOLLOW-UP QUESTION ON THIS PDF RULE -->
    <div class="ai-followup-wrap no-print">
      <div style="font-size:0.8rem; font-weight:700; color:#002b54;">
        💬 Bu Ekipman / Kural Hakkında Yapay Zekaya Ek Soru Sor (PDF Sayfa ${s.pdfPage} baz alınır):
      </div>
      <form id="aiFollowupForm" class="ai-followup-form">
        <input
          type="text"
          id="aiFollowupInput"
          class="ai-followup-input"
          placeholder="Örn: Tasarım basıncı 25 bar ise hidrostatik test basıncı kaç bar olur? / 3.1 sertifikası yeterli mi?"
        />
        <button type="submit" id="aiFollowupBtn" class="btn-primary">Sor</button>
      </form>
      <div id="aiFollowupAnswer" class="ai-followup-answer ${s.followupAnswer ? '' : 'hidden'}">${escapeHtml(s.followupAnswer || '')}</div>
    </div>
  `;

  card.querySelector('.js-open-summary-pdf')?.addEventListener('click', (e) => {
    const btn = e.currentTarget;
    openRuleModal(btn.dataset.sec, parseInt(btn.dataset.page, 10) || s.pdfPage);
  });

  const followupForm = document.getElementById('aiFollowupForm');
  followupForm?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const qInp = document.getElementById('aiFollowupInput');
    const ansBox = document.getElementById('aiFollowupAnswer');
    const btn = document.getElementById('aiFollowupBtn');
    const fq = qInp?.value.trim();
    if (!fq) return;

    btn.disabled = true;
    ansBox.classList.remove('hidden');
    ansBox.textContent = '⏳ RINA 2026 PDF metnine göre hesaplanıyor / yanıtlanıyor...';

    try {
      const pdfContext = (state.matchedPdfPages || [])
        .slice(0, 4)
        .map((p) => `[${p.secId} | PDF Page ${p.page}]\n${p.text}`)
        .join('\n\n')
        .slice(0, 10000);

      const answer = await callGeminiInteraction({
        model: GEMINI_CONFIG.fastModel,
        systemInstruction:
          'You are an expert RINA Marine Surveyor assistant. Answer the surveyor question clearly and concisely in both Turkish and English (with exact RINA 2026 rule references and calculations) based on the provided RINA 2026 PDF pages.',
        input: `Equipment/Topic: ${s.titleTr} (${s.ruleRef})\nFollow-up Question: "${fq}"\n\nRINA 2026 PDF Context:\n${pdfContext}`
      });

      s.followupAnswer = answer;
      ansBox.textContent = answer;
      persistState();
    } catch (err) {
      ansBox.textContent = 'Şu anda bağlantı kurulamadı. Lütfen aşağıdaki orijinal PDF metnini kontrol edin.';
    } finally {
      btn.disabled = false;
    }
  });
}

/* =====================================================
   LEONARDO TEST SHEET RENDERER (SUPPORTS BOTH AI & PRESET SHEETS)
   ===================================================== */
function getCurrentEquipment() {
  if (state.activeDynamicSheet) return state.activeDynamicSheet;
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

function getMetaBannerHtml() {
  const hasMeta =
    state.meta.factory ||
    state.meta.project ||
    state.meta.serial ||
    state.meta.typeSerial ||
    state.meta.surveyor;

  if (!hasMeta) return '';
  return `
    <div class="leo-meta-summary">
      ${state.meta.factory ? `<div class="leo-meta-item"><strong>Manufacturer / Fabrika:</strong> ${escapeHtml(state.meta.factory)}</div>` : ''}
      ${state.meta.project ? `<div class="leo-meta-item"><strong>Project / Ship No:</strong> ${escapeHtml(state.meta.project)}</div>` : ''}
      ${state.meta.serial ? `<div class="leo-meta-item"><strong>Serial / Heat No:</strong> ${escapeHtml(state.meta.serial)}</div>` : ''}
      ${state.meta.typeSerial ? `<div class="leo-meta-item"><strong>Type-Tested Prototype S/N:</strong> ${escapeHtml(state.meta.typeSerial)}</div>` : ''}
      ${state.meta.surveyor ? `<div class="leo-meta-item"><strong>Attending Surveyor:</strong> ${escapeHtml(state.meta.surveyor)}</div>` : ''}
    </div>
  `;
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

  // Application Terms HTML
  const appTermsRows = (eq.applicationTerms || [])
    .map((q) => {
      const currentVal = eqAnswers[q.id] ?? q.default;
      const optionsHtml = (q.options || [
        { value: 'Yes', labelEn: 'Yes', labelTr: 'Evet (Yes)' },
        { value: 'No', labelEn: 'No', labelTr: 'Hayır (No)' }
      ])
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

  const calcHtml = eq.calculator ? renderCalculatorHtml(eq) : '';

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
          <button type="button" class="leo-rule-link js-open-rule" data-sec="${escapeHtml(r.sectionId || eq.sectionId)}" data-page="${r.page || eq.pdfPage}">
            📄 ${escapeHtml(r.ruleRef)} (s.${r.page || eq.pdfPage})
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
                        📖 ${escapeHtml(step.ruleRef)} (PDF s.${step.page || eq.pdfPage})
                      </button>
                    </div>`
                  : `<div class="cert-main-title-en">
                      (${displayNum}) ${escapeHtml(step.titleTr)}
                      <button type="button" class="inline-rule-chip no-print js-open-rule" data-sec="${escapeHtml(step.sectionId || eq.sectionId)}" data-page="${step.page || eq.pdfPage}">
                        📖 ${escapeHtml(step.ruleRef)} (PDF s.${step.page || eq.pdfPage})
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
              placeholder="✍️ Saha Notu / Ölçülen Değer (Örn: Hidrotest: 15 bar 10dk sızıntı yok, Megger: 250 MΩ, Sertifika No...)"
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
        <div class="leo-doc-subtitle">Leonardo TEST &bull; RINA Rules 2026 ${eq.isAiGenerated ? '&bull; ✨ AI PDF Synthesis' : ''}</div>
        <div class="leo-cert-according">Certification according to RINA Rules for the Classification of Ships - Products</div>
        ${showEn ? `<div class="leo-product-title-en">${escapeHtml(eq.titleEn)} (See Application Terms below)</div>` : ''}
        ${showTr ? `<div class="leo-product-title-tr">🇹🇷 ${escapeHtml(eq.titleTr)}</div>` : ''}
        <div class="leo-rule-ref-row">
          <button type="button" class="leo-rule-link js-open-rule" data-sec="${escapeHtml(eq.sectionId)}" data-page="${eq.pdfPage}">
            Rule Reference: <strong>${escapeHtml(eq.ruleRef)}</strong> (PDF Sayfa ${eq.pdfPage} Aç 📖)
          </button>
        </div>
      </div>
    </div>

    <div id="leoMetaBannerWrap">${getMetaBannerHtml()}</div>

    <!-- SECTION 1: APPLICATION TERMS -->
    <div class="leo-section">
      <div class="leo-section-title">APPLICATION TERMS</div>
      <div class="leo-section-desc">
        List of circumstances which affect the applicable acceptance requirements and certification activities
        ${showTr ? `<span class="leo-section-desc-tr">🇹🇷 Uygulanacak kabul gereksinimlerini ve fabrika test adımlarını belirleyen uygulama koşulları</span>` : ''}
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
        <div class="progress-stats" id="checklistProgressStats">
          ✅ Tamamlanan Test Adımı: <strong>${okCount} / ${visibleSteps.length}</strong>
        </div>
        <div class="quick-check-btns">
          <button type="button" class="btn-xs" id="markAllOkBtn">✓ Tümünü OK İşaretle</button>
          <button type="button" class="btn-xs" id="resetChecklistBtn">↺ İşaretleri Sıfırla</button>
        </div>
      </div>

      <div class="cert-activities-list" id="certActivitiesList">
        ${certStepsHtml}
      </div>
    </div>

    <div class="leo-footer">
      <span>RINA Rules for the Classification of Ships 2026 — ${escapeHtml(eq.ruleRef)}</span>
      <span>Page 1 of 1</span>
    </div>
  `;

  bindSheetInteractions(eq, visibleSteps.length);
}

/* =====================================================
   MATCHED VERBATIM RINA 2026 PDF PAGES PANEL
   ===================================================== */
function renderMatchedPdfPagesPanel() {
  const panel = document.getElementById('matchedPdfPagesPanel');
  if (!panel) return;

  const pages = state.matchedPdfPages || [];
  if (pages.length === 0) {
    panel.innerHTML = '';
    return;
  }

  const highlightTerms = state.lastQuery
    ? expandQueryToRinaTerms(state.lastQuery).terms.filter((t) => t.length >= 3)
    : [];

  panel.innerHTML = `
    <div class="matched-pdf-header">
      <div>
        <span class="ai-sum-badge">📕 RINA RULES 2026 PDF — DOĞRUDAN BULUNAN ORİJİNAL SAYFALAR (${pages.length} Sayfa)</span>
        <h3 style="margin-top:0.3rem; color:#002b54; font-size:1.05rem;">
          Aramanızla Eşleşen Orijinal RINA 2026 PDF Kural Metinleri
        </h3>
      </div>
      <span style="font-size:0.78rem; color:#64748b;">Tam bölümü açmak için sayfa başlığındaki butona tıklayın</span>
    </div>

    <div>
      ${pages
        .map(
          (p) => `
        <div class="pdf-page-block">
          <div class="pdf-page-header">
            <span>📖 ${escapeHtml(p.secId)} &bull; ${escapeHtml(p.chapter)} — ${escapeHtml(p.section)}</span>
            <button type="button" class="btn-xs js-open-matched-pdf" data-sec="${escapeHtml(p.secId)}" data-page="${p.page}">
              📄 PDF Sayfa ${p.page} Tam Bölüm Görünümü Aç
            </button>
          </div>
          <div class="pdf-page-text">${highlightMultipleTerms(p.text, highlightTerms)}</div>
        </div>
      `
        )
        .join('')}
    </div>
  `;

  panel.querySelectorAll('.js-open-matched-pdf').forEach((btn) => {
    btn.addEventListener('click', () => {
      openRuleModal(btn.dataset.sec, parseInt(btn.dataset.page, 10));
    });
  });
}

/* =====================================================
   QUICK FIELD CALCULATOR
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
            <input type="number" id="calcTrafoU" value="${c.defaultVoltage || 440}" min="12" max="36000" />
          </div>
          <div class="calc-input-group">
            <label>Anma Frekansı fn (Hz)</label>
            <input type="number" id="calcTrafoFn" value="${c.defaultFreq || 60}" min="50" max="60" />
          </div>
          <div class="calc-input-group">
            <label>Endüklenen Test Frekansı fp (Hz)</label>
            <input type="number" id="calcTrafoFp" value="${(c.defaultFreq || 60) * 2}" min="50" max="400" />
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
      <div class="calc-box no-print">
        <div class="calc-header">
          <span>🧮 ${escapeHtml(c.labelTr)}</span>
          <span style="font-size:0.75rem; color:#0369a1;">Pt C, Ch 2, Sec 8 [3.3.4] Tab. 2 &amp; Tab. 3</span>
        </div>
        <div class="calc-grid">
          <div class="calc-input-group">
            <label>Ana Bara Yalıtım Gerilimi Ui (V)</label>
            <input type="number" id="calcSwbUi" value="${c.defaultVoltage || 440}" min="24" max="1000" />
          </div>
          <div class="calc-input-group">
            <label>Kumanda Devresi Ui (V)</label>
            <input type="number" id="calcSwbAux" value="${c.defaultAuxVoltage || 230}" min="12" max="690" />
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
        <div class="calc-res-card"><span class="lbl">Aksesuar / Hava Tüpü (1.5×p) [3.9.2]</span><span class="val">${(1.5 * pBar).toFixed(1)} bar</span></div>
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

function bindSheetInteractions(eq, totalVisibleSteps) {
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

  // Rule reference buttons -> Open Fast Paginated Rule PDF Modal
  document.querySelectorAll('#leonardoSheet .js-open-rule').forEach((btn) => {
    btn.addEventListener('click', () => {
      const secId = btn.dataset.sec || eq.sectionId;
      const page = parseInt(btn.dataset.page, 10) || eq.pdfPage;
      openRuleModal(secId, page);
    });
  });

  // In-place Checklist status buttons (Zero scroll jump / zero full DOM re-render!)
  document.querySelectorAll('#leonardoSheet .status-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const stepNum = btn.dataset.step;
      const targetStatus = btn.dataset.status;
      if (!state.checklist[eq.id]) state.checklist[eq.id] = {};
      const curr = state.checklist[eq.id][stepNum] || { status: 'pending', note: '' };
      curr.status = curr.status === targetStatus ? 'pending' : targetStatus;
      state.checklist[eq.id][stepNum] = curr;
      persistState();

      // Update card classes in-place
      const itemEl = btn.closest('.cert-item');
      if (itemEl) {
        itemEl.classList.remove('status-pending', 'status-ok', 'status-fail', 'status-na');
        itemEl.classList.add(`status-${curr.status}`);
        itemEl.querySelectorAll('.status-btn').forEach((b) => {
          b.classList.remove('active-ok', 'active-fail', 'active-na');
          if (b.dataset.status === curr.status) {
            b.classList.add(`active-${curr.status}`);
          }
        });
      }

      // Update counter in-place
      const okCount = Object.values(state.checklist[eq.id] || {}).filter((v) => v.status === 'ok').length;
      const statsEl = document.getElementById('checklistProgressStats');
      if (statsEl) {
        statsEl.innerHTML = `✅ Tamamlanan Test Adımı: <strong>${okCount} / ${totalVisibleSteps}</strong>`;
      }
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
   FAST PAGINATED RINA 2026 PDF RULE MODAL & READER (ZERO LAG)
   ===================================================== */
async function openRuleModal(sectionId, targetPage) {
  const modal = document.getElementById('ruleModal');
  const badge = document.getElementById('ruleModalBadge');
  const title = document.getElementById('ruleModalTitle');
  const body = document.getElementById('ruleModalBody');
  const pills = document.getElementById('modalArticlePills');
  const filterInput = document.getElementById('modalRuleFilterInput');
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

  const sec = fullDb.find((s) => s.id === sectionId) || fullDb[0];
  state.modalSectionId = sec.id;
  const validPage = sec.pages.some((p) => p.page === targetPage)
    ? targetPage
    : sec.pages[0]?.page || sec.start_page;
  state.modalCurrentPage = validPage;

  badge.textContent = `${sec.id} (PDF Sayfa ${sec.start_page}–${sec.end_page})`;
  title.textContent = `${sec.chapter} — ${sec.section}`;
  filterInput.value = '';

  // Populate page selector dropdown
  pageSelect.innerHTML = sec.pages
    .map((p) => `<option value="${p.page}" ${p.page === state.modalCurrentPage ? 'selected' : ''}>PDF Sayfa ${p.page} / ${sec.end_page}</option>`)
    .join('');

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

  const renderModalView = () => {
    const q = filterInput.value.trim().toLowerCase();
    if (q.length >= 2) {
      // Show up to 8 matching pages when filtering
      const matched = sec.pages.filter((p) => p.text.toLowerCase().includes(q)).slice(0, 8);
      if (matched.length === 0) {
        body.innerHTML = `<div style="padding:1.5rem; text-align:center;">Bu bölümde "${escapeHtml(filterInput.value)}" bulunamadı.</div>`;
        return;
      }
      body.innerHTML = matched
        .map(
          (p) => `
          <div class="pdf-page-block" style="border: 2px solid #0284c7;">
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

    // Fast single-page (+ next page preview) mode for zero lag on mobile
    const idx = sec.pages.findIndex((p) => p.page === state.modalCurrentPage);
    const slice = idx !== -1 ? sec.pages.slice(idx, idx + 2) : sec.pages.slice(0, 2);
    pageSelect.value = String(state.modalCurrentPage);
    prevBtn.disabled = idx <= 0;
    nextBtn.disabled = idx === -1 || idx >= sec.pages.length - 1;

    body.innerHTML = slice
      .map(
        (p, i) => `
        <div class="pdf-page-block" style="${i === 0 ? 'border: 2px solid #0284c7; background:#f8fbff;' : ''}">
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

function renderRulesSidebar() {
  const sidebar = document.getElementById('rulesSidebar');
  if (!sidebar || !state.rulesIndex.length) return;

  sidebar.innerHTML = state.rulesIndex
    .map((sec) => {
      const active = sec.id === state.activeRuleSectionId;
      return `
        <button type="button" class="sec-nav-item ${active ? 'active' : ''}" data-sec-id="${escapeHtml(sec.id)}">
          <div style="font-weight:700; font-size:0.75rem; opacity:0.85;">${escapeHtml(sec.id)} (s.${sec.start_page})</div>
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

async function renderSelectedRuleSectionInTab(secId, highlightQuery = '', startPage = null) {
  const reader = document.getElementById('rulesReader');
  if (!reader) return;

  if (!state.rulesFull) {
    reader.innerHTML = `<div style="padding:2rem; text-align:center;">⏳ RINA 2026 PDF Tam Metin Veritabanı Yükleniyor...</div>`;
    await ensureFullRulesLoaded();
  }
  if (!state.rulesFull) return;

  const sec = state.rulesFull.find((s) => s.id === secId) || state.rulesFull[0];
  let currentPage = startPage && sec.pages.some((p) => p.page === startPage) ? startPage : sec.pages[0]?.page || sec.start_page;

  const renderReaderPage = () => {
    const idx = sec.pages.findIndex((p) => p.page === currentPage);
    const slice = idx !== -1 ? sec.pages.slice(idx, idx + 3) : sec.pages.slice(0, 3);

    reader.innerHTML = `
      <div style="margin-bottom:0.9rem; padding-bottom:0.75rem; border-bottom:2px solid #004b87; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
        <div>
          <span class="equip-code">${escapeHtml(sec.id)}</span>
          <h3 style="margin-top:0.3rem; color:#002b54;">${escapeHtml(sec.chapter)} — ${escapeHtml(sec.section)}</h3>
          <div style="font-size:0.78rem; color:#64748b;">RINA Rules 2026 Interactive PDF Sayfa: ${sec.start_page} – ${sec.end_page}</div>
        </div>
        <div class="modal-page-controls">
          <button type="button" class="btn-xs" id="tabPrevPageBtn" ${idx <= 0 ? 'disabled' : ''}>◀ Önceki</button>
          <select id="tabPageSelect" class="modal-page-select">
            ${sec.pages.map((p) => `<option value="${p.page}" ${p.page === currentPage ? 'selected' : ''}>Sayfa ${p.page}</option>`).join('')}
          </select>
          <button type="button" class="btn-xs" id="tabNextPageBtn" ${idx >= sec.pages.length - 1 ? 'disabled' : ''}>Sonraki ▶</button>
        </div>
      </div>
      ${slice
        .map(
          (p) => `
        <div class="pdf-page-block" id="tab-pdf-page-${p.page}">
          <div class="pdf-page-header">
            <span>${escapeHtml(sec.id)} &bull; ${escapeHtml(sec.section)}</span>
            <span>PDF Sayfa ${p.page}</span>
          </div>
          <div class="pdf-page-text">${highlightText(p.text, highlightQuery)}</div>
        </div>
      `
        )
        .join('')}
    `;

    document.getElementById('tabPageSelect')?.addEventListener('change', (e) => {
      currentPage = parseInt(e.target.value, 10);
      renderReaderPage();
    });
    document.getElementById('tabPrevPageBtn')?.addEventListener('click', () => {
      if (idx > 0) {
        currentPage = sec.pages[idx - 1].page;
        renderReaderPage();
      }
    });
    document.getElementById('tabNextPageBtn')?.addEventListener('click', () => {
      if (idx < sec.pages.length - 1) {
        currentPage = sec.pages[idx + 1].page;
        renderReaderPage();
      }
    });
  };

  renderReaderPage();
}

async function performFullRulesSearch() {
  const inp = document.getElementById('fullRulesSearchInput');
  const resultsBox = document.getElementById('fullRulesSearchResults');
  const q = inp.value.trim();

  if (!q || q.length < 2) {
    resultsBox.classList.add('hidden');
    return;
  }

  resultsBox.classList.remove('hidden');
  resultsBox.innerHTML = `<div>🔍 1.631 sayfalık RINA 2026 PDF içinde aranıyor...</div>`;

  const fullDb = await ensureFullRulesLoaded();
  if (!fullDb) return;

  const hits = searchRinaPdfPages(q, fullDb, [], [], 25);
  const terms = expandQueryToRinaTerms(q).terms.filter((t) => t.length >= 2);

  if (hits.length === 0) {
    resultsBox.innerHTML = `<div>"${escapeHtml(q)}" için eşleşme bulunamadı.</div>`;
    return;
  }

  resultsBox.innerHTML = `
    <div style="font-size:0.8rem; font-weight:700; color:#004b87; margin-bottom:0.5rem;">
      Bulunan En İlgili PDF Sayfaları (${hits.length}) — İlgili sayfayı açmak için tıklayın:
    </div>
    ${hits
      .map((h) => {
        const snippet = h.text.slice(0, 240).replace(/\s+/g, ' ');
        return `
        <div class="search-hit-item" data-sec="${escapeHtml(h.secId)}" data-page="${h.page}">
          <div style="font-weight:700; font-size:0.82rem; color:#002b54;">
            ${escapeHtml(h.secId)} — ${escapeHtml(h.section)} <span style="color:#0284c7;">(PDF Sayfa ${h.page})</span>
          </div>
          <div style="font-size:0.78rem; color:#475569; margin-top:0.15rem;">
            ${highlightMultipleTerms(snippet, terms)}...
          </div>
        </div>
      `;
      })
      .join('')}
  `;

  resultsBox.querySelectorAll('.search-hit-item').forEach((item) => {
    item.addEventListener('click', async () => {
      const secId = item.dataset.sec;
      const page = parseInt(item.dataset.page, 10);
      state.activeRuleSectionId = secId;
      renderRulesSidebar();
      await renderSelectedRuleSectionInTab(secId, terms[0] || q, page);
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
    equipmentCode: eq.code || 'AI',
    equipmentTitleTr: eq.titleTr,
    equipmentTitleEn: eq.titleEn,
    ruleRef: eq.ruleRef,
    dynamicSheet: eq.isAiGenerated ? JSON.parse(JSON.stringify(eq)) : null,
    aiSummary: state.aiSummary ? JSON.parse(JSON.stringify(state.aiSummary)) : null,
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
        Henüz kaydedilmiş bir fabrika testi bulunmuyor. Test ekranındaki <strong>"💾 Kaydet"</strong> butonuna basarak fabrika test kayıtlarınızı burada saklayabilirsiniz.
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
          <div style="font-size:0.76rem; color:#0284c7; font-weight:700;">${escapeHtml(rec.ruleRef || '')}</div>
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
      if (rec.dynamicSheet) {
        state.activeDynamicSheet = rec.dynamicSheet;
      } else {
        state.activeDynamicSheet = null;
        state.selectedEquipmentId = rec.equipmentId;
      }
      state.aiSummary = rec.aiSummary || null;
      state.meta = { ...state.meta, ...(rec.meta || {}) };
      state.answers[rec.equipmentId] = { ...(rec.answers || {}) };
      state.checklist[rec.equipmentId] = JSON.parse(JSON.stringify(rec.checklist || {}));
      syncMetaInputs();
      persistState();
      populatePresetSelect();
      renderAiSummaryCard();
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
  if (tabName === 'rules') {
    renderSelectedRuleSectionInTab(state.activeRuleSectionId);
  }
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
  document.querySelectorAll('.main-tabs .tab-btn').forEach((btn) => {
    btn.addEventListener('click', () => switchMainTab(btn.dataset.tab));
  });

  document.getElementById('brandHomeBtn')?.addEventListener('click', () => {
    switchMainTab('fat');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // AI Search Form Submit
  const searchForm = document.getElementById('aiSearchForm');
  const searchInp = document.getElementById('aiSearchInput');
  const clearBtn = document.getElementById('clearSearchBtn');

  searchForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    if (searchInp?.value.trim()) {
      runAiPdfSearch(searchInp.value.trim());
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

  // Quick Search Chips
  document.querySelectorAll('#aiQuickChips .q-chip').forEach((chip) => {
    chip.addEventListener('click', () => {
      const q = chip.dataset.query;
      if (q) runAiPdfSearch(q);
    });
  });

  // Preset 23 Equipment Selector
  const presetSel = document.getElementById('presetEquipmentSelect');
  presetSel?.addEventListener('change', () => {
    const val = presetSel.value;
    if (!val) return;
    state.activeDynamicSheet = null;
    state.aiSummary = null;
    state.selectedEquipmentId = val;
    const eq = getCurrentEquipment();
    if (eq && state.rulesFull) {
      state.matchedPdfPages = getPdfPagesForEquipment(eq);
    }
    persistState();
    renderAiSummaryCard();
    renderLeonardoSheet();
    renderMatchedPdfPagesPanel();
    showToast(`${eq.titleTr} şablonu yüklendi.`);
  });

  // Toggle Collapsible Meta Bar
  document.getElementById('toggleMetaBarBtn')?.addEventListener('click', () => {
    document.getElementById('surveyMetaBar')?.classList.toggle('hidden');
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
      renderAiSummaryCard();
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

  // Metadata fields — update ONLY the small banner in-place without re-rendering the entire sheet!
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
      const wrap = document.getElementById('leoMetaBannerWrap');
      if (wrap) wrap.innerHTML = getMetaBannerHtml();
    });
  });

  document.getElementById('openRulePdfModalBtn')?.addEventListener('click', () => {
    const eq = getCurrentEquipment();
    if (eq) openRuleModal(eq.sectionId, eq.pdfPage);
  });

  document.getElementById('saveInspectionBtn')?.addEventListener('click', saveCurrentInspection);

  document.getElementById('printSheetBtn')?.addEventListener('click', () => {
    window.print();
  });

  // Full Rules Search in Tab 2
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
      .then((reg) => {
        reg.update();
      })
      .catch((err) => console.warn('SW registration error:', err));
  }

  const updateOnlineBadge = () => {
    const badge = document.getElementById('offlineBadge');
    const txt = document.getElementById('offlineBadgeText');
    if (!badge || !txt) return;
    if (navigator.onLine) {
      badge.className = 'status-pill online';
      txt.textContent = '1.631 Sayfa PDF Hazır';
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

function highlightMultipleTerms(text, terms) {
  let escaped = escapeHtml(text);
  if (!terms || !terms.length) return escaped;
  const clean = terms
    .filter((t) => t && t.length >= 3)
    .slice(0, 6)
    .map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
  if (!clean.length) return escaped;
  const regex = new RegExp(`(${clean.join('|')})`, 'gi');
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
