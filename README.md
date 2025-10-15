# kovan.studio-case-todo

## Case:
<img width="2043" height="884" alt="image" src="https://github.com/user-attachments/assets/b56fccd2-faeb-437c-bfaa-a0613fd898ff" />


## Amaç
Bu uygulama, bir CV dosyası ile bir iş ilanı dosyasını karşılaştırarak adayın ilana uygunluğunu yapay zeka ile analiz eder. Sonuç olarak adayın güçlü yönleri, riskleri, yetkinlik özeti ve işe alım önerisi gibi başlıklar altında yapılandırılmış bir çıktı üretir.

## Kurulum ve Kullanım

1. `.env` dosyası oluşturun ve aşağıdaki gibi Gemini API anahtarınızı ekleyin:

	```env
	GEMINI_API_KEY=your_gemini_api_key_here
	```

2. Gerekli paketleri yükleyin:

	```bash
	pip install uv
	```

3. Uygulamayı başlatın:

	```bash
	uv run agent.py
	```

## Nasıl Çalışır?

- `cv.md` dosyasındaki aday bilgileri ile `ilan.md` dosyasındaki iş ilanı detayları alınır.
- Yapay zeka, bu iki dosyayı karşılaştırır ve adayın ilana uygunluğunu değerlendirir.
- Sonuç, JSON formatında ve başlıklar halinde ekrana yazdırılır.

Her çalıştırmada, güncel CV ve ilan dosyalarını kullanarak değerlendirme yapar.

## EXAMPLE STRUCTURED OUTPUT:
```json
{
  "score": 95,
  "strong_points": "Aday, Yapay Zeka, LLM'ler (OpenAI dahil) ve REST API'leri (FastAPI tecrübesi) konularında aranan tüm temel yetkinliklere fazlasıyla sahiptir. 5 yıllık kapsamlı deneyimi ve mekatronik mühendisliği eğitimi, hem yazılım hem de otomasyon ihtiyacını karşılamaktadır. 80'den fazla freelance projesi, işe koyulma ve öğrenme hevesini kanıtlamaktadır.",
  "risks": "Aday, aranan staj pozisyonu için tecrübe bakımından aşırı niteliklidir (Lead Engineer pozisyonu geçmişi var). 3 aylık bir staj süresi için motivasyonunu ve bağlılığını sürdürmek adına görevlerin yeterince zorlayıcı ve bağımsız olması gerekebilir. n8n/Zapier gibi spesifik otomasyon araçlarının kullanımı doğrudan belirtilmemiştir, ancak genel otomasyon deneyimi bunu telafi etmektedir.",
  "summary_of_reason": "Hamza Yeşilmen, hem teknik gereksinimleri (API, LLM) hem de aranan öğrenme/üretme merakını fazlasıyla karşılayan, mükemmel bir adaydır. Kendisi bu pozisyon için çok güçlü bir profildir ve hemen katkı sağlamaya başlayabilir.",
  "suggestion": "evet"
}
```


## WEB Arayüzü Kullanımı

Projeyi bir web arayüzü ile kullanmak için aşağıdaki adımları izleyin:

1. Web arayüzünü başlatmak için aşağıdaki komutu çalıştırın:
	```bash
	uv run mainWeb.py
	```
2. Başarılı bir şekilde başlatıldığında, terminalde yerel bir adres (ör. `http://localhost:8080`) göreceksiniz. Bu adresi tarayıcınızda açarak web arayüzüne erişebilirsiniz.

Web arayüzü üzerinden CV ve ilan dosyalarını yükleyebilir, değerlendirme sonuçlarını görsel olarak inceleyebilirsiniz. Arayüz, adayın ilana uygunluğunu ve detaylı analiz sonuçlarını kullanıcı dostu bir şekilde sunar. 

Sonuçları ise data klasöründe JSON formatında saklar.

## Başvuru:
<img width="1002" height="703" alt="image" src="https://github.com/user-attachments/assets/27293505-3691-4cbd-8a3a-9fb1c181041a" />

## Sonuç:
<img width="844" height="1390" alt="image" src="https://github.com/user-attachments/assets/b134a06c-1e68-4b11-ac07-8a713e51051f" />

## Lokal Kayıt:
<img width="1101" height="256" alt="image" src="https://github.com/user-attachments/assets/24329a18-26d6-4abe-8818-df48f1a1f6fb" />

