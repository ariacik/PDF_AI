# 📄 PDF-Bot: Qwen 2.5 Destekli Akıllı Asistan

Bu proje, kullanıcıların yüklediği PDF dosyalarını analiz eden ve içerik hakkında sorulan sorulara yapay zeka desteğiyle yanıt veren bir web uygulamasıdır. **Qwen 2.5-7B** modelini kullanarak akademik ve teknik metinlerde yüksek doğrulukla çalışır.

## 🚀 Özellikler
- **PDF Metin Çıkarma:** `pdfplumber` ile tablolar ve karmaşık metin yapılarında yüksek hassasiyet.
- **Yapay Zeka Sor-Cevap:** Hugging Face Inference API üzerinden güncel **Qwen 2.5** entegrasyonu.
- **Kullanıcı Dostu Arayüz:** `Gradio` ile modern ve hızlı web tabanlı kontrol paneli.
- **Hızlı ve Ücretsiz:** Yerel GPU gücüne ihtiyaç duymadan bulut tabanlı ücretsiz model kullanımı.

## 🛠️ Kurulum

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. **Depoyu bilgisayarınıza indirin:**
```bash
git clone https://github.com/ariacik/PDF_AI
cd pdf-bot
```

2. **Gerekli kütüphaneleri kurun:**
```bash
pip install -r requirements.txt
```


3. **API Anahtarını Ayarlayın:**
`main.py` dosyası içindeki `HF_TOKEN` değişkenine [Hugging Face](https://huggingface.co/settings/tokens) adresinden aldığınız ücretsiz token'ı yapıştırın.
4. **Uygulamayı başlatın:**
```bash
python main.py
```



## 📂 Dosya Yapısı

* `main.py`: Uygulamanın tüm mantığını ve arayüz kodlarını içerir.
* `requirements.txt`: Projenin çalışması için gerekli Python paketleri.
* `example.pdf`: Test etmek için kullanabileceğiniz örnek makale.

## 📖 Kullanım Kılavuzu

1. Uygulama açıldığında sol taraftaki panelden istediğiniz bir **PDF** dosyasını yükleyin.
2. **"Metni Çözümle"** butonuna basarak yapay zekanın metni hafızasına almasını sağlayın.
3. Sağ taraftaki kutucuğa PDF içeriğiyle ilgili sorunuzu yazın (Örn: "Bu makalede iklim değişikliğinin Türkiye üzerindeki etkileri nelerdir?").
4. **"Soruyu Sor"** butonuna basın ve yapay zekanın yanıtını bekleyin.

## ⚠️ Önemli Notlar

* Bu uygulama ücretsiz katman API kullandığı için dakikada belirli bir istek sınırına sahiptir.
* Çok büyük PDF dosyalarında (50+ sayfa) metnin tamamını göndermek yerine sistem ilk bölümlere odaklanır. Gelişmiş versiyonlar için Vektör Veritabanı (RAG) eklenmesi önerilir.

---

**Geliştiren:** Can
**Lisans:** MIT