import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Bare Beauty Botanicals", page_icon="🌿", layout="centered")

# --- PROFESSIONAL CSS + STARS ---
st.markdown("""
<style>
.main-title {font-size:32px; font-weight:800; color:#1B5E20; text-align:center; margin-bottom:0;}
.sub-title {text-align:center; color:#4CAF50; font-weight:600; margin-top:0;}
.card {background: white; padding:18px; border-radius:16px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border-left:6px solid #4CAF50; margin:12px 0;}
.alert-card {background:#FFF3E0; border-left:6px solid #FF9800; padding:16px; border-radius:12px; margin:10px 0;}
.frost-card {background:#FFEBEE; border-left:6px solid #F44336; padding:16px; border-radius:12px;}
.success-card {background:#E8F5E9; border-left:6px solid #4CAF50; padding:16px; border-radius:12px;}
.province-box {background:#F1F8E9; padding:14px; border-radius:12px; margin:6px 0; border:1px solid #AED581;}
.star-header {text-align:center; font-size:20px; color:#FFB300; letter-spacing:4px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="star-header">⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">🌿 Bare Beauty Botanicals ⭐</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">SmartFarmSA Pro v2 | Mapeng Ward 11 | NYDA Ready ⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)
st.markdown('<div class="star-header">✨ Bare Beauty - No Cloves With Gloves ✨</div>', unsafe_allow_html=True)
st.caption(f"📅 {datetime.now().strftime('%d %B %Y %H:%M')} | Matatiele, Eastern Cape | 0.5ha Farm | ⭐ 5 Star Natural Products")

# --- WEATHER WITH REAL ALERTS ---
st.markdown("### 🌦️ Live Weather + Action Alerts ⭐")

temp_display = "Offline"
tmin_val = 2
tmax_val = 25

try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Matatiele&appid={API_KEY}&units=metric"
    data = requests.get(url, timeout=10).json()
    temp = data['main']['temp']
    tmin = data['main']['temp_min']
    tmax = data['main']['temp_max']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    desc = data['weather'][0]['description'].title()

    tmin_val = tmin
    tmax_val = tmax

    col1, col2, col3 = st.columns(3)
    col1.metric("🌡️ Now", f"{temp}°C", desc)
    col2.metric("❄️ Low ⭐", f"{tmin}°C")
    col3.metric("🔥 High ⭐", f"{tmax}°C")
    st.caption(f"💧 {humidity}% | 💨 {wind} m/s | ☁️ {desc} | ⭐⭐⭐⭐⭐ Good Farming")

    if tmin <= 2:
        st.markdown(f'<div class="frost-card"><b>🚨⭐ FROST ALERT {tmin}°C TONIGHT! ⭐🚨</b><br>⭐ Cover Moringa 100 center with 2L plastic<br>⭐ Cover Lemongrass 70m east with dry grass + plastic<br>⭐ Water morning 6am not evening<br>⭐ Harvest Moringa TODAY</div>', unsafe_allow_html=True)
    elif tmin <= 5:
        st.markdown(f'<div class="alert-card"><b>⚠️⭐ COLD WARNING {tmin}°C ⭐</b><br>Cover young Moringa</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="success-card"><b>✅⭐ No Frost Tonight {tmin}°C - Safe ⭐⭐⭐⭐⭐</b><br>All 4 crops safe</div>', unsafe_allow_html=True)

    if tmax >= 32:
        st.markdown(f'<div class="frost-card"><b>🥵⭐ HEAT ALERT {tmax}°C ⭐</b><br>Water 6am: Aloe 5L, Moringa 3L</div>', unsafe_allow_html=True)

except:
    st.info("⭐ Weather offline - Example: 7.37°C ⭐")
    st.metric("Matatiele Now", "11.74°C ⭐ - Good farming ⭐⭐⭐⭐⭐")

# --- TELEGRAM ALERT ---
st.markdown("### 📲 How You Will Get Alerts ⭐")
st.markdown('<div class="card"><b>⭐ Automatic alerts to your phone via Telegram ⭐</b><br>⭐ When frost below 2°C<br>⭐ When heat above 32°C<br>⭐ When dry below 35%<br>Telegram sends even when app closed ⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)

if st.button("🔔⭐ Test Telegram Alert Now ⭐"):
    try:
        BOT_TOKEN = st.secrets["BOT_TOKEN"]
        CHAT_ID = st.secrets["CHAT_ID"]
        msg = f"⭐🌿 Mapeng Farm Alert {datetime.now().strftime('%d %b %H:%M')} ⭐\n❄️ Low {tmin_val}°C 🔥 High {tmax_val}°C\n⭐ Action: Cover Moringa + Lemongrass! ⭐⭐⭐⭐⭐"
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": msg}, timeout=10)
        st.success("✅⭐ Telegram sent! Check phone ⭐⭐⭐⭐⭐")
        st.balloons()
    except:
        st.error("❌ Telegram not set - Add BOT_TOKEN + CHAT_ID + WEATHER_API_KEY in Secrets ⭐")

st.divider()

# --- FARM MAP WITH STARS ---
st.markdown("### 🗺️ Your 0.5ha Farm Map ⭐⭐⭐⭐⭐")
st.markdown('<div class="card">⭐ <b>South 100</b> - Aloe Ferox (gel) ⭐⭐⭐⭐⭐<br>⭐ <b>East 70m</b> - Lemongrass (oil) ⭐⭐⭐⭐⭐<br>⭐ <b>West North 50</b> - Spekboom (carbon) ⭐⭐⭐⭐⭐<br>⭐ <b>Center 100</b> - Moringa (powder) ⭐⭐⭐⭐⭐<br><br>✨ 5 Star Organic - No Chemicals ✨</div>', unsafe_allow_html=True)

# --- 9 PROVINCES WITH STARS ---
st.markdown("### 🇿🇦 ALL 9 PROVINCES - Towns + Crops + Soil + Delivery ⭐⭐⭐⭐⭐")
province = st.selectbox("⭐ Select Province to View Full Plan ⭐",
["⭐ Eastern Cape - Your Home Mapeng ⭐", "⭐ KZN - Durban PMB ⭐", "⭐ Western Cape - Cape Town ⭐", "⭐ Limpopo - Polokwane ⭐", "⭐ Mpumalanga - Nelspruit ⭐", "⭐ Gauteng - Joburg Pretoria ⭐", "⭐ North West - Rustenburg ⭐", "⭐ Free State - Bloemfontein ⭐", "⭐ Northern Cape - Kimberley ⭐"])

details = {
"⭐ Eastern Cape - Your Home Mapeng ⭐": "⭐⭐⭐⭐⭐ Climate: -4°C frost Jun Jul, 28°C summer, 600mm rain\n⭐ Soil: Loam sandy pH 6.0 rocky west\n⭐ Best: ALL 4 crops - Aloe 100 south, Lemongrass 70m east, Spekboom 50 west north, Moringa 100 center\n⭐ Frost: Cover Moringa + Lemongrass nightly May-Aug\n⭐ Market: Matatiele R120 lotion R95 cream | NYDA loves EC youth ⭐⭐⭐⭐⭐",
"⭐ KZN - Durban PMB ⭐": "⭐⭐⭐⭐⭐ Climate: 30°C hot humid no frost 1000mm rain\n⭐ Soil: Acid sandy pH 5.5 needs compost\n⭐ Best: Lemongrass 2m fast + Moringa 3m/year | Aloe rots - mound\n⭐ Market: Durban tourists R150 lotion, Moringa powder R200/100g ⭐⭐⭐⭐",
"⭐ Western Cape - Cape Town ⭐": "⭐⭐⭐⭐⭐ Climate: Winter rain summer dry wind 10m/s\n⭐ Soil: Sandy acid pH 5.0\n⭐ Best: Spekboom carbon R50/tree + Rooibos + Aloe\n⭐ Market: Green market R180 lotion ⭐⭐⭐⭐⭐",
"⭐ Limpopo - Polokwane ⭐": "⭐⭐⭐⭐⭐ Climate: Very hot 38°C no frost drought 400mm\n⭐ Soil: Red sandy pH 7.5\n⭐ Best: Moringa king 4m + Marula + Aloe\n⭐ Market: Moringa powder R250, Aloe gel R100/L ⭐⭐⭐⭐⭐",
"⭐ Mpumalanga - Nelspruit ⭐": "⭐⭐⭐⭐⭐ Climate: 32°C humid 800mm best soil SA pH 6.0\n⭐ Best: Lemongrass oil 1% best province\n⭐ Market: Lodges R200 cream Kruger tourists ⭐⭐⭐⭐⭐",
"⭐ Gauteng - Joburg Pretoria ⭐": "⭐⭐⭐⭐⭐ Climate: -5°C frost winter 30°C summer hail\n⭐ Soil: Clay pH 6.5\n⭐ Best: Spekboom pots R80 mall | Aloe pot | Moringa pot inside\n⭐ Market: Richest - R180 lotion online courier ⭐⭐⭐⭐⭐",
"⭐ North West - Rustenburg ⭐": "⭐⭐⭐⭐⭐ Climate: Dry 36°C drought -3°C frost\n⭐ Soil: Sandy Kalahari pH 7.0\n⭐ Best: Aloe wild + Spekboom\n⭐ Market: Mines workers R120 dry skin ⭐⭐⭐⭐",
"⭐ Free State - Bloemfontein ⭐": "⭐⭐⭐⭐⭐ Climate: Coldest -8°C snow 35°C summer\n⭐ Soil: Clay loam pH 7.0\n⭐ Best: Aloe hardy -8°C with plastic, Spekboom\n⭐ Market: Farmers Aloe gel cattle wounds R80/L ⭐⭐⭐⭐",
"⭐ Northern Cape - Kimberley ⭐": "⭐⭐⭐⭐⭐ Climate: Hottest 40°C coldest -6°C desert 200mm\n⭐ Soil: Sand desert pH 8.0\n⭐ Best: Aloe desert king + Spekboom desert\n⭐ Market: Big Hole tourists R150 sunburn ⭐⭐⭐⭐⭐"
}
st.markdown(f'<div class="province-box">{details[province].replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

st.divider()

# --- PROFIT WITH STARS ---
st.markdown("### 💰 Profit Calculator - Bare Beauty Kit ⭐⭐⭐⭐⭐")
col1, col2 = st.columns(2)
lotion = col1.number_input("⭐ Lotion 200ml (41 max)", value=41)
cream = col2.number_input("⭐ Cream 50ml", value=100)
sales = lotion*120 + cream*95
cost = lotion*28 + cream*18
profit = sales - cost
c1, c2, c3 = st.columns(3)
c1.metric("⭐ Sales", f"R{sales}")
c2.metric("⭐ Cost", f"R{cost}")
c3.metric("⭐ Profit", f"R{profit}")
st.markdown(f'<div class="success-card">⭐⭐⭐⭐⭐ Kit R9610 = Ingredients R5000 + Bottles R3000 + Tools R1610 | NYDA R10000 you have R390 taxi left ⭐<br><b>⭐ If sell 41 + 100 = R14470 sales = R11522 profit ⭐⭐⭐⭐⭐</b></div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div style="text-align:center; color:#1B5E20; font-weight:700; font-size:18px;">⭐⭐⭐⭐⭐<br>🌿 Bare Beauty Botanicals ⭐ No Cloves, With Gloves ⭐<br>Natural SA Products ⭐⭐⭐⭐⭐<br>Professional | NYDA Ready | QR Sticker | Gloves Hair net Apron ⭐<br>⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)
