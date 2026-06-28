# 🤖 Telegram Döviz Botu

Python ile geliştirilmiş, anlık döviz, altın, kripto ve borsa verilerini gösteren Telegram botu.

## 🚀 Özellikler

- 💵 Anlık döviz kurları (Dolar, Euro, Sterlin)
- 🥇 Altın ve gümüş fiyatları
- ₿ Bitcoin ve BIST 100
- 🔘 Tıklanabilir buton menüsü
- 📊 Renkli değişim göstergeleri
- 💱 Tüm kurları tek komutta gösterme (/tumu)

## 🛠️ Kullanılan Teknolojiler

- Python
- python-telegram-bot
- BeautifulSoup (web scraping)
- python-dotenv (güvenli token yönetimi)

## 📦 Kurulum

```bash
pip install python-telegram-bot requests beautifulsoup4 python-dotenv
```

`.env` dosyası oluşturup BotFather'dan aldığınız token'ı ekleyin:
TOKEN=your_bot_token
Sonra çalıştırın:

```bash
python bot.py
```

## 📱 Komutlar

- `/start` - Başlangıç menüsü
- `/dolar` - Dolar kuru
- `/euro` - Euro kuru
- `/altin` - Gram altın
- `/bitcoin` - Bitcoin
- `/tumu` - Tüm kurlar
