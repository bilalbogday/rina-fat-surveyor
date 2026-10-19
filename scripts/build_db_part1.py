import json, os

os.makedirs("public/data", exist_ok=True)

part1_items = [
  {
    "id": "transformers-essential",
    "code": "EL-01",
    "category": "electrical",
    "categoryTitleEn": "Part C, Ch 2 — Electrical Installations",
    "categoryTitleTr": "Part C, Ch 2 — Elektrik Sistemleri",
    "titleEn": "Transformers for essential services of 100 kVA and over (60 kVA for single phase transformers)",
    "titleTr": "Esas (Essential) Servisler İçin Güç ve Dağıtım Trafoları (Üç Faz ≥ 100 kVA / Tek Faz ≥ 60 kVA)",
    "ruleRef": "Part. C - Ch. 2 - Sec. 5",
    "sectionId": "Pt C, Ch 2, Sec 5",
    "pdfPage": 2071,
    "keywords": ["transformer", "trafo", "transformator", "transformatör", "100 kva", "60 kva", "power transformer", "isolation transformer", "essential service", "sec 5", "iec 60076"],
    "calculator": {
      "type": "transformer",
      "labelTr": "Trafo Test Gerilimi & İzolasyon Hesaplayıcı (Pt C, Ch 2, Sec 5 [1.5])",
      "labelEn": "Transformer Test Voltage & Insulation Calculator (Pt C, Ch 2, Sec 5 [1.5])",
      "defaultVoltage": 440,
      "defaultFreq": 60
    },
    "referenceTables": [
      {
        "titleEn": "Table 1 : Temperature rise limits for dry-type transformers (Ambient 45°C)",
        "titleTr": "Tablo 1 : Kuru Tip Trafolar İçin Sıcaklık Artış Sınırları (45°C Ortam Bazlı - Direnç Yöntemi)",
        "headers": ["Insulation Class / Yalıtım Sınıfı", "Class A", "Class E", "Class B", "Class F", "Class H", "Liquid Cooled (Air / Water)"],
        "rows": [
          ["Winding Temp. Rise Limit (ΔT) / Sargı Sıcaklık Artış Sınırı", "55 °C", "70 °C", "75 °C", "95 °C", "120 °C", "55 °C (Hava) / 68 °C (Su)"],
          ["Core & Adjacent Parts / Nüve ve Komşu Parçalar", "≤ 55 °C", "≤ 70 °C", "≤ 75 °C", "≤ 95 °C", "≤ 120 °C", "Yalıtıma zarar vermeyecek sınırda"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "already_type_tested",
        "questionEn": "Type tests are to be carried out on a prototype machine or on the first of a batch of machines. Is the transformer already type tested?",
        "questionTr": "Tip testleri (Type test) prototip bir makinede veya seri üretimin ilk trafosunda yapılmalıdır. Bu trafo daha önce tip testinden geçti mi (Type Approved / Özdeş Tip Test Raporu var mı)?",
        "options": [
          { "value": "No", "labelEn": "No (Prototype / First of batch — Type + Routine Tests)", "labelTr": "Hayır (Prototip / İlk Üretim — Tip + Rutin Testler)" },
          { "value": "Yes", "labelEn": "Yes (Identical to type-tested transformer — Routine Tests)", "labelTr": "Evet (Tip Testli Trafo ile Özdeş — Sadece Rutin Testler)" }
        ],
        "default": "No"
      },
      {
        "id": "rating_scope",
        "questionEn": "What is the transformer kVA rating for essential services?",
        "questionTr": "Esas servis (essential service) trafosunun anma gücü (kVA) nedir?",
        "options": [
          { "value": "over_100", "labelEn": "≥ 100 kVA (3-phase) or ≥ 60 kVA (1-phase) — Surveyor Attendance Required", "labelTr": "≥ 100 kVA (3 Faz) veya ≥ 60 kVA (Tek Faz) — Sörveyör Katılımı Zorunlu" },
          { "value": "5_to_100", "labelEn": "5 kVA up to 100 kVA (60 kVA 1-ph) — Case-by-case / Routine Test Report", "labelTr": "5 kVA – 100 kVA arası — Doküman İncelemesi ve Rutin Test Raporu ([2.1.5])" }
        ],
        "default": "over_100"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 1",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2071,
        "reqEn": "Construction (Dry-type preferred, double wound, IP rating, short-circuit withstand, temperature rise limits per Tab. 1)",
        "reqTr": "Konstrüksiyon ve Tasarım (Aksi onaylanmadıkça kuru tip, primer-sekonder ayrı sargılı, kısa devre dayanımı ve Tablo 1 sıcaklık artış limitleri)"
      },
      {
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2072,
        "reqEn": "Testing (Type tests and Routine tests in accordance with Tab. 2 and IEC 60076)",
        "reqTr": "Testler (Tablo 2 ve IEC 60076 uyarınca Tip ve Rutin fabrika kabul testleri)"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 2 Sec. 15",
        "sectionId": "Pt C, Ch 2, Sec 15",
        "page": 2126,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify valid calibration certificates (traceable to national/international standards) of the megger, high-voltage dielectric tester, winding resistance bridge, thermometer/thermocouples, and power analyzer prior to starting tests.",
        "titleTr": "Testte kullanılan ölçüm cihazlarının kalibrasyon durumu ve uygunluğunun doğrulanması.",
        "detailTr": "Testlere başlamadan önce Megger, Yüksek Gerilim (Hi-Pot) cihazı, sargı direnci ölçer (mikro-ohmmetre), voltmetre/ampermetre ve sıcaklık sensörlerinin geçerli kalibrasyon sertifikalarını ve seri numaralarını kontrol edin.",
        "tipTr": "Kalibrasyon tarihi geçmiş cihazla teste başlamayın; sertifika numaralarını raporunuza not edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2073,
        "titleEn": "Examination of the technical documentation, as appropriate, and visual inspection (Part. C Ch. 2 Sec. 5 Par. 2)",
        "detailEn": "- The manufacturer is to provide a technical file giving, inter alia, information concerning the construction, type, serial number, insulation class and all other technical data relevant to the transformer. A visual inspection is to be made to ensure that the transformer complies with technical documentation.",
        "titleTr": "Teknik dokümantasyonun incelenmesi ve görsel muayene (Part. C Ch. 2 Sec. 5 Par. 2 [2.1.2 & Tab. 2 No.1])",
        "detailTr": "- Üretici; trafonun yapısını, tipini, seri numarasını, yalıtım sınıfını (Class B/F/H vb.), kVA gücünü, gerilim oranını, bağlantı grubunu (örn. Dyn11), kısa devre empedansını (%Uk) ve RINA onaylı resmi içeren teknik dosyayı sunmalıdır. Trafonun onaylı resme, etiket bilgilerine (Nameplate), IP koruma sınıfına ve topraklama terminallerine uygunluğu görsel olarak muayene edilir.",
        "tipTr": "Etikette (Nameplate) ortam sıcaklığının 45°C (veya kurallara uygun referans değer), yalıtım sınıfının ve seri numarasının doğru basıldığını mutlaka kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2071,
        "titleEn": "Temperature rise measurement (Part. C Ch. 2 Sec. 5 Par. 2)",
        "detailEn": "Measured by resistance method for windings and thermometer method for core ([1.4.3]). Permissible temperature rise limits at 45°C ambient (Tab. 1): Class A = 55°C, Class E = 70°C, Class B = 75°C, Class F = 95°C, Class H = 120°C. For liquid-cooled transformers: 55°C (air-cooled) or 68°C (water-cooled). Under [2.1.3], if completely identical transformers have already been type-tested, this test need not be repeated provided the type-tested transformer's serial number and test results are inserted in the routine test report.",
        "titleTr": "Sıcaklık artış (Isınma / Temperature Rise) testi ve ölçümü (Part. C Ch. 2 Sec. 5 Par. 1.4 & Par. 2)",
        "detailTr": "Sargılarda direnç değişimi yöntemiyle (soğuk direnç R1 ve ısınma sonrası sıcak direnç R2 ölçülerek), nüvede ise termometre/termokupl yöntemiyle ölçülür. 45°C deniz ortam sıcaklığı baz alınarak izin verilen maksimum sıcaklık artış (ΔT) limitleri (Tablo 1): Sınıf A: 55°C, Sınıf E: 70°C, Sınıf B: 75°C, Sınıf F: 95°C, Sınıf H: 120°C. Tamamen özdeş bir trafoda daha önce yapılmışsa ([2.1.3]), tip testi yapılan trafonun seri numarası ve test sonucu sertifikaya yazılmak şartıyla tekrarlanmayabilir.",
        "tipTr": "Fabrika ortam sıcaklığı 45°C'den düşük olsa bile ΔT (Sıcaklık Artışı = T_son - T_ortam) doğrudan Tablo 1 limitlerini (örn. Class F için 95 K, Class H için 120 K) aşmamalıdır.",
        "condition": { "field": "already_type_tested", "equals": "No" }
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2072,
        "titleEn": "Insulation resistance measurement (Part. C Ch. 2 Sec. 5 Par. 2)",
        "detailEn": "- The certificates of transformers routine tested are to contain the manufacturer's serial number of the transformer which has been type tested and the test result.\n- Per [1.5.5]: The insulation resistance of a new, clean and dry transformer, measured after the temperature rise test has been carried out (at or near operating temperature) at a voltage equal to 500 V d.c., is to be not less than 5 MΩ.",
        "titleTr": "İzolasyon direnci (Megger) ölçümü (Part. C Ch. 2 Sec. 5 Par. 1.5.5 & Par. 2)",
        "detailTr": "- Rutin test yapılan trafoların sertifikalarında, daha önce tip testi (type test) yapılmış olan özdeş trafonun üretici seri numarası ve sıcaklık artış test sonucu mutlaka yer almalıdır.\n- Kural [1.5.5]: Yeni, temiz ve kuru bir trafonun (varsa sıcaklık artış testinden hemen sonra, çalışma sıcaklığında veya yakınında) 500 V DC test gerilimi ile ölçülen izolasyon direnci en az 5 MΩ olmalıdır (YG-AG, YG-Gövde, AG-Gövde arasında).",
        "tipTr": "Kural sınırı min. 5 MΩ @ 500V DC'dir (pratikte yeni kuru tip trafolarda yüzlerce MΩ veya GΩ okunur). Ölçümü YG-AG, YG-Toprak ve AG-Toprak arasında ayrı ayrı doğrulayın.",
        "condition": "always"
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2072,
        "titleEn": "High voltage test (Part. C Ch. 2 Sec. 5 Par. 2)",
        "detailEn": "Per [1.5.1] - [1.5.3]: Applied between each winding under test and the other windings not under test, core and enclosure all connected together to earth. The r.m.s. value of the test voltage is to be equal to 2 U + 1000 V, with a minimum of 2500 V, where U is the rated voltage of the winding. The full voltage is to be maintained for 1 minute (60 s) without breakdown or flashover.",
        "titleTr": "Yüksek gerilim (Uygulanan Gerilim / Dielectric High Voltage) testi (Part. C Ch. 2 Sec. 5 Par. 1.5.1 - 1.5.3)",
        "detailTr": "Test edilen her bir sargı ile test edilmeyen diğer tüm sargılar, nüve ve gövde (toprak) birbirine bağlıyken uygulanır. Test geriliminin etkin (r.m.s.) değeri; U sargı anma gerilimi olmak üzere 2U + 1000 V, ancak en az 2500 V (2.5 kV) olmalıdır. Tam test gerilimi 1 dakika (60 saniye) boyunca delinme veya atlama (breakdown/flashover) olmadan uygulanmalıdır. (Kısmen yeniden sarılmış trafolarda %75'i uygulanır).",
        "tipTr": "Örnek: 440V veya 690V sargılar için 2U+1000V değeri 2500V'un altında kaldığından minimum kural gereği 2500 V AC (60 sn) uygulanmalıdır!",
        "condition": "always"
      },
      {
        "num": 6,
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2072,
        "titleEn": "Induced voltage test (Part. C Ch. 2 Sec. 5 Par. 2)",
        "detailEn": "Per [1.5.6]: Transformers are to be subjected to an induced voltage insulation test by applying to the terminals of the winding under test a voltage equal to twice the rated voltage (2 x U_rated). The duration of the test is to be 60 s for any test frequency fp up to and including twice the rated frequency fn. If the test frequency exceeds twice the rated frequency (fp > 2 fn), the test time in seconds will be 120 x (fn / fp) with a minimum of 15 s.",
        "titleTr": "Endüklenen gerilim (Sarım Arası İzolasyon / Induced Voltage) testi (Part. C Ch. 2 Sec. 5 Par. 1.5.6)",
        "detailTr": "Aynı sargının sarımları (sipirleri) arasındaki izolasyonu test etmek amacıyla sargı uçlarına anma geriliminin 2 katı (2 × Un) gerilim uygulanır. Nüve doygunluğunu önlemek için artırılmış frekans (fp) kullanılır: Test frekansı anma frekansının 2 katına kadar ise (fp ≤ 2 fn) test süresi 60 saniyedir. Eğer fp > 2 fn ise test süresi t = 120 × (fn / fp) saniye (en az 15 saniye) olarak uygulanır.",
        "tipTr": "Genellikle 50 Hz trafoda 100 Hz veya 60 Hz trafoda 120 Hz ile 2×Un gerilimde 60 saniye uygulanır; 200 Hz kullanılırsa süre 30 saniyedir (min 15 sn).",
        "condition": "always"
      },
      {
        "num": 7,
        "ruleRef": "Part. C Ch. 2 Sec. 5 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 5",
        "page": 2073,
        "titleEn": "Voltage ratio (Part. C Ch. 2 Sec. 5 Par. 2)",
        "detailEn": "Per Tab. 2 No. 6 and IEC 60076-1: Measurement of voltage ratio on all tapping positions and check of phase displacement / vector group (e.g., Dyn11, Yyn0). Measured tolerance typically within ±0.5% of declared ratio.",
        "titleTr": "Gerilim dönüşüm oranı (Voltage Ratio) ve bağlantı grubu kontrolü (Part. C Ch. 2 Sec. 5 Par. 2, Tab. 2)",
        "detailTr": "Tüm kademe (tap) uçlarında dönüşüm oranı ölçülür ve vektör/bağlantı grubu (örn. Dyn11, Ynd11, II0) doğrulanır. IEC 60076-1 uyarınca ölçülen dönüşüm oranı sapması beyan edilen değerin ±%0.5'i (veya kısa devre empedansı %'sinin 1/10'u) sınırları içinde olmalıdır.",
        "tipTr": "Trafo üzerinde kademe ( ±%2.5, ±%5 tap ) uçları varsa her kademede ve her üç fazda dönüşüm oranının simetrik olduğunu kontrol edin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "rotating-machines-generators-motors",
    "code": "EL-02",
    "category": "electrical",
    "categoryTitleEn": "Part C, Ch 2 — Electrical Installations",
    "categoryTitleTr": "Part C, Ch 2 — Elektrik Sistemleri",
    "titleEn": "Rotating Electrical Machines — AC Generators (Alternators) and Electric Motors (≥ 100 kW / kVA)",
    "titleTr": "Döner Elektrik Makineleri — Alternatörler (Jeneratörler) ve Elektrik Motorları (≥ 100 kW / kVA)",
    "ruleRef": "Part. C - Ch. 2 - Sec. 4",
    "sectionId": "Pt C, Ch 2, Sec 4",
    "pdfPage": 2064,
    "keywords": ["generator", "alternator", "alternatör", "jeneratör", "electric motor", "elektrik motoru", "rotating machine", "shaft generator", "propulsion motor", "avr", "sec 4", "iec 60034"],
    "calculator": {
      "type": "rotating_machine",
      "labelTr": "Alternatör / Motor Test Gerilimi & İzolasyon Hesaplayıcı (Pt C, Ch 2, Sec 4 [4.2 & 4.9])",
      "labelEn": "Rotating Machine Dielectric & Megger Calculator (Pt C, Ch 2, Sec 4 [4.2 & 4.9])",
      "defaultVoltage": 440,
      "defaultSpeed": 1800
    },
    "referenceTables": [
      {
        "titleEn": "Table 2 : Minimum Insulation Resistance & Test Voltage (Pt C, Ch 2, Sec 4 [4.2.1])",
        "titleTr": "Tablo 2 : Minimum İzolasyon Direnci ve Test Gerilimi (Pt C, Ch 2, Sec 4 [4.2.1])",
        "headers": ["Rated Voltage Un (V)", "Min. DC Test Voltage (V)", "Min. Insulation Resistance (MΩ)"],
        "rows": [
          ["Un ≤ 250 V", "2 × Un", "1 MΩ"],
          ["250 V < Un ≤ 1000 V", "500 V DC", "1 MΩ"],
          ["1000 V < Un ≤ 7200 V", "1000 V DC", "(Un / 1000) + 1 MΩ"],
          ["7200 V < Un ≤ 15000 V", "5000 V DC", "(Un / 1000) + 1 MΩ"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "already_type_tested",
        "questionEn": "Type tests are to be carried out on a prototype machine or on the first of a batch of machines. Is the machine already type tested?",
        "questionTr": "Tip testleri prototip makinede veya serinin ilk makinesinde yapılır. Bu makine daha önce tip testinden geçti mi (Özdeş Tip Test Raporu var mı)?",
        "options": [
          { "value": "No", "labelEn": "No (Prototype / First of batch — Type Test Scope)", "labelTr": "Hayır (Prototip / İlk Üretim — Tip Test Kapsamı)" },
          { "value": "Yes", "labelEn": "Yes (Already Type Tested — Routine Test Scope)", "labelTr": "Evet (Tip Testi Mevcut — Rutin Test Kapsamı)" }
        ],
        "default": "No"
      },
      {
        "id": "machine_type",
        "questionEn": "Is the machine a Synchronous AC Generator (Alternator) or an Electric Motor?",
        "questionTr": "Test edilen makine Senkron Alternatör (Jeneratör) mü yoksa Elektrik Motoru mu?",
        "options": [
          { "value": "generator", "labelEn": "AC Synchronous Generator / Alternator", "labelTr": "AC Senkron Jeneratör / Alternatör" },
          { "value": "squirrel_motor", "labelEn": "Squirrel Cage Induction Motor (Sincap Kafesli Asenkron Motor)", "labelTr": "Sincap Kafesli Asenkron Motor (Squirrel Cage)" },
          { "value": "other_motor", "labelEn": "Wound Rotor / DC / Synchronous Propulsion Motor", "labelTr": "Bilezikli / DC / Senkron Tahrik Motoru" }
        ],
        "default": "generator"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 1 & 2",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2064,
        "reqEn": "Constructional and operational requirements, excitation and voltage regulation",
        "reqTr": "Yapısal ve işletme gereksinimleri, ikaz (excitation) sistemi ve gerilim regülasyonu (AVR)"
      },
      {
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 3 & 4",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2065,
        "reqEn": "Testing of rotating machines (Tab. 1 & Tab. 2) and test descriptions ([4.1] to [4.12])",
        "reqTr": "Döner makinelerin testleri (Tablo 1 ve Tablo 2) ve test prosedürleri ([4.1] - [4.12])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 2 Sec. 15",
        "sectionId": "Pt C, Ch 2, Sec 15",
        "page": 2126,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify valid calibration certificates of power analyzer, resistance bridge, tachometer, vibration meter, high-voltage tester, and insulation tester.",
        "titleTr": "Test ölçüm cihazlarının kalibrasyon durumu ve uygunluğunun doğrulanması.",
        "detailTr": "Güç analizörü, mikro-ohmmetre, takometre, vibrasyon ölçer, Hi-Pot ve Megger cihazlarının kalibrasyon geçerlilik tarihlerini kontrol edin.",
        "tipTr": "Yüksek güçlü alternatör/motor test yataklarında akım ve gerilim trafolarının (CT/PT) kalibrasyonunu da kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.1",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2067,
        "titleEn": "Examination of the technical documentation, as appropriate, and visual inspection (Part. C Ch. 2 Sec. 4 Par. 4.1)",
        "detailEn": "Technical documentation of machines rated at 100 kW (kVA) and over is to be available for examination by the Surveyor. A visual examination is to be made to ensure compliance with approved technical documentation, IP protection, space heaters, PT100 sensors, and nameplate.",
        "titleTr": "Teknik dokümantasyonun incelenmesi ve görsel muayene (Part. C Ch. 2 Sec. 4 Par. 4.1)",
        "detailTr": "100 kW (kVA) ve üzeri makinelerin onaylı çizimleri, sargı/yalıtım sınıfı, klemens kutusu, anti-kondens ısıtıcıları (space heater), sargı/yatak PT100 sıcaklık sensörleri ve etiket bilgileri incelenir.",
        "tipTr": "Rutin test sertifikasında, tip testi yapılmış olan prototip makinenin seri numarası ve tip test sonuçları mutlaka referans gösterilmelidir (Tab. 1 Not 2).",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.3",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2067,
        "titleEn": "Winding resistance measurement (Part. C Ch. 2 Sec. 4 Par. 4.3)",
        "detailEn": "The resistances of the machine windings (stator phases, rotor field, exciter windings) are to be measured and recorded using an appropriate bridge method or voltage and current method at known cold ambient temperature.",
        "titleTr": "Sargı direnci (Soğuk Direnç / Winding Resistance) ölçümü (Part. C Ch. 2 Sec. 4 Par. 4.3)",
        "detailTr": "Stator faz sargıları (U-V, V-W, W-U), rotor uyartım sargısı ve ikaz sargılarının soğuk dirençleri köprü (bridge) veya gerilim-akım yöntemiyle ortam sıcaklığı kaydedilerek ölçülür.",
        "tipTr": "Üç faz arasındaki direnç dengesizliğinin %1-2'yi aşmadığından emin olun; bu değer aynı zamanda ısınma (temperature rise) hesabında referans R1 değeridir.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.5",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2067,
        "titleEn": "Rated load test and temperature rise measurement (Part. C Ch. 2 Sec. 4 Par. 4.5)",
        "detailEn": "Temperature rises are to be measured at rated output, voltage, and frequency until thermal equilibrium is reached per IEC 60034-1, adjusted for marine ambient reference temperature (45°C air / 32°C cooling water per Sec 2).",
        "titleTr": "Nominal yük testi ve sıcaklık artış (Temperature Rise) ölçümü (Part. C Ch. 2 Sec. 4 Par. 4.5)",
        "detailTr": "Makine nominal güç, gerilim ve frekansta ısıl dengeye (saatte ≤ 2 K değişim) ulaşana kadar çalıştırılır. IEC 60034-1'e göre 45°C gemi ortam sıcaklığına göre düzeltilmiş sıcaklık artış sınırları: Sınıf B = 75 K, Sınıf F = 100 K, Sınıf H = 120 K (direnç yöntemiyle).",
        "tipTr": "Eğer test yatağında tam yük verilemiyorsa, senkron makineler için Bölüm 2 Ek 1'deki (App 1) dolaylı test yöntemi (Indirect Test Method) RINA onayı ile uygulanabilir.",
        "condition": { "field": "already_type_tested", "equals": "No" }
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.6",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2068,
        "titleEn": "Overload / overcurrent test (Part. C Ch. 2 Sec. 4 Par. 4.6)",
        "detailEn": "Carried out as a type test for generators as proof of overload capability of generator and excitation system (1.5 × rated current for 2 min per IEC 60034-1), and for motors as proof of momentary excess torque (1.6 × rated torque for 15 s). At routine tests on machines >100 kW/kVA, overload test can be replaced by an overcurrent test at reduced speed (motors) or short-circuit (generators).",
        "titleTr": "Aşırı yük / aşırı akım (Overload / Overcurrent) testi (Part. C Ch. 2 Sec. 4 Par. 4.6)",
        "detailTr": "100 kW/kVA üzerindeki esas servis makinelerinde uygulanır (Tab. 1 Not 4). IEC 60034-1 uyarınca jeneratörlerde 1.5 × In akımda (en az 15 sn - 2 dk), motorlarda ise 1.6 × nominal torkta 15 sn dayanım doğrulanır. Rutin testlerde düşük devirde veya kısa devrede aşırı akım testi olarak yapılabilir.",
        "tipTr": "Irgat (windlass) gibi özel amaçlı motorlarda onaylı projede belirtilen özel aşırı yük değerleri esas alınır ([4.6.2]).",
        "condition": "always"
      },
      {
        "num": 6,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.4",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2067,
        "titleEn": "Verification of the voltage regulation system — AVR (Part. C Ch. 2 Sec. 4 Par. 4.4)",
        "detailEn": "- Steady state: Keep rated voltage within ±2.5% (±3.5% for emergency sets) from no-load to full load at rated power factor.\n- Transient load change (Type test): Sudden switching of 60% rated current at cos φ ≤ 0.4 lagging; voltage must not drop below 85% nor exceed 120% of Un, and must recover within ±3% in ≤ 1.5 s (emergency sets: ±4% in ≤ 5 s).\n- Note (7) (1/7/2026): Electronic/Digital AVR with CBS communication must comply with Ch 3, Sec 5 (IACS UR E27 Cyber Resilience).",
        "titleTr": "Gerilim regülasyon sisteminin (AVR) doğrulanması (Part. C Ch. 2 Sec. 4 Par. 4.4)",
        "detailTr": "- Kalıcı durum (Steady-state): Boştan tam yüke kadar gerilim ±%2.5 (acil jeneratörde ±%3.5) içinde kalmalıdır.\n- Geçici rejim (Transient - Tip Testi): cos φ ≤ 0.4 endüktif yükte %60 anma akımı aniden basıldığında gerilim %85 Un altına düşmemeli, yük atıldığında %120 Un üzerine çıkmamalı ve ≤ 1.5 saniyede ±%3 bandına dönmelidir (Acil jeneratörde ≤ 5 sn içinde ±%4).\n- Rutin testlerde (Tab. 1 Not 3) AVR'nin fonksiyonel regülasyon kontrolü yapılır. Dijital haberleşmeli AVR'lerde IACS UR E27 siber güvenlik uyumu aranır.",
        "tipTr": "Rutin testte tip testindeki ani yük (transient) kayıtları/hesapları onaylıysa fiziksel darbe yük testi tekrarlanmadan AVR fonksiyon testi yeterli kabul edilebilir ([4.4.4]).",
        "condition": { "field": "machine_type", "equals": "generator" }
      },
      {
        "num": 7,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.7",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2068,
        "titleEn": "Verification of steady short-circuit conditions (Part. C Ch. 2 Sec. 4 Par. 4.7)",
        "detailEn": "Applies to synchronous generators (Type test, Tab. 1 Note 5): Verify that under steady-state 3-phase short-circuit conditions, the generator with its voltage regulating system is capable of maintaining, without sustaining any damage, a current of at least 3 × rated current (3 In) for a duration of at least 2 seconds. Short-circuit decrement curve is to be provided.",
        "titleTr": "Kalıcı kısa devre koşullarının doğrulanması (Part. C Ch. 2 Sec. 4 Par. 4.7)",
        "detailTr": "Sadece senkron jeneratörlerin tip testinde uygulanır (Tab. 1 Not 5): Jeneratör ve AVR sistemi, 3 fazlı simetrik kısa devre altında hasar görmeksizin en az 3 × In (anma akımının 3 katı) akımı en az 2 saniye boyunca sürdürebilmelidir. Üretici kısa devre azalım eğrisini (decrement curve) sunmalıdır.",
        "tipTr": "Bu test pano şalterlerinin (ACB) selektivite açma süresi boyunca alternatörün ikazını kaybetmeden arıza akımı basabilmesini garanti eder.",
        "condition": { "field": "already_type_tested", "equals": "No" }
      },
      {
        "num": 8,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.10",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2069,
        "titleEn": "No load test (Part. C Ch. 2 Sec. 4 Par. 4.10)",
        "detailEn": "Machines are to be operated at no load and rated speed whilst being supplied at rated voltage and frequency as a motor while generators are to be driven by a suitable means and excited to give rated terminal voltage. Vibration and operation of bearing lubrication system are to be checked.",
        "titleTr": "Boşta çalışma (No-Load) testi, vibrasyon ve yatak kontrolü (Part. C Ch. 2 Sec. 4 Par. 4.10)",
        "detailTr": "Motorlar nominal gerilim ve frekansta boşta döndürülür; jeneratörler ise nominal devirde tahrik edilerek nominal terminal gerilimi verecek şekilde ikazlanır. Çalışma esnasında yatak sıcaklıkları, yağlama sistemi ve titreşim (vibrasyon) seviyeleri kontrol edilir.",
        "tipTr": "Faz sırasını, boşta çekilen akım dengesini ve rulman/kaymalı yatak ses ile titreşim değerlerini (IEC 60034-14) kaydedin.",
        "condition": "always"
      },
      {
        "num": 9,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.8",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2068,
        "titleEn": "Overspeed test (Part. C Ch. 2 Sec. 4 Par. 4.8)",
        "detailEn": "Machines are to withstand the overspeed test as specified in IEC 60034-1 (typically 1.2 × rated speed for 2 minutes). Note 6: This test is NOT applicable for squirrel cage motors.",
        "titleTr": "Aşırı devir (Overspeed) testi (Part. C Ch. 2 Sec. 4 Par. 4.8)",
        "detailTr": "IEC 60034-1 uyarınca makine 2 dakika süreyle anma devrinin %120'sinde (1.2 × n_N) aşırı devir testine tabi tutulur ve mekanik deformasyon/sürtme olmadığı doğrulanır. (Not 6: Sincap kafesli asenkron motorlarda uygulanmaz).",
        "tipTr": "Sargılı rotora sahip alternatörlerde, bilezikli motorlarda ve DC motorlarda zorunludur; sincap kafesli motorlarda muaf tutulur.",
        "condition": { "field": "machine_type", "notEquals": "squirrel_motor" }
      },
      {
        "num": 10,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.9",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2068,
        "titleEn": "Dielectric strength test — High Voltage Test (Part. C Ch. 2 Sec. 4 Par. 4.9)",
        "detailEn": "New and completed rotating machines are to withstand a dielectric test for 1 minute as specified in IEC 60034-1: generally 2 Un + 1000 V (minimum 1500 V) at power frequency between windings and frame/earth and between phases/windings. For high-voltage machines, impulse test on coils per Sec 13.",
        "titleTr": "Dielektrik dayanım (Yüksek Gerilim / High Voltage) testi (Part. C Ch. 2 Sec. 4 Par. 4.9)",
        "detailTr": "Yeni ve tamamlanmış döner makineler IEC 60034-1 uyarınca 1 dakika (60 sn) süreyle sargılar ile gövde (toprak) arasında ve sargılar arasında 2 Un + 1000 V (minimum 1500 V AC) dielektrik testine tabi tutulur. (PT100/ısıtıcı devrelerine de ilgili test gerilimi uygulanır).",
        "tipTr": "Örnek: 440V makine için 2×440 + 1000 = 1880 V AC; 690V makine için 2×690 + 1000 = 2380 V AC (60 saniye) uygulanır.",
        "condition": "always"
      },
      {
        "num": 11,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.2",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2067,
        "titleEn": "Insulation resistance measurement (Part. C Ch. 2 Sec. 4 Par. 4.2 & Tab. 2)",
        "detailEn": "Immediately after the high voltage tests, insulation resistances are to be measured using a DC insulation tester between all current-carrying parts and earth, and between phases/polarities. Minimum values per Tab. 2: for 250 < Un ≤ 1000 V, test at 500 V DC with min. 1 MΩ; for 1000 < Un ≤ 7200 V, test at 1000 V DC with min. (Un/1000 + 1) MΩ.",
        "titleTr": "İzolasyon direnci (Megger) ölçümü (Part. C Ch. 2 Sec. 4 Par. 4.2 & Tab. 2)",
        "detailTr": "Yüksek gerilim (HV) testinin hemen ardından çalışma sıcaklığına yakın durumda fazlar-gövde ve fazlar-arası izolasyon direnci ölçülür. Tablo 2'ye göre: 250V < Un ≤ 1000V için 500V DC'de min. 1 MΩ; 1000V < Un ≤ 7200V için 1000V DC'de min. (Un/1000 + 1) MΩ olmalıdır.",
        "tipTr": "İzolasyon ölçümünün mutlaka Yüksek Gerilim (HV) testinden SONRA tekrarlandığından emin olun ([4.2.1]).",
        "condition": "always"
      },
      {
        "num": 12,
        "ruleRef": "Part. C Ch. 2 Sec. 4 Par. 4.11 & 4.12",
        "sectionId": "Pt C, Ch 2, Sec 4",
        "page": 2069,
        "titleEn": "Verification of bearings and degree of protection (Part. C Ch. 2 Sec. 4 Par. 4.11 & 4.12)",
        "detailEn": "Upon completion of tests, machines which have sleeve bearings are to be opened upon request for examination by the Surveyor to establish that the shaft is correctly seated in the bearing shells. Degree of protection (IP) verified per IEC 60034-5 (Type test).",
        "titleTr": "Yatakların (Sleeve Bearings) ve IP koruma derecesinin doğrulanması (Part. C Ch. 2 Sec. 4 Par. 4.11 & 4.12)",
        "detailTr": "Testler tamamlandıktan sonra, kaymalı yataklı (sleeve bearing) makinelerde sörveyör talebiyle yatak kepi açılarak şaftın yatak burcuna düzgün oturduğu ve iz/aşınma olmadığı kontrol edilir. IP koruma sınıfı IEC 60034-5'e göre doğrulanır.",
        "tipTr": "Kaymalı yataklarda mil yalıtımını (bearing insulation - dolaşım akımlarını önlemek için) ölçmeyi unutmayın!",
        "condition": "always"
      }
    ]
  },
  {
    "id": "switchboards-distribution-mcc",
    "code": "EL-03",
    "category": "electrical",
    "categoryTitleEn": "Part C, Ch 2 — Electrical Installations",
    "categoryTitleTr": "Part C, Ch 2 — Elektrik Sistemleri",
    "titleEn": "Switchgear and Controlgear Assemblies — Main & Emergency Switchboards, MCC & Distribution Boards (≥ 100 A)",
    "titleTr": "Ana Pano (MSB), Acil Pano (ESB), MCC, Dümen Starteri ve Dağıtım Panoları (Bara Akımı ≥ 100 A)",
    "ruleRef": "Part. C - Ch. 2 - Sec. 8",
    "sectionId": "Pt C, Ch 2, Sec 8",
    "pdfPage": 2083,
    "keywords": ["switchboard", "main switchboard", "emergency switchboard", "msb", "esb", "mcc", "distribution board", "pano", "ana pano", "acil pano", "dağıtım panosu", "steering gear starter", "sec 8", "iec 60092-302"],
    "calculator": {
      "type": "switchboard",
      "labelTr": "Pano Ana ve Yardımcı Devre Yüksek Gerilim (HV) Hesaplayıcı (Pt C, Ch 2, Sec 8 Tab. 2 & 3)",
      "labelEn": "Switchboard Main & Auxiliary Circuit HV Calculator (Pt C, Ch 2, Sec 8 Tab. 2 & 3)",
      "defaultVoltage": 440,
      "defaultAuxVoltage": 230
    },
    "referenceTables": [
      {
        "titleEn": "Table 2 : Test voltages for main circuits (Pt C, Ch 2, Sec 8 [3.3.4])",
        "titleTr": "Tablo 2 : Ana Devreler İçin Yüksek Gerilim Test Değerleri (1 Dakika, 25-100 Hz AC)",
        "headers": ["Rated Insulation Voltage Ui (V)", "AC Test Voltage (r.m.s.)"],
        "rows": [
          ["Ui ≤ 60 V", "1000 V"],
          ["60 V < Ui ≤ 300 V", "2000 V"],
          ["300 V < Ui ≤ 660 V", "2500 V"],
          ["660 V < Ui ≤ 800 V", "3000 V"],
          ["800 V < Ui ≤ 1000 V", "3500 V"]
        ]
      },
      {
        "titleEn": "Table 3 : Test voltages for auxiliary circuits (Pt C, Ch 2, Sec 8 [3.3.4])",
        "titleTr": "Tablo 3 : Yardımcı / Kumanda Devreleri İçin Yüksek Gerilim Test Değerleri",
        "headers": ["Rated Insulation Voltage Ui (V)", "AC Test Voltage (r.m.s.)"],
        "rows": [
          ["Ui ≤ 12 V", "250 V"],
          ["12 V < Ui ≤ 60 V", "500 V"],
          ["Ui > 60 V", "2 × Ui + 1000 V (minimum 1500 V)"]
        ]
      }
    ],
    "applicationTerms": [
      {
        "id": "board_type",
        "questionEn": "Which type of switchgear or controlgear assembly is being tested? (Pt C, Ch 2, Sec 8 [3.1.5])",
        "questionTr": "Hangi tip pano veya kontrol donanımı test ediliyor? (Pt C, Ch 2, Sec 8 [3.1.5])",
        "options": [
          { "value": "msb_esb", "labelEn": "Main or Emergency Switchboard (Ana veya Acil Pano)", "labelTr": "Ana Pano (MSB) veya Acil Jeneratör Panosu (ESB)" },
          { "value": "mcc_db", "labelEn": "LV Distribution Board / Starter / MCC (Busbar ≥ 100 A) or Steering Gear Starter", "labelTr": "Dağıtım Panosu / MCC (Bara ≥ 100 A) veya Dümen Donanımı Starteri" },
          { "value": "hv_board", "labelEn": "High Voltage Switchboard (> 1000 V AC — Sec 8 & Sec 13)", "labelTr": "Orta/Yüksek Gerilim Panosu (> 1000 V AC — Sec 8 & Sec 13)" }
        ],
        "default": "msb_esb"
      },
      {
        "id": "has_cbs",
        "questionEn": "Does the switchboard contain computer-based electronic components (e.g. PMS PLC, digital relays) capable of communicating with other equipment? ([3.2.4])",
        "questionTr": "Panoda diğer sistemlerle haberleşebilen bilgisayar tabanlı elektronik bileşenler (PMS, PLC, dijital koruma rölesi vb.) var mı? ([3.2.4])",
        "options": [
          { "value": "Yes", "labelEn": "Yes (IACS UR E27 Cyber Resilience verification applies per Ch 3, Sec 5)", "labelTr": "Evet (Ch 3, Sec 5 / IACS UR E27 Siber Güvenlik kontrolü uygulanır)" },
          { "value": "No", "labelEn": "No (Conventional non-communicating components only)", "labelTr": "Hayır (Haberleşmeli bilgisayar tabanlı sistem yok)" }
        ],
        "default": "Yes"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 2 Sec. 8 Par. 1 & 2",
        "sectionId": "Pt C, Ch 2, Sec 8",
        "page": 2083,
        "reqEn": "Constructional requirements for main, emergency and distribution switchboards (busbars, clearance/creepage, instrumentation, internal arc/partitioning)",
        "reqTr": "Ana, acil ve dağıtım panoları için yapım kuralları (baralar, yalıtım/atlama mesafeleri, ölçü aletleri, bölmelendirme, tutamaklar ve damlama siperi)"
      },
      {
        "ruleRef": "Part. C Ch. 2 Sec. 8 Par. 3",
        "sectionId": "Pt C, Ch 2, Sec 8",
        "page": 2087,
        "reqEn": "Testing prior to installation on board per [3.2] to [3.4] and IEC 60092-302-2",
        "reqTr": "Gemiye montaj öncesi [3.2] - [3.4] ve IEC 60092-302-2 uyarınca fabrika kabul testleri"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 2 Sec. 15",
        "sectionId": "Pt C, Ch 2, Sec 15",
        "page": 2126,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify valid calibration certificates of AC High-Voltage tester, 500V/1000V DC Megger, secondary current injection test set, multimeter, and torque wrench.",
        "titleTr": "Testte kullanılan ölçüm cihazlarının kalibrasyon durumu ve uygunluğunun doğrulanması.",
        "detailTr": "AC Yüksek Gerilim (Hi-Pot) cihazı, Megger, röle sekonder akım enjeksiyon cihazı, multimetre ve bara tork anahtarının kalibrasyon sertifikalarını doğrulayın.",
        "tipTr": "Bara civatalarının tork kontrolü için kullanılan tork anahtarının kalibrasyonunu da mutlaka kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 2 Sec. 8 Par. 3.2.1 & 3.2.2",
        "sectionId": "Pt C, Ch 2, Sec 8",
        "page": 2088,
        "titleEn": "Visual inspection, compliance with approved drawings, creepage/clearance and bolted connection torque check (Part. C Ch. 2 Sec. 8 Par. 3.2.1 & 3.2.2)",
        "detailEn": "Verify that the switchboard complies with approved drawings, maintains the prescribed IP degree of protection (min IP22 / IP23 drip-proof hood), satisfies creepage and clearance distances (Tab. 1), and that screwed/bolted busbar connections have adequate contact (random torque check). Verify earth continuity of doors and frames.",
        "titleTr": "Görsel muayene, onaylı resme uygunluk, bara mesafeleri ve civata tork kontrolü (Part. C Ch. 2 Sec. 8 Par. 3.2.1 & 3.2.2)",
        "detailTr": "Panonun RINA onaylı tek hat ve genel yerleşim resimlerine uygunluğu, IP koruma sınıfı, ön/arka ahşap veya yalıtkan tutamakları (handrails), damlama siperi (drip-proof canopy), Tablo 1 bara açıklık/yüzey mesafeleri (creepage & clearance), şalter/kablo etiketleri, kapak topraklama köprüleri ve rastgele seçilen bara civatalarının sıkılık torkları kontrol edilir.",
        "tipTr": "Ana panoda >500 kW toplam jeneratör gücünde jeneratör bölmeleri arasındaki ayırıcı perdeleri (partitioning) ve 400V/440V/690V acil aydınlatma/tehlike uyarı etiketlerini kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 2 Sec. 8 Par. 3.2.3",
        "sectionId": "Pt C, Ch 2, Sec 8",
        "page": 2088,
        "titleEn": "Electrical operation and functional test of interlocks, protections and instrumentation (Part. C Ch. 2 Sec. 8 Par. 3.2.3)",
        "detailEn": "Carry out electrical functioning tests including: ACB/MCCB closing/tripping, mechanical & electrical interlocks (shore connection vs generators, tie-breaker interlocks), reverse power / overcurrent / undervoltage trips, preferential tripping (load shedding) sequence & timers, automatic & manual synchronising (synchroscope, lamps, check-synchroniser relay), insulation monitoring device (IMD) alarm test ([1.7.13]), and space heater auto-switching.",
        "titleTr": "Elektriksel çalışma, kilitleme (interlock), koruma ve senkronizasyon fonksiyon testleri (Part. C Ch. 2 Sec. 8 Par. 3.2.3)",
        "detailTr": "Şalter açma/kapama, sahil beslemesi (shore connection) ile jeneratör şalterleri arasındaki elektriksel/mekanik kilitleme, ters güç (reverse power), düşük gerilim (undervoltage), aşırı akım açmaları, kademeli yük atma (preferential trip / load shedding) zamanlamaları, senkronoskop ve senkronizasyon rölesi testi, kaçak akım/izolasyon izleme cihazı (IMD) alarm testi ([1.7.13]) ve pano ısıtıcılarının şalter kapandığında otomatik devreden çıkması test edilir.",
        "tipTr": "Acil panoda (ESB) ana panodan besleme kesildiğinde acil jeneratörün otomatik devreye girme ve tie-breaker (kuplaj) şalterinin otomatik açma kilidini mutlaka simüle ettirin.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 2 Sec. 8 Par. 3.2.4",
        "sectionId": "Pt C, Ch 2, Sec 8",
        "page": 2088,
        "titleEn": "Cyber resilience verification of communicating electronic components — IACS UR E27 (Part. C Ch. 2 Sec. 8 Par. 3.2.4 & Ch. 3 Sec. 5)",
        "detailEn": "Per [3.2.4] (1/7/2026): Electronic components having a computer-based system capable of communicating with other equipment are to comply with the cyber resilience requirements in Ch 3, Sec 5 (IACS UR E27).",
        "titleTr": "Haberleşmeli elektronik bileşenlerin siber güvenlik doğrulaması — IACS UR E27 (Part. C Ch. 2 Sec. 8 Par. 3.2.4)",
        "detailTr": "1 Temmuz 2026 kuralı uyarınca, diğer ekipmanlarla ağ üzerinden haberleşebilen bilgisayar tabanlı sistem (PMS kontrolörü, PLC, HMI, akıllı röleler) içeren panolarda Ch 3, Sec 5 (IACS UR E27) siber güvenlik varlık envanteri, port kısıtlamaları ve parola/erişim kontrolleri doğrulanır.",
        "tipTr": "Panodaki PLC/HMI üzerindeki kullanılmayan USB ve RJ45 Ethernet portlarının fiziksel veya yazılımsal olarak kapatıldığını (hardening) kontrol edin.",
        "condition": { "field": "has_cbs", "equals": "Yes" }
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 2 Sec. 8 Par. 3.3",
        "sectionId": "Pt C, Ch 2, Sec 8",
        "page": 2088,
        "titleEn": "High voltage test on main and auxiliary circuits (Part. C Ch. 2 Sec. 8 Par. 3.3, Tab. 2 & Tab. 3)",
        "detailEn": "Performed with AC voltage (25–100 Hz) for 1 minute:\n- Between all live parts connected together and earth\n- Between each polarity/phase and all other polarities/phases connected to earth.\nMain circuit test voltages (Tab. 2): Ui ≤ 60V -> 1000V; 60 < Ui ≤ 300V -> 2000V; 300 < Ui ≤ 660V -> 2500V; 660 < Ui ≤ 800V -> 3000V; 800 < Ui ≤ 1000V -> 3500V.\nAuxiliary circuits (Tab. 3): Ui > 60V -> 2 Ui + 1000V (min 1500V). Sensitive electronic devices may be disconnected during HV test.",
        "titleTr": "Ana ve yardımcı devre yüksek gerilim (Dielektrik / Hi-Pot) testi (Part. C Ch. 2 Sec. 8 Par. 3.3, Tab. 2 & Tab. 3)",
        "detailTr": "25–100 Hz sinüzoidal AC gerilimle 1 dakika (60 sn) boyunca hem tüm aktif baralar/devreler ile gövde (toprak) arasında, hem de her bir faz (R, S, T) ile toprağa bağlanmış diğer fazlar arasında uygulanır.\n- Ana Devre (Tablo 2): 300 < Ui ≤ 660 V için 2500 V AC; 660 < Ui ≤ 800 V için 3000 V AC; 800 < Ui ≤ 1000 V için 3500 V AC.\n- Yardımcı/Kumanda Devresi (Tablo 3): Ui > 60 V için 2 Ui + 1000 V (en az 1500 V AC).",
        "tipTr": "440V gemi panolarında nominal yalıtım gerilimi Ui genellikle 660V (test: 2500V) veya 690V/1000V (test: 3000V / 3500V) seçilir; teknik dosyadaki beyan edilen Ui değerine göre Tablo 2'yi uygulayın!",
        "condition": "always"
      },
      {
        "num": 6,
        "ruleRef": "Part. C Ch. 2 Sec. 8 Par. 3.4",
        "sectionId": "Pt C, Ch 2, Sec 8",
        "page": 2089,
        "titleEn": "Measurement of insulation resistance (Part. C Ch. 2 Sec. 8 Par. 3.4)",
        "detailEn": "Immediately after the high voltage test, the insulation resistance is to be measured using a device with a DC voltage of at least 500 V. The insulation resistance between all current-carrying parts and earth (and between each polarity/phase and the other polarities) is to be at least equal to 1 MΩ.",
        "titleTr": "İzolasyon direnci (Megger) ölçümü (Part. C Ch. 2 Sec. 8 Par. 3.4)",
        "detailTr": "Yüksek gerilim (HV) testinin hemen ardından en az 500 V DC gerilimle tüm akım taşıyan bölümler ile toprak arasında ve fazlar (L1-L2, L2-L3, L3-L1) arasında izolasyon direnci ölçülür. Ölçülen değer en az 1 MΩ olmalıdır.",
        "tipTr": "HV testi sırasında sökülen elektronik kartlar/cihazlar tekrar devreye alındıktan sonra da son bir kontrol yapılması iyi saha uygulamasıdır.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "semiconductor-convertors-vfd",
    "code": "EL-04",
    "category": "electrical",
    "categoryTitleEn": "Part C, Ch 2 — Electrical Installations",
    "categoryTitleTr": "Part C, Ch 2 — Elektrik Sistemleri",
    "titleEn": "Semiconductor Convertors, Frequency Drives (VFD) & Static Inverters (≥ 50 kVA)",
    "titleTr": "Yarı İletken Konvertörler, Frekans Konvertörleri (VFD / Sürücü) ve Statik İnvertörler (≥ 50 kVA)",
    "ruleRef": "Part. C - Ch. 2 - Sec. 6",
    "sectionId": "Pt C, Ch 2, Sec 6",
    "pdfPage": 2074,
    "keywords": ["convertor", "converter", "vfd", "inverter", "frequency drive", "sürücü", "frekans konvertörü", "redresör", "rectifier", "thruster drive", "propulsion drive", "sec 6", "iec 60146"],
    "applicationTerms": [
      {
        "id": "already_type_tested",
        "questionEn": "Type tests are to be carried out on a prototype convertor or the first of a batch of convertors. Is the convertor already type tested? ([2.1.3 & Tab. 2])",
        "questionTr": "Tip testleri prototip konvertörde veya serinin ilk ürününde yapılır. Bu konvertör daha önce tip testinden geçti mi (Özdeş Tip Testi var mı)?",
        "options": [
          { "value": "No", "labelEn": "No (Prototype / First of batch — Type + Routine Tests)", "labelTr": "Hayır (Prototip / İlk Üretim — Tip + Rutin Testler)" },
          { "value": "Yes", "labelEn": "Yes (Identical to type-tested convertor — Routine Tests)", "labelTr": "Evet (Tip Testli Konvertör ile Özdeş — Rutin Testler)" }
        ],
        "default": "No"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 2 Sec. 6 Par. 1",
        "sectionId": "Pt C, Ch 2, Sec 6",
        "page": 2074,
        "reqEn": "Constructional and operational requirements, cooling monitoring, protection, THD limits and IACS UR E27 cyber resilience",
        "reqTr": "Yapısal ve işletme kuralları, soğutma izleme/alarm, kısa devre/aşırı gerilim koruması, harmonik (THD) sınırları ve IACS UR E27 siber güvenlik"
      },
      {
        "ruleRef": "Part. C Ch. 2 Sec. 6 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 6",
        "page": 2075,
        "reqEn": "Testing of semiconductor convertors ≥ 50 kVA for essential services (Tab. 1 & Tab. 2, IEC 60146)",
        "reqTr": "Esas servisler için ≥ 50 kVA yarı iletken konvertörlerin testleri (Tablo 1, Tablo 2 ve IEC 60146)"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 2 Sec. 15",
        "sectionId": "Pt C, Ch 2, Sec 15",
        "page": 2126,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify calibration certificates of all electrical and thermal test instruments.",
        "titleTr": "Testte kullanılan ölçüm cihazlarının kalibrasyon durumu ve uygunluğunun doğrulanması.",
        "detailTr": "Kullanılan tüm elektriksel güç analizörü, Hi-Pot, Megger ve sıcaklık ölçüm cihazlarının kalibrasyon sertifikalarını doğrulayın.",
        "tipTr": "Harmonik (THD) ölçümü yapılacaksa güç analizörünün harmonik bant genişliğini kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 2 Sec. 6 Par. 2.2 (Tab. 2 No. 1)",
        "sectionId": "Pt C, Ch 2, Sec 6",
        "page": 2076,
        "titleEn": "Examination of the technical documentation, as appropriate, and visual inspection including check of earth continuity (Part. C Ch. 2 Sec. 6 Par. 2)",
        "detailEn": "Verify compliance with approved drawings, modular removable arrangement of semiconductor stacks/fuses/control boards ([1.1.6]), drip trays and fluid resistivity monitoring for liquid-cooled units ([1.1.3]), earth continuity, and IACS UR E27 cyber resilience ([1.1.2] & [2.1.1]).",
        "titleTr": "Teknik dokümantasyon incelemesi, görsel muayene ve topraklama sürekliliği kontrolü (Part. C Ch. 2 Sec. 6 Par. 2, Tab. 2 No. 1)",
        "detailTr": "Onaylı resimlere uygunluk, yarı iletken modüllerin/sigortaların/kontrol kartlarının komple ünite sökülmeden çıkarılabilir olması ([1.1.6]), sıvı soğutmalı ünitelerde damlama tavası ve soğutma sıvısı iletkenlik/direnç (resistivity) alarmı ([1.1.3]), gövde topraklama sürekliliği ve haberleşmeli kartlarda IACS UR E27 siber güvenlik uyumu kontrol edilir.",
        "tipTr": "Rutin test sertifikasında tip testi yapılmış prototip konvertörün seri numarası ve test sonuçları yer almalıdır (Tab. 2 Not 2).",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 2 Sec. 6 Par. 2.2 (Tab. 2 No. 2)",
        "sectionId": "Pt C, Ch 2, Sec 6",
        "page": 2076,
        "titleEn": "Light load function test to verify all basic and auxiliary functions (Part. C Ch. 2 Sec. 6 Par. 2)",
        "detailEn": "Verify firing/control circuits, start/stop sequences, speed/frequency control, voltage regulation, current limiting, and overvoltage/overcurrent trip alarms ([1.2.4]).",
        "titleTr": "Tüm temel ve yardımcı fonksiyonları doğrulamak için düşük yükte fonksiyon testi (Part. C Ch. 2 Sec. 6 Par. 2, Tab. 2 No. 2)",
        "detailTr": "Tetikleme ve kontrol devreleri, start/stop sıralaması, frekans/hız referans kontrolü, akım sınırlama ve aşırı akım/aşırı gerilim koruma alarmları ([1.2.4]) düşük yükte çalıştırılarak doğrulanır.",
        "tipTr": "Acil servis veya elektrikli tahrik (propulsion) konvertörlerinde koruma açma alarmlarının uzaktan izleme çıkışlarını mutlaka test edin.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 2 Sec. 6 Par. 2.2 (Tab. 2 No. 3 & 4)",
        "sectionId": "Pt C, Ch 2, Sec 6",
        "page": 2076,
        "titleEn": "Rated current test and temperature rise measurement (Part. C Ch. 2 Sec. 6 Par. 1.4 & Par. 2)",
        "detailEn": "Type test on prototype or first of batch ([2.1.3]): Verify operation at rated current and measure temperature rise of semiconductor elements/enclosure based on 45°C ambient air or 32°C cooling water ([1.4.1]).",
        "titleTr": "Nominal akım testi ve sıcaklık artış (Temperature Rise) ölçümü (Part. C Ch. 2 Sec. 6 Par. 1.4 & Par. 2, Tab. 2 No. 3 & 4)",
        "detailTr": "Prototip veya serinin ilk konvertöründe nominal akımda çalıştırılarak yarı iletken modüllerin ve pano/soğutucu blokların sıcaklık artışı 45°C ortam havası veya 32°C deniz suyu referansına göre doğrulanır ([1.4.1]). Özdeş konvertörlerde tekrarlanmayabilir ([2.1.3]).",
        "tipTr": "Üreticinin beyan ettiği maksimum referans nokta sıcaklığının (heatsink / junction referans noktası) aşılmadığını kontrol edin ([1.4.2]).",
        "condition": { "field": "already_type_tested", "equals": "No" }
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 2 Sec. 6 Par. 1.5 & 2.2 (Tab. 2 No. 5)",
        "sectionId": "Pt C, Ch 2, Sec 6",
        "page": 2075,
        "titleEn": "Insulation test — Dielectric strength test and insulation resistance measurement (Part. C Ch. 2 Sec. 6 Par. 1.5 & Par. 2)",
        "detailEn": "Per IEC 60146 and Tab. 1 (where U = Um / √2): for U ≤ 60V -> 600V; for 60V < U ≤ 90V -> 900V; for U > 90V -> 2U + 1000V (minimum 2000V AC) for 1 minute, followed by insulation resistance measurement.",
        "titleTr": "İzolasyon testi — Yüksek gerilim (Dielektrik) ve izolasyon direnci ölçümü (Part. C Ch. 2 Sec. 6 Par. 1.5 & Tab. 1)",
        "detailTr": "IEC 60146 ve Tablo 1 uyarınca (U = Um / √2 olmak üzere): U > 90 V olan konvertörlerde 2U + 1000 V (en az 2000 V AC) test gerilimi 1 dakika uygulanır ve ardından Megger ile izolasyon direnci ölçülür.",
        "tipTr": "Yüksek gerilim testi sırasında yarı iletken IGBT/tristör uçları kendi içinde kısa devre edilerek gövdeye (toprağa) karşı test edilir.",
        "condition": "always"
      },
      {
        "num": 6,
        "ruleRef": "Part. C Ch. 2 Sec. 6 Par. 1.1.4, 1.1.5 & Tab. 2 No. 6",
        "sectionId": "Pt C, Ch 2, Sec 6",
        "page": 2076,
        "titleEn": "Protection of the convertors in case of failure of forced cooling system (Part. C Ch. 2 Sec. 6 Par. 1.1.4, 1.1.5 & Par. 2)",
        "detailEn": "Where forced (air or liquid) cooling is provided, verify that the convertor cannot be or remain loaded unless effective cooling is maintained, and that overtemperature of cooling medium initiates an alarm and activates convertor shutdown.",
        "titleTr": "Cebri soğutma sistemi (fan veya sıvı pompası) arızasında konvertör koruma testi (Part. C Ch. 2 Sec. 6 Par. 1.1.4, 1.1.5 & Tab. 2 No. 6)",
        "detailTr": "Cebri hava (fan) veya sıvı soğutma bulunan konvertörlerde soğutma durduğunda veya soğutucu akışkan sıcaklığı sınır değeri aştığında alarm verildiği ve konvertörün yük altında kalmasının engellendiği (otomatik trip/shutdown veya yük azaltma) simüle edilerek doğrulanır.",
        "tipTr": "Soğutma fanı şalterini açtırarak veya hava/sıvı akış/sıcaklık sensörünü simüle ettirerek alarm ve trip fonksiyonunu bizzat görün.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "ups-battery-chargers",
    "code": "EL-05",
    "category": "electrical",
    "categoryTitleEn": "Part C, Ch 2 — Electrical Installations",
    "categoryTitleTr": "Part C, Ch 2 — Elektrik Sistemleri",
    "titleEn": "Uninterruptible Power Systems (UPS ≥ 50 kVA) and Battery Chargers (≥ 2 kW)",
    "titleTr": "Kesintisiz Güç Kaynakları (UPS ≥ 50 kVA) ve Akü Şarj Redresörleri (Battery Chargers ≥ 2 kW)",
    "ruleRef": "Part. C - Ch. 2 - Sec. 7",
    "sectionId": "Pt C, Ch 2, Sec 7",
    "pdfPage": 2077,
    "keywords": ["ups", "uninterruptible power", "battery charger", "charger", "akü şarj", "redresör", "kesintisiz güç kaynağı", "batarya", "battery", "sec 7", "iec 62040"],
    "applicationTerms": [
      {
        "id": "equip_subtype",
        "questionEn": "Is the unit an Uninterruptible Power System (UPS ≥ 50 kVA) or a Battery Charger?",
        "questionTr": "Test edilen ekipman Kesintisiz Güç Kaynağı (UPS ≥ 50 kVA) mı yoksa Akü Şarj Cihazı (Redresör) mı?",
        "options": [
          { "value": "ups", "labelEn": "UPS Unit (≥ 50 kVA — Sec 7 [3.6])", "labelTr": "UPS Ünitesi (≥ 50 kVA — Sec 7 [3.6])" },
          { "value": "charger", "labelEn": "Battery Charger (≥ 2 kW — Sec 7 [2.2] & Tab. 1)", "labelTr": "Akü Şarj Redresörü (≥ 2 kW — Sec 7 [2.2] & Tab. 1)" }
        ],
        "default": "ups"
      },
      {
        "id": "already_type_tested",
        "questionEn": "Is the unit already type tested?",
        "questionTr": "Ünitenin daha önce yapılmış Tip Testi (Type Test) mevcut mu?",
        "options": [
          { "value": "No", "labelEn": "No (Prototype / First of batch — includes Temperature Rise)", "labelTr": "Hayır (Prototip / İlk Üretim — Sıcaklık Artış Testi dahil)" },
          { "value": "Yes", "labelEn": "Yes (Routine Test on subsequent battery charger)", "labelTr": "Evet (Tip Testi Mevcut — Akü Şarj Cihazı Rutin Test)" }
        ],
        "default": "No"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 2 Sec. 7 Par. 2 & 3",
        "sectionId": "Pt C, Ch 2, Sec 7",
        "page": 2078,
        "reqEn": "Construction, performance, alarms ([3.3.5]), SOLAS II-1/42 & 43 backup duration, and IACS UR E27 cyber resilience ([3.6.1])",
        "reqTr": "Yapım, performans, alarmlar ([3.3.5]), SOLAS II-1/42 ve 43 yedekleme süresi ve IACS UR E27 siber güvenlik ([3.6.1])"
      },
      {
        "ruleRef": "Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6",
        "sectionId": "Pt C, Ch 2, Sec 7",
        "page": 2081,
        "reqEn": "Testing and survey of battery chargers (Tab. 1) and UPS units of 50 kVA and over ([3.6.2])",
        "reqTr": "Akü şarj cihazlarının (Tablo 1) ve 50 kVA ve üzeri UPS ünitelerinin ([3.6.2]) test ve sörveyi"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 2 Sec. 15",
        "sectionId": "Pt C, Ch 2, Sec 15",
        "page": 2126,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify calibration certificates of load banks, power analyzer, DC voltmeters/ammeters, Hi-Pot, and Megger.",
        "titleTr": "Testte kullanılan ölçüm cihazlarının kalibrasyon durumu ve uygunluğunun doğrulanması.",
        "detailTr": "Kullanılan yük bankası, güç analizörü, DC pensampermetre/voltmetre, Hi-Pot ve Megger cihazlarının kalibrasyonlarını doğrulayın.",
        "tipTr": "Akü deşarj ve ripple (dalgalanma) ölçümleri için True-RMS multimetre/analizör kullanıldığından emin olun.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6",
        "sectionId": "Pt C, Ch 2, Sec 7",
        "page": 2081,
        "titleEn": "Examination of the technical documentation, as appropriate, and visual inspection including check of earth continuity (Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6)",
        "detailEn": "Verify compliance with approved drawings, IEC 62040 series standards (for UPS), reverse current protection ([2.1.6]), earth continuity, and IACS UR E27 cyber resilience for communicating CBS components ([3.6.1]).",
        "titleTr": "Teknik dokümantasyon incelemesi, görsel muayene ve topraklama sürekliliği kontrolü (Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6)",
        "detailTr": "Onaylı resimlere, IEC 62040 standartlarına (UPS için), ters akım korumasına ([2.1.6]), gövde/kapak topraklama sürekliliğine ve haberleşmeli kontrol kartlarında IACS UR E27 siber güvenlik gereksinimlerine ([3.6.1]) uygunluk kontrol edilir.",
        "tipTr": "Şarj redresörlerinde AC besleme kesildiğinde akünün şarj cihazı üzerinden deşarj olmasını önleyen ters akım korumasını kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6.2",
        "sectionId": "Pt C, Ch 2, Sec 7",
        "page": 2081,
        "titleEn": "Functional tests — regulation, charging modes, seamless transfer & alarms (Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6.2)",
        "detailEn": "- For Battery Chargers (Tab. 1 No. 2): Current and voltage regulation, quick, slow, floating charge, and alarms.\n- For UPS ([3.6.2] & [3.3.5]): Functionality including operation of audible/visual alarms for: a) power supply failure (voltage/freq outside limits), b) earth fault in battery circuit, c) operation of battery protective device, d) when battery is being discharged, e) when bypass is in operation for on-line UPS. Verify unbreakable supply upon input power failure.",
        "titleTr": "Fonksiyon testleri — regülasyon, şarj modları, kesintisiz geçiş ve alarmlar (Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6.2)",
        "detailTr": "- Akü Şarj Cihazları (Tablo 1 No. 2): Akım/gerilim regülasyonu, hızlı (boost), yavaş ve tampon (floating) şarj modları ile şarj arıza alarmları.\n- UPS ([3.6.2] & [3.3.5]): Şebeke kesintisinde kesintisiz (without break) aküye geçiş, statik bypass geçişi ve şu alarmların doğrulanması: a) şebeke arızası, b) batarya devresi toprak kaçağı, c) batarya koruma açması, d) batarya deşarjda uyarısı, e) online UPS bypass'ta uyarısı.",
        "tipTr": "Şebeke giriş şalterini yük altında açtırarak çıkışta kesinti olmadığını (osiloskop veya yük sürekliliği ile) ve tekrar şebeke geldiğinde hem yükü besleyip hem aküyü şarj edebildiğini ([3.5.3]) doğrulayın.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 2 Sec. 7 Par. 3.6.2",
        "sectionId": "Pt C, Ch 2, Sec 7",
        "page": 2081,
        "titleEn": "Battery capacity and ventilation rate verification (Part. C Ch. 2 Sec. 7 Par. 3.5 & 3.6.2)",
        "detailEn": "For UPS units ([3.6.2]): Verify battery capacity (capable of supplying designated loads for the time required by SOLAS II-1/42 or 43, typically 30 min or 18h) and cabinet/battery ventilation rate.",
        "titleTr": "Batarya kapasite (deşarj süresi) ve havalandırma debisi doğrulaması (Part. C Ch. 2 Sec. 7 Par. 3.5 & 3.6.2)",
        "detailTr": "UPS ünitelerinde ([3.6.2]) batarya grubunun projede belirtilen gücü SOLAS II-1/42 veya 43'te istenen süre boyunca (örn. 30 dakika) besleyebildiği ve kabin havalandırma oranının uygunluğu doğrulanır.",
        "tipTr": "Eğer bataryalar UPS kabini içindeyse havalandırma fanı çalışmasını ve gaz birikimini önleyici tasarımı kontrol edin.",
        "condition": { "field": "equip_subtype", "equals": "ups" }
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 2 Sec. 7 Par. 2.2 & 3.6.2",
        "sectionId": "Pt C, Ch 2, Sec 7",
        "page": 2081,
        "titleEn": "Temperature rise measurement and insulation tests (Part. C Ch. 2 Sec. 7 Par. 2.2, 3.6.2 & Sec. 6)",
        "detailEn": "Verify temperature rise limits at rated load (always required for UPS survey per [3.6.2], and Type test for chargers per Tab. 1 No. 3), followed by dielectric strength (HV) test and insulation resistance measurement per Sec 6 [1.5].",
        "titleTr": "Sıcaklık artış (Temperature Rise) ölçümü ve izolasyon testleri (Part. C Ch. 2 Sec. 7 Par. 2.2, 3.6.2 & Sec. 6)",
        "detailTr": "Nominal yükte sıcaklık artış testi (UPS'lerde [3.6.2] gereği, şarj cihazlarında tip testinde Tablo 1 No.3 gereği) yapılır; ardından Sec 6 [1.5] uyarınca yüksek gerilim (dielektrik) ve Megger izolasyon direnci ölçümü gerçekleştirilir.",
        "tipTr": "Trafolu UPS ve redresörlerde hem giriş/çıkış devrelerinin gövdeye karşı hem de primer-sekonder arasındaki izolasyonunu ölçtürün.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "electric-cables",
    "code": "EL-06",
    "category": "electrical",
    "categoryTitleEn": "Part C, Ch 2 — Electrical Installations",
    "categoryTitleTr": "Part C, Ch 2 — Elektrik Sistemleri",
    "titleEn": "Electric Power, Control & Electrical Propulsion Cables",
    "titleTr": "Gemi Elektrik Güç, Kumanda ve Elektrikli Tahrik (Propulsion) Kabloları",
    "ruleRef": "Part. C - Ch. 2 - Sec. 9",
    "sectionId": "Pt C, Ch 2, Sec 9",
    "pdfPage": 2090,
    "keywords": ["cable", "electric cable", "kablo", "gemi kablosu", "marine cable", "propulsion cable", "fire resistant cable", "flame retardant", "iec 60092-350", "iec 60332", "iec 60331", "sec 9"],
    "applicationTerms": [
      {
        "id": "cable_service",
        "questionEn": "Are the cables intended for electrical propulsion systems or general shipboard power/control/instrumentation? ([2.2.5])",
        "questionTr": "Kablolar elektrikli ana tahrik (electrical propulsion) sistemi için mi yoksa genel gemi güç/kumanda devreleri için mi? ([2.2.5])",
        "options": [
          { "value": "propulsion", "labelEn": "Power cables for electrical propulsion systems — Surveyor Attendance Mandatory ([2.2.5])", "labelTr": "Elektrikli Tahrik (Propulsion) Güç Kablosu — Sörveyör Katılımı Zorunlu ([2.2.5])" },
          { "value": "general", "labelEn": "General shipboard power, lighting & control cables — Routine & Type Tests ([2.1] & [2.2])", "labelTr": "Genel Gemi Güç ve Kumanda Kabloları — Rutin ve Tip Testleri ([2.1] & [2.2])" }
        ],
        "default": "propulsion"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 2 Sec. 9 Par. 1",
        "sectionId": "Pt C, Ch 2, Sec 9",
        "page": 2090,
        "reqEn": "Constructional requirements, insulating/sheathing materials (Tab. 1), flame retardancy (IEC 60332-1 / 60332-3 Cat A), fire resistance (IEC 60331) and identification marking ([1.6])",
        "reqTr": "Yapısal gereksinimler, yalıtım/kılıf malzemeleri (Tablo 1), alev yaymama (IEC 60332-1 / 60332-3 Kat A), yangına dayanım (IEC 60331) ve kılıf markalaması ([1.6])"
      },
      {
        "ruleRef": "Part. C Ch. 2 Sec. 9 Par. 2",
        "sectionId": "Pt C, Ch 2, Sec 9",
        "page": 2091,
        "reqEn": "Type tests ([2.1]) and Routine tests on every length of finished cable ([2.2]) per IEC 60092-350",
        "reqTr": "IEC 60092-350 uyarınca Tip testleri ([2.1]) ve her bitmiş kablo boyunda yapılan Rutin testler ([2.2])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 2 Sec. 15",
        "sectionId": "Pt C, Ch 2, Sec 15",
        "page": 2126,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify valid calibration certificates of Kelvin/Wheatstone resistance bridge, HV test set, megger, and micrometer/optical profile projector.",
        "titleTr": "Testte kullanılan ölçüm cihazlarının kalibrasyon durumu ve uygunluğunun doğrulanması.",
        "detailTr": "Kelvin direnç köprüsü, Yüksek Gerilim test sistemi, Megger ve et kalınlığı ölçüm cihazlarının kalibrasyonlarını doğrulayın.",
        "tipTr": "İletken direnci ölçümünde kablo sıcaklığını ölçen termometrenin kalibrasyonunu ve 20°C'ye sıcaklık düzeltme katsayısını kontrol edin.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 2 Sec. 9 Par. 1.6 & 2.2.2 a), e)",
        "sectionId": "Pt C, Ch 2, Sec 9",
        "page": 2091,
        "titleEn": "Visual inspection, identification marking check and dimensional checks (Part. C Ch. 2 Sec. 9 Par. 1.6 & 2.2.2)",
        "detailEn": "Check every finished cable length for clear manufacturer identification, voltage rating, conductor cross-section, fire non-propagating standard & category (IEC 60332-3 Cat A), and fire-resisting standard (IEC 60331) where applicable. Carry out dimensional checks of insulation and sheath thickness.",
        "titleTr": "Görsel muayene, kablo kılıf markalaması ve boyut/et kalınlığı kontrolleri (Part. C Ch. 2 Sec. 9 Par. 1.6 & 2.2.2)",
        "detailTr": "Kablo dış kılıfı üzerinde üretici adı, gerilim sınıfı (örn. 0.6/1 kV), kesit, IEC 60332-3 Cat A (alev yaymaz) ve varsa IEC 60331 (yangına dayanıklı / FE180) markalaması ile RINA Tip Onay Sertifikası (TAC) kontrol edilir. İzolasyon (XLPE/EPR) ve dış kılıf (SHF1/SHF2) kalınlıkları ölçülür.",
        "tipTr": "Halojensiz (HF / Low Smoke Zero Halogen) kablolarda kılıf kodunun (SHF1 veya SHF2) onaylı sertifika ile birebir uyumlu olduğunu doğrulayın.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 2 Sec. 9 Par. 2.2.2 b)",
        "sectionId": "Pt C, Ch 2, Sec 9",
        "page": 2091,
        "titleEn": "Check of conductor cross-sectional area by measuring electrical resistance (Part. C Ch. 2 Sec. 9 Par. 2.2.2 b)",
        "detailEn": "Measure DC electrical resistance of every conductor per IEC 60092-350 and IEC 60228 corrected to 20°C and 1 km length.",
        "titleTr": "Elektriksel direnç ölçümü ile iletken kesit alanının kontrolü (Part. C Ch. 2 Sec. 9 Par. 2.2.2 b)",
        "detailTr": "Her bir damarın DC iletken direnci ölçülerek 20°C sıcaklığa ve 1 km uzunluğa indirgenir (Ω/km); IEC 60228'deki maksimum direnç sınırını aşmadığı doğrulanır.",
        "tipTr": "Kalaylı (tinned) bakır iletkenler ile çıplak (plain) bakır iletkenlerin IEC 60228'deki maksimum direnç tabloları birbirinden farklıdır; doğru sütuna bakın.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 2 Sec. 9 Par. 2.2.2 c) & 2.2.5 a)",
        "sectionId": "Pt C, Ch 2, Sec 9",
        "page": 2091,
        "titleEn": "High voltage test on finished cable lengths (Part. C Ch. 2 Sec. 9 Par. 2.2.2 c & 2.2.5 a)",
        "detailEn": "Carry out high voltage dielectric test on every length of finished cable in accordance with IEC 60092-350 (typically 3.5 kV AC for 5 min on 0.6/1 kV cables, or per rated voltage U0/U for MV propulsion cables) without breakdown.",
        "titleTr": "Bitmiş kablo boylarında yüksek gerilim (High Voltage) testi (Part. C Ch. 2 Sec. 9 Par. 2.2.2 c & 2.2.5 a)",
        "detailTr": "Bitmiş her kablo makarası/boyu üzerinde IEC 60092-350'ye göre yüksek gerilim testi (0.6/1 kV kablolarda genellikle 3500 V AC / 5 dakika; orta gerilim tahrik kablolarında beyan edilen U0/U gerilimine göre) delinme olmaksızın uygulanır.",
        "tipTr": "Elektrikli tahrik (propulsion) güç kablolarında bu testin sörveyör huzurunda yapılması zorunludur ([2.2.5]).",
        "condition": "always"
      },
      {
        "num": 5,
        "ruleRef": "Part. C Ch. 2 Sec. 9 Par. 2.2.2 d) & 2.2.5 b)",
        "sectionId": "Pt C, Ch 2, Sec 9",
        "page": 2091,
        "titleEn": "Insulation resistance measurement (Part. C Ch. 2 Sec. 9 Par. 2.2.2 d & 2.2.5 b)",
        "detailEn": "Measure insulation resistance of each core per IEC 60092-350 and calculate volume resistivity / insulation constant Ki (MΩ·km) at 20°C.",
        "titleTr": "İzolasyon direnci ölçümü (Part. C Ch. 2 Sec. 9 Par. 2.2.2 d & 2.2.5 b)",
        "detailTr": "Yüksek gerilim testinin ardından her damarın izolasyon direnci ölçülerek 1 km uzunluk için MΩ·km değeri hesaplanır ve IEC 60092-350/353 minimum sınırının üzerinde olduğu doğrulanır.",
        "tipTr": "Ölçülen direnci makara uzunluğu (km) ile çarparak MΩ·km değerini kontrol edin.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "automation-alarm-monitoring-fat",
    "code": "AU-01",
    "category": "automation",
    "categoryTitleEn": "Part C, Ch 3 — Automation & Cyber Resilience",
    "categoryTitleTr": "Part C, Ch 3 — Otomasyon ve Siber Güvenlik",
    "titleEn": "Automation, Alarm & Monitoring (AMS), PMS and Computer-Based Control Systems (FAT)",
    "titleTr": "Otomasyon, Alarm ve İzleme (AMS/IAS), Güç Yönetimi (PMS) ve Bilgisayar Tabanlı Kontrol Sistemleri (FAT)",
    "ruleRef": "Part. C - Ch. 3 - Sec. 8 & Sec. 3",
    "sectionId": "Pt C, Ch 3, Sec 8",
    "pdfPage": 2235,
    "keywords": ["automation", "ams", "ias", "alarm monitoring", "pms", "power management", "plc", "scada", "computer based system", "cbs", "otomasyon", "alarm izleme", "uzaktan kontrol", "sec 8", "sec 3"],
    "applicationTerms": [
      {
        "id": "cbs_category",
        "questionEn": "What is the Computer-Based System (CBS) category according to Part C, Ch 3, Sec 3 [1.3]?",
        "questionTr": "Part C, Ch 3, Sec 3 [1.3]'e göre Bilgisayar Tabanlı Sistemin (CBS) kategorisi nedir?",
        "options": [
          { "value": "cat_II_III", "labelEn": "Category II or III (Failure causes dangerous situation / essential propulsion, steering, safety)", "labelTr": "Kategori II veya III (Esas servis, ana tahrik, dümen, PMS, güvenlik/shutdown sistemleri)" },
          { "value": "cat_I", "labelEn": "Category I (Failure will not lead to dangerous situation)", "labelTr": "Kategori I (Arızası tehlikeli duruma yol açmayan genel izleme sistemleri)" }
        ],
        "default": "cat_II_III"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 3 Sec. 2 & Sec. 3",
        "sectionId": "Pt C, Ch 3, Sec 3",
        "page": 2166,
        "reqEn": "Design requirements, fail-safe principle, power supply redundancy, and Computer-Based Systems (CBS) software/hardware lifecycle",
        "reqTr": "Tasarım kuralları, arıza-güvenli (fail-safe) prensibi, çift besleme yedekliliği ve Bilgisayar Tabanlı Sistem (CBS) donanım/yazılım gereksinimleri"
      },
      {
        "ruleRef": "Part. C Ch. 3 Sec. 8 Par. 2 & 3",
        "sectionId": "Pt C, Ch 3, Sec 8",
        "page": 2246,
        "reqEn": "Type approval ([2]) and Factory Acceptance Testing (FAT) of hardware ([3.2]) and application software ([3.3])",
        "reqTr": "Tip onayı ([2]) ile donanım ([3.2]) ve uygulama yazılımının ([3.3]) Fabrika Kabul Testleri (FAT)"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "General / Pt C Ch. 3 Sec. 8",
        "sectionId": "Pt C, Ch 3, Sec 8",
        "page": 2235,
        "titleEn": "The calibration status and adequacy of the test measurements devices used have been satisfactorily verified.",
        "detailEn": "Verify calibration certificates of loop calibrators (4-20mA / PT100 / RTD simulators), multimeters, HV tester, and Megger.",
        "titleTr": "Testte kullanılan sinyal simülatörleri ve ölçüm cihazlarının kalibrasyon durumunun doğrulanması.",
        "detailTr": "4-20 mA / PT100 proses kalibratörü, multimetre, Hi-Pot ve Megger cihazlarının kalibrasyon sertifikalarını doğrulayın.",
        "tipTr": "Analog kanal doğruluk testlerinde kullanılan sinyal jeneratörünün kalibrasyonu kritik önemdedir.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 3 Sec. 8 Par. 3.2.1 & 3.2.2",
        "sectionId": "Pt C, Ch 3, Sec 8",
        "page": 2246,
        "titleEn": "Visual inspection, Type Approval Certificate verification and hardware configuration check (Part. C Ch. 3 Sec. 8 Par. 3.2)",
        "detailEn": "Verify compliance of PLC racks, I/O modules, power supplies, network switches, and HMI workstations with approved drawings, hardware BOM, and valid RINA Type Approval Certificates ([3.2.2]).",
        "titleTr": "Görsel muayene, Tip Onay Sertifikalarının (TAC) ve donanım konfigürasyonunun doğrulanması (Part. C Ch. 3 Sec. 8 Par. 3.2)",
        "detailTr": "PLC modülleri, I/O kartları, güç kaynakları, endüstriyel ethernet switch'ler ve operatör istasyonlarının (HMI) onaylı sistem mimarisine, malzeme listesine (BOM) ve geçerli RINA Tip Onay Sertifikalarına ([3.2.2]) uygunluğu kontrol edilir.",
        "tipTr": "PLC CPU ve I/O modüllerinin donanım/firmware versiyonlarının RINA Tip Onay Sertifikasında (TAC) listelenen versiyonlarla uyumlu olduğunu kontrol edin.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 3 Sec. 8 Par. 3.2.1",
        "sectionId": "Pt C, Ch 3, Sec 8",
        "page": 2246,
        "titleEn": "Hardware operational tests — Sensors, actuators, indicators, HV & insulation test (Part. C Ch. 3 Sec. 8 Par. 3.2.1)",
        "detailEn": "Per [3.2.1], verify:\n- All alarm and safety functions (audible/visual alarm, acknowledge, mute, flickering-to-steady light)\n- Analogue sensors/inputs (range, calibration, 4-20mA / PT100 accuracy, wire-break / short-circuit sensor fault alarm)\n- On/off sensors (set points, time delays)\n- Actuators & indicating instruments\n- High voltage test & insulation resistance measurement (and hydrostatic test if pressure enclosures are included).",
        "titleTr": "Donanım çalışma testleri — Analog/Dijital I/O, sensör hatası, alarm/güvenlik fonksiyonları ve YG testi (Part. C Ch. 3 Sec. 8 Par. 3.2.1)",
        "detailTr": "[3.2.1] uyarınca:\n- Tüm alarm ve emniyet (safety/shutdown) fonksiyonları\n- Analog girişlerin ölçüm aralığı, kalibrasyonu ve kablo kopuk/kısa devre (wire-break / <4mA / >20mA) arıza alarmları\n- Dijital (on/off) kanalların set değerleri ve gecikme süreleri\n- Aktüatör ve göstergelerin tepki süreleri\n- Pano yüksek gerilim ve izolasyon direnci testleri gerçekleştirilir.",
        "tipTr": "Rastgele seçilen analog I/O kanallarında klemensi sökerek 'Sensor Fault / Wire Break' alarmının ana alarm sisteminden farklı/ayırt edilebilir şekilde geldiğini doğrulayın.",
        "condition": "always"
      },
      {
        "num": 4,
        "ruleRef": "Part. C Ch. 3 Sec. 8 Par. 3.3 & Sec. 3 Par. 9",
        "sectionId": "Pt C, Ch 3, Sec 8",
        "page": 2246,
        "titleEn": "Application software module, integration and single-failure / redundancy functional test (Part. C Ch. 3 Sec. 8 Par. 3.3)",
        "detailEn": "Per [3.3.1] - [3.3.3]: Verify that software modules of the application software are tested individually and subjected to an integration test against the approved FAT protocol and Cause & Effect (C&E) matrix. Verify power supply changeover without loss of data/control, network redundancy (ring break test), and Watchdog / CPU failover alarm.",
        "titleTr": "Uygulama yazılımı entegrasyon, yedeklilik (Redundancy) ve tekil arıza (Single-Failure) testleri (Part. C Ch. 3 Sec. 8 Par. 3.3)",
        "detailTr": "Uygulama yazılımı modülleri onaylı FAT prosedürü ve I/O / Cause & Effect (Sebep-Sonuç) listesine göre entegrasyon testine tabi tutulur ([3.3.2]). Ana/yedek (Main/Standby) 24V DC besleme kesintisinde kesintisiz geçiş, yedekli ağ (network ring) kablosu çekildiğinde haberleşmenin kopmaması ve CPU/Watchdog arıza alarmları doğrulanır.",
        "tipTr": "Onaylı yazılım versiyon numarasının (Software Version / Checksum) HMI ekranından okunabildiğini ve FAT raporuna kaydedildiğini doğrulayın.",
        "condition": "always"
      }
    ]
  },
  {
    "id": "cyber-resilience-cbs-ur-e27",
    "code": "AU-02",
    "category": "automation",
    "categoryTitleEn": "Part C, Ch 3 — Automation & Cyber Resilience",
    "categoryTitleTr": "Part C, Ch 3 — Otomasyon ve Siber Güvenlik",
    "titleEn": "Cyber Resilience of On-Board Systems and Equipment (IACS UR E27 FAT)",
    "titleTr": "Gemi Sistem ve Ekipmanlarının Siber Dayanıklılık Fabrika Kabul Testi (IACS UR E27 FAT)",
    "ruleRef": "Part. C - Ch. 3 - Sec. 5",
    "sectionId": "Pt C, Ch 3, Sec 5",
    "pdfPage": 2216,
    "keywords": ["cyber", "cyber resilience", "siber", "siber güvenlik", "ur e27", "iacs ur e27", "cbs", "security capabilities", "sec 5", "firewall", "network"],
    "applicationTerms": [
      {
        "id": "has_tac_e27",
        "questionEn": "Does the Computer-Based System (CBS) hold a valid Type Approval Certificate specifically covering Part C, Ch 3, Sec 5 (IACS UR E27)? ([6.3.1])",
        "questionTr": "Bilgisayar Tabanlı Sistem (CBS), Part C, Ch 3, Sec 5 (IACS UR E27) gereksinimlerini kapsayan geçerli bir Tip Onay Sertifikasına sahip mi? ([6.3.1])",
        "options": [
          { "value": "No", "labelEn": "No (Full vessel-specific UR E27 Survey & FAT required per [6.3])", "labelTr": "Hayır (Gemiye özel tam kapsamlı UR E27 Sörvey ve FAT zorunlu — [6.3])" },
          { "value": "Yes", "labelEn": "Yes (Reduced document submission per Tab. 3 & verification of ship-specific configuration [6.3.4])", "labelTr": "Evet (Tablo 3 azaltılmış doküman ve gemiye özel güvenlik konfigürasyonu doğrulaması)" }
        ],
        "default": "No"
      }
    ],
    "acceptanceRequirements": [
      {
        "ruleRef": "Part. C Ch. 3 Sec. 5 Par. 3 & 4",
        "sectionId": "Pt C, Ch 3, Sec 5",
        "page": 2218,
        "reqEn": "Required security capabilities (Tab. 1 — IEC 62443-3-3 SL-C) and secure development lifecycle requirements",
        "reqTr": "Zorunlu siber güvenlik yetenekleri (Tablo 1 — IEC 62443-3-3) ve güvenli yazılım/donanım geliştirme yaşam döngüsü"
      },
      {
        "ruleRef": "Part. C Ch. 3 Sec. 5 Par. 6.3",
        "sectionId": "Pt C, Ch 3, Sec 5",
        "page": 2227,
        "reqEn": "Survey and Factory Acceptance Test (FAT) at supplier's premises ([6.3.1] to [6.3.4])",
        "reqTr": "Üretici tesislerinde Siber Güvenlik Sörveyi ve Fabrika Kabul Testi ([6.3.1] - [6.3.4])"
      }
    ],
    "certificationActivities": [
      {
        "num": 1,
        "ruleRef": "Part. C Ch. 3 Sec. 5 Par. 6.3.2",
        "sectionId": "Pt C, Ch 3, Sec 5",
        "page": 2227,
        "titleEn": "General survey items — Verification of asset inventory and topology diagrams (Part. C Ch. 3 Sec. 5 Par. 6.3.2)",
        "detailEn": "Inspect the CBS to be delivered and compare its hardware/software components, OS/firmware versions, ports, and network arrangement/architecture with the approved Asset Inventory ([3.1.2]) and Topology Diagrams ([3.1.3]).",
        "titleTr": "Varlık envanteri (Asset Inventory) ve ağ topoloji diyagramlarının doğrulanması (Part. C Ch. 3 Sec. 5 Par. 6.3.2)",
        "detailTr": "Teslim edilecek sistem fiziksel ve yazılımsal olarak incelenerek; donanım bileşenleri, işletim sistemi/firmware versiyonları, açık portlar ve ağ mimarisinin onaylı Varlık Envanteri ([3.1.2]) ve Topoloji Diyagramları ([3.1.3]) ile birebir örtüştüğü doğrulanır.",
        "tipTr": "Onaylı envanterde yer almayan hiçbir ekstra switch, kablosuz modül (Wi-Fi/4G) veya yazılım paketi sistemde bulunmamalıdır.",
        "condition": "always"
      },
      {
        "num": 2,
        "ruleRef": "Part. C Ch. 3 Sec. 5 Par. 6.3.3",
        "sectionId": "Pt C, Ch 3, Sec 5",
        "page": 2227,
        "titleEn": "Test of security capabilities per approved test procedure (Part. C Ch. 3 Sec. 5 Par. 6.3.3 & Tab. 1)",
        "detailEn": "Witness testing of the 31 required security capabilities (Tab. 1) in accordance with the approved test procedure ([3.1.5]), including: human user identification & authentication, account management, unsuccessful login attempts limit, least privilege access control, session lock, audit event logging & storage, malicious code protection,禁用/blocking of unused physical & logical ports, and deterministic output / DoS protection.",
        "titleTr": "Onaylı test prosedürüne göre siber güvenlik yeteneklerinin (Tablo 1) test edilmesi (Part. C Ch. 3 Sec. 5 Par. 6.3.3)",
        "detailTr": "Onaylı UR E27 FAT prosedürüne ([3.1.5]) göre Tablo 1'deki güvenlik yetenekleri test edilir: Kullanıcı kimlik doğrulama ve parola politikası, hatalı giriş kilitlemesi, yetki kısıtlaması (Least Privilege), otomatik oturum kilitleme, güvenlik olay kayıtları (Audit Logs), kötücül yazılım (Malware/USB) koruması, kullanılmayan fiziksel/mantıksal portların kapatılması ve ağ taşması (DoS) altında sistemin güvenli durumda kalması.",
        "tipTr": "Rastgele bir USB bellek takarak veya yetkisiz bir hesapla parametre değiştirmeyi deneyerek erişimin engellendiğini ve Audit Log'a kaydedildiğini bizzat görün.",
        "condition": "always"
      },
      {
        "num": 3,
        "ruleRef": "Part. C Ch. 3 Sec. 5 Par. 6.3.4",
        "sectionId": "Pt C, Ch 3, Sec 5",
        "page": 2227,
        "titleEn": "Verification of correct configuration of security capabilities (Part. C Ch. 3 Sec. 5 Par. 6.3.4)",
        "detailEn": "Verify that security settings in the system's components have been configured in accordance with the configuration guidelines ([3.1.6]) and documented in a ship-specific configuration report.",
        "titleTr": "Gemiye özel siber güvenlik konfigürasyon ayarlarının doğrulanması (Part. C Ch. 3 Sec. 5 Par. 6.3.4)",
        "detailTr": "Sistem bileşenlerindeki güvenlik ayarlarının (varsayılan şifrelerin değiştirilmesi, firewall kuralları, açık/kapalı servisler) onaylı konfigürasyon kılavuzuna ([3.1.6]) göre yapılandırıldığı ve gemiye özel raporda dokümante edildiği doğrulanır.",
        "tipTr": "Fabrika varsayılan (default) kullanıcı adı/şifrelerinin (örn. admin/admin) bırakılmadığını mutlaka kontrol edin.",
        "condition": "always"
      }
    ]
  }
]

with open("public/data/part1.json", "w", encoding="utf-8") as f:
    json.dump(part1_items, f, ensure_ascii=False, indent=2)

print("Part 1 items written:", len(part1_items))
