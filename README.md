# RINA Marine Surveyor — FAT & Certification Rules Assistant (2026 Rules)

**Canlı Uygulama (Firebase Hosting):** [https://rina-fat-surveyor.web.app](https://rina-fat-surveyor.web.app)

RINA Marine Surveyor'ların fabrika kabul testlerinde (**FAT — Factory Acceptance Tests**) ve malzeme/ekipman sertifikasyon süreçlerinde **RINA Rules 2026 (1 July 2026)** kurallarına, Leonardo TEST formatındaki **Certification Activities** adımlarına, hidrostatik/izolasyon test hesaplayıcılarına ve tam kural metinlerine **İngilizce orijinal metin + Türkçe saha açıklaması** ile saniyeler içinde erişmesini sağlayan **%100 Offline destekli PWA (Progressive Web App)** uygulamasıdır.

---

## Öne Çıkan Özellikler

1. **Leonardo TEST Formatında Sertifikasyon Akışı:**
   - **Acceptance Requirements:** Malzeme sertifikası (`3.1` / `3.2`), NDT ve boyut kontrol ön şartları.
   - **Application Terms (Uygulama Şartları):** `Yes / No` seçimleriyle (örn. *Type Test vs Routine Test*, *Design Pressure > 40 bar*) sadece o saha testinde geçerli olan adımların otomatik filtrelenmesi veya **"Tüm Adımları Göster"** modu.
   - **Certification Activities:** Her adım için resmi RINA 2026 kural metni (EN), Türkçe saha rehberi ve sörveyör ipuçları (TR), `OK` / `Ret` / `N/A` durum butonları, ölçülen değer ve saha notu girişi.

2. **Kapsanan RINA 2026 Kural Kategorileri (Part C & Part D):**
   - **Part C, Ch 1 — Machinery & Piping:** Vanalar ve fittingler (`Sec 10`), Pompalar (`Sec 10`), Esnek Hortumlar (`Sec 10`), Basınçlı Kaplar ve Eşanjörler (`Sec 3`), Kazanlar (`Sec 3`), Ana ve Yardımcı Dizel Motorlar (`Sec 2`), Şaft ve Pervane Sistemleri (`Sec 7 & 8`), Dümen Makinesi / Steering Gear (`Sec 11`), Hava Kompresörleri, Irgat ve Vinçler (`Sec 12`), Turboşarjlar (`Sec 16`), Sintine Separatörü (`Pt F`), İçten Yanmalı Motor Güvenlik Vanaları.
   - **Part C, Ch 2 — Electrical Installations:** Elektrik Motorları (`Sec 4`), Alternatörler / Jeneratörler (`Sec 4`), Güç Transformatörleri (`Sec 5`), Ana ve Acil Dağıtım Panoları / MSB & ESB (`Sec 8`), Deniz Kabloları (`Sec 9`), Akü ve UPS Sistemleri (`Sec 6`).
   - **Part C, Ch 3 — Automation & Cyber Resilience:** Otomasyon, Alarm ve PMS Panoları (`Sec 6`), Bilgisayar Tabanlı Sistemler Yazılım FAT (`Sec 3`), IACS UR E27 Siber Güvenlik FAT kontrolleri.
   - **Part C, Ch 4 — Fire Protection:** Sabit Yangın Algılama ve Söndürme Sistemleri (`CO2`, `Water Mist`, `Foam`, `Yangın Damperleri`, `A-60 Kapılar`).
   - **Part D — Metallic Materials & Welding:** Gemi Sacları (`Normal / AH36 / DH36 / EH36`), Çelik Dövmeler (`Shaft / Crankshaft Forgings`), Çelik Dökümler, Bakır Alaşımlı Pervane Dökümleri (`CU1 / CU2 / CU3 / CU4`), Çapa ve Zincirler (`Anchors & Stud Link Chain Cables`), Kaynak Prosedürü Onayı (`WPQR / WPS`).

3. **2026 RINA Rules Tam Metin Arama & Kural Görüntüleyici (1.238 Sayfa / 87 Bölüm):**
   - Kural referans rozetlerine (`Pt C, Ch 1, Sec 10, [20.5]` vb.) tıklandığında ilgili RINA 2026 PDF bölümünün tam metni ve tabloları uygulama içinden açılır.
   - Üst menüdeki **"2026 PDF Tam Arama"** penceresinden tüm Part C ve Part D bölümleri içinde kelime veya kural numarası araması yapılabilir.

4. **İnteraktif Saha Hesaplayıcıları:**
   - **Vana / Gövde ve Yuva Test Basıncı Hesaplayıcı:** $P_{\text{body}} = 1.5 \times P_d$ (min 5 bar) ve $P_{\text{seat}} = 1.1 \times P_d$
   - **Boru Devresi / Pompa / Basınçlı Kap Hidrostatik Test Hesaplayıcı**
   - **Elektrik Makinesi Yüksek Gerilim (Dielectric / Hi-Pot) Test Hesaplayıcı:** $U_{\text{test}} = 2 \times U_n + 1000\text{ V}$ (min 1500 V)
   - **Dövme / Döküm / Sac Çekme ve Charpy Darbe Enerjisi Referans Değerleri**

5. **Saha Raporu Kaydetme & PDF Çıktısı:**
   - İşlenen `OK / Ret / N/A` durumları, ölçülen değerler, iş emri numarası, üretici adı ve sörveyör notları cihaz hafızasında (`localStorage`) saklanır ve **PDF / Yazdır** butonuyla resmi kontrol listesi çıktısı alınabilir.

6. **iOS & Android PWA + %100 Offline Çalışma:**
   - iPhone / iPad (Safari -> *Paylaş* -> *Ana Ekrana Ekle*) ve Android (Chrome -> *Uygulamayı Yükle*) üzerinden tam ekran mobil uygulama olarak kurulur.
   - Service Worker önbelleklemesi sayesinde tersanede veya fabrika içinde internet çekmeyen ortamlarda tüm veritabanı ve kural metinleri çevrimdışı çalışır.
