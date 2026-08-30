import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA", page_icon="🌿", layout="centered")

st.title("🌿 SmartFarmSA v2")
st.write("**Built for Mapeng Ward 11 - Bare Beauty Farm**")
st.write("Check weather + What each province can grow - Matatiele base online everywhere")

# LOCATION + WEATHER WITH HIDDEN KEY
st.subheader("📍 Your Farm")
location = st.selectbox("Select Province to see tips", ["Mapeng Ward 11 (Matatiele) - Eastern Cape", "KwaZulu-Natal", "Western Cape", "Limpopo", "Mpumalanga", "Gauteng", "North West", "Free State", "Northern Cape"])
city = "Matatiele" if "Mapeng" in location or "Eastern Cape" in location else location.split(" ")[0]

try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
except:
    API_KEY = st.secrets.get("WEATHER_API_KEY", "b6a9082fddf3edfdb3c8903722f60c71")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
try:
    r = requests.get(url, timeout=10)
    data = r.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    desc = data['weather'][0]['description']
    col1, col2, col3 = st.columns(3)
    col1.metric("Temp", f"{temp}°C")
    col2.metric("Humidity", f"{humidity}%")
    col3.metric("Condition", desc)
    st.caption(f"Updated: {datetime.now().strftime('%H:%M')} - {city}")
except:
    st.warning("Weather loading... 22°C sunny Matatiele - good for Aloe")
    temp = 22
    desc = "clear"

# EACH PROVINCE WHAT THEY CAN GROW
st.divider()
st.header("🌱 Each Province - What They Can Grow")

if "Eastern Cape" in location:
    st.subheader("Eastern Cape - Matatiele Mapeng Ward 11 (Your Farm 0.5ha)")
    st.write("**Soil:** Sandy loam brown near mountain, degraded/donga near Mapfontein JSS, drains fast")
    st.write("**Base:** PTO land free, 100% youth, near Mapfontein JSS")

    st.write("**1. Aloe Ferox 100 plants - SOUTH SIDE of farm**")
    st.write("- Where: South side slope, rocky, poor soil, no compost")
    st.write("- Why Matatiele: Wild Aloe grows here, frost hardy, loves Eastern Cape cold winter -5°C to 30°C")
    st.write("- How: Holes 30cm, no water after 1 month, cut outer leaves after 6 months, 5L every 3 months free")
    st.write("- Soil tip: Degraded soil BEST, don't add dung will rot")

    st.write("**2. Lemongrass 70m row - EAST SIDE morning sun**")
    st.write("- Where: East side where morning sun comes, near compost area")
    st.write("- Why Matatiele: Needs water, Matatiele rain 600mm, summer hot")
    st.write("- How: 100 buckets compost mix, water 2x week, cut every 2 months for scent in lotion")
    st.write("- Soil tip: Rich soil, needs dung + leaves, plant after rain")

    st.write("**3. Spekboom 50 plants - WEST and NORTH fence**")
    st.write("- Where: West and North edge where wind comes, donga edge to stop erosion")
    st.write("- Why Matatiele: Municipality IDP likes Spekboom carbon credit, stops donga, survives drought")
    st.write("- How: Stick cuttings directly in ground, no water, no compost, best plant on rainy day")
    st.write("- Soil tip: Any degraded soil, holds soil, windbreak for other plants")

    st.write("**4. Moringa 100 plants - CENTER full sun**")
    st.write("- Where: Center of farm full sun, deep holes")
    st.write("- Why Matatiele: Needs protection first winter from frost, center warmest, cover with sack if frost")
    st.write("- How: 200 buckets compost, holes 50cm deep, water first 3 months, then drought tolerant")
    st.write("- Soil tip: Deep compost, full sun, leaves for tea, seeds oil for premium lotion later")

elif "KwaZulu-Natal" in location:
    st.subheader("KwaZulu-Natal - Durban, Pietermaritzburg")
    st.write("- What can grow: **Lemongrass ⭐⭐⭐⭐⭐**, Moringa ⭐⭐⭐⭐⭐, Aloe ⭐⭐⭐, Spekboom ⭐⭐⭐")
    st.write("- Soil: Red loam, humid, lots rain")
    st.write("- Tip: KZN hot humid - Lemongrass and Moringa love it, grow fast, cut 4x year. Aloe too wet - plant on mound. Spekboom less frost hardy but ok coast")
    st.write("- Market: Sell lotion in Durban - beach tourists love natural")

elif "Western Cape" in location:
    st.subheader("Western Cape - Cape Town, Stellenbosch")
    st.write("- What can grow: **Spekboom ⭐⭐⭐⭐⭐**, Aloe Ferox ⭐⭐⭐⭐⭐, Lemongrass ⭐⭐⭐, Rooibos ⭐⭐⭐⭐⭐")
    st.write("- Soil: Sandy, windy, dry summer")
    st.write("- Tip: WC dry - Spekboom and Aloe perfect, no water. Rooibos grows wild here - use for your tea water. Lemongrass needs water in summer")
    st.write("- Market: Eco shops, tourists pay R200 for lotion")

