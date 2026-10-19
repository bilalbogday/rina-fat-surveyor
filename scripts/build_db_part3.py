import json, os

part3_items = [
  {
    "id": "rolled-steel-plates-sections-bars",
    "code": "MT-01",
    "category": "materials",
    "categoryTitleEn": "Part D — Materials, Equipment & Welding",
    "categoryTitleTr": "Part D — Malzeme, Dövme, Döküm, Zincir/Çapa ve Kaynak Testleri",
    "titleEn": "Rolled Steel Plates, Sections & Bars (Hull Structural Steels A, B, D, E, AH/DH/EH/FH 32–40 & Boiler Steels)",
    "titleTr": "Hadde Çelik Saclar, Profiller ve Çubuklar (Gemi İnşa Sacları A, B, D, E, AH/DH/EH/FH 32–40 ve Kazan Sacları)",
    "ruleRef": "Part. D - Ch. 2 - Sec. 1 & Ch. 1 - Sec. 2",
    "sectionId": "Pt D, Ch 2, Sec 1",
    "pdfPage": 2320,
    "keywords": ["steel plate", "hull steel", "ah36", "dh36", "eh36", "fh36", "ah32", "grade a", "grade d", "grade e", "z25", "z35", "sac", "gemi sacı", "hadde çelik", "profil", "holland", "charpy", "tensile", "sec 1", "pt d"],
    "referenceTables": [
      {
        "titleEn": "Hull Structural Steel Mechanical Properties & Charpy V-Notch Impact Summary (Pt D, Ch 2, Sec 1)",
        "titleTr": "Gemi İnşa Çelikleri Mekanik Özellikler ve Charpy V-Çentik Darbe Test Özeti (t ≤ 50 mm)",
        "headers": ["Grade / Kalite", "Min. Yield ReH (MPa)", "Tensile Rm (MPa)", "Min. Elong. A5 (%)", "Charpy Impact Temp", "Min. Avg Impact Energy (Long. / Transv.)"],
        "rows": [
          ["Grade A / B / D / E (Normal Strength)", "≥ 235 MPa", "400 – 520 MPa", "≥ 22 %", "A: +20°C (if >50mm) | B: 0°C | D: -20°C | E: -40°C", "27 J (Long.) / 20 J (Transv.)"],
          ["AH32 / DH32 / EH32 / FH32", "≥ 315 MPa", "440 – 570 MPa", "≥ 22 %", "AH: 0°C | DH: -20°C | EH: -40°C | FH: -60°C", "31 J (Long.) / 22 J (Transv.)"],
          ["AH36 / DH36 / EH36 / FH36", "≥ 355 MPa", "490 – 630 MPa", "≥ 21 %", "AH: 0°C | DH: -20°C | EH: -40°C | FH: -60°C", "34 J (Long.) / 24 J (Transv.)"],
          ["AH40 / DH40 / EH40 / FH40", "≥ 390 MPa", "510 – 660 MPa", "≥ 20 %", "AH: 0°C | DH: -20°C | EH: -40°C | FH: -60°C", "39 J (Long.) / 26 J (Transv.)"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "z_quality",
        "questionEn": "Is through-thickness (Z-quality: Z25 or Z35) tensile testing required to prevent lamellar tearing? (Pt D, Ch 2, Sec 1 [9])",
        "questionTr": "Lameller yırtılmaya karşı kalınlık yönünde (Z-kalite: Z25 veya Z35) çekme testi isteniyor mu? (Pt D, Ch 2, Sec 1 [9])",
        "options": [
          { "value": "No", "labelEn": "No (Standard hull, boiler or machinery rolled steel)", "labelTr": "Hayır (Standart gemi inşa, kazan veya makine sacı/profili)" },
          { "value": "Yes", "labelEn": "Yes — Z25 or Z35 quality (Through-thickness reduction of area Z% test + 100% UT required)", "labelTr": "Evet — Z25 veya Z35 Kalite (Kalınlık yönünde kesit daralması Z% testi ve %100 UT zorunlu)" }
        ],
        "default": "No"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. D Ch. 1 Sec. 2 & Ch. 2 Sec. 1 Par. 1 & 2",
        "sectionId": "Pt D, Ch 2, Sec 1",
        "page": 2320,
        "reqEn": "RINA Mill Approval, chemical composition (Ladle analysis, Ceq/Pcm), delivery condition (AR, N, TMCP, QT) and mechanical testing",
        "reqTr": "RINA Haddehane Onayı, kimyasal analiz (Ceq / Pcm karbon eşdeğeri), teslimat durumu (AR, N, TMCP, QT) ve mekanik testler"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. D Ch. 1 Sec. 2 Par. 1.2",
        "sectionId": "Pt D, Ch 1, Sec 2",
        "page": 2301,
        "titleEn": "Verification of RINA Works Approval of steel mill and calibration of tensile & Charpy testing machines (Part. D Ch. 1 Sec. 2 Par. 1.2)",
        "detailEn": "Verify that the steelmaker holds a valid RINA Works Approval certificate for the specific steel grade, thickness range, deoxidation practice, and rolling process (N / TMCP / QT). Verify valid calibration certificates (Class 1 / ISO 7500-1 & ISO 148-2) of tensile and Charpy V-notch impact machines.",
        "titleTr": "Çelik üreticisi (Haddehane) RINA onay kapsamının ve çekme/darbe test cihazları kalibrasyonunun doğrulanması",
        "detailTr": "Üretici haddehanenin ilgili çelik kalitesi (örn. EH36), kalınlık ve haddeleme yöntemi (Normalizeli / TMCP) için geçerli RINA fabrika onayına sahip olduğu ve çekme/Charpy cihazlarının kalibrasyonları doğrulanır.",
        "tipTr": "Test numunelerinin üzerindeki RINA soğuk damgasını (stamp) ve döküm/plaka numarasını testten önce bizzat kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. D Ch. 2 Sec. 1 Par. 2.2 - 2.4",
        "sectionId": "Pt D, Ch 2, Sec 1",
        "page": 2326,
        "titleEn": "Verification of chemical composition (Ladle analysis, Ceq, Pcm and grain-refining elements Al, Nb, V, Ti)",
        "detailEn": "Check ladle analysis against Rule limits for C, Mn, Si, P, S, grain refining elements (Al, Nb, V, Ti), and Carbon Equivalent Ceq = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15.",
        "titleTr": "Kimyasal analiz, Karbon Eşdeğeri (Ceq) ve ince taneli element (Al, Nb, V, Ti) oranlarının kontrolü",
        "detailTr": "Pota (ladle) analizinde C, Mn, Si, P, S oranları, tane inceltici elementler ve Karbon Eşdeğeri (Ceq) formül değerinin kural tablosundaki maksimum sınırı aşmadığı doğrulanır.",
        "tipTr": "TMCP (Termomekanik haddelenmiş) saclarda kaynaklanabilirlik için Ceq sınırları normalizeli saclara göre daha düşüktür; sertifikadan kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. D Ch. 1 Sec. 2 Par. 2 & 4 / Ch. 2 Sec. 1 Par. 2.7",
        "sectionId": "Pt D, Ch 2, Sec 1",
        "page": 2333,
        "titleEn": "Witnessing of Tensile Test and Charpy V-Notch Impact Test (3 specimens per batch) (Part. D Ch. 2 Sec. 1 Par. 2.7)",
        "detailEn": "Witness transverse tensile test (ReH, Rm, A5%) and set of 3 Charpy V-notch impact specimens at the prescribed temperature (0°C for B/AH, -20°C for D/DH, -40°C for E/EH, -60°C for FH).\n- Single specimen rule (Ch 1, Sec 2 [4.3]): Average of 3 specimens ≥ required energy; at most 1 individual value may be below required average, provided it is NOT less than 70% of the required average!\n- Sub-size specimen factor (if t < 10 mm): 10×7.5 mm -> 5/6 of required energy; 10×5 mm -> 2/3 of required energy.",
        "titleTr": "Çekme Testi (Tensile) ve Charpy V-Çentik Darbe (Impact) Testlerine nezaret edilmesi (Part. D Ch. 2 Sec. 1 Par. 2.7)",
        "detailTr": "Çekme testinde akma (ReH), çekme (Rm) ve kopma uzaması (%A5); Charpy V-çentik darbe testinde ise ilgili sıcaklıkta (0°C, -20°C, -40°C, -60°C) kırılan 3 numunenin enerjisi doğrulanır.\n- Tekil Değer Kuralı: 3 numunenin ortalaması tablo değerini sağlamalıdır; en fazla 1 numune ortalamanın altında kalabilir ancak bu değer de istenen ortalamanın %70'inden düşük olamaz!",
        "tipTr": "Charpy numunelerinin banyodan çıkarıldıktan sonra 5 saniye içinde kırılmasına ve banyo sıcaklığının ±1°C tolerans içinde olmasına dikkat edin.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. D Ch. 2 Sec. 1 Par. 9",
        "sectionId": "Pt D, Ch 2, Sec 1",
        "page": 2361,
        "titleEn": "Through-thickness tensile test (Z25 / Z35) and 100% Ultrasonic Testing (Part. D Ch. 2 Sec. 1 Par. 9)",
        "detailEn": "For Z25: minimum average reduction of area (3 specimens) ≥ 25% (min single value ≥ 15%). For Z35: minimum average reduction of area ≥ 35% (min single value ≥ 25%). All Z-grade plates must undergo 100% Ultrasonic Testing (UT) per [9.9].",
        "titleTr": "Kalınlık yönünde çekme testi (Z25 / Z35) ve %100 Ultrasonik Muayene (UT) (Part. D Ch. 2 Sec. 1 Par. 9)",
        "detailTr": "Z25 kalite saclarda 3 numunenin ortalama kesit daralması (Reduction of Area) ≥ %25 (tekil min ≥ %15); Z35 kalitede ortalama ≥ %35 (tekil min ≥ %25) olmalı ve her plakaya %100 Ultrasonik (UT) laminasyon kontrolü yapılmalıdır.",
        "tipTr": "Z-kalite sacların markalamasında kalite harfinin sonunda 'Z25' veya 'Z35' ibaresinin (örn. EH36-Z35) basıldığını kontrol edin.",
        "condition": { "field": "z_quality", "equals": "Yes" }
      },
      {
        "num": 5,
        "ruleRef": "Part. D Ch. 2 Sec. 1 Par. 1.7, 1.9 & 1.10",
        "sectionId": "Pt D, Ch 2, Sec 1",
        "page": 2324,
        "titleEn": "Surface inspection, dimensional thickness tolerance check (max -0.3 mm for hull plates) and RINA stamping",
        "detailEn": "Check surface finish (freedom from laminations, cracks, scabs), verify minus thickness tolerance (typically -0.3 mm for hull structural steel plates ≥ 5 mm per [2.5]), and verify RINA brand, steel grade, heat number, and plate number stamping.",
        "titleTr": "Yüzey muayenesi, kalınlık eksi tolerans kontrolü (Gemi saclarında maks. -0.3 mm) ve RINA damgalama",
        "detailTr": "Sac yüzeyinde hadde kusuru/laminasyon olmadığı, gemi inşa saclarında kalınlık eksi toleransının -0.3 mm'yi aşmadığı ([2.5]) ve her plaka üzerinde RINA damgası, çelik kalitesi (örn. RINA DH36), döküm ve plaka numarasının bulunduğu doğrulanır.",
        "tipTr": "Gemi inşa saclarında kumpas/ultrasonik kalınlık ölçer ile özellikle sac kenar ve ortasında eksi toleransı (-0.3 mm) kontrol edin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "steel-forgings-shafts-crankshafts",
    "code": "MT-02",
    "category": "materials",
    "categoryTitleEn": "Part D — Materials, Equipment & Welding",
    "categoryTitleTr": "Part D — Malzeme, Dövme, Döküm, Zincir/Çapa ve Kaynak Testleri",
    "titleEn": "Steel Forgings — Machinery, Shafting, Rudder Stocks, Crankshafts, Gearing & Hull Forgings",
    "titleTr": "Çelik Dövmeler (Steel Forgings) — Pervane/Ara Şaftlar, Dümen Роdu, Krank Milleri, Dişli Dövmeleri ve Tekne Dövmeleri",
    "ruleRef": "Part. D - Ch. 2 - Sec. 3",
    "sectionId": "Pt D, Ch 2, Sec 3",
    "pdfPage": 2390,
    "keywords": ["forging", "steel forging", "shaft forging", "rudder stock", "crankshaft forging", "pinion forging", "dövme", "çelik dövme", "şaft dövmesi", "dümen rodu", "krank dövmesi", "sec 3", "pt d"],
    "applicationTerms": [
      {
        "id": "forging_type",
        "questionEn": "What is the intended application of the steel forging? (Pt D, Ch 2, Sec 3)",
        "questionTr": "Çelik dövme parçanın kullanım yeri nedir? (Pt D, Ch 2, Sec 3)",
        "options": [
          { "value": "machinery_shaft", "labelEn": "Machinery, Propulsion Shafting or Rudder Stock / Pintle ([2], [3])", "labelTr": "Makine, Pervane/Ara Şaft veya Dümen Rodu / İğnecik Dövmeleri ([2], [3])" },
          { "value": "crank_gear", "labelEn": "Diesel Engine Crankshaft ([4]) or Gearing / Pinions ([5])", "labelTr": "Krank Mili ([4]) veya Redüktör Pinyon / Dişli Dövmeleri ([5])" },
          { "value": "pressure_boiler", "labelEn": "Boilers, Pressure Vessels ([7]) or Stainless Steel Forgings ([9])", "labelTr": "Kazan, Basınçlı Kap ([7]) veya Paslanmaz Çelik Dövmeler ([9])" }
        ],
        "default": "machinery_shaft"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. D Ch. 2 Sec. 3 Par. 1.4 - 1.13",
        "sectionId": "Pt D, Ch 2, Sec 3",
        "page": 2391,
        "reqEn": "Forge approval, reduction ratio (≥ 3:1 from ingot), heat treatment, mechanical tests (tensile, Charpy, hardness) and 100% UT & MT/PT",
        "reqTr": "Dövmehane onayı, dövme küçültme oranı (ingottan ≥ 3:1), ısıl işlem, mekanik testler (çekme, darbe, sertlik) ve %100 UT ve MT/PT"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. D Ch. 2 Sec. 3 Par. 1.4 - 1.7",
        "sectionId": "Pt D, Ch 2, Sec 3",
        "page": 2391,
        "titleEn": "Verification of RINA Forge Approval, reduction ratio, chemical composition and heat treatment furnace charts",
        "detailEn": "Verify RINA Works Approval of the forge, total forging reduction ratio (typically ≥ 3:1 from ingot or ≥ 6:1 from continuous cast billet), ladle chemical analysis, and heat treatment furnace charts (Normalising & Tempering or Quenching & Tempering).",
        "titleTr": "RINA Dövmehane Onayı, dövme oranı (Reduction Ratio), kimyasal analiz ve ısıl işlem fırın grafiklerinin kontrolü",
        "detailTr": "Dövmehanenin RINA onayı, dövme küçültme oranı (ingottan ≥ 3:1), kimyasal analiz ve Normalizasyon+Temperleme (N+T) veya Su Verme+Temperleme (Q+T) fırın ısıl işlem diyagramları incelenir.",
        "tipTr": "Test uzantısı (test coupon) dövme parçadan ısıl işlem TAMAMLANMADAN ÖNCE kesinlikle kesilmemelidir ([1.11])!",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. D Ch. 2 Sec. 3 Par. 1.11 & 3.6 - 5.7",
        "sectionId": "Pt D, Ch 2, Sec 3",
        "page": 2393,
        "titleEn": "Witnessing of mechanical tests — Tensile, Charpy V-Notch Impact and Brinell Hardness uniformity",
        "detailEn": "Verify RINA stamp on integral test coupon before removal; witness longitudinal/tangential tensile test (ReH, Rm, A5, Z% reduction of area), Charpy V-notch impact test, and Brinell hardness (HBW) uniformity check across the forging length/circumference.",
        "titleTr": "Mekanik testlere nezaret — Çekme, Charpy V-Çentik Darbe ve Brinell Sertlik (HBW) homojenlik testi",
        "detailTr": "Parça üzerindeki RINA damgalı test kuponundan alınan boyuna/teğetsel çekme (ReH, Rm, %A5, %Z kesit daralması), Charpy darbe ve parça boyunca Brinell sertlik (HBW) homojenlik ölçümlerine nezaret edilir.",
        "tipTr": "Islah çeliklerinde (Q+T) ve dişli dövmelerinde parça üzerindeki sertlik farkının (ΔHBW) kural sınırını aşmadığını kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. D Ch. 2 Sec. 3 Par. 1.9",
        "sectionId": "Pt D, Ch 2, Sec 3",
        "page": 2392,
        "titleEn": "Non-destructive testing (100% Ultrasonic UT and Magnetic Particle / Penetrant MT/PT) & dimensional inspection",
        "detailEn": "Verify 100% Ultrasonic examination (UT) and surface Magnetic Particle / Liquid Penetrant (MT/PT) examination per acceptance zones, plus visual and dimensional check and RINA hard stamping.",
        "titleTr": "%100 Ultrasonik (UT), Manyetik Parçacık / Penetran (MT/PT) NDT, boyutsal muayene ve RINA damgalama",
        "detailTr": "Dövme parçaya %100 Ultrasonik (UT) ve yüzey MT/PT kontrolü uygulanır, boyutsal ölçüm yapılır ve bitmiş parça alnına RINA soğuk damgası vurulur.",
        "tipTr": "Dövme parçalarda kaynakla tamir (weld repair) kural olarak kabul edilmez; herhangi bir kusur tespitinde özel RINA onayı şarttır.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "steel-and-iron-castings",
    "code": "MT-03",
    "category": "materials",
    "categoryTitleEn": "Part D — Materials, Equipment & Welding",
    "categoryTitleTr": "Part D — Malzeme, Dövme, Döküm, Zincir/Çapa ve Kaynak Testleri",
    "titleEn": "Steel Castings & Spheroidal / Grey Iron Castings (Stern Frame, Rudder Horn, Valve Bodies, Engine Casings)",
    "titleTr": "Çelik Dökümler ve Sfero / Pik Demir Dökümler (Stern Frame, Dümen Topuğu, Valf Gövdeleri, Makine Parçaları — GGG40 / GGG40.3)",
    "ruleRef": "Part. D - Ch. 2 - Sec. 4 & Sec. 5",
    "sectionId": "Pt D, Ch 2, Sec 4",
    "pdfPage": 2418,
    "keywords": ["casting", "steel casting", "iron casting", "spheroidal graphite", "nodular iron", "ggg40", "ggg40.3", "ggg50", "stern frame", "rudder horn", "döküm", "çelik döküm", "sfero döküm", "pik döküm", "sec 4", "sec 5", "pt d"],
    "applicationTerms": [
      {
        "id": "casting_kind",
        "questionEn": "Is the component a Steel Casting (Sec 4) or a Spheroidal/Grey Iron Casting (Sec 5)?",
        "questionTr": "Parça Çelik Döküm (Sec 4) mü yoksa Sfero / Gri Demir Döküm (Sec 5) mü?",
        "options": [
          { "value": "steel_cast", "labelEn": "Carbon / Alloy Steel Casting (Hull Stern Frame, Rudder, Valve, Crankthrow — Sec 4)", "labelTr": "Karbon / Alaşımlı Çelik Döküm (Stern Frame, Dümen, Valf, Krank — Sec 4)" },
          { "value": "sg_iron", "labelEn": "Spheroidal / Nodular Graphite Cast Iron (GGG40 / 350-22 / 400-18 — Sec 5 [3])", "labelTr": "Sfero (Küresel Grafitli) Dökme Demir (GGG40 / GGG40.3 / 400-18 — Sec 5 [3])" }
        ],
        "default": "steel_cast"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. D Ch. 2 Sec. 4 & Sec. 5",
        "sectionId": "Pt D, Ch 2, Sec 4",
        "page": 2418,
        "reqEn": "Foundry approval, heat treatment, mechanical tests (tensile, Charpy impact, metallographic nodularity for SG iron), NDT (UT, MT/PT) and weld repair control",
        "reqTr": "Dökümhane onayı, ısıl işlem, mekanik testler (çekme, darbe, sfero dökümde küresellik/mikroyapı), NDT (UT, MT/PT) ve kaynak tamir kontrolü"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. D Ch. 2 Sec. 4 Par. 1.4 - 1.7 / Sec. 5 Par. 1",
        "sectionId": "Pt D, Ch 2, Sec 4",
        "page": 2419,
        "titleEn": "Verification of RINA Foundry Approval, chemical analysis and heat treatment furnace charts",
        "detailEn": "Verify RINA foundry approval, ladle chemical composition, and heat treatment records (full annealing, normalising, or normalising + tempering for steel castings; ferritising heat treatment for ferritic SG iron grades 350-22 / 400-18).",
        "titleTr": "RINA Dökümhane Onayı, kimyasal analiz ve ısıl işlem fırın diyagramlarının incelenmesi",
        "detailTr": "Dökümhanenin RINA onayı, kimyasal analiz sonuçları ve çelik dökümlerde tavlama/normalizasyon, ferritik sfero dökümlerde (350-22 / 400-18 / GGG40.3) ise ısıl işlem kayıtları doğrulanır.",
        "tipTr": "Parçaya bitişik dökülen (gated) test kuponları, parça ile birlikte ısıl işlem görmeden önce parçadan ayrılmamalıdır!",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. D Ch. 2 Sec. 4 Par. 1.11 & 2.6 / Sec. 5 Par. 3.4",
        "sectionId": "Pt D, Ch 2, Sec 4",
        "page": 2422,
        "titleEn": "Witnessing of Tensile Test, Charpy Impact Test and Metallographic Examination (for Spheroidal Graphite Iron)",
        "detailEn": "- Steel Castings (Sec 4): Witness tensile test (ReH, Rm, A5%, Z%) and Charpy V-notch impact test.\n- Spheroidal Graphite Cast Iron (Sec 5 [3.4]): Witness tensile test, Charpy V-notch impact test (for 350-22 at +20°C / -20°C and 400-18 at +20°C / 0°C), and verify metallographic structure (nodular graphite form ≥ 80–90% plus ferritic matrix).",
        "titleTr": "Çekme Testi, Charpy Darbe Testi ve Sfero Dökümde Küresellik (Metalografi) incelemesine nezaret",
        "detailTr": "- Çelik Dökümlerde: Çekme (ReH, Rm, %A5, %Z) ve Charpy darbe testi yapılır.\n- Sfero Dökümlerde (Sec 5 [3.4]): Çekme testi, darbe testi (özellikle borda valfi ve soğuk servis GGG40.3 / 350-22 / 400-18 kalitelerinde) ve mikroskop altında grafit küresellik oranı (nodularity) kontrol edilir.",
        "tipTr": "Gemi borda valflerinde kullanılan sfero dökümlerde kopma uzaması (%A5 ≥ %18 veya %22) ve darbe enerjisi zorunludur!",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. D Ch. 2 Sec. 4 Par. 1.8 - 1.10",
        "sectionId": "Pt D, Ch 2, Sec 4",
        "page": 2421,
        "titleEn": "Visual, dimensional, Non-Destructive Testing (UT & MT/PT), weld repair verification and hydrostatic test (if applicable)",
        "detailEn": "Carry out visual & dimensional inspection; verify Ultrasonic (UT) and Magnetic Particle / Penetrant (MT/PT) reports on critical radii, weld ends, and machined zones; verify approved weld repair maps & post-weld heat treatment (PWHT); and witness hydrostatic test if pressure-retaining.",
        "titleTr": "Görsel, boyutsal, NDT (UT ve MT/PT), kaynak tamir haritası/PWHT ve (basınçlı ise) hidrostatik test kontrolü",
        "detailTr": "Stern frame, dümen boynu ve kaynak ağızları başta olmak üzere UT ve MT/PT kontrolleri yapılır; büyük döküm tamirleri varsa onaylı WPS, tamir haritası ve tamir sonrası gerilim giderme ısıl işlemi (PWHT) doğrulanır.",
        "tipTr": "Tekneye kaynaklanacak çelik dökümlerde (Stern frame, rudder horn) kaynak ağızlarının (weld preparation ends) %100 UT ve MT kontrolünü mutlaka isteyin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "anchors-chain-cables-accessories",
    "code": "MT-04",
    "category": "materials",
    "categoryTitleEn": "Part D — Materials, Equipment & Welding",
    "categoryTitleTr": "Part D — Malzeme, Dövme, Döküm, Zincir/Çapa ve Kaynak Testleri",
    "titleEn": "Anchors (Ordinary, HHP, SHHP), Stud-Link / Studless Chain Cables (Grades Q1, Q2, Q3) & Accessories",
    "titleTr": "Gemi Çapaları (Normal, HHP, SHHP), Baklalı / Lokmalı Demir Zincirleri (Grade Q1, Q2, Q3) ve Kenter / Çapa Kilitleri",
    "ruleRef": "Part. D - Ch. 4 - Sec. 1",
    "sectionId": "Pt D, Ch 4, Sec 1",
    "pdfPage": 2495,
    "keywords": ["anchor", "hhp anchor", "chain", "chain cable", "stud link", "kenter shackle", "swivel", "grade q2", "grade q3", "çapa", "demir", "zincir", "demir zinciri", "kenter kilidi", "fırdöndü", "proof load", "breaking load", "sec 1", "ch 4", "pt d"],
    "applicationTerms": [
      {
        "id": "equip_sub",
        "questionEn": "Are you inspecting an Anchor or a Marine Chain Cable / Accessory? (Pt D, Ch 4, Sec 1)",
        "questionTr": "Gemi Çapası (Anchor) mı yoksa Demir Zinciri / Kenter Kilidi (Chain Cable / Accessory) mi test ediliyor?",
        "options": [
          { "value": "anchor", "labelEn": "Anchor (Ordinary, HHP or SHHP — Drop test, Proof load & NDT per [1])", "labelTr": "Gemi Çapası (Normal, HHP veya SHHP — Düşürme testi, Proof Load çekme ve NDT — [1])" },
          { "value": "chain", "labelEn": "Chain Cable & Accessories (Grade Q1 / Q2 / Q3 — Breaking load, Proof load & Mechanical tests per [2] & [3])", "labelTr": "Demir Zinciri ve Aksesuarları (Grade Q1 / Q2 / Q3 — Kopma yükü, Proof Load ve Mekanik testler — [2] & [3])" }
        ],
        "default": "anchor"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. D Ch. 4 Sec. 1 Par. 1",
        "sectionId": "Pt D, Ch 4, Sec 1",
        "page": 2495,
        "reqEn": "Anchors: Material testing ([1.3]), Drop & Hammering test ([1.5]), Proof Load test (Tab. 1 & [1.6]), Visual/NDT ([1.7]) and Weighing/Stamping",
        "reqTr": "Çapalar: Malzeme testi ([1.3]), Düşürme ve Çekiçleme testi ([1.5]), Proof Load çekme testi (Tablo 1 & [1.6]), NDT ([1.7]) ve Tartım/Damgalama"
      },
      {
        "ruleRef": "Part. D Ch. 4 Sec. 1 Par. 2 & 3",
        "sectionId": "Pt D, Ch 4, Sec 1",
        "page": 2500,
        "reqEn": "Chain Cables & Accessories: Works approval, bar material, Breaking Load & Proof Load tests ([2.10], [2.11]), Charpy/Tensile and 5-link dimensional check",
        "reqTr": "Demir Zincirleri ve Kilitler: Fabrika onayı, Kopma Yükü (Breaking Load) ve Proof Load testleri ([2.10], [2.11]), Mekanik testler ve 5 bakla ölçü kontrolü"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. D Ch. 4 Sec. 1 Par. 1.3 / Par. 2.3",
        "sectionId": "Pt D, Ch 4, Sec 1",
        "page": 2496,
        "titleEn": "Verification of RINA Manufacturer Approval, Type Approval (for HHP/SHHP anchors), material certificates & tensile machine calibration",
        "detailEn": "Verify valid RINA approval of anchor/chain manufacturer, HHP/SHHP anchor Type Approval Certificate, RINA material certificates (cast steel / forged steel / rolled bar), heat treatment charts, and calibration of the horizontal proof/breaking load tensile bench.",
        "titleTr": "Üretici RINA Onayı, HHP/SHHP Çapa Tip Onayı, malzeme sertifikaları ve çekme tezgahı kalibrasyonunun doğrulanması",
        "detailTr": "Çapa veya zincir üreticisinin RINA onayı, HHP/SHHP çapalar için onaylı resim ve Tip Onayı, çelik döküm/hadde malzeme sertifikaları, ısıl işlem kayıtları ve yatay çekme (Proof/Breaking load) tezgahının kalibrasyonu kontrol edilir.",
        "tipTr": "HHP (Yüksek Tutma Güçlü) çapalarda gerçek kütleye karşılık gelen eşdeğer (ex-mass = 1.33 × gerçek kütle) Proof Load tablosuna dikkat edin ([1.6.2]).",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. D Ch. 4 Sec. 1 Par. 1.5",
        "sectionId": "Pt D, Ch 4, Sec 1",
        "page": 2497,
        "titleEn": "Anchor Drop Test (from 4 m height onto steel slab) and Hammering / Ringing Test (Part. D Ch. 4 Sec. 1 Par. 1.5)",
        "detailEn": "For cast steel anchors ([1.5]): Each cast piece is to be lifted to a height of 4 m and dropped onto a steel slab on a solid foundation, then suspended clear of the ground and hammered with a ≥ 3 kg sledgehammer to verify a clear ringing sound.",
        "titleTr": "Çelik döküm çapalar için Düşürme Testi (4 m yükseklikten çelik plakaya) ve Çekiçleme (Çınlama) Testi (Part. D Ch. 4 Sec. 1 Par. 1.5)",
        "detailTr": "Çelik döküm çapa tırnak (fluke/crown) ve beden (shank) parçaları 4 metre yükseklikten çelik bir zemin plakası üzerine serbest düşürülür; ardından askıya alınarak ≥ 3 kg balyozla vurulduğunda temiz/net bir çınlama sesi verdiği doğrulanır.",
        "tipTr": "Düşürme testi mutlaka Proof Load çekme testinden ÖNCE yapılır.",
        "condition": { "field": "equip_sub", "equals": "anchor" }
      },
      {
        "num": 3,
        "ruleRef": "Part. D Ch. 4 Sec. 1 Par. 1.6 & 1.7",
        "sectionId": "Pt D, Ch 4, Sec 1",
        "page": 2497,
        "titleEn": "Anchor Proof Load Test (Tab. 1), post-test MT/PT NDT, mass weighing and RINA stamping (Part. D Ch. 4 Sec. 1 Par. 1.6 - 1.8)",
        "detailEn": "Apply Proof Load per Tab. 1 between shackle and flukes at 1/3 distance from bill (tip) on each side; check freedom of rotation of fluke through full angle; carry out MT/PT (and UT for SHHP) after proof load; verify mass on calibrated scale (excluding stock, minus tolerance not allowed / +7% max, crown ≥ 60% of total mass for stockless anchors) and stamp RINA brand, mass, and certificate number.",
        "titleTr": "Çapa Proof Load Çekme Testi (Tablo 1), test sonrası MT/PT kontrolü, tartım ve RINA damgalama (Part. D Ch. 4 Sec. 1 Par. 1.6 - 1.8)",
        "detailTr": "Tablo 1'deki Proof Load yükü çapa tırnak ucundan 1/3 mesafeden uygulanır; kalıcı deformasyon olmadığı ve tırnakların her iki yöne tam açıyla rahatça döndüğü kontrol edilir. Çekme sonrası kritik radyüslere MT/PT uygulanır; kalibreli kantarda tartılarak ağırlığı doğrulanır ve RINA damgası vurulur.",
        "tipTr": "Çapa ağırlığı onaylı projedeki nominal kütleden düşük olmamalıdır; ayrıca tırnak+taç (crown) kütlesinin toplam çapa kütlesinin en az %60'ı olduğunu kontrol edin.",
        "condition": { "field": "equip_sub", "equals": "anchor" }
      },
      {
        "num": 4,
        "ruleRef": "Part. D Ch. 4 Sec. 1 Par. 2.10 & 2.11",
        "sectionId": "Pt D, Ch 4, Sec 1",
        "page": 2507,
        "titleEn": "Chain Cable & Accessories: Breaking Load Test (3-link sample), Full-Length Proof Load Test, Mechanical Tests & 5-Link Dimensional Check",
        "detailEn": "- Breaking Load (BL) Test: One 3-link sample taken from every 4 lengths (each 27.5 m) must withstand the Rule Breaking Load (Tab. 5) for 30 s.\n- Proof Load (PL) Test: Every full 27.5 m length of chain (and every shackle/swivel accessory) must undergo the full Proof Load test.\n- Mechanical Tests: Tensile and Charpy V-notch impact tests on link material & flash-butt weld zone (for Grade Q2/Q3).\n- Dimensional & NDT check: Check 5-link length (+2.5% / -0% tolerance), diameter, stud fit, MT/UT on welds/accessories, and RINA stamping on end links.",
        "titleTr": "Demir Zinciri ve Aksesuarları: Kopma Testi (Breaking Load), Tam Boy Proof Load Testi, Mekanik Testler ve 5-Bakla Ölçü Kontrolü ([2.10 & 2.11])",
        "detailTr": "- Kopma Yükü (Breaking Load) Testi: Her 4 kilit (4 × 27.5 m) zincirden alınan 3 baklalık numune Tablo 5'teki kopma yüküne 30 saniye dayanmalıdır.\n- Proof Load Testi: Her 27.5 m zincir boyunun tamamı ve her bir Kenter/Çapa kilidi Tablo 5/6'daki Proof Load yüküne tabi tutulur.\n- Mekanik ve Boyutsal Kontrol: Çekme ve Charpy darbe testleri yapılır; Proof Load sonrası 5 bakla boyu (tolerans +%2.5 / -%0), bakla çapı, lokma (stud) sıkılığı ve Kenter kilitlerinde MT/UT kontrol edilerek uç baklalar RINA damgalanır.",
        "tipTr": "Kenter kilitlerinde ve fırdöndülerde (swivel) Proof Load testi sonrası pimlerin el/çekiç ile rahatça sökülüp takılabildiğini (sıkışma olmadığını) ve %100 MT kontrolünü doğrulayın.",
        "condition": { "field": "equip_sub", "equals": "chain" }
      }
    ]
  },
  {
    "id": "welding-wpqr-and-consumables",
    "code": "MT-05",
    "category": "materials",
    "categoryTitleEn": "Part D — Materials, Equipment & Welding",
    "categoryTitleTr": "Part D — Malzeme, Dövme, Döküm, Zincir/Çapa ve Kaynak Testleri",
    "titleEn": "Welding Procedure Qualification Tests (WPQR — Steel, Aluminium, Pipes) & Welding Consumables Approval",
    "titleTr": "Kaynak Prosedürü Onay Testleri (WPQR — Çelik Sac/Boru, Alüminyum, Döküm Tamiri) ve Kaynak Sarf Malzemesi Testleri",
    "ruleRef": "Part. D - Ch. 5 - Sec. 2 & Sec. 4",
    "sectionId": "Pt D, Ch 5, Sec 4",
    "pdfPage": 2592,
    "keywords": ["welding", "wpqr", "wps", "pwps", "welder qualification", "butt weld", "fillet weld", "consumable", "electrode", "wire", "hardness hv10", "charpy", "macro", "kaynak", "kaynak prosedürü", "elektrot", "gazaltı", "tozaltı", "sec 2", "sec 4", "ch 5", "pt d"],
    "referenceTables": [
      {
        "titleEn": "Summary of Destructive Tests for Butt Weld WPQR on Steel Plates (Pt D, Ch 5, Sec 4 [2.3 & Fig. 2])",
        "titleTr": "Çelik Alın Kaynağı (Butt Weld) WPQR Test Plakası Tahribatlı Test Özeti (Pt D, Ch 5, Sec 4 [2.3])",
        "headers": ["Test Type / Test Türü", "Quantity / Adet", "Acceptance Criteria / Kabul Kriteri"],
        "rows": [
          ["Transverse Tensile Test (Enine Çekme)", "2 specimens", "Rm ≥ minimum specified tensile strength of base metal"],
          ["Transverse Bend Test (Enine Eğme: 2 Face + 2 Root, or 4 Side if t ≥ 12mm)", "4 specimens", "180° bend around mandrel (4×t for normal/32/36/40 steels); no flaw > 3 mm"],
          ["Charpy V-Notch Impact (WM, FL, FL+2mm, FL+5mm)", "3 specimens per notch location", "Per base steel grade temp & energy (e.g. AH36/DH36/EH36: 34 J or 47 J if heat input > 50 kJ/cm)"],
          ["Macro Examination & Vickers Hardness (HV10)", "1 cross-section", "Complete fusion, no cracks; Max HV10 ≤ 350 HV (≤ 380 HV for single-run; ≤ 420 HV for QT steels)"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "wpqr_joint",
        "questionEn": "What type of welding qualification test is being witnessed? (Pt D, Ch 5, Sec 4 / Sec 2)",
        "questionTr": "Hangi tip kaynak onay testine nezaret ediliyor? (Pt D, Ch 5, Sec 4 / Sec 2)",
        "options": [
          { "value": "butt_wpqr", "labelEn": "Butt Weld WPQR (Steel Plate or Pipe — 100% VT/RT/UT/MT + Tensile, Bend, Charpy, Macro, HV10)", "labelTr": "Alın Kaynağı (Butt Weld) WPQR (Sac veya Boru — %100 NDT + Çekme, Eğme, Charpy, Makro ve Sertlik)" },
          { "value": "fillet_wpqr", "labelEn": "Fillet Weld WPQR (T-Joint — VT + MT/PT + 2 Macro + HV10 + Fracture/Break Test)", "labelTr": "Köşe Kaynağı (Fillet Weld) WPQR (T-Birleştirme — VT + MT/PT + 2 Makro + HV10 Sertlik + Kırma Testi)" },
          { "value": "consumable", "labelEn": "Welding Consumable Initial / Annual Upgrade Test (Sec 2 — Deposited Metal + Butt Weld + Hydrogen)", "labelTr": "Kaynak Sarf Malzemesi (Tel/Elektrot/Toz) İlk veya Yıllık Onay Testi (Sec 2)" }
        ],
        "default": "butt_wpqr"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. D Ch. 5 Sec. 4 Par. 1 & 2",
        "sectionId": "Pt D, Ch 5, Sec 4",
        "page": 2592,
        "reqEn": "Welding of test assemblies per pWPS, non-destructive testing (VT, RT/UT, MT/PT after required delay) and destructive testing",
        "reqTr": "pWPS'e göre test plakasının kaynatılması, tahribatsız muayene (VT, RT/UT, MT/PT) ve tahribatlı mekanik/metalografik testler"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. D Ch. 5 Sec. 4 Par. 1.3 & 2.1",
        "sectionId": "Pt D, Ch 5, Sec 4",
        "page": 2592,
        "titleEn": "Verification of pWPS, base metal & RINA-approved welding consumable certificates, and witnessing of test assembly welding",
        "detailEn": "Check base metal certificates (steel grade, thickness, Ceq) and RINA Approval Certificate of welding consumables (Grade 2/3/3Y/4Y H15/H10/H5). Witness bevel preparation, fit-up, preheating temperature, interpass temperature, welding current (A), voltage (V), travel speed (mm/s), heat input (kJ/cm), shielding gas flow, and back-gouging in the specified welding position (PA, PB, PC, PD, PE, PF, PG).",
        "titleTr": "pWPS, ana malzeme ve RINA onaylı kaynak teli/elektrot sertifikalarının kontrolü ve kaynağın yapılmasına nezaret",
        "detailTr": "Ana malzeme sertifikası ve kaynak sarf malzemesinin (tel/elektrot/gaz) RINA Onay Sertifikası kontrol edilir. Kaynak ağzı hazırlığı, ön ısıtma (preheat), pasolar arası sıcaklık (interpass temp), akım (A), gerilim (V), ilerleme hızı, ısı girdisi (Heat Input — kJ/cm) ve kaynak pozisyonu kaydedilerek plaka sörveyör huzurunda kaynatılır ve damgalanır.",
        "tipTr": "Yüksek ısı girdili kaynaklarda (> 50 kJ/cm) ITAB (HAZ) darbe direncini doğrulamak için FL+2mm ve FL+5mm çentik yerlerinden de Charpy numunesi alınması zorunludur!",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. D Ch. 5 Sec. 4 Par. 2.2",
        "sectionId": "Pt D, Ch 5, Sec 4",
        "page": 2594,
        "titleEn": "Non-destructive testing (100% VT, 100% RT or UT, and 100% MT or PT) after required post-weld delay (Part. D Ch. 5 Sec. 4 Par. 2.2)",
        "detailEn": "Carry out NDT after any required PWHT and after minimum 24 hours delay (or 48 hours for high-strength quenched & tempered steels R ≥ 500 MPa to detect delayed hydrogen cold cracking): 100% Visual (VT per ISO 5817 Level B), 100% Surface NDT (MT or PT), and 100% Volumetric NDT (RT or UT for butt welds).",
        "titleTr": "Zorunlu bekleme süresi sonrası %100 Tahribatsız Muayene (VT, RT/UT ve MT/PT) (Part. D Ch. 5 Sec. 4 Par. 2.2)",
        "detailTr": "Gecikmeli hidrojen çatlağını tespit edebilmek için kaynak bitiminden en az 24 saat (yüksek mukavemetli QT çeliklerde 48 saat) sonra %100 Görsel (VT - ISO 5817 Seviye B), %100 Yüzey (MT veya PT) ve alın kaynaklarında %100 Radyografik (RT) veya Ultrasonik (UT) muayene yapılır.",
        "tipTr": "24 saat bekleme süresi dolmadan kesilen ve NDT yapılan WPQR plakalarını kabul etmeyin!",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. D Ch. 5 Sec. 4 Par. 2.3 & 2.4",
        "sectionId": "Pt D, Ch 5, Sec 4",
        "page": 2595,
        "titleEn": "Witnessing of Destructive Tests: Transverse Tensile, Bend, Charpy V-Notch Impact, Macrosection & Vickers Hardness (HV10)",
        "detailEn": "- For Butt Welds ([2.3]): Witness 2 transverse tensile tests (Rm ≥ min base metal Rm), 4 transverse bend tests (2 root + 2 face, or 4 side bends for t ≥ 12 mm; 180° around 4t mandrel with no defect > 3 mm), Charpy V-notch impact sets (weld centreline WM, fusion line FL, FL+2mm, FL+5mm), 1 macrosection etching, and Vickers HV10 hardness traverses (cap & root across BM–HAZ–WM; max ≤ 350 HV10).\n- For Fillet Welds ([2.4]): Witness 2 macrosections, HV10 hardness survey, and fracture/break test along full length.",
        "titleTr": "Tahribatlı Testlere Nezaret: Enine Çekme, Eğme, Charpy Darbe, Makro Dağlama ve Vickers Sertlik (HV10) (Part. D Ch. 5 Sec. 4 Par. 2.3 & 2.4)",
        "detailTr": "- Alın Kaynaklarında ([2.3]): 2 adet enine çekme, 4 adet 180° eğme (t ≥ 12 mm ise 4 adet yan eğme / side bend; kusur ≤ 3 mm), Charpy V-çentik darbe setleri (Kaynak merkezi WM, Ergime hattı FL, FL+2, FL+5), 1 adet makro kesit ve HV10 sertlik taraması (ITAB dahil maks. ≤ 350 HV10; tek paso ≤ 380 HV10) yapılır.\n- Köşe Kaynaklarında ([2.4]): 2 adet makro kesit, HV10 sertlik ve tam boy kırma (fracture) testi yapılır.",
        "tipTr": "Vickers sertlik (HV10) ölçüm noktalarının ergime hattına (Fusion Line) en çok 0.5 mm mesafede ITAB (HAZ) içinden alındığından emin olun!",
        "condition": "always"
      }
    ]
  }
]

with open("public/data/part3.json", "w", encoding="utf-8") as f:
    json.dump(part3_items, f, ensure_ascii=False, indent=2)

# Merge part1, part2, part3 into equipment-fat-db.json
with open("public/data/part1.json", "r", encoding="utf-8") as f1:
    p1 = json.load(f1)
with open("public/data/part2.json", "r", encoding="utf-8") as f2:
    p2 = json.load(f2)

all_items = p1 + p2 + part3_items
with open("public/data/equipment-fat-db.json", "w", encoding="utf-8") as fout:
    json.dump(all_items, fout, ensure_ascii=False, indent=2)

print("Total merged FAT items:", len(all_items))
