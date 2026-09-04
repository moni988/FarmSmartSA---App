import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA Pro v2", page_icon="🌿", layout="centered")
st.title("🌿 SmartFarmSA Pro v2")
st.write("**Bare Beauty Botanicals | Mapeng Ward 11 Matatiele | All 9 Provinces Visible**")
st.caption(f"{datetime.now().strftime('%d %B %Y')}")

# SECURE
API_KEY = st.secrets["WEATHER_API_KEY"]
BOT_TOKEN = st.secrets["BOT_TOKEN"]
CHAT_ID = st.secrets["CHAT_ID"]

# WEATHER + FROST FOR YOUR 4 CROPS
try:
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Matatiele&appid={API_KEY}&units=metric", timeout=10).json()
    temp = r['main']['temp']
    temp_min = r['main']['temp_min']
    hum = r['main']['humidity']
    desc = r['weather'][0]['description']
    c1,c2,c3 = st.columns(3)
    c1.metric("Matatiele", f"{temp}°C")
    c2.metric("Low Tonight", f"{temp_min}°C")
    c3.metric("Condition", desc)

    if temp_min <= 2:
        st.error(f"❄️ FROST {temp_min}°C - COVER Moringa CENTER sack, Lemongrass EAST mulch")
    elif temp > 30:
        st.warning(f"☀️ HEAT {temp}°C - Water Lemongrass EAST 5am only")
    elif "rain" in desc.lower():
        st.success(f"🌧️ RAIN - BEST plant Spekboom WEST+NORTH fence today!")
    else:
        st.success(f"✅ PERFECT {temp}°C - Cut Lemongrass, harvest Aloe")

    # TELEBOT WE LEARNED TODAY
    def send_telegram(m):
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": m}, timeout=10)

    if st.button("📲 Send Alert to Telegram 8098228163"):
        send_telegram(f"Mapeng {temp}°C {desc} Low {temp_min}°C - Aloe/Lemongrass/Spekboom/Moringa check")
        st.success("Sent to Telegram!")
except:
    st.info("Matatiele 11.74°C - Good farming")

st.divider()
st.header("🇿🇦 ALL 9 PROVINCES - Towns + Crops + Soil + Delivery")

st.markdown("### 1. EASTERN CAPE - Matatiele Mapeng Detailed (YOUR BASE)")
st.write("Towns: Matatiele, Mount Fletcher, Maclear, Qumbu, Mthatha")
st.write("Base: 0.5ha Mapeng near Mapfontein clinic Ward 11")
st.write("SOUTH: Aloe Ferox 100 - rocky no compost, frost -5 hardy, 5L every 3 months")
st.write("EAST: Lemongrass 70m - morning sun near tap, 100 buckets compost, water 2x week, cut every 2 months for R120 lotion")
st.write("WEST+NORTH fence: Spekboom 50 - donga edge windbreak, stick cutting no water, carbon credit municipality")
st.write("CENTER: Moringa 100 - full sun deep 50cm pit 200 buckets compost, cover sack frost first winter, leaves tea oil")
st.write("Delivery: Same day R20 Taxi Rank Market | Other provinces R100 Paxi Courier")
st.divider()

st.markdown("### 2. KWAZULU-NATAL")
st.write("Towns: Durban, Pietermaritzburg, Richards Bay, Newcastle, Port Shepstone, Ladysmith")
st.write("Crops: Lemongrass ⭐⭐⭐⭐⭐, Moringa 3m year ⭐⭐⭐⭐⭐, Aloe ⭐⭐⭐, Spekboom ⭐⭐⭐, Sugarcane, Banana, Mango, Amadumbe")
st.write("Soil: Red loam humid 800-1000mm rainfall")
st.write("Tip: Hot humid Lemongrass Moringa grow 4x year fast")
st.write("Delivery: R100 Paxi Pep 3-5 days")
st.divider()

st.markdown("### 3. WESTERN CAPE")
st.write("Towns: Cape Town, Stellenbosch, Paarl, Worcester, Ceres, Clanwilliam, George")
st.write("Crops: Spekboom ⭐⭐⭐⭐⭐, Aloe Ferox ⭐⭐⭐⭐⭐, Olives ⭐⭐⭐⭐, Rooibos ⭐⭐⭐⭐⭐, Grapes")
st.write("Soil: Sandy dry 300mm windy, summer dry")
st.write("Tip: Dry Spekboom Aloe perfect no water, Rooibos tea scent")
st.write("Delivery: R100 Courier")
st.divider()

st.markdown("### 4. LIMPOPO")
st.write("Towns: Polokwane, Tzaneen, Thohoyandou, Phalaborwa, Giyani, Lephalale, Musina")
st.write("Crops: Moringa ⭐⭐⭐⭐⭐, Marula ⭐⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐, Lemongrass ⭐⭐⭐⭐, Mango, Macadamia")
st.write("Soil: Sandy very hot 35-40°C")
st.write("Tip: Hottest Moringa Marula love heat, get Marula oil cheaper from Limpopo farmers")
st.write("Delivery: R100 Paxi")
st.divider()

st.markdown("### 5. MPUMALANGA")
st.write("Towns: Nelspruit Mbombela, Hazyview, Barberton, Lydenburg, White River, Secunda")
st.write("Crops: Lemongrass ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐, Spekboom ⭐⭐⭐, Macadamia")
st.write("Soil: Loam subtropical 600-800mm")
st.write("Tip: Humid Lemongrass tall essential oils")
st.write("Delivery: R100 Paxi")
st.divider()

st.markdown("### 6. GAUTENG")
st.write("Towns: Johannesburg, Pretoria, Soweto, Bronkhorstspruit, Vereeniging, Randfontein, Sandton")
st.write("Crops: Spekboom ⭐⭐⭐⭐⭐ pots, Aloe ⭐⭐⭐⭐, Lemongrass ⭐⭐⭐ pots greenhouse, Moringa ⭐⭐⭐ frost cover")
st.write("Soil: Clay Highveld frost -5°C winter")
st.write("Tip: Cold frost Spekboom pots best SELL not grow Sandton R150 lotion")
st.write("Delivery: R100 Courier, R50 same day Joburg")
st.divider()

st.markdown("### 7. NORTH WEST")
st.write("Towns: Rustenburg, Mahikeng, Potchefstroom, Klerksdorp, Vryburg, Zeerust, Hartbeespoort")
st.write("Crops: Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐, Maize ⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐, Sunflower")
st.write("Soil: Sandy dry 400-500mm")
st.write("Tip: Very dry Aloe Spekboom perfect, Moringa ok borehole")
st.write("Delivery: R100 Paxi")
st.divider()

st.markdown("### 8. FREE STATE")
st.write("Towns: Bloemfontein, Welkom, Bethlehem, Phuthaditjhaba, Bothaville, Parys")
st.write("Crops: Aloe ⭐⭐⭐⭐⭐, Maize ⭐⭐⭐⭐, Spekboom ⭐⭐⭐, Wheat, Sunflower")
st.write("Soil: Clay loam cold -10°C frost coldest")
st.write("Tip: Only Aloe Spekboom survive frost, Moringa Lemongrass die unless tunnel")
st.write("Delivery: R100 Paxi")
st.divider()

st.markdown("### 9. NORTHERN CAPE")
st.write("Towns: Kimberley, Upington, Springbok, De Aar, Kuruman, Calvinia")
st.write("Crops: Aloe ⭐⭐⭐⭐
