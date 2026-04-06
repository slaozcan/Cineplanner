# 🎬 CinePlanner AI & Web Scraper

CinePlanner, sinemaseverlerin vizyondaki filmleri takip etmesini ve planlamasını kolaylaştıran interaktif bir takvim (dashboard) uygulamasıdır. 
Farklı web sitelerini ayrı ayrı gezmek yerine, anlık web kazıma (web scraping) ve `TMDB API` entegrasyonu ile en popüler güncel filmleri bulur ve şık bir takvim üzerinde plan yapmanıza olanak tanır.

![CinePlanner Ekran Görüntüsü](screenshot.png)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-000000?style=for-the-badge)
![TMDB API](https://img.shields.io/badge/TMDB_API-01B4E4?style=for-the-badge&logo=TMDB&logoColor=white)

## ✨ Özellikler

- **Anlık Veri Çekme (Web Scraping):** `BeautifulSoup` kütüphanesi kullanılarak Türkiye'nin en büyük sinema platformlarından o an vizyonda olan filmler otomatik olarak çekilir.
- **Dinamik Afişler:** Çekilen film adları temizlenerek `The Movie Database (TMDB)` API'sine gönderilir ve yüksek çözünürlüklü %100 doğru orijinal afişler arayüze eklenir.
- **İnteraktif Takvim:** Takviminize film seanslarını ekleyebilir, ay ve hafta görünümünde dilediğiniz gibi sürükleyip bırakabilirsiniz. (`streamlit-calendar` entegrasyonu).
- **Hızlı ve Modern Arayüz:** Streamlit sayesinde tamamen mobil uyumlu, karanlık (dark mode) ve modern bir kullanıcı deneyimi sunar.

## 🚀 Kurulum & Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. **Depoyu İndirin:**
   ```bash
   git clone https://github.com/KULLANICI_ADIN/cineplanner.git
   cd cineplanner
   ```

2. **Gerekli Kütüphaneleri Yükleyin:**
   ```bash
   pip install streamlit requests beautifulsoup4 python-dotenv
   ```
   *(Eğer `streamlit-calendar` kütüphanesi kurulu değilse onu da yükleyin: `pip install streamlit-calendar`)*

3. **Çevre Değişkenlerini (Environment Variables) Ayarlayın:**
   - Proje dizininde `.env` isimli bir dosya oluşturun veya `.env.example` dosyasının adını `.env` olarak değiştirin.
   - TMDB'den aldığınız ücretsiz API Anahtarınızı aşağıdaki gibi dosyaya ekleyin:
   ```env
   TMDB_API_KEY=buraya_kendi_api_keyinizi_yazın
   ```

4. **Uygulamayı Başlatın:**
   ```bash
   streamlit run main.py
   ```

## 🏗️ Mimari ve Teknolojik Yaklaşım

Projenin geliştirilme sürecinde öncelikle *LLM (Büyük Dil Modeli) ile Arama Motoru Özetlerinden Veri Çıkarımı (Hallucination AI Method)* denenmiş, ancak arama motoru özetlerinin seans verilerindeki eksikliğini doldururken AI'ın halüsinasyon görmesi problemi tespit edilmiştir. 
Bu sorunu mimari bir değişiklikle çözerek projeye **Gerçek Web Kazıma (BeautifulSoup tabanlı Scraper Engine)** eklenmiş ve %100 doğru vizyon verisi elde edilmesi sağlanmıştır.

## 📄 Lisans
Bu proje açık kaynaklıdır. Eğitim ve portfolyo amacıyla geliştirilmiştir. Küresel ve yerel sinema verileri ilgili platformların telif haklarına tabidir.
