import json, os

part2_items = [
  {
    "id": "diesel-engines-shop-trial",
    "code": "MC-01",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Diesel Engines (Main Propulsion, Auxiliary Generator Sets & Dual-Fuel) — Workshop Trials & Hydrostatic Tests",
    "titleTr": "Dizel Motorlar (Ana Makine, Jeneratör Seti ve Çift Yakıtlı Motorlar) — Fabrika Test Yatağı (Shop Trial) ve Hidrostatik Testler",
    "ruleRef": "Part. C - Ch. 1 - Sec. 2",
    "sectionId": "Pt C, Ch 1, Sec 2",
    "pdfPage": 1450,
    "keywords": ["diesel engine", "main engine", "auxiliary engine", "genset", "dizel motor", "ana makine", "yardımcı makine", "shop trial", "crankshaft", "turbocharger surge", "sec 2"],
    "referenceTables": [
      {
        "titleEn": "Summary of Shop Trial Load Points (Pt C, Ch 1, Sec 2 [7.4.4])",
        "titleTr": "Dizel Motor Test Yatağı (Shop Trial) Yük Kademeleri Özeti ([7.4.4])",
        "headers": ["Load Point / Yük Kademesi", "Main Propulsion Engine (Ana Makine)", "Generator Driving Engine (Jeneratör Motoru)"],
        "rows": [
          ["100% Power (MCR) at n0", "At least 60 min (2 sets of readings 30 min apart)", "At least 60 min (2 sets of readings 30 min apart)"],
          ["110% Overload Power", "At 1.032 × n0 for 15 min after steady state", "At rated speed n0 for 15 min after steady state"],
          ["Partial Loads", "90%, 75%, 50%, 25% along nominal propeller curve", "75%, 50%, 25% power and Idle at constant speed n0"],
          ["Fuel Rack / Governor Limit", "Block fuel delivery to 100% MCR after trial", "Adjust to 100% + 10% transient overload margin"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "engine_app",
        "questionEn": "What is the intended application of the diesel engine? (Pt C, Ch 1, Sec 2 [7.4.4])",
        "questionTr": "Dizel motorun kullanım amacı nedir? (Pt C, Ch 1, Sec 2 [7.4.4])",
        "options": [
          { "value": "propulsion", "labelEn": "Main Propulsion Engine driving propeller/impeller ([7.4.4 a])", "labelTr": "Pervane Tahrik Eden Ana Makine ([7.4.4 a])" },
          { "value": "generator", "labelEn": "Engine driving Generator for Electric Propulsion or Auxiliary Services ([7.4.4 b & c])", "labelTr": "Jeneratör Tahrik Eden Yardımcı / Elektrikli Tahrik Motoru ([7.4.4 b & c])" },
          { "value": "propulsion_pto", "labelEn": "Propulsion Engine also driving PTO Generator ([7.4.4 d])", "labelTr": "PTO (Şaft Jeneratörü) Tahrikli Ana Makine ([7.4.4 d])" }
        ],
        "default": "propulsion"
      },
      {
        "id": "electronic_control",
        "questionEn": "Is the engine electronically controlled (e.g. Common Rail / electronic fuel injection & valve actuation)? ([7.4.6])",
        "questionTr": "Motor elektronik kontrollü mü (örn. Common Rail / elektronik yakıt enjeksiyonlu)? ([7.4.6])",
        "options": [
          { "value": "Yes", "labelEn": "Yes (Integration tests required per [7.4.6] & IACS UR E27)", "labelTr": "Evet (Entegrasyon testleri [7.4.6] ve siber güvenlik uygulanır)" },
          { "value": "No", "labelEn": "No (Conventional mechanical fuel injection)", "labelTr": "Hayır (Klasik mekanik enjeksiyonlu)" }
        ],
        "default": "Yes"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.1 - 7.3",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1476,
        "reqEn": "Material and NDT certification of major engine components (Tab. 8) and Hydrostatic tests (Tab. 9)",
        "reqTr": "Ana motor bileşenlerinin malzeme/NDT sertifikaları (Tablo 8) ve hidrostatik basınç testleri (Tablo 9)"
      },
      {
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.4",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1482,
        "reqEn": "Workshop inspections and testbed trials ([7.4.1] to [7.4.7])",
        "reqTr": "Fabrika muayeneleri ve test yatağı (Shop Trial) kabul testleri ([7.4.1] - [7.4.7])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.4.3 c)",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1483,
        "titleEn": "Verification of calibration records for testbed instrumentation and recording of ambient conditions (Part. C Ch. 1 Sec. 2 Par. 7.4.3)",
        "detailEn": "Check calibration certificates of dynamometer/water brake, fuel flowmeter, tachometer, pressure/temperature sensors. Record ambient air temperature, ambient air pressure (barometric), and atmospheric relative humidity ([7.4.3 a]).",
        "titleTr": "Test yatağı ölçüm cihazlarının kalibrasyon kontrolü ve ortam şartlarının kaydedilmesi (Part. C Ch. 1 Sec. 2 Par. 7.4.3)",
        "detailTr": "Dinamometre (su freni), yakıt debimetresi, takometre, silindir maksimum yanma basıncı (Pmax) ölçer ve sıcaklık sensörlerinin kalibrasyonları kontrol edilir. Ortam sıcaklığı, barometrik basınç ve bağıl nem kaydedilir.",
        "tipTr": "Özgül yakıt sarfiyatı (SFOC) hesabında kullanılan yakıtın alt ısıl değeri (LHV) analiz raporunu kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.1 - 7.3 (Tab. 8 & Tab. 9)",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1476,
        "titleEn": "Examination of Type Approval Certificate, component material/NDT certificates (Tab. 8) and hydrostatic test records (Tab. 9)",
        "detailEn": "Verify valid RINA Engine Type Approval Certificate, Society Certificates (SC) / Works Certificates (W) for crankshaft, connecting rods, piston crowns, cylinder liners, cylinder heads, tie rods, and bolts (Tab. 8), plus hydrostatic test records (Tab. 9: cylinder cover cooling space 0.7 MPa, liner 0.7 MPa, water jacket 0.4 MPa, charge air cooler 1.5×p min 0.4 MPa, fuel injection system 1.5×p or p+30 MPa).",
        "titleTr": "Tip Onay Sertifikası, parça malzeme/NDT sertifikaları (Tablo 8) ve hidrostatik test kayıtlarının (Tablo 9) incelenmesi",
        "detailTr": "RINA Tip Onay Sertifikası, krank mili, biyel kolları, piston kafaları, gömlekler, kaverler ve saplamaların (Tablo 8) RINA sertifikaları ile Tablo 9 hidrostatik test raporları (kaver/gömlek soğutma 7 bar, ceket 4 bar, hava soğutucu 1.5×p min 4 bar) doğrulanır.",
        "tipTr": "Krank mili üzerindeki RINA soğuk damgasını (hard stamp) ve seri numarasını sertifika ile karşılaştırın.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.4.1",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1482,
        "titleEn": "Inspection of fire safety arrangements: jacketed high-pressure fuel lines, pipe screening and hot surfaces (< 220°C) (Part. C Ch. 1 Sec. 2 Par. 7.4.1)",
        "detailEn": "Inspect jacketing of high-pressure fuel oil lines and leakage detection alarm system; screening of flammable liquid pipe connections; and insulation of hot surfaces by taking random temperature readings at rated power (must not exceed 220°C per Sec 1 [3.7.1]).",
        "titleTr": "Çift cidarlı (Jacketed) yüksek basınç yakıt boruları, sıçrama siperleri ve sıcak yüzey (< 220°C) kontrolü (Part. C Ch. 1 Sec. 2 Par. 7.4.1)",
        "detailTr": "Yüksek basınç yakıt borularının çift cidarlı (jacketed) olduğu ve kaçak alarmının çalıştığı, yanıcı sıvı flanşlarında sıçrama koruyucu bant/siper bulunduğu ve %100 yükte egzoz/turbo sıcak yüzey sıcaklıklarının 220°C'yi aşmadığı (termal kamera / temas termometresi ile) doğrulanır.",
        "tipTr": "220°C üzerindeki açıkta kalan flanş veya egzoz kompansatörleri gemide yangın riski oluşturur; yalıtım eksiklerini test yatağında raporlayın.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.4.3 & 7.4.4",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1483,
        "titleEn": "Testbed load trials — 100% MCR (60 min), 110% Overload (15 min), and partial loads (Part. C Ch. 1 Sec. 2 Par. 7.4.4)",
        "detailEn": "Run engine at:\n- 100% power (MCR) at n0 for at least 60 min (take at least two full sets of readings at 30 min interval: power, speed, fuel index, Pmax, exhaust temp per cylinder & before/after TC, charge air temp/press, TC speed, lube oil & cooling water temp/press).\n- 110% overload for 15 min after reaching steady state (at 1.032×n0 for propulsion or n0 for generator engines).\n- Partial loads: 90%, 75%, 50%, 25% (and idle for gensets). Adjust/block fuel stop after test.",
        "titleTr": "Test yatağı yük testleri — %100 MCR (60 dk), %110 Aşırı Yük (15 dk) ve kısmi yük kademeleri (Part. C Ch. 1 Sec. 2 Par. 7.4.4)",
        "detailTr": "- %100 MCR yükte en az 60 dakika çalıştırılır ve 30 dk arayla en az iki tam kayıt (güç, devir, yakıt indeksi, Pmax, her silindir egzoz sıcaklığı, turbo devri, dolgulu hava ve yağ/su basınç-sıcaklıkları) alınır.\n- %110 aşırı yükte rejime girdikten sonra 15 dakika çalıştırılır.\n- %90, %75, %50, %25 kısmi yüklerde çalıştırılır. Test sonunda yakıt kremayeri/limiti ana makinede %100'e, jeneratörde %110 geçici regülasyon payına ayarlanır/mühürlenir.",
        "tipTr": "Silindirler arası egzoz sıcaklık sapmasının ve maksimum yanma basıncı (Pmax) farklarının üretici limitleri içinde olduğunu kontrol edin.",
        "condition": "always"
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.4.5",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1484,
        "titleEn": "Turbocharger matching and surge margin verification (Part. C Ch. 1 Sec. 2 Par. 7.4.5)",
        "detailEn": "For propulsion engines with Category C turbochargers (unless waived by identical configuration test): verify no continuous surging occurs during speed reduction at constant torque (4-stroke: 100% down to 90% power, and 50% power/80% speed down to 72% speed; 2-stroke: ≥10% surge margin or sudden load drop 100% to 50% / single-cylinder fuel cut-off stabilizing within 20 s).",
        "titleTr": "Turboşarj uyumu ve pompaj (Surge Margin) doğrulaması (Part. C Ch. 1 Sec. 2 Par. 7.4.5)",
        "detailTr": "Kategori C turboşarjlı ana makinelerde (özdeş konfigürasyonda daha önce kanıtlanmamışsa) sabit torkta devir düşürme (4 zamanlıda %100'den %90'a ve %80 devirden %72'ye) veya ani yük düşümü (%100'den %50'ye) sırasında sürekli pompaj (continuous surging) oluşmadığı doğrulanır.",
        "tipTr": "Süpürme (scavenge) bölgesinden patlama benzeri tekrarlayan pompaj sesi gelmemelidir.",
        "condition": { "field": "engine_app", "notEquals": "generator" }
      },
      {
        "num": 6,
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 4.7, 7.4.1 & 7.4.6",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1484,
        "titleEn": "Governor tests, overspeed trip, safety alarms/shutdowns and electronic integration test (Part. C Ch. 1 Sec. 2 Par. 4.7, 7.4.1 & 7.4.6)",
        "detailEn": "Verify governor compliance ([4.7.3]-[4.7.5]: sudden load drop/pick-up speed excursion ≤ 10% transient and ≤ 5% permanent), overspeed protective device trip (+15% speed), lube oil low pressure / jacket water high temp / oil mist detector / crankcase relief valve arrangements, and electronic control system integration tests ([7.4.6]: primary/backup power failure, ECU redundancy).",
        "titleTr": "Governör testi, aşırı devir (Overspeed) trip, emniyet durdurmaları ve elektronik entegrasyon testi (Part. C Ch. 1 Sec. 2 Par. 4.7 & 7.4.6)",
        "detailTr": "Governör ani yük atma/alma hız regülasyonu (geçici ≤ %10, kalıcı ≤ %5), aşırı devir emniyet kapaması (%115 devir), düşük yağ basıncı / yüksek ceket suyu sıcaklığı alarm ve shutdown fonksiyonları, karter yağ buharı dedektörü (OMD) ve elektronik kontrollü motorlarda ECU/güç yedekliliği entegrasyon testleri ([7.4.6]) yapılır.",
        "tipTr": "Elektronik motorlarda ana güç beslemesi kesildiğinde yedek besleme ile motorun stop etmeden çalışmaya devam ettiğini doğrulayın.",
        "condition": "always"
      },
      {
        "num": 7,
        "ruleRef": "Part. C Ch. 1 Sec. 2 Par. 7.4.3 d) & 7.4.7",
        "sectionId": "Pt C, Ch 1, Sec 2",
        "page": 1484,
        "titleEn": "Post-trial crankshaft deflection check and opening up of selected components for inspection (Part. C Ch. 1 Sec. 2 Par. 7.4.3 d & 7.4.7)",
        "detailEn": "After testbed trials, stop engine, check crankcase safety doors, measure hot crankshaft web deflections, and open up random cylinder/crankcase components selected by the Surveyor (main/crankpin bearing shells, piston skirt/rings, cylinder liner surface, cams/rollers) for visual inspection.",
        "titleTr": "Test sonrası krank mili defleksiyon ölçümü ve seçilen yatak/silindirlerin açılarak muayenesi (Part. C Ch. 1 Sec. 2 Par. 7.4.3 d & 7.4.7)",
        "detailTr": "Test bitiminde krank mili web defleksiyonları ölçülür; sörveyör tarafından seçilen en az bir silindirin ana yatak, kol yatağı (crankpin), piston etek/segmanları, silindir gömleği honlama yüzeyi ve kem şaftı açılarak sürtünme veya aşırı ısınma izi olmadığı doğrulanır.",
        "tipTr": "Açılan yatak keplerinin tekrar sıkılmasında hidrolik gerdirme basıncı veya tork değerini kontrol edin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "boilers-pressure-vessels-heaters",
    "code": "MC-02",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Boilers, Steam Generators, Thermal Oil Heaters, Heat Exchangers & Pressure Vessels (Class 1, 2, 3)",
    "titleTr": "Kazanlar, Kızgın Yağ Kazanı, Eşanjörler (Cooler/Heater) ve Basınçlı Kaplar (Class 1, 2, 3 — Hava Tüpleri vb.)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 3",
    "sectionId": "Pt C, Ch 1, Sec 3",
    "pdfPage": 1486,
    "keywords": ["boiler", "pressure vessel", "air receiver", "heat exchanger", "cooler", "heater", "condenser", "thermal oil", "kazan", "basınçlı kap", "hava tüpü", "eşanjör", "kuler", "sec 3"],
    "calculator": {
      "type": "pressure_vessel",
      "labelTr": "Kazan & Basınçlı Kap Hidrostatik Test Basıncı Hesaplayıcı (Pt C, Ch 1, Sec 3 [7.3.2])",
      "labelEn": "Boiler & Pressure Vessel Hydrostatic Test Pressure Calculator (Pt C, Ch 1, Sec 3 [7.3.2])",
      "defaultPressureBar": 30
    },
    "referenceTables": [
      {
        "titleEn": "Hydrostatic Test Pressure Formulae (Pt C, Ch 1, Sec 3 [7.3.2])",
        "titleTr": "Hidrostatik Test Basıncı Formülleri (Pt C, Ch 1, Sec 3 [7.3.2])",
        "headers": ["Design Pressure Range (p)", "Hydrostatic Test Pressure (pt)", "Notes / Notlar"],
        "rows": [
          ["p ≤ 4 MPa (≤ 40 bar)", "pt = 1.5 × p", "Accessories tested at ≥ 1.5 × p ([7.3.3])"],
          ["4 MPa < p ≤ 25 MPa (40 – 250 bar)", "pt = 1.4 × p + 0.4 MPa (1.4×p + 4 bar)", "Design temp > 300°C: pt = 1.5 × (K100 / K) × p"],
          ["p > 25 MPa (> 250 bar)", "pt = p + 10.4 MPa (p + 104 bar)", "Membrane stress ≤ 90% of yield stress at test temp"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "vessel_class",
        "questionEn": "What is the class/type of the boiler or pressure vessel? (Pt C, Ch 1, Sec 3 [1.4 & 7.1])",
        "questionTr": "Kazan veya basınçlı kabın sınıfı/tipi nedir? (Pt C, Ch 1, Sec 3 [1.4 & 7.1])",
        "options": [
          { "value": "class1_boiler", "labelEn": "Boiler, Thermal Oil Heater or Class 1 Pressure Vessel (Surveyor material + fabrication + hydrotest)", "labelTr": "Kazan, Kızgın Yağ Isıtıcısı veya Class 1 Basınçlı Kap (Malzeme + İmalat + Hidrostatik Test)" },
          { "value": "class2_3", "labelEn": "Class 2 or Class 3 Pressure Vessel / Heat Exchanger (Mill material cert + Surveyor hydrotest)", "labelTr": "Class 2 veya Class 3 Basınçlı Kap / Eşanjör / Hava Tüpü (Üretici malzeme sertifikası + Sörveyör Hidrotest)" }
        ],
        "default": "class1_boiler"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 3 Par. 3 & 4",
        "sectionId": "Pt C, Ch 1, Sec 3",
        "page": 1500,
        "reqEn": "Design, fabrication, welding qualification (WPQR), post-weld heat treatment (PWHT) and NDT (RT/UT/MT/PT)",
        "reqTr": "Tasarım, imalat, kaynak prosedür onayı (WPQR), kaynak sonrası ısıl işlem (PWHT) ve tahribatsız muayene (NDT)"
      },
      {
        "ruleRef": "Part. C Ch. 1 Sec. 3 Par. 7",
        "sectionId": "Pt C, Ch 1, Sec 3",
        "page": 1547,
        "reqEn": "Material test ([7.1]), workshop inspections ([7.2]), hydrostatic tests ([7.3]) and certification ([7.4])",
        "reqTr": "Malzeme testi ([7.1]), atölye kontrolleri ([7.2]), hidrostatik test ([7.3]) ve sertifikasyon ([7.4])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 1 Sec. 3",
        "sectionId": "Pt C, Ch 1, Sec 3",
        "page": 1547,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify valid calibration certificates of at least two independent pressure gauges (or calibrated digital transducer + gauge) used on the hydrostatic test rig.",
        "titleTr": "Hidrostatik test manometrelerinin ve ölçüm cihazlarının kalibrasyon durumunun doğrulanması.",
        "detailTr": "Hidrostatik test düzeneğinde kullanılan manometrelerin (tercihen çift manometre, kadranda test basıncı skala ortasında ~1.5-2 kat aralığında olacak şekilde) geçerli kalibrasyon sertifikaları kontrol edilir.",
        "tipTr": "Manometre kadran aralığının test basıncının yaklaşık 1.5 ile 3 katı arasında olması hassas okuma için şarttır.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 3 Par. 7.1",
        "sectionId": "Pt C, Ch 1, Sec 3",
        "page": 1547,
        "titleEn": "Verification of material certificates for pressure parts and welding consumables (Part. C Ch. 1 Sec. 3 Par. 7.1)",
        "detailEn": "For boilers, steam generators, thermal oil heaters, and Class 1 pressure vessels ([7.1.2] & [7.1.3]), testing of materials for pressure parts is to be witnessed by the Surveyor (RINA Class Certificate 'C'). For Class 2 & 3 vessels, 3.1 material manufacturer certificates are verified against approved drawings.",
        "titleTr": "Basınçlı kısımların malzeme sertifikaları ve kaynak sarf malzemelerinin kontrolü (Part. C Ch. 1 Sec. 3 Par. 7.1)",
        "detailTr": "Kazanlar, kızgın yağ ısıtıcıları ve Class 1 basınçlı kapların basınç taşıyan sac, aynalık, boru ve nozul malzemelerinde RINA (C) sertifikası ([7.1.2], [7.1.3]); Class 2/3 kaplarda ise onaylı resme uygun EN 10204 3.1 sertifikaları ve döküm (heat) numaraları kontrol edilir.",
        "tipTr": "Gövde sacı ve bombeli kapak (dish end) üzerindeki malzeme döküm (heat/plate) numaralarını sertifika ile eşleştirin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 3 Par. 4 & 7.2",
        "sectionId": "Pt C, Ch 1, Sec 3",
        "page": 1548,
        "titleEn": "Review of welding (WPQR/WQ), NDT reports (RT/UT/MT/PT), weld production test plates and PWHT charts (Part. C Ch. 1 Sec. 3 Par. 4 & 7.2)",
        "detailEn": "Verify approved WPS/WPQR, welder qualifications, mechanical test results of production weld test plates (where required for Class 1/2), NDT reports (100% RT/UT on Class 1 butt welds, spot RT on Class 2, MT/PT on nozzles/fillets), and Post-Weld Heat Treatment (PWHT) time-temperature furnace charts.",
        "titleTr": "Kaynak (WPS/WPQR), NDT raporları (RT/UT/MT/PT), kaynak test plakası ve ısıl işlem (PWHT) diyagramlarının incelenmesi",
        "detailTr": "Onaylı WPS/WPQR, kaynakçı sertifikaları, üretim kaynak test plakası (production test coupon) mekanik test sonuçları, radyografik/ultrasonik/manyetik/penetran NDT raporları ve gerilim giderme ısıl işlemi (PWHT) fırın sıcaklık-zaman grafikleri incelenir.",
        "tipTr": "Isıl işlem (PWHT) gereken kaplarda hidrostatik test mutlaka tüm kaynaklar ve ısıl işlem TAMAMLANDIKTAN sonra yapılmalıdır ([7.3.4 a]).",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 3 Par. 7.3.2 - 7.3.5",
        "sectionId": "Pt C, Ch 1, Sec 3",
        "page": 1548,
        "titleEn": "Hydrostatic pressure test prior to lagging, painting or lining (Part. C Ch. 1 Sec. 3 Par. 7.3.2 & 7.3.4)",
        "detailEn": "Carry out hydrostatic test after all openings are cut, all welding and heat treatment completed, and WITHOUT lagging, paint or lining ([7.3.4 a]):\n- For p ≤ 4 MPa: pt = 1.5 × p\n- For 4 < p ≤ 25 MPa: pt = 1.4 × p + 0.4 MPa\n- For p > 25 MPa: pt = p + 10.4 MPa\n- If design temp > 300°C: pt = 1.5 × (K100 / K) × p.\n- Accessories ([7.3.3]): pt ≥ 1.5 × p. Maintain pressure long enough for complete visual examination with zero leakage or permanent deformation.",
        "titleTr": "İzolasyon ve boya öncesi hidrostatik basınç testi (Part. C Ch. 1 Sec. 3 Par. 7.3.2 & 7.3.4)",
        "detailTr": "Tüm delikler açıldıktan, kaynak ve ısıl işlemler bittikten sonra, ÜZERİNDE İZOLASYON, BOYA VEYA KAPLAMA YOKKEN ([7.3.4 a]) hidrostatik test uygulanır:\n- p ≤ 4 MPa (40 bar) ise: pt = 1.5 × p\n- 4 < p ≤ 25 MPa ise: pt = 1.4 × p + 0.4 MPa\n- Tasarım sıcaklığı > 300°C ise: pt = 1.5 × (K100 / K) × p.\nEşanjörlerde hem gövde (shell) hem boru (tube) tarafı ayrı ayrı test edilir; kaçak, terleme veya kalıcı deformasyon olmamalıdır.",
        "tipTr": "Eşanjörlerde (cooler/heater) bir taraf basınçlandırılırken diğer tarafın tapaları açık bırakılarak boru aynasından (tube sheet) iç kaçak olup olmadığı gözlemlenmelidir!",
        "condition": "always"
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 1 Sec. 3 Par. 7.2 & 7.3.3",
        "sectionId": "Pt C, Ch 1, Sec 3",
        "page": 1548,
        "titleEn": "Internal & external visual/dimensional inspection, safety valve set-pressure check and stamping (Part. C Ch. 1 Sec. 3 Par. 7.2 & 7.3.3)",
        "detailEn": "Carry out internal and external visual and dimensional examination (shell thickness, dished heads, manholes, tube expansion/rolling), verify safety valve set pressure & popping test, and verify permanent nameplate & RINA stamp.",
        "titleTr": "İç/dış görsel ve boyutsal muayene, emniyet valfi (Safety Valve) açma basıncı testi ve damgalama",
        "detailTr": "Menhollerden iç ve dış görsel kontrol, et kalınlığı ve boyut kontrolü yapılır; kazan/hava tüpü emniyet valflerinin (safety relief valve) tasarım basıncında açma ve sızdırmazlık testi doğrulanır, etiket (Nameplate) ve RINA soğuk damgası vurulur.",
        "tipTr": "Emniyet valfi ayarlandıktan sonra kurşun mühür (lead seal) ile mühürlendiğini kontrol edin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "pumps-and-compressors",
    "code": "MC-03",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Pumps & Air Compressors (Bilge, Fire, Ballast, Boiler Feed, Fuel/Lube Oil Pumps & Starting Air Compressors)",
    "titleTr": "Pompalar ve Hava Kompresörleri (Sintine, Yangın, Balast, Kazan Besleme, Yakıt/Yağ Pompaları ve İlk Hareket Hava Kompresörleri)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 10, Par. 21.4.5 & 21.5.1",
    "sectionId": "Pt C, Ch 1, Sec 10",
    "pdfPage": 1713,
    "keywords": ["pump", "compressor", "fire pump", "bilge pump", "ballast pump", "boiler feed pump", "air compressor", "pompa", "yangın pompası", "sintine pompası", "balast pompası", "kompresör", "hava kompresörü", "sec 10", "tab 36"],
    "calculator": {
      "type": "pump_compressor",
      "labelTr": "Pompa & Kompresör Hidrostatik Test Basıncı Hesaplayıcı (Pt C, Ch 1, Sec 10 [21.4.5])",
      "labelEn": "Pump & Compressor Hydrostatic Test Pressure Calculator (Pt C, Ch 1, Sec 10 [21.4.5])",
      "defaultPressureBar": 10
    },
    "referenceTables": [
      {
        "titleEn": "Table 36 (Extract) : Certification & Testing of Pumps and Compressors (Pt C, Ch 1, Sec 10 [21.6])",
        "titleTr": "Tablo 36 (Özet) : Pompa ve Kompresörler İçin Malzeme ve Ürün Sertifika Gereksinimleri",
        "headers": ["Item / Ekipman", "Material Cert / Malzeme Sert.", "Product Cert / Ürün Sert.", "Special Required Tests / Özel Zorunlu Testler"],
        "rows": [
          ["All Pumps & Compressors (Essential)", "W (Works' Cert)", "C (RINA Class Cert)", "Hydrostatic test pH ([21.4.5]): 1.5×p (min 0.4 MPa / 4 bar)"],
          ["Bilge and Fire Pumps", "W (Works' Cert)", "C (RINA Class Cert)", "Hydrostatic test ([21.4.5]) + Performance (Q-H) Running Test ([21.5.1 a])"],
          ["Main Boiler Feed & Forced Circ. Pumps", "C (RINA Class Cert for casing, bolts, main parts, rotor)", "C (RINA Class Cert)", "Hydrostatic test + Rotor Balancing Test ([21.5.1 b]) + Performance Test"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "pump_comp_type",
        "questionEn": "Which type of pump or compressor is being inspected? (Pt C, Ch 1, Sec 10 [21.4.5, 21.5.1 & Tab. 36])",
        "questionTr": "Hangi tip pompa veya kompresör test ediliyor? (Pt C, Ch 1, Sec 10 [21.4.5, 21.5.1 & Tab. 36])",
        "options": [
          { "value": "bilge_fire", "labelEn": "Bilge Pump / Fire Pump / Emergency Fire Pump ([21.5.1 a])", "labelTr": "Sintine Pompası / Yangın Pompası / Acil Yangın Pompası ([21.5.1 a])" },
          { "value": "boiler_feed", "labelEn": "Main Boiler Feed Pump / Forced Circulation Pump ([21.5.1 b & Tab. 36])", "labelTr": "Ana Kazan Besleme (Feed) veya Sirkülasyon Pompası ([21.5.1 b & Tab. 36])" },
          { "value": "compressor", "labelEn": "Starting / Service Air Compressor ([21.4.5 & Sec 2])", "labelTr": "İlk Hareket (Starting) veya Servis Hava Kompresörü ([21.4.5])" },
          { "value": "other_pump", "labelEn": "Other Essential Service Pump (Cooling, Ballast, Fuel Oil, Lube Oil)", "labelTr": "Diğer Esas Servis Pompaları (Soğutma, Balast, Yakıt, Yağlama)" }
        ],
        "default": "bilge_fire"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.4.5",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1713,
        "reqEn": "Hydrostatic tests of cylinders, covers, casings and coolers of pumps and compressors",
        "reqTr": "Pompa ve kompresörlerin silindir, kapak, gövde (casing) ve ara soğutucularının hidrostatik testleri"
      },
      {
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.5.1 & Tab. 36",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1713,
        "reqEn": "Performance tests, rotor balancing test (boiler feed pumps) and certification per Tab. 36",
        "reqTr": "Performans (debi-basma yüksekliği) testi, rotor balans testi (kazan besleme pompaları) ve Tablo 36 sertifikasyonu"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 1 Sec. 10",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1710,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify valid calibration certificates of pressure gauges, flowmeters (magnetic/orifice), tachometer, power analyzer, and thermometer.",
        "titleTr": "Test manometreleri, debimetre ve güç ölçüm cihazlarının kalibrasyon durumunun doğrulanması.",
        "detailTr": "Basınç manometreleri, debimetre, takometre ve elektrik güç analizörünün kalibrasyon sertifikalarını doğrulayın.",
        "tipTr": "Hem hidrostatik test standındaki hem de performans test standındaki manometrelerin kalibrasyonunu ayrı ayrı kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 10 Tab. 36",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1714,
        "titleEn": "Examination of technical documentation, material certificates and visual inspection (Part. C Ch. 1 Sec. 10 Tab. 36)",
        "detailEn": "Per Tab. 36 No. 3: Verify Works' Certificates (W) for materials of general pumps/compressors, or Society Certificates (C) for casing, bolts, main parts, and rotor of main boiler feed & forced circulation pumps. Verify compliance with approved drawings and nameplate data.",
        "titleTr": "Teknik dokümantasyon, malzeme sertifikaları (Tablo 36) ve görsel muayene",
        "detailTr": "Tablo 36 No. 3 uyarınca genel pompa ve kompresörlerde üretici malzeme sertifikası (W - 3.1), ana kazan besleme ve sirkülasyon pompalarının gövde, saplama, mil ve çarklarında ise RINA (C - 3.2) malzeme sertifikası kontrol edilir. Gövde döküm numaraları ve etiket bilgileri doğrulanır.",
        "tipTr": "Ana kazan besleme pompalarında (Main Boiler Feed Pump) malzeme sertifikasının W değil C (RINA 3.2) olması kural gereğidir!",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.4.5",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1713,
        "titleEn": "Hydrostatic test of cylinders, covers, casings and coolers (Part. C Ch. 1 Sec. 10 Par. 21.4.5)",
        "detailEn": "Cylinders, covers and casings of pumps and compressors are to be subjected to a hydrostatic test at pressure pH:\n- pH = 1.5 × p (where p ≤ 4 MPa)\n- pH = 1.4 × p + 0.4 MPa (where 4 < p ≤ 25 MPa)\n- pH = p + 10.4 MPa (where p > 25 MPa)\n- Minimum pH = 0.4 MPa (4 bar).\n- Compressor water spaces & intercoolers ([21.4.5 c, d]): 1.5 × design pressure (minimum 0.2 MPa / 2 bar for water spaces).",
        "titleTr": "Pompa ve kompresör gövde, silindir, kapak ve soğutucularının hidrostatik testi (Part. C Ch. 1 Sec. 10 Par. 21.4.5)",
        "detailTr": "Pompa gövdeleri ve kompresör silindir/kapakları aşağıdaki pH basıncında hidrostatik teste tabi tutulur:\n- p ≤ 4 MPa (40 bar) için: pH = 1.5 × p (ancak en az 0.4 MPa = 4 bar!)\n- 4 < p ≤ 25 MPa için: pH = 1.4 × p + 0.4 MPa\n- Kompresör su ceketleri için: 1.5 × p (en az 0.2 MPa = 2 bar).",
        "tipTr": "Tasarım basıncı düşük (örn. 2 bar) olan pompalarda bile 1.5×p = 3 bar yerine kural gereği minimum 4 bar (0.4 MPa) uygulanmalıdır!",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.5.1 b)",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1713,
        "titleEn": "Rotor balancing test for main boiler centrifugal feed pumps (Part. C Ch. 1 Sec. 10 Par. 21.5.1 b)",
        "detailEn": "Rotors of centrifugal feed pumps for main boilers are to undergo a balancing test.",
        "titleTr": "Ana kazan santrifüj besleme (Feed) pompası rotoru balans testi (Part. C Ch. 1 Sec. 10 Par. 21.5.1 b)",
        "detailTr": "Ana kazan santrifüj besleme pompalarının rotor/çark grubuna dinamik balans testi uygulanır ve balans raporu doğrulanır.",
        "tipTr": "Diğer santrifüj pompalarda da çark (impeller) statik/dinamik balans raporunu inceleyin.",
        "condition": { "field": "pump_comp_type", "equals": "boiler_feed" }
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.5.1 a)",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1713,
        "titleEn": "Performance and running test — Q-H curve, power, vibration, relief valve & temperature rise (Part. C Ch. 1 Sec. 10 Par. 21.5.1)",
        "detailEn": "Verify pump/compressor running performance across operating points (shut-off/minimum flow, rated capacity Q & head H, overload flow, NPSH/suction capability, shaft power, bearing temperature & vibration, and safety relief valve set pressure on positive displacement pumps and each compressor stage).",
        "titleTr": "Performans (Debi - Basma Yüksekliği Q-H / Kapasite) ve çalışma testi (Part. C Ch. 1 Sec. 10 Par. 21.5.1)",
        "detailTr": "Pompalarda en az 5 noktada (kapalı vana/min debi, nominal debi Q ve basma yüksekliği H, maksimum debi) performans eğrisi, çekilen akım/güç, yatak sıcaklığı, salmastra sızdırmazlığı ve titreşim ölçülür. Dişli/vidalı pompalarda ve hava kompresörlerinin her kademesinde emniyet valfi (safety valve) açma testi ile kompresör dolum kapasitesi/hava verimi doğrulanır.",
        "tipTr": "Sintine pompalarında vakum/emiş (self-priming) testini, yangın pompalarında ise %100 ve %140 kapasitedeki basma yüksekliğini kontrol edin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "valves-piping-flexible-hoses",
    "code": "MC-04",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Valves, Piping Systems, Fittings, Flexible Hoses & Expansion Joints (Class I, II, III & Ship-Side Valves)",
    "titleTr": "Valfler (Vanalar), Boru Devreleri, Fittingler, Esnek Hortumlar (Flexible Hoses) ve Kompansatörler (Class I, II, III ve Borda Valfleri)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 10, Par. 21.4 & Tab. 36",
    "sectionId": "Pt C, Ch 1, Sec 10",
    "pdfPage": 1710,
    "keywords": ["valve", "ship side valve", "overboard valve", "pipe", "piping", "fitting", "flexible hose", "expansion joint", "bellows", "valf", "vana", "borda valfi", "kinistin", "boru", "esnek hortum", "kompansatör", "sec 10", "tab 36"],
    "calculator": {
      "type": "valve_pipe",
      "labelTr": "Valf, Boru ve Esnek Hortum Hidrostatik Test Basıncı Hesaplayıcı (Pt C, Ch 1, Sec 10 [21.4])",
      "labelEn": "Valve, Pipe & Flexible Hose Hydrostatic Calculator (Pt C, Ch 1, Sec 10 [21.4])",
      "defaultPressureBar": 16
    },
    "referenceTables": [
      {
        "titleEn": "Table 36 & [21.4] Summary : Valves, Pipes & Flexible Hoses Testing",
        "titleTr": "Tablo 36 & [21.4] Özeti : Valf, Boru ve Esnek Hortum Test Basınçları ve Sertifika Tipleri",
        "headers": ["Component / Bileşen", "Material Cert", "Product Cert", "Hydrostatic Test Pressure / Hidrostatik Test Basıncı"],
        "rows": [
          ["Valves & Fittings (Class I d ≥ 50mm or Class II d ≥ 100mm)", "C (RINA 3.2)", "C (RINA 3.2)", "Shell: 1.5 × p (Ship-side below LWL: min 0.5 MPa = 5 bar) + Seat tightness test"],
          ["Valves & Fittings (Class I d < 50mm or Class II d < 100mm)", "W (3.1)", "C (RINA 3.2)", "Shell: 1.5 × p (Ship-side below LWL: min 0.5 MPa = 5 bar) + Seat tightness test"],
          ["Carbon Steel Pressure Pipes (Class I & II)", "C or W per Tab. 36", "C (RINA 3.2)", "pH = 2.0 × p (min 0.4 MPa = 4 bar) [21.4.2 e]"],
          ["Flexible Hoses & Expansion Joints", "W (3.1 if metallic)", "C (RINA 3.2)", "pH = 1.5 × max service pressure while repeatedly deformed from axis [21.4.6]"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "item_kind",
        "questionEn": "Which piping component is being tested at the factory? (Pt C, Ch 1, Sec 10 [21.4 & Tab. 36])",
        "questionTr": "Fabrikada hangi boru devresi elemanı test ediliyor? (Pt C, Ch 1, Sec 10 [21.4 & Tab. 36])",
        "options": [
          { "value": "valve", "labelEn": "Valves & Fittings (Class I / II or Ship-Side Overboard Valves — [21.4.3])", "labelTr": "Valfler ve Fittingler (Class I / II veya Su Hattı Altı Borda/Kinistin Valfleri — [21.4.3])" },
          { "value": "pipe_spool", "labelEn": "Prefabricated Pressure Pipes / Welded Spools (Class I & II — [21.4.2])", "labelTr": "Prefabrik Basınçlı Boru Devreleri / Spool'lar (Class I & II — [21.4.2])" },
          { "value": "flex_hose", "labelEn": "Flexible Hoses & Expansion Joints / Bellows ([21.4.6])", "labelTr": "Esnek Hortumlar (Flexible Hoses) ve Kompansatörler ([21.4.6])" }
        ],
        "default": "valve"
      },
      {
        "id": "size_class",
        "questionEn": "Is the nominal diameter d ≥ 50 mm (for Class I) or d ≥ 100 mm (for Class II) or a Ship-Side Valve?",
        "questionTr": "Anma çapı Class I için d ≥ 50 mm veya Class II için d ≥ 100 mm (veya Borda Valfi) mi?",
        "options": [
          { "value": "large_c", "labelEn": "Yes — Class I (d ≥ 50 mm), Class II (d ≥ 100 mm) or Ship-Side Valve (Requires 'C' Material Cert + 'C' Product Cert)", "labelTr": "Evet — Class I (d ≥ 50 mm), Class II (d ≥ 100 mm) veya Borda Valfi (Malzeme: C, Ürün: C)" },
          { "value": "small_w", "labelEn": "No — Class I (d < 50 mm) or Class II (d < 100 mm) (Requires 'W' Material Cert + 'C' Product Cert)", "labelTr": "Hayır — Class I (d < 50 mm) veya Class II (d < 100 mm) (Malzeme: W, Ürün: C)" }
        ],
        "default": "large_c"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 3.6 & 21.3",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1711,
        "reqEn": "Material testing and NDT of welded joints (100% RT for Class I d > 75mm, 10% RT for Class II d > 100mm, MT/PT on fillet welds)",
        "reqTr": "Malzeme testleri ve kaynak dikişlerinin NDT kontrolü (Class I d > 75mm için %100 RT, Class II d > 100mm için %10 RT, köşe kaynaklarına MT/PT)"
      },
      {
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.4 & Tab. 36",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1712,
        "reqEn": "Hydrostatic testing of pipes ([21.4.2]), valves/fittings ([21.4.3]), and flexible hoses/expansion joints ([21.4.6])",
        "reqTr": "Boru ([21.4.2]), valf/fitting ([21.4.3]) ve esnek hortum/kompansatörlerin ([21.4.6]) hidrostatik testleri"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 1 Sec. 10",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1710,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify valid calibration certificates of pressure gauges on the hydrostatic test bench.",
        "titleTr": "Hidrostatik test tezgahındaki manometrelerin kalibrasyon durumunun doğrulanması.",
        "detailTr": "Test tezgahında kullanılan manometrelerin kalibrasyon sertifikalarını ve ölçüm aralıklarını kontrol edin.",
        "tipTr": "Valf sit (seat) sızdırmazlık testi ile gövde (shell) testi farklı basınçlarda yapıldığından uygun kadranda manometre kullanıldığından emin olun.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.3 & Tab. 36",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1714,
        "titleEn": "Verification of material certificates ('C' or 'W' per Tab. 36), Type Approval and visual/dimensional inspection",
        "detailEn": "Check cast/forged heat numbers on valve bodies, bonnets, discs, pipes, and flanges against material certificates (Society Certificate 'C' required for Class I d ≥ 50mm and Class II d ≥ 100mm; Works' Certificate 'W' for smaller sizes). Note: Grey cast iron is prohibited for ship-side valves and fuel/lube oil valves! Verify RINA Type Approval Certificate for flexible hoses/expansion joints.",
        "titleTr": "Malzeme sertifikalarının (Tablo 36'ya göre C veya W), döküm numaralarının ve görsel/boyutsal uygunluğun kontrolü",
        "detailTr": "Valf gövdesi, kapak ve klapesi üzerindeki döküm (heat) numaraları sertifikalarla karşılaştırılır (Class I d ≥ 50mm ve Class II d ≥ 100mm için RINA 3.2 'C' malzeme sertifikası zorunludur). Esnek hortum ve kompansatörler için geçerli RINA Tip Onay Sertifikası (TAC) kontrol edilir.",
        "tipTr": "DİKKAT: Borda/kinistin valflerinde (ship-side valves) gri pik döküm (GG20/GG25) kesinlikle yasaktır; sfero döküm (GGG40.3), bronz veya çelik döküm olmalı ve malzeme kopma uzaması (elongation) kurallara uymalıdır!",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 3.6 & Tab. 36 Notes (6),(7)",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1714,
        "titleEn": "Verification of Non-Destructive Testing (NDT) on welded construction (Part. C Ch. 1 Sec. 10 Tab. 36 Notes 4, 6, 7)",
        "detailEn": "For welded valves, pipes and fittings: verify 100% radiographic examination (RT) on butt-welded joints of Class I pipes with external diameter > 75 mm; 10% RT on butt-welded joints of Class II pipes with external diameter > 100 mm; and Magnetic Particle (MT) or Liquid Penetrant (PT) on fillet/branch welds.",
        "titleTr": "Kaynaklı imalatlarda Tahribatsız Muayene (NDT — RT / MT / PT) kontrolü (Tablo 36 Not 4, 6, 7)",
        "detailTr": "Kaynaklı boru ve valfler için: Dış çapı > 75 mm olan Class I alın kaynaklarında %100 Radyografi (RT), dış çapı > 100 mm olan Class II alın kaynaklarında %10 RT; flanş/branşman köşe kaynaklarında ise MT veya PT raporları incelenir.",
        "tipTr": "Kaynakçı sertifikalarını ve onaylı WPS/WPQR dokümanlarını NDT raporlarıyla birlikte kontrol edin.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 10 Par. 21.4.2, 21.4.3 & 21.4.6",
        "sectionId": "Pt C, Ch 1, Sec 10",
        "page": 1712,
        "titleEn": "Hydrostatic shell pressure test and valve seat tightness test (Part. C Ch. 1 Sec. 10 Par. 21.4.2, 21.4.3 & 21.4.6)",
        "detailEn": "- Valves & Fittings ([21.4.3 a]): Hydrostatic shell test at ≥ 1.5 × design pressure p (open valve, ends blanked). Followed by seat closure tightness test (typically 1.1 × p from each side per ISO 5208 / EN 12266).\n- Ship-side valves below LWL ([21.4.3 b]): Hydrostatic test pressure NOT LESS THAN 0.5 MPa (5 bar).\n- Pressure Pipes ([21.4.2 e]): Carbon steel pipes tested at 2.0 × p (minimum 0.4 MPa / 4 bar).\n- Flexible Hoses & Expansion Joints ([21.4.6]): Hydrostatic test at ≥ 1.5 × maximum service pressure while repeatedly deformed from its geometrical axis.",
        "titleTr": "Hidrostatik gövde (Shell) basınç testi ve valf sit (Seat) sızdırmazlık testi (Part. C Ch. 1 Sec. 10 Par. 21.4)",
        "detailTr": "- Valfler ve Fittingler ([21.4.3 a]): Gövde (shell) testi valf açıkken 1.5 × p basıncında; ardından klape (seat) sızdırmazlık testi valf kapalıyken 1.1 × p basıncında yapılır.\n- Su hattı altı Borda/Kinistin Valfleri ([21.4.3 b]): Gövde test basıncı EN AZ 0.5 MPa (5 bar) olmalıdır!\n- Karbon Çelik Basınçlı Borular ([21.4.2 e]): 2.0 × p (en az 0.4 MPa = 4 bar).\n- Esnek Hortum ve Kompansatörler ([21.4.6]): Geometrik ekseninden tekrarlı olarak bükülerek/esneme yaptırılarak 1.5 × maksimum servis basıncında test edilir.",
        "tipTr": "Borda (ship-side) valflerinde nominal basınç PN6 veya tasarım basıncı 2 bar olsa bile kural [21.4.3 b] gereği gövde testi minimum 5 bar'da yapılmalıdır!",
        "condition": "always"
      }
    ]
  },
  {
    "id": "reduction-gears-gearing",
    "code": "MC-05",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Reduction Gears, Reversing Gears & Clutches (Main Propulsion & Auxiliary Gearing ≥ 100 kW)",
    "titleTr": "Redüksiyon Dişlileri (Reduction Gears), Tornistan Dişlileri ve Kavramalar (Ana Tahrik ve Yardımcı Sistemler)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 6",
    "sectionId": "Pt C, Ch 1, Sec 6",
    "pdfPage": 1569,
    "keywords": ["gear", "gearing", "reduction gear", "gearbox", "clutch", "redüktör", "dişli kutusu", "şanzıman", "kavrama", "meshing test", "sec 6"],
    "applicationTerms": [
      {
        "id": "has_clutch",
        "questionEn": "Is the reduction gear fitted with hydraulic or pneumatic clutches?",
        "questionTr": "Redüktörde hidrolik veya pnömatik kavrama (clutch) bulunuyor mu?",
        "options": [
          { "value": "Yes", "labelEn": "Yes (Hydrostatic test of clutches at 1.5 × max pump pressure per [5.2.6])", "labelTr": "Evet (Kavramalar 1.5 × maks. pompa basıncında hidrostatik teste tabi tutulur — [5.2.6])" },
          { "value": "No", "labelEn": "No (Gearbox without hydraulic/pneumatic clutch)", "labelTr": "Hayır (Hidrolik/pnömatik kavrama yok)" }
        ],
        "default": "Yes"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 6 Par. 5.1 & 5.2.1 - 5.2.3",
        "sectionId": "Pt C, Ch 1, Sec 6",
        "page": 1588,
        "reqEn": "Material tests, surface hardening verification, NDT of gear teeth (MT/PT & UT) and balancing of rotating parts",
        "reqTr": "Malzeme sertifikaları, diş yüzey sertleştirme kontrolü, dişlerde NDT (MT/PT ve UT) ve döner parçaların balans testi"
      },
      {
        "ruleRef": "Part. C Ch. 1 Sec. 6 Par. 5.2.4 - 5.2.6",
        "sectionId": "Pt C, Ch 1, Sec 6",
        "page": 1588,
        "reqEn": "Tightness test, Tooth Meshing Contact test ([5.2.5]) and Hydrostatic tests of clutches & piping ([5.2.6])",
        "reqTr": "Sızdırmazlık testi, Diş Basma/Temas (Meshing) testi ([5.2.5]) ve kavrama/boru hidrostatik testleri ([5.2.6])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 1 Sec. 6 Par. 5.1 & 5.2.1",
        "sectionId": "Pt C, Ch 1, Sec 6",
        "page": 1588,
        "titleEn": "Examination of approved drawings, material certificates, heat treatment/case-hardening and NDT reports (Part. C Ch. 1 Sec. 6 Par. 5.1 & 5.2)",
        "detailEn": "Verify RINA material certificates for pinions, gear wheel rims, shafts, and couplings; review carburising/nitriding/induction hardening depth & hardness records; and verify Ultrasonic (UT) and Magnetic Particle / Liquid Penetrant (MT/PT) reports on all gear teeth.",
        "titleTr": "Onaylı resimler, malzeme sertifikaları, diş yüzey sertleştirme ve NDT (UT/MT/PT) raporlarının incelenmesi",
        "detailTr": "Pinyon, çark (wheel rim), şaft ve kaplinlerin RINA malzeme sertifikaları, sementasyon/nitrasyon sertlik derinliği raporları ve diş yüzeylerinin %100 MT/PT ile dövmelerin UT raporları kontrol edilir.",
        "tipTr": "Diş dibi ve çalışma yüzeylerinde taşlama çatlağı (grinding crack) olmadığını MT raporu ve görsel muayene ile doğrulayın.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 6 Par. 5.2.3",
        "sectionId": "Pt C, Ch 1, Sec 6",
        "page": 1588,
        "titleEn": "Verification of balancing of rotating elements (Part. C Ch. 1 Sec. 6 Par. 5.2.3)",
        "detailEn": "Rotating components (pinions, gear wheels, shafts, clutches, couplings) are to undergo static and/or dynamic balancing.",
        "titleTr": "Döner elemanların statik/dinamik balans kontrolü (Part. C Ch. 1 Sec. 6 Par. 5.2.3)",
        "detailTr": "Pinyon, dişli çark, şaft ve kavrama gruplarının statik/dinamik balans raporları doğrulanır.",
        "tipTr": "Balans kalitesinin ISO 1940 (genellikle G2.5 veya G6.3) tasarım kriterine uygunluğunu kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 6 Par. 5.2.6",
        "sectionId": "Pt C, Ch 1, Sec 6",
        "page": 1589,
        "titleEn": "Hydrostatic tests of hydraulic/pneumatic clutches, pumps, coolers and pressure piping (Part. C Ch. 1 Sec. 6 Par. 5.2.6)",
        "detailEn": "a) Hydraulic or pneumatic clutches are to be hydrostatically tested before assembly to 1.5 times the maximum working pressure of the pumps.\nb) Pressure piping, pump casings, oil coolers, valves and fittings are to be hydrostatically tested per Sec 10 [21].",
        "titleTr": "Hidrolik/pnömatik kavramalar (Clutches), yağ soğutucu ve basınçlı boruların hidrostatik testi (Part. C Ch. 1 Sec. 6 Par. 5.2.6)",
        "detailTr": "a) Hidrolik veya pnömatik kavramalar montaj öncesinde maksimum pompa çalışma basıncının 1.5 katında (1.5 × p) hidrostatik teste tabi tutulur.\nb) Yağlama/kontrol devresi boruları, pompa gövdesi ve yağ soğutucusu (cooler) Sec 10 [21]'e göre test edilir.",
        "tipTr": "Kavrama (clutch) piston ve silindirinin hidrostatik test kaydını montaj öncesi veya test tezgahında mutlaka doğrulayın.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 6 Par. 5.2.4 & 5.2.5",
        "sectionId": "Pt C, Ch 1, Sec 6",
        "page": 1588,
        "titleEn": "Shop running trial, casing tightness, noise/vibration and Tooth Meshing Contact test (Part. C Ch. 1 Sec. 6 Par. 5.2.4 & 5.2.5)",
        "detailEn": "Per [5.2.5]: Coat tooth surfaces with a thin layer of coloured compound (Prussian blue / Dykem) before the running test. Run gearbox at load sufficient to ensure tooth contact. Verify that tooth contact is adequately distributed along the length and profile of the teeth with NO strong contact marks at the ends of the teeth. Make a permanent record (Scotch tape lift / photo) for subsequent onboard alignment verification. Verify oil tightness, bearing temperatures, and alarms (Tab. 15).",
        "titleTr": "Test yatağında çalıştırma, yağ sızdırmazlığı ve Diş Basma / Temas (Tooth Meshing) testi (Part. C Ch. 1 Sec. 6 Par. 5.2.5)",
        "detailTr": "Test öncesi pinyon ve çark dişlerine ince bir tabaka kontrol boyası (Prussian blue / Dykem) sürülür. Redüktör çalıştırılarak yatak sıcaklıkları, titreşim, yağ sızdırmazlığı ve Tablo 15 alarmları kontrol edilir. Test sonunda diş temas izinin diş boyu boyunca düzgün dağıldığı ve DİŞ UÇLARINDA/KENARLARINDA SERT BASMA OLMADIĞI doğrulanır; gemideki şaft laynı (alignment) kontrolüne referans olması için kalıcı temas izi kaydı (bant izi / fotoğraf) alınır ([5.2.5 c]).",
        "tipTr": "Diş temas izinin (contact pattern) şeffaf bantla kağıda alınmış orijinal kopyasını FAT raporuna ekletin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "main-propulsion-shafting",
    "code": "MC-06",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Main Propulsion Shafting — Propeller Shafts, Intermediate Shafts, Thrust Shafts, Couplings & Stern Tubes",
    "titleTr": "Ana Tahrik Şaft Sistemi — Pervane Şaftı, Ara Şaft, İtme (Thrust) Şaftı, Kaplinler ve Stern Tube (Kovan)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 7",
    "sectionId": "Pt C, Ch 1, Sec 7",
    "pdfPage": 1590,
    "keywords": ["shaft", "propeller shaft", "tail shaft", "intermediate shaft", "thrust shaft", "stern tube", "shaft liner", "coupling", "şaft", "pervane şaftı", "ara şaft", "kovan", "kaplin", "sec 7", "tab 4"],
    "referenceTables": [
      {
        "titleEn": "Table 4 : Material and Non-Destructive Tests for Shafting Components (Pt C, Ch 1, Sec 7 [4.1])",
        "titleTr": "Tablo 4 : Şaft Sistemi Elemanları İçin Malzeme, NDT ve Sertifika Tablosu ([4.1 & 4.2])",
        "headers": ["Shafting Component / Bileşen", "Material Cert", "MT / PT (Surface NDT)", "Ultrasonic Testing (UT)", "Hydrostatic Test"],
        "rows": [
          ["1-5) Propeller, Intermediate, Thrust, Cardan Shafts & Separate Couplings", "C (RINA 3.2)", "Required if diameter ≥ 250 mm", "Required if diameter ≥ 250 mm", "—"],
          ["6, 8) Stern Tubes & Propeller Shaft Liners (machine-finished)", "W (3.1)", "—", "—", "0.2 MPa (2 bar) [4.1.2]"],
          ["Hydraulic Couplings, Clutches & CPP Hubs/Cylinders", "C / W", "Per Tab. 4", "Per Tab. 4", "1.5 × Max Working Pressure [4.1.2]"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "shaft_dia",
        "questionEn": "Is the shaft or coupling diameter ≥ 250 mm? (Pt C, Ch 1, Sec 7, Tab. 4)",
        "questionTr": "Şaft veya kaplin çapı 250 mm ve üzerinde mi? (Pt C, Ch 1, Sec 7, Tablo 4)",
        "options": [
          { "value": "over_250", "labelEn": "Yes — Diameter ≥ 250 mm (MT/PT and Ultrasonic UT mandatory per Tab. 4)", "labelTr": "Evet — Çap ≥ 250 mm (Tablo 4 gereği MT/PT ve Ultrasonik UT zorunlu)" },
          { "value": "under_250", "labelEn": "No — Diameter < 250 mm (Material test + visual/dimensional + Pt D forging NDT)", "labelTr": "Hayır — Çap < 250 mm (Malzeme testi + görsel/boyutsal + Pt D dövme kontrolleri)" }
        ],
        "default": "over_250"
      },
      {
        "id": "has_liner_sterntube",
        "questionEn": "Are Stern Tubes, Shaft Liners, or Hydraulic Couplings/CPP Cylinders included in the inspection? ([4.1.2])",
        "questionTr": "Stern Tube (Kovan), Şaft Gömleği (Liner) veya Hidrolik Kaplin/CPP Silindiri teste dahil mi? ([4.1.2])",
        "options": [
          { "value": "Yes", "labelEn": "Yes (Hydrostatic tests required per [4.1.2]: 0.2 MPa for stern tube/liner; 1.5×MWP for hydraulic parts)", "labelTr": "Evet (Kovan ve Liner için 0.2 MPa / 2 bar; Hidrolik kaplin/CPP için 1.5×p hidrostatik test zorunlu)" },
          { "value": "No", "labelEn": "No (Solid forged shaft/coupling inspection only)", "labelTr": "Hayır (Sadece dövme şaft / kaplin kontrolü)" }
        ],
        "default": "Yes"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 7 Par. 4.1 & Tab. 4",
        "sectionId": "Pt C, Ch 1, Sec 7",
        "page": 1601,
        "reqEn": "Material tests, MT/PT and Ultrasonic NDT (Tab. 4) in compliance with Part D, Ch 2, Sec 3",
        "reqTr": "Part D, Ch 2, Sec 3 ve Tablo 4 uyarınca malzeme testleri, yüzey (MT/PT) ve hacimsel (UT) NDT kontrolleri"
      },
      {
        "ruleRef": "Part. C Ch. 1 Sec. 7 Par. 4.1.2 & 4.2",
        "sectionId": "Pt C, Ch 1, Sec 7",
        "page": 1601,
        "reqEn": "Hydrostatic tests ([4.1.2]) and Society Certificate (C) / Works' Certificate (W) requirements ([4.2.1])",
        "reqTr": "Hidrostatik testler ([4.1.2]) ve RINA Sertifikası (C) / Üretici Sertifikası (W) gereksinimleri ([4.2.1])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 1 Sec. 7 Par. 4.1.1 & 4.2.1 (Tab. 4)",
        "sectionId": "Pt C, Ch 1, Sec 7",
        "page": 1601,
        "titleEn": "Verification of Society Certificates (C) for shaft forgings and chemical/mechanical properties (Part. C Ch. 1 Sec. 7 Tab. 4)",
        "detailEn": "Per [4.2.1], RINA Society Certificates (C) are mandatory for material tests of: (1) Separate couplings, (2) Propeller shafts, (3) Intermediate shafts, (4) Thrust shafts, and (5) Cardan shafts. Verify heat numbers, forging reduction ratio, heat treatment, tensile strength Rm, yield stress ReH, elongation, and Charpy V-notch impact results per Pt D, Ch 2, Sec 3.",
        "titleTr": "Şaft dövmelerinin RINA Malzeme Sertifikaları (C) ve mekanik/kimyasal testlerinin doğrulanması (Tablo 4)",
        "detailTr": "[4.2.1] uyarınca; (1) Kaplinler, (2) Pervane şaftları, (3) Ara şaftlar, (4) Thrust (itme) şaftları ve (5) Kardan şaftlarının malzeme testleri için RINA Sertifikası (C - 3.2) zorunludur. Şaft alnındaki döküm (heat) numarası, RINA damgası ve mekanik test değerleri (Pt D, Ch 2, Sec 3) kontrol edilir.",
        "tipTr": "Paslanmaz veya alaşımlı çelik ara şaftlarda korozyonlu yorulma dayanımı için Pt D, Ch 2, Sec 3 [3.8] ek onay şartlarını kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 7 Par. 4.1.1 (Tab. 4)",
        "sectionId": "Pt C, Ch 1, Sec 7",
        "page": 1601,
        "titleEn": "Non-destructive testing — Ultrasonic (UT) and Magnetic Particle / Liquid Penetrant (MT/PT) (Part. C Ch. 1 Sec. 7 Tab. 4)",
        "detailEn": "Verify UT and MT/PT examination (mandatory per Tab. 4 if diameter ≥ 250 mm, and per Pt D Ch 2 Sec 3 for forgings), particularly on propeller shaft cone/taper, keyway fillets, coupling flange fillets, and shrink-fit zones.",
        "titleTr": "Tahribatsız muayene — Ultrasonik (UT) ve Manyetik Parçacık / Penetran (MT/PT) kontrolü (Tablo 4)",
        "detailTr": "Özellikle pervane şaft koniği (taper), kama kanalı radyüsleri (keyway spoon/fillet), kaplin flanş boyunları ve sıkı geçme yüzeylerinde MT/PT ve UT kontrolleri doğrulanır (Tablo 4 gereği çap ≥ 250 mm ise zorunludur).",
        "tipTr": "Pervane koniği kama kanalı (keyway) ön ucundaki kaşık radyüslerinde (spoon end) çatlak bulunmadığını MT/PT ile bizzat inceleyin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 7 Par. 4.1",
        "sectionId": "Pt C, Ch 1, Sec 7",
        "page": 1601,
        "titleEn": "Dimensional inspection, runout check and cone contact (Prussian blue) check with propeller/coupling",
        "detailEn": "Check finished diameters, bearing journals, flange dimensions, concentricity/runout on lathe, surface roughness, and blue-contact bedding check (>70-80% contact area) between shaft taper and propeller hub / coupling.",
        "titleTr": "Boyutsal muayene, salgısızlık (Runout) ve konik alıştırma (Prussian Blue) kontrolü",
        "detailTr": "Torna üzerinde şaft yatak muyluları, flanş ölçüleri, yüzey pürüzlülüğü ve salgısızlık (runout) ölçülür; pervane göbeği veya kaplin koniği ile şaft koniği arasındaki boya alıştırma teması (Prussian blue bedding) kontrol edilir.",
        "tipTr": "Bronz şaft gömleği (shaft liner) sıcak geçirilmişse, gömleğin şafta tam oturduğu çekiç/ses testi (ringing test) ile kontrol edilmeli ve uç sızdırmazlığı doğrulanmalıdır.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 7 Par. 4.1.2",
        "sectionId": "Pt C, Ch 1, Sec 7",
        "page": 1601,
        "titleEn": "Hydrostatic tests of stern tubes, propeller shaft liners (0.2 MPa) and hydraulic couplings / CPP cylinders (1.5 × MWP) (Part. C Ch. 1 Sec. 7 Par. 4.1.2)",
        "detailEn": "- Sterntubes (when machine-finished) and propeller shaft liners (when machine-finished on inside and with overthickness ≤ 3 mm on outside) are to be hydrostatically tested to 0.2 MPa (2 bar) before shrink-fitting.\n- Hydraulic couplings, clutches, and CPP hubs/cylinders are to be hydrostatically tested to 1.5 × maximum working pressure.",
        "titleTr": "Stern tube, şaft gömleği (0.2 MPa = 2 bar) ve hidrolik kaplin/CPP silindiri (1.5 × p) hidrostatik testleri (Part. C Ch. 1 Sec. 7 Par. 4.1.2)",
        "detailTr": "- İşlenmiş stern tube (kovan) ve şafta çakılmadan önce içten işlenmiş (dış payı ≤ 3 mm) bronz şaft gömlekleri (liner) 0.2 MPa (2 bar) basınçta hidrostatik teste tabi tutulur.\n- Hidrolik kaplinler (SKF/OK kaplin vb.) ve CPP göbek/silindirleri maksimum çalışma basıncının 1.5 katında test edilir.",
        "tipTr": "Şaft gömleği (liner) hidrostatik testi şafta sıcak geçirilmeden ÖNCE yapılmalı ve hiçbir terleme/gözenek görülmemelidir.",
        "condition": { "field": "has_liner_sterntube", "equals": "Yes" }
      }
    ]
  },
  {
    "id": "propellers-fpp-cpp",
    "code": "MC-07",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Marine Propellers — Solid Fixed Pitch Propellers (FPP) & Controllable Pitch Propellers (CPP)",
    "titleTr": "Gemi Pervaneleri — Sabit Hatveli Yekpare Pervaneler (FPP) ve Değişken Hatveli Pervaneler (CPP)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 8 & Part. D - Ch. 4 - Sec. 2",
    "sectionId": "Pt C, Ch 1, Sec 8",
    "pdfPage": 1602,
    "keywords": ["propeller", "fpp", "cpp", "controllable pitch propeller", "fixed pitch propeller", "blade", "cu1", "cu2", "cu3", "cu4", "pervane", "kanat", "pitch", "hatve", "sec 8", "pt d ch 4 sec 2"],
    "applicationTerms": [
      {
        "id": "prop_type",
        "questionEn": "Is the propeller a Solid Fixed Pitch Propeller (FPP) or a Controllable Pitch / Built-up Propeller (CPP)? ([4.1 & 4.2])",
        "questionTr": "Pervane yekpare Sabit Hatveli (FPP) mi yoksa Değişken Hatveli / Parçalı (CPP) mı? ([4.1 & 4.2])",
        "options": [
          { "value": "cpp", "labelEn": "Controllable Pitch Propeller (CPP) / Built-up Propeller ([4.1.2 & 4.2.2])", "labelTr": "Değişken Hatveli Pervane (CPP) / Parçalı Pervane ([4.1.2 & 4.2.2])" },
          { "value": "fpp", "labelEn": "Solid Fixed Pitch Propeller (FPP — [4.1.1 & 4.2.1])", "labelTr": "Yekpare Sabit Hatveli Pervane (FPP — [4.1.1 & 4.2.1])" }
        ],
        "default": "cpp"
      },
      {
        "id": "prop_rpm",
        "questionEn": "Does the propeller operate at a speed above 500 rpm? ([4.2.3])",
        "questionTr": "Pervane çalışma devri 500 rpm'in üzerinde mi? ([4.2.3])",
        "options": [
          { "value": "over_500", "labelEn": "Yes — > 500 rpm (Dynamic balancing mandatory for copper alloy, may be required for steel)", "labelTr": "Evet — > 500 rpm (Bakır alaşımlı pervanelerde Dinamik Balans zorunlu — [4.2.3])" },
          { "value": "under_500", "labelEn": "No — ≤ 500 rpm (Static balancing or individual blade weight/CoG check)", "labelTr": "Hayır — ≤ 500 rpm (Statik balans veya CPP kanat ağırlık/ağırlık merkezi kontrolü)" }
        ],
        "default": "under_500"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 8 Par. 4.1 & Pt. D Ch. 4 Sec. 2 Par. 1",
        "sectionId": "Pt D, Ch 4, Sec 2",
        "page": 2526,
        "reqEn": "Material chemical analysis, mechanical tests (CU1/CU2/CU3/CU4 or Cast Steel), metallographic structure check and Severity Zone A/B/C NDT",
        "reqTr": "Malzeme kimyasal analizi, mekanik testler (CU1/CU2/CU3/CU4 bronz veya çelik döküm), metalografik yapı kontrolü ve Bölge A/B/C NDT muayenesi"
      },
      {
        "ruleRef": "Part. C Ch. 1 Sec. 8 Par. 4.2 & 4.3",
        "sectionId": "Pt C, Ch 1, Sec 8",
        "page": 1610,
        "reqEn": "Dimensional/profile check, liquid penetrant (PT) inspection, balancing ([4.2.3]), and CPP hydraulic system test at 1.5 × design pressure ([4.2.2])",
        "reqTr": "Kanat profil/hatve ölçümü, penetran (PT) testi, balans ([4.2.3]) ve CPP hidrolik sistem 1.5 × tasarım basıncı testi ([4.2.2])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 1 Sec. 8 Par. 4.1 & Pt. D Ch. 4 Sec. 2 Par. 1.7-1.8",
        "sectionId": "Pt D, Ch 4, Sec 2",
        "page": 2527,
        "titleEn": "Material testing of propeller casting (CU1–CU4 / Cast Steel) and torque-transmitting parts (Part. C Ch. 1 Sec. 8 Par. 4.1)",
        "detailEn": "Verify chemical composition, tensile test (Rm, Rp0.2, A5%), Charpy impact test (where applicable), and metallographic alpha/beta phase structure proportion (for CU1/CU2/CU3 copper alloys per Pt D, Ch 4, Sec 2 [1.7]) on keel-block specimens in Surveyor's presence. For CPP/built-up propellers ([4.1.2]), also verify RINA material certificates for blade bolts/studs, hub body, crank pin rings, and yoke.",
        "titleTr": "Pervane dökümü (CU1–CU4 Bronz / Çelik) ve tork ileten parçaların malzeme/mikroyapı testleri (Part. C Ch. 1 Sec. 8 Par. 4.1)",
        "detailTr": "Döküm numunelerinde kimyasal analiz, çekme testi ve bakır alaşımlarında (CU1/CU2/CU3) metalografik alfa fazı oranı kontrolü (Pt D, Ch 4, Sec 2 [1.7]) sörveyör huzurunda yapılır. CPP pervanelerde ([4.1.2]) kanat saplamaları (studs), göbek (hub) ve tork ileten mekanizma parçalarının RINA malzeme sertifikaları doğrulanır.",
        "tipTr": "CU3 (Nikel-Alüminyum Bronz) ve CU4 (Mangan-Alüminyum Bronz) pervanelerde mikro yapı ve mekanik değerler sörveyör huzurunda çekilmelidir.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 8 Par. 4.2.1 & Pt. D Ch. 4 Sec. 2 Par. 1.9-1.11",
        "sectionId": "Pt C, Ch 1, Sec 8",
        "page": 1610,
        "titleEn": "Visual examination, conformity to approved blade profile/pitch/thickness plans and Liquid Penetrant (PT) NDT of Severity Zones A, B, C",
        "detailEn": "Carry out visual examination of the entire blade & hub surfaces; verify blade thickness, width, pitch at 0.2R–0.9R radii, diameter, rake, and track against approved ISO 484 Class (S, I, II, III) tolerances; and inspect 100% of Severity Zone A (and critical Zones B/C) by Liquid Penetrant (PT) per Pt D, Ch 4, Sec 2 [1.10]-[1.11]. Any weld repair requires prior RINA approval.",
        "titleTr": "Görsel muayene, kanat profil/kalınlık/hatve (Pitch) ölçümü ve Bölge A, B, C Penetran (PT) NDT kontrolü (Part. C Ch. 1 Sec. 8 Par. 4.2.1)",
        "detailTr": "Kanatların emme ve basınç yüzeyleri görsel olarak incelenir; 0.2R – 0.9R yarıçap kesitlerinde kanat kalınlığı, genişlik ve hatve (pitch) değerlerinin onaylı resme ve ISO 484 tolerans sınıfına uygunluğu ölçülür. Kritik Gerilme Bölgesi A (Zone A - kanat kökü/fillet) %100 Penetran (PT) testine tabi tutulur. (Zone A'da kaynak tamiri prensip olarak yasaktır / özel onaya tabidir!).",
        "tipTr": "DİKKAT: Pervane kanat kökü (Zone A) bölgesinde sörveyör onayı olmadan hiçbir kaynak tamiri yapılamaz (Pt D, Ch 4, Sec 2 [1.12])!",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 8 Par. 4.2.3",
        "sectionId": "Pt C, Ch 1, Sec 8",
        "page": 1611,
        "titleEn": "Static balancing (or individual CPP blade weight & CoG check) and dynamic balancing if > 500 rpm (Part. C Ch. 1 Sec. 8 Par. 4.2.3)",
        "detailEn": "Finished propellers are to be statically balanced. For built-up and controllable pitch propellers, static balancing of the complete propeller may be replaced by an individual check of blade weight and centre of gravity (CoG) position. For propellers running above 500 rpm, dynamic balancing is required for cast copper alloy propellers.",
        "titleTr": "Statik balans (veya CPP kanat ağırlık/ağırlık merkezi kontrolü) ve > 500 rpm ise dinamik balans testi (Part. C Ch. 1 Sec. 8 Par. 4.2.3)",
        "detailTr": "Bitmiş pervaneye statik balans testi uygulanır. CPP pervanelerde komple statik balans yerine her bir kanadın ağırlığı ve ağırlık merkezi (CoG) tolerans kontrolü yapılabilir. Devir > 500 rpm ise bakır alaşımlı pervanelerde dinamik balans zorunludur.",
        "tipTr": "CPP kanatlarının birbirleriyle yer değiştirilebilir (interchangeable) olması için her kanadın ağırlık ve CoG değerlerini raporda doğrulayın.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 8 Par. 4.2.2",
        "sectionId": "Pt C, Ch 1, Sec 8",
        "page": 1610,
        "titleEn": "Controllable Pitch Propeller (CPP) hydraulic system hydrostatic test (1.5 × design pressure), safety valve & pitch stroke test (Part. C Ch. 1 Sec. 8 Par. 4.2.2)",
        "detailEn": "Per [4.2.2]: The complete hydraulic system for the control of the controllable pitch propeller mechanism is to be hydrotested at a pressure equal to 1.5 times the design pressure. The proper operation of the safety valve and full ahead-to-astern blade pitch actuation & feedback are to be tested in the presence of the Surveyor.",
        "titleTr": "CPP hidrolik sisteminin hidrostatik testi (1.5 × tasarım basıncı), emniyet valfi ve hatve (Pitch) değiştirme fonksiyon testi (Part. C Ch. 1 Sec. 8 Par. 4.2.2)",
        "detailTr": "CPP mekanizmasının komple hidrolik kontrol sistemi (hub, servo silindir, OD box, HPU ve borular) tasarım basıncının 1.5 katında (1.5 × p) hidrostatik teste tabi tutulur. Emniyet valfinin açma basıncı ve kanatların tam ileri (Full Ahead) ile tam tornistan (Full Astern) arasındaki hatve hareketi sörveyör huzurunda test edilir.",
        "tipTr": "CPP göbeği (hub) sızdırmazlık testini ve acil durumda mekanik/yedek pitch kilitleme mekanizmasını da kontrol edin.",
        "condition": { "field": "prop_type", "equals": "cpp" }
      }
    ]
  },
  {
    "id": "steering-gear-thrusters-windlass",
    "code": "MC-08",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Steering Gear, Azimuth / Tunnel Thrusters & Anchor Windlasses",
    "titleTr": "Dümen Donanımı (Steering Gear), Baş/Kıç İticiler (Azimuth / Tunnel Thrusters) ve Demir Irgatları (Anchor Windlass)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 11, Sec. 12 & Sec. 15",
    "sectionId": "Pt C, Ch 1, Sec 11",
    "pdfPage": 1734,
    "keywords": ["steering gear", "rudder", "actuator", "thruster", "bow thruster", "azimuth thruster", "windlass", "anchor windlass", "dümen", "dümen donanımı", "thruster", "baş itici", "ırgat", "demir ırgatı", "sec 11", "sec 12", "sec 15"],
    "applicationTerms": [
      {
        "id": "deck_mach_type",
        "questionEn": "Which machinery is being tested at the manufacturer's works?",
        "questionTr": "Üretici fabrikasında hangi ekipman test ediliyor?",
        "options": [
          { "value": "steering", "labelEn": "Steering Gear (Hydraulic cylinders/actuators, pumps, tiller & valves — Sec 11 [8])", "labelTr": "Dümen Donanımı (Hidrolik silindirler, роtary vane, pompalar, yeke — Sec 11 [8])" },
          { "value": "windlass", "labelEn": "Anchor Windlass (No-load 30 min, load & brake test — Sec 15 [4])", "labelTr": "Demir Irgatı / Anchor Windlass (30 dk boşta, yük ve fren testi — Sec 15 [4])" },
          { "value": "thruster", "labelEn": "Thruster (Transverse Tunnel or Azimuth Thruster — Sec 12 [3])", "labelTr": "Baş/Kıç İtici veya Azimut Thruster (Sec 12 [3])" }
        ],
        "default": "steering"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 11 Par. 8 / Sec. 12 Par. 3 / Sec. 15 Par. 4",
        "sectionId": "Pt C, Ch 1, Sec 11",
        "page": 1734,
        "reqEn": "Material & NDT tests of torque/load-bearing parts, hydrostatic tests (1.5 × design pressure), and workshop running/load trials",
        "reqTr": "Yük taşıyan parçaların malzeme ve NDT testleri, hidrostatik basınç testleri (1.5 × p) ve atölye çalışma/yük testleri"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 1 Sec. 11 Par. 8.2 / Sec. 12 Par. 3.1 / Sec. 15 Par. 4.1",
        "sectionId": "Pt C, Ch 1, Sec 11",
        "page": 1734,
        "titleEn": "Examination of approved drawings, material certificates ('C' / 'W') and NDT reports (UT & MT/PT)",
        "detailEn": "Verify RINA material certificates and UT/MT/PT reports for rudder actuators, cylinders, rams, tiller, thruster shafts, bevel gears, propeller blades, or windlass main shaft, cable lifter (gypsy), and brake parts.",
        "titleTr": "Onaylı resimler, malzeme sertifikaları (C / W) ve NDT (UT / MT / PT) raporlarının kontrolü",
        "detailTr": "Dümen silindirleri, piston kolları (ram), yeke (tiller), thruster şaft/konik dişlileri veya ırgat ana şaftı ve kavelata (cable lifter) parçalarının malzeme sertifikaları ve UT/MT/PT raporları incelenir.",
        "tipTr": "Dümen yekesi (tiller) ve piston kollarında %100 UT ve MT/PT kontrollerinin tamamlandığını doğrulayın.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 11 Par. 8.1 & 8.4 / Sec. 10 Par. 21.4",
        "sectionId": "Pt C, Ch 1, Sec 11",
        "page": 1734,
        "titleEn": "Hydrostatic pressure tests (1.5 × design pressure) of hydraulic cylinders, actuators, pump casings, valves and piping",
        "detailEn": "Carry out hydrostatic testing at 1.5 × design pressure on steering gear hydraulic cylinders/actuators, valve blocks, piping, hydraulic power units, or thruster gear housing/CPP hub. Verify relief valve settings and hydraulic pump type test records ([8.1]).",
        "titleTr": "Hidrolik silindirler, aktüatörler, valf blokları ve boruların hidrostatik testi (1.5 × tasarım basıncı)",
        "detailTr": "Dümen silindirleri/aktüatörleri, hidrolik güç ünitesi (HPU) blokları ve boruları veya thruster gövde/CPP silindiri tasarım basıncının 1.5 katında hidrostatik teste tabi tutulur; emniyet valfi açma basınçları doğrulanır.",
        "tipTr": "Dümen hidrolik pompalarının RINA Tip Testi ([8.1]) kapsamındaki dayanım raporunu kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 11 Par. 8.4 / Sec. 12 Par. 3.2",
        "sectionId": "Pt C, Ch 1, Sec 11",
        "page": 1734,
        "titleEn": "Workshop functional test, gear tooth meshing contact check and alarm simulation",
        "detailEn": "For Steering Gear & Thrusters: verify full stroke travel (35° port to 35° starboard), hydraulic oil tightness, low oil level / phase failure / overload / hydraulic lock alarms, and for thrusters verify bevel gear tooth meshing contact pattern (per Sec 6) and blade pitch actuation.",
        "titleTr": "Atölye fonksiyon testi, konik dişli basma izi (Thruster) ve alarm simülasyonu",
        "detailTr": "Dümen donanımında sancak-iskele tam kurs (35°-0°-35°) hareketi, HPU yedeklilik geçişi ve alarmlar; Thruster'larda ise konik dişli (bevel gear) basma/temas izi (Prussian blue), sızdırmazlık ve kanat hatve kontrolü test edilir.",
        "tipTr": "Dümen sisteminde tek bir hidrolik devre izole edildiğinde diğer devrenin sistemi sürmeye devam ettiğini doğrulayın.",
        "condition": { "field": "deck_mach_type", "notEquals": "windlass" }
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 1 Sec. 15 Par. 4.2 & 5.1",
        "sectionId": "Pt C, Ch 1, Sec 15",
        "page": 1753,
        "titleEn": "Anchor Windlass workshop tests — 30-min no-load run, continuous duty pull, overload capacity, brake holding test & permanent marking (Part. C Ch. 1 Sec. 15 Par. 4.2 & 5.1)",
        "detailEn": "Per Sec 15 [4.2]:\n- [4.2.1] No-load test: Run windlass without load at nominal speed in each direction for a total of 30 minutes (plus 5 min in each direction for each gear change).\n- [4.2.2] Load test: Verify continuous duty pull (for 30 min at nominal speed ≥ 0.15 m/s), temporary overload pull (1.5 × continuous duty pull for 2 min), and overload protection.\n- [4.2.3] Brake capacity test: Verify holding power of cable lifter brake (45% of chain breaking load with single reeving / 80% without chain stopper).\n- [5.1.1] Permanent marking: Verify marking of nominal size (e.g. 100/3/45 = chain dia / grade / holding %) and maximum anchorage depth in metres.",
        "titleTr": "Demir Irgatı (Windlass) fabrika testleri — 30 dk boşta çalışma, çekme yük testi, fren tutma testi ve kalıcı markalama (Part. C Ch. 1 Sec. 15 Par. 4.2 & 5.1)",
        "detailTr": "- [4.2.1] Boşta çalışma testi: Her iki yönde toplam 30 dakika nominal hızda çalıştırılır (vitesli ise her viteste her yöne +5 dk).\n- [4.2.2] Yük testi: Sürekli çekme kapasitesi (≥ 0.15 m/sn hızda 30 dk) ve aşırı yük kapasitesi (1.5 × sürekli çekme yükünde 2 dk) doğrulanır.\n- [4.2.3] Fren kapasite testi: Kavelata şerit freninin tutma kapasitesi (zincir kopma yükünün %45'i veya kastanyolasız %80'i) test veya hesapla doğrulanır.\n- [5.1.1] Kalıcı Markalama: Irgat üzerinde nominal ölçü (örn. 100/3/45) ve maksimum demirleme derinliği (m) markalaması kontrol edilir.",
        "tipTr": "Hidrolik veya elektrikli kavramanın (clutch) acil durumda el ile (manuel) ayrılabilir olduğunu ([3.6.1]) sahada mutlaka deneyin!",
        "condition": { "field": "deck_mach_type", "equals": "windlass" }
      }
    ]
  },
  {
    "id": "turbochargers-cat-b-c",
    "code": "MC-09",
    "category": "machinery",
    "categoryTitleEn": "Part C, Ch 1 — Machinery & Piping Systems",
    "categoryTitleTr": "Part C, Ch 1 — Makine, Şaft, Kazan ve Boru Sistemleri",
    "titleEn": "Exhaust Gas Turbochargers (Category B & Category C)",
    "titleTr": "Egzoz Gazı Turboşarjları (Turbochargers — Kategori B ve Kategori C)",
    "ruleRef": "Part. C - Ch. 1 - Sec. 14",
    "sectionId": "Pt C, Ch 1, Sec 14",
    "pdfPage": 1744,
    "keywords": ["turbocharger", "turbo", "compressor wheel", "turbine rotor", "turboşarj", "türbin", "sec 14"],
    "applicationTerms": [
      {
        "id": "tc_category",
        "questionEn": "What is the category of the turbocharger based on connected engine power? (Pt C, Ch 1, Sec 14 [1.1.3])",
        "questionTr": "Bağlı olduğu motor gücüne göre turboşarjın kategorisi nedir? (Pt C, Ch 1, Sec 14 [1.1.3])",
        "options": [
          { "value": "cat_c", "labelEn": "Category C (Connected engine power > 2500 kW per turbocharger — RINA Society Certificate)", "labelTr": "Kategori C (Turboşarj başına motor gücü > 2500 kW — RINA Sertifikası zorunlu)" },
          { "value": "cat_b", "labelEn": "Category B (1000 kW ≤ power ≤ 2500 kW per turbocharger — Works' Certificate + TAC)", "labelTr": "Kategori B (1000 kW ≤ güç ≤ 2500 kW — Üretici Sertifikası + Tip Onayı)" }
        ],
        "default": "cat_c"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 1 Sec. 14 Par. 3.1 & 3.2",
        "sectionId": "Pt C, Ch 1, Sec 14",
        "page": 1747,
        "reqEn": "Type testing (containment, 500 load cycles, 1h hot running) and Workshop inspections & testing ([3.2.2])",
        "reqTr": "Tip testleri (parça tutma/containment, 500 çevrim, 1 saat sıcak çalışma) ve atölye kontrolleri ([3.2.2])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 1 Sec. 14 Par. 3.2.2",
        "sectionId": "Pt C, Ch 1, Sec 14",
        "page": 1747,
        "titleEn": "Verification of chemical composition, mechanical properties, UT and crack detection (MT/PT) of rotating parts and casing (Part. C Ch. 1 Sec. 14 Par. 3.2.2)",
        "detailEn": "Verify material certificates (chemical & mechanical properties) of compressor wheel, turbine disc/blades, shaft, and casing; verify Ultrasonic Testing (UT) and surface crack detection (PT/MT) of rotating parts; and verify dimensional inspection.",
        "titleTr": "Döner parçaların ve gövdenin kimyasal/mekanik özellikleri ile UT ve çatlak (MT/PT) kontrolleri (Part. C Ch. 1 Sec. 14 Par. 3.2.2)",
        "detailTr": "Kompresör çarkı, türbin diski/kanatları, şaft ve gövdenin malzeme test sonuçları ile döner parçaların Ultrasonik (UT), Penetran/Manyetik (PT/MT) çatlak kontrolleri ve boyutsal muayenesi doğrulanır.",
        "tipTr": "Kategori C turboşarjlarda döner parçalar ilgili sertifika ile kolayca eşleştirilecek şekilde markalanmalıdır ([3.4.3]).",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 1 Sec. 14 Par. 3.2.2",
        "sectionId": "Pt C, Ch 1, Sec 14",
        "page": 1748,
        "titleEn": "Rotor balancing and hydraulic test of cooling spaces (max(4 bar, 1.5 × MWP)) (Part. C Ch. 1 Sec. 14 Par. 3.2.2)",
        "detailEn": "Verify dynamic rotor balancing and witness hydraulic testing of cooling spaces to 4 bars (0.4 MPa) or 1.5 times maximum working pressure, whichever is higher.",
        "titleTr": "Rotor dinamik balans testi ve soğutma bölmelerinin hidrolik testi (en az 4 bar veya 1.5 × MWP) (Part. C Ch. 1 Sec. 14 Par. 3.2.2)",
        "detailTr": "Rotor grubunun dinamik balans testi ve soğutma su bölmelerinin 4 bar (0.4 MPa) veya 1.5 × maksimum çalışma basıncından (hangisi büyükse) yapılan hidrostatik testi doğrulanır.",
        "tipTr": "Hava/gaz soğutmalı gövdelerde varsa yağlama/soğutma ceketlerinin sızdırmazlığını kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 1 Sec. 14 Par. 3.2.2",
        "sectionId": "Pt C, Ch 1, Sec 14",
        "page": 1748,
        "titleEn": "Overspeed test of compressor wheel (3 min at +20% alarm speed at room temp or +10% at 45°C) (Part. C Ch. 1 Sec. 14 Par. 3.2.2)",
        "detailEn": "Verify overspeed test of compressor wheels for a duration of 3 minutes at either 20% above alarm level speed at room temperature or 10% above alarm level speed at 45°C inlet temperature. (May be waived for forged wheels that are individually controlled by an approved non-destructive method).",
        "titleTr": "Kompresör çarkı aşırı devir (Overspeed) testi (3 dakika: oda sıcaklığında +%20 veya 45°C'de +%10 alarm devri) (Part. C Ch. 1 Sec. 14 Par. 3.2.2)",
        "detailTr": "Kompresör çarklarının 3 dakika süreyle oda sıcaklığında alarm devrinin %20 üzerinde (veya 45°C emiş sıcaklığında %10 üzerinde) aşırı devir testine tabi tutulduğu doğrulanır. (Onaylı NDT yöntemiyle tek tek kontrol edilen dövme çarklarda muaf tutulabilir).",
        "tipTr": "Dövme çarklarda aşırı devir testi muafiyeti uygulanıyorsa her çarka ait bireysel UT/PT NDT raporunu mutlaka görün.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "fire-protection-extinguishing-systems",
    "code": "FP-01",
    "category": "fire",
    "categoryTitleEn": "Part C, Ch 4 — Fire Protection, Detection & Extinction",
    "categoryTitleTr": "Part C, Ch 4 — Yangın Koruma, Algılama ve Söndürme Sistemleri",
    "titleEn": "Fixed Fire Extinguishing Systems (High-Pressure CO2 / Clean Agent Cylinders & Manifolds), Fire Dampers & Detection Panels",
    "titleTr": "Sabit Yangın Söndürme Sistemleri (CO2 / Gaz Tüpleri ve Kollektörleri), Yangın Damperleri ve Yangın Algılama Panelleri",
    "ruleRef": "Part. C - Ch. 4 - Sec. 1 & FSS Code",
    "sectionId": "Pt C, Ch 4, Sec 1",
    "pdfPage": 2248,
    "keywords": ["fire", "co2", "co2 cylinder", "manifold", "fire damper", "fire detection", "foam", "water mist", "yangın", "co2 tüpü", "kollektör", "yangın damperi", "yangın algılama", "sec 1", "ch 4"],
    "applicationTerms": [
      {
        "id": "fire_equip_type",
        "questionEn": "Which fire protection or extinction equipment is being inspected?",
        "questionTr": "Hangi yangın koruma veya söndürme ekipmanı test ediliyor?",
        "options": [
          { "value": "co2_gas", "labelEn": "Fixed CO2 / Gas Extinguishing Cylinders, Valves, Manifolds & Flexible Hoses", "labelTr": "Sabit CO2 / Gazlı Söndürme Tüpleri, Vanaları, Kollektör (Manifold) ve Hortumları" },
          { "value": "damper_panel", "labelEn": "Fire Dampers (A-0 / A-60) or Fire Detection & Alarm Control Panel", "labelTr": "Yangın Damperleri (A-0 / A-60) veya Yangın Algılama ve Alarm Paneli" }
        ],
        "default": "co2_gas"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 4 Sec. 1 Par. 4.1 & FSS Code",
        "sectionId": "Pt C, Ch 4, Sec 1",
        "page": 2255,
        "reqEn": "Type approval (RINA TAC / MED), material certification, hydrostatic testing of high-pressure cylinders/manifolds, and functional testing",
        "reqTr": "Tip onayı (RINA TAC / MED), malzeme sertifikasyonu, yüksek basınçlı tüp/kollektörlerin hidrostatik testi ve fonksiyon testleri"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 4 Sec. 1 Par. 4.1",
        "sectionId": "Pt C, Ch 4, Sec 1",
        "page": 2255,
        "titleEn": "Examination of approved drawings, RINA Type Approval / MED Certificates and material certificates",
        "detailEn": "Verify valid RINA Type Approval Certificates (or MED Module B+D/F where applicable), approved system drawings, and material certificates for seamless CO2 cylinders, manifold pipes, non-return valves, and pilot cabinets.",
        "titleTr": "Onaylı resimler, RINA Tip Onay / MED sertifikaları ve malzeme sertifikalarının incelenmesi",
        "detailTr": "Geçerli RINA Tip Onay Sertifikası (veya MED sertifikası), onaylı sistem hesapları/resimleri ile dikişsiz CO2 tüpleri, kollektör (manifold) boruları ve çekvalflerin malzeme sertifikaları kontrol edilir.",
        "tipTr": "CO2 tüplerinde dolum oranı (filling ratio ≤ 0.67 kg/L) ve tüp darası/brüt ağırlık damgalarını kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 4 Sec. 1 & Ch. 1 Sec. 3 / Sec. 10",
        "sectionId": "Pt C, Ch 4, Sec 1",
        "page": 2255,
        "titleEn": "Hydrostatic pressure test of CO2 cylinders, manifolds, valves and flexible discharge hoses",
        "detailEn": "Witness hydrostatic pressure testing of seamless CO2 cylinders (typically 25 MPa / 250 bar), high-pressure distribution manifolds (≥ 1.5 × max working pressure, typically ≥ 19 MPa / 190 bar), cylinder valves, and flexible hoses.",
        "titleTr": "CO2 tüpleri, kollektörler (Manifold), vanalar ve esnek hortumların hidrostatik basınç testi",
        "detailTr": "Dikişsiz CO2 tüpleri (genellikle 250 bar), yüksek basınç kollektörleri (manifold — 1.5 × MWP, en az 190 bar), tüp vanaları ve esnek deşarj hortumları hidrostatik basınç testine tabi tutulur.",
        "tipTr": "Kollektör (manifold) üzerindeki emniyet patlama diski veya relief valfinin (180-190 bar) sertifikasını ve bağlantısını doğrulayın.",
        "condition": { "field": "fire_equip_type", "equals": "co2_gas" }
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 4 Sec. 1 & Ch. 3 Sec. 8",
        "sectionId": "Pt C, Ch 4, Sec 1",
        "page": 2255,
        "titleEn": "Functional test of release mechanism, time delay, alarms, fire dampers or detection panel",
        "detailEn": "Verify pneumatic/mechanical pilot release cabinet operation, 20s/30s pre-discharge time delay unit, pressure switches for release alarm & ventilation fan shutdown interlock; or for Fire Dampers / Fire Detection Panels: verify fail-safe spring closure, fusible link / thermal trip, position indicators (Open/Closed), dual power supply changeover, and zone fault/fire alarm functions.",
        "titleTr": "Boşaltma kabini, gecikme ünitesi, damper fail-safe kapanma ve alarm fonksiyon testleri",
        "detailTr": "Pilot boşaltma kabini kapak açma alarmı, 20-30 sn zaman gecikme (time delay) ünitesi ve fan durdurma basınç şalteri; Yangın Damperlerinde ise enerji/hava kesildiğinde yaylı fail-safe kapanma, sigorta (fusible link) ve Açık/Kapalı limit switch göstergeleri test edilir.",
        "tipTr": "Yangın damperlerinde FTP Code (A-0 / A-60) sertifikasındaki sac kalınlığı ve çerçeve detaylarının üretilen damperle aynı olduğunu kontrol edin.",
        "condition": "always"
      }
    ]
  }
]

with open("public/data/part2.json", "w", encoding="utf-8") as f:
    json.dump(part2_items, f, ensure_ascii=False, indent=2)

print("Part 2 items written:", len(part2_items))
