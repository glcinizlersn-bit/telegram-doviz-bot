from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Application,CommandHandler,ContextTypes,CallbackQueryHandler
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()#env dosyasını oku 
TOKEN=os.getenv("TOKEN")#Tokeni al 




#DÖVİZ KURU ÇEKEN FONKSİYON
def  kur_cek (aranan):

    url="https://www.doviz.com"
    headers={"User-Agent":"Mozilla/5.0"}
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    dovizler=soup.find_all("div",class_="item")

    for doviz in dovizler :
        ad=doviz.find("span",class_="name").text.strip()
      
        if aranan.upper()in ad.upper():
            fiyat=doviz.find("span",class_="value").text.strip()
            #Değişim bilgisini çek
            try:
                degisim=doviz.find("div",class_="change-rate").text.strip()
            except:
                degisim="0"
            #Emoji belirle
            if degisim.startswith("%-"):
                emoji="🔴"
            else:
                emoji="🟢"
            return f"{emoji}  {ad}\n 💰{fiyat}TL \n📊 Değişim:{degisim}"
    return "Bulunamadı"

# Tüm kurları çeken fonksiyon
def tum_kurlar():
    url = "https://www.doviz.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    dovizler = soup.find_all("div", class_="item")
    
    mesaj = "💱 TÜM KURLAR\n\n"
    
    for doviz in dovizler:
        try:
            ad = doviz.find("span", class_="name").text.strip()
            fiyat = doviz.find("span", class_="value").text.strip()
            degisim = doviz.find("div", class_="change-rate").text.strip()
            
            if degisim.startswith("%-"):
                emoji = "🔴"
            else:
                emoji = "🟢"
            
            mesaj += f"{emoji} {ad}: {fiyat} ({degisim})\n"
        except:
            continue
    
    return mesaj
# /tumu komutu
async def tumu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sonuc = tum_kurlar()
    await update.message.reply_text(sonuc)
#/START KOMUTU
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    butonlar=[
        [InlineKeyboardButton("💵Dolar",callback_data="DOLAR"),
         InlineKeyboardButton("💶Euro ",callback_data="EURO")],
         [InlineKeyboardButton("💷Sterlin ",callback_data="STERLİN"),
         InlineKeyboardButton("🥇Altın",callback_data="GRAM ALTIN")],
         [InlineKeyboardButton("₿ Bitcoin", callback_data="BITCOIN")]
    ]
    klavye=InlineKeyboardMarkup(butonlar)
    await update.message.reply_text(
        "merhaba!Anlık Kur Bot'una hoş geldin !\n\nBir kura tıkla :",
        reply_markup=klavye
        )
 

 

#BUTON YIKLAMALRINI YAKALA   
async def buton_tikla(update:Update,context:ContextTypes.DEFAULT_TYPE):
    query=update.callback_query
    await query.answer()#TIKLAMAYI ONAYLA

    aranan=query.data#BUTONUN CALBACK_DATASI
    sonuc=kur_cek(aranan)
    await query.message.reply_text(sonuc)

#/dolar komutu 
async def dolar(update:Update,context:ContextTypes.DEFAULT_TYPE):
    sonuc = kur_cek("DOLAR")
    await update.message.reply_text(sonuc)

#euro komutu 
async def euro (update:Update,context:ContextTypes.DEFAULT_TYPE):
    sonuc = kur_cek("EURO")
    await update.message.reply_text(sonuc)

#altın komutu
async def altin(update:Update,context:ContextTypes.DEFAULT_TYPE):
    sonuc= kur_cek("GRAM ALTIN")
    await update.message.reply_text(sonuc)

async def bitcoin(update :Update,context:ContextTypes.DEFAULT_TYPE):
    sonuc= kur_cek("BITCOIN")
    await update.message.reply_text(sonuc)
async def sterlin (update:Update,context:ContextTypes.DEFAULT_TYPE):
    sonuc=kur_cek("STERLİN")
    await update.message.reply_text(sonuc)
#Botu başlat
app=Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("dolar",dolar))
app.add_handler(CommandHandler("euro",euro))
app.add_handler(CommandHandler("altin",altin))
app.add_handler(CommandHandler("bitcoin",bitcoin))
app.add_handler(CommandHandler("sterlin",sterlin))
app.add_handler(CallbackQueryHandler(buton_tikla))
app.add_handler(CommandHandler("tumu", tumu))



print("Bot çalışıyor...")
app.run_polling()
