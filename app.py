import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Bare Beauty Botanicals", page_icon="🌿", layout="centered")

st.markdown("""
<style>
.main-title {font-size:30px; font-weight:800; color:#1B5E20; text-align:center;}
.card {background: white; padding:16px; border-radius:14px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left:5px solid #4CAF50; margin:10px 0; color:#212121!important;}
.alert-card {background:#FFF3E0; border-left:5px solid #FF9800; padding:14px; border-radius:10px; color:#212121!important;}
.frost-card {background:#FFEBEE; border-left:5px solid #D32F2F; padding:14px; border-radius:10px; color:#212121!important;}
.success-card {background:#E8F5E9; border-left:5px solid #2E7D32; padding:14px; border-radius:10px; color:#212121!important;}
</style>
""", unsafe_allow_html=True)

# --- ALL 9 PROVINCES DATA ---
PROVINCES = {
    "Eastern Cape - Matatiele": {"city": "Matatiele", "crops": ["Aloe Ferox (South 100)", "Lemongrass (East 70m)", "Moringa (Center 100)", "Spekboom (West North 50)", "Maize", "Cabbage"]},
    "KwaZulu-Natal": {"city": "Durban", "crops": ["Sugarcane", "Aloe Ferox", "Moringa", "Lemongrass", "Amadumbe", "Bananas"]},
    "Free State": {"city": "Bloemfontein", "crops": ["Maize", "Sunflower", "Wheat", "Potatoes", "Spekboom"]},
    "Gauteng": {"city": "Johannesburg", "crops": ["Vegetables", "Moringa (greenhouse)", "Herbs", "Tomatoes"]},
    "Limpopo": {"city": "Polokwane", "crops": ["Moringa", "Mangoes", "Avocado", "Tomatoes", "Aloe"]},
    "Mpumalanga": {"city": "Nelspruit", "crops": ["Macadamia", "Avocado", "Sugarcane", "Lemongrass", "Moringa"]},
    "North West": {"city": "Mahikeng", "crops": ["Maize", "Sunflower", "Spekboom", "Aloe Ferox"]},
    "Northern Cape": {"city": "Kimberley", "crops": ["Grapes", "Dates", "Aloe Ferox", "Spekboom (drought resistant)"]},
    "Western Cape": {"city": "Cape Town", "crops": ["Grapes", "Rooibos", "Aloe Ferox", "Lavender", "Lemongrass"]}
}

st.markdown('<div class="main-title">🌿 Bare Beauty Botanicals</div>', unsafe_allow_html=True)

# Province selector
province = st.selectbox("📍 Select Province / Farm Location", list(PROVINCES.keys()), index=0)
city = PROVINCES[province]["city"]
crops_list = PROVINCES[province]["crops"]

st.caption(f"{datetime.now().strftime('%d %B %Y %H:%M')} | {province} | Weather city: {city}")
st.markdown(f'<div class="card"><b>{province} grows:</b><br>{" • ".join(crops_list)}</div>', unsafe_allow_html=True)

# --- WEATHER + ALERTS ---
st.markdown("### 🌦️ Live Weather & Solutions")

tmin_val = 99
try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url, timeout=10).json()
    temp = data['main']['temp']
    tmin = data['main']['temp_min']
    tmax = data['main']['temp_max']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    desc = data['weather'][0]['description'].title()

    tmin_val = tmin
    col1, col2, col3 = st.columns(3)
    col1.metric("Now", f"{temp}°C", desc)
    col2.metric("Low Tonight", f"{tmin}°C")
    col3.metric("High", f"{tmax}°C")
    st.caption(f"Humidity {humidity}% | Wind {wind} m/s | {city}")

    if tmin <= 2:
        st.markdown(f'<div class="frost-card"><b>🚨 FROST {tmin}°C - {province}</b><br><b>Solution:</b><br>1. Cover Moringa with bottle<br>2. Cover Lemongrass with grass+plastic<br>3. Water Spekboom+Aloe 6AM only<br>4. Harvest leaves TODAY<br><b>Crops at risk:</b> {", ".join(crops_list[:3])}</div>', unsafe_allow_html=True)
    elif tmin <= 5:
        st.markdown(f'<div class="alert-card"><b>⚠️ COLD {tmin}°C</b><br>Solution: Cover young Moringa seedlings in {province}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="success-card"><b>✅ No Frost {tmin}°C - Safe for {province}</b></div>', unsafe_allow_html=True)

    if tmax >= 32:
        st.markdown(f'<div class="frost-card"><b>🥵 HEAT {tmax}°C</b><br>Solution: Water 6AM Aloe 5L, Moringa 3L, mulch</div>', unsafe_allow_html=True)
    if humidity < 35:
        st.markdown(f'<div class="alert-card"><b>🏜️ DROUGHT {humidity}%</b><br>Solution: Grey water for Aloe, stones in soil</div>', unsafe_allow_html=True)
    if wind > 8:
        st.markdown(f'<div class="alert-card"><b>💨 WIND {wind} m/s</b><br>Solution: Support Moringa with sticks</div>', unsafe_allow_html=True)

except Exception as e:
    st.error(f"Weather error: {e}")

# --- TELEGRAM TEST ---
st.markdown("### 📲 Telegram (already working)")
if st.button("🔔 Test Telegram Now"):
    try:
        BOT_TOKEN = st.secrets["BOT_TOKEN"]
        CHAT_ID = st.secrets["CHAT_ID"]
        msg = f"🌿 {province} Test {datetime.now().strftime('%H:%M')} - Low {tmin_val}C - Crops: {', '.join(crops_list[:2])} - Alert working!"
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": msg}, timeout=10)
        st.success("✅ Sent! Check phone Telegram")
        st.balloons()
    except:
        st.error("Add BOT_TOKEN + CHAT_ID in Streamlit Secrets")

st.divider()
st.markdown("### 🗺️ Your Matatiele Farm Map")
st.markdown('<div class="card"><b>South 100</b> - Aloe Ferox<br><b>East 70m</b> - Lemongrass<br><b>West North 50</b> - Spekboom<br><b>Center 100</b> - Moringa</div>', unsafe_allow_html=True)

st.markdown("### 💰 Profit")
lotion = st.number_input("Lotion 200ml", value=41)
cream = st.number_input("Cream 50ml", value=100)
profit = (lotion*120 + cream*95) - (lotion*28 + cream*18)
st.metric("Profit", f"R{profit}")