elif "Limpopo" in location:
    st.subheader("Limpopo - Polokwane, Tzaneen")
    st.write("- What can grow: **Moringa ⭐⭐⭐⭐⭐**, Marula ⭐⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐, Lemongrass ⭐⭐⭐⭐")
    st.write("- Soil: Sandy, very hot")
    st.write("- Tip: Hottest province - Moringa and Marula love heat, Marula oil from Limpopo best. Aloe ok. Water Lemongrass daily")
    st.write("- Market: Marula oil source - get oil cheaper from Limpopo farmers")

elif "Mpumalanga" in location:
    st.subheader("Mpumalanga - Nelspruit, Hazyview")
    st.write("- What can grow: **Lemongrass ⭐⭐⭐⭐⭐**, Moringa ⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐, Spekboom ⭐⭐⭐")
    st.write("- Soil: Loam, subtropical, rain")
    st.write("- Tip: Like KZN, humid - Lemongrass grows tall, Moringa fast. Aloe on slope. Good for essential oils")

elif "Gauteng" in location:
    st.subheader("Gauteng - Johannesburg, Pretoria")
    st.write("- What can grow: **Spekboom ⭐⭐⭐⭐⭐**, Aloe ⭐⭐⭐⭐, Lemongrass ⭐⭐⭐ (in pots), Moringa ⭐⭐⭐ (frost protection)")
    st.write("- Soil: Clay, Highveld frost -5°C winter")
    st.write("- Tip: Gauteng cold winter - Spekboom in pots, Aloe frost hardy. Lemongrass and Moringa need greenhouse or cover winter. Best province to SELL not grow - market R150 lotion in Sandton")

elif "North West" in location:
    st.subheader("North West - Rustenburg, Mahikeng")
    st.write("- What can grow: **Aloe ⭐⭐⭐⭐⭐**, Spekboom ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐, Lemongrass ⭐⭐⭐")
    st.write("- Soil: Sandy, dry, hot")
    st.write("- Tip: Very dry - Aloe and Spekboom perfect, no water. Moringa ok. Lemongrass needs borehole water")

elif "Free State" in location:
    st.subheader("Free State - Bloemfontein")
    st.write("- What can grow: **Aloe ⭐⭐⭐⭐⭐**, Spekboom ⭐⭐⭐⭐, Lemongrass ⭐⭐, Moringa ⭐⭐ (frost)")
    st.write("- Soil: Clay loam, very cold winter -10°C frost")
    st.write("- Tip: Coldest - Only Aloe and Spekboom survive frost. Moringa and Lemongrass die winter unless in tunnel. Best grow Aloe")

elif "Northern Cape" in location:
    st.subheader("Northern Cape - Kimberley, Upington")
    st.write("- What can grow: **Aloe ⭐⭐⭐⭐⭐**, Spekboom ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐")
    st.write("- Soil: Desert sandy, hottest and driest")
    st.write("- Tip: Desert - Only Aloe Ferox and Spekboom survive. No water needed. Moringa needs irrigation. Lemongrass impossible without water")

# SELLING
st.divider()
st.header("🌍 Selling - Matatiele to All Provinces")
st.write("Base Matatiele Ward 11 Mapeng PTO land free, Aloe wild, cost low R120 not R200 like Clicks")
provinces_all = ["Eastern Cape - Matatiele same day R20", "KwaZulu-Natal R100 Paxi", "Western Cape R100", "Limpopo R100", "Mpumalanga R100", "Gauteng R100", "North West R100", "Free State R100", "Northern Cape R100"]
selected2 = st.selectbox("Delivery province?", provinces_all)
st.success(f"Yes! Deliver to {selected2}")

# PRODUCTS
st.divider()
st.header("🧴 Products Whole Purpose")
st.subheader("Body Lotion 200ml R120")
st.write("Purpose whole: Heals whole body dry cracked skin from sun wind, Matatiele winter dry, for farmers teachers kids, soft not sticky")
st.subheader("Face Cream 50ml R95")
st.write("Purpose whole: Face only pimples dark spots sunburn, light not oily, youth glow")
st.write("Combo R200 save R15")

st.divider()
st.header("📦 Whole Kit")
st.write("Ingredients: Aloe 5L farm, Shea 10kg, Marula 8L, Beeswax 4kg, Vit E 800ml, Rooibos 4 boxes, Geogard 200ml")
st.write("Tools: Blender, 2 pots, 2 jugs, spoons, pH strips 5.5, thermometer, gloves blue, hair net apron, scale")

st.caption("SmartFarmSA | Eastern Cape detailed Matatiele locations | Other provinces tips")




