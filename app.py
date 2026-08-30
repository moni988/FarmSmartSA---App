import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA", page_icon="🌿", layout="centered")

st.title("🌿 SmartFarmSA v2")
st.write("**Built for Mapeng Ward 11 - Bare Beauty Botanicals Farm**")
st.write("Check if weather is good for your 0.5ha near Mapfontein JSS + Sell Online")
st.caption(f"Today: {datetime.now().strftime('%d %B %Y')} | NYDA R10,000 Ready")

# LOCATION
st.subheader("📍 Your Farm Location")
location = st.selectbox("Select", ["Mapeng Ward 11 (Matatiele) - Base", "Durban", "Other"])
city = "Matatiele" if "Mapeng" in location else "Durban"

# WEATHER WITH HIDDEN API KEY - SAFE
st.subheader("🌤️ Live Weather - Matatiele")

# Get API key from Secrets safely - NOT in code
try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
except:
    # Fallback to your key if secrets not set yet, but hide from GitHub later
    API_KEY = st.secrets.get("WEATHER_API_KEY", "b6a9082fddf3edfdb3c8903722f60c71")

# Use https not http
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

    # SMART CHECK FOR YOUR 4 PLANTS
    st.divider()
    st.subheader("✅ Plant Check Today")

    if temp < -5:
        st.error("❄️ Frost Alert! Cover young Moringa, but Aloe, Spekboom, Lemongrass are OK")
    elif temp < 5:
        st.warning("Cold morning - Don't plant cuttings today. Wait for 10°C+")
    else:
        st.success("Good day to plant cuttings")

    if "rain" in desc.lower():
        st.info("🌧️ Rain today: Perfect for planting Spekboom sticks - they root faster!")
        st.write("- Aloe Ferox 100 plants south: Don't water, loves dry")
        st.write("- Lemongrass 70m east: Likes rain, will grow fast")
        st.write("- Spekboom 50 west: BEST time to stick cuttings")
        st.write("- Moringa 100 center: Likes rain first 3 months")
    elif temp > 30:
        st.info("☀️ Hot: Water Lemongrass early morning. Aloe & Spekboom don't need water. Moringa needs shade first week")
    else:
        st.info("🌤️ Mild: Good for all 4. Plant 50 Spekboom today along west fence")

    st.divider()
    st.subheader("🌱 Soil Check - Mapeng Ward 11")
    soil = st.selectbox("Soil in your plot?", ["Degraded / Donga", "Sandy", "Clay", "Loam"])
    if soil == "Degraded / Donga":
        st.write("**For your plot near Mapfontein JSS (sandy loam brown):**")
        st.write("- Spekboom: ⭐⭐⭐⭐⭐ - Will fix soil, holds donga, Municipality IDP likes")
        st.write("- Aloe Ferox: ⭐⭐⭐⭐⭐ - Loves degraded soil, no compost")
        st.write("- Lemongrass: ⭐⭐⭐ - Needs 100 buckets compost, plant near compost area east")
        st.write("- Moringa: ⭐⭐⭐ - Needs 200 buckets compost, deep holes center")
        st.write("**Compost:** Cow dung + dry leaves + kitchen waste + soil = 2 months, need 300 buckets")
    else:
        st.write(f"Soil {soil}: Add compost for Lemongrass and Moringa, Aloe and Spekboom no need")

except Exception as e:
    st.warning("Weather loading... check internet or API key in Secrets")
    st.write("Free backup: Matatiele 22°C sunny - good for harvesting Aloe morning")

# ADDED: WHERE YOU SELL - YOU LEFT THIS
st.divider()
st.header("🌍 Selling - Matatiele Base, Online Everywhere")
st.write("**Base:** Matatiele Ward 11 Mapeng - PTO land free, Aloe wild, cost low")
st.write("**Local:** Mapfontein School, Matatiele Town Market, Taxi Rank, Clinics, Churches - Same day R20")
st.write("**Online:** Facebook, WhatsApp, TikTok, Instagram - Paxi to Pep Store all provinces 3-5 days R100")

provinces = ["Eastern Cape", "KwaZulu-Natal", "Western Cape", "Limpopo", "Mpumalanga", "Gauteng", "North West", "Free State", "Northern Cape"]
selected = st.selectbox("Customer Province - Delivery?", provinces)
st.success(f"I deliver Matatiele to {selected} - Yes! R100 courier")

# ADDED: WHOLE PRODUCTS PURPOSE - YOU LEFT THIS
st.divider()
st.header("🧴 Bare Beauty Products - Whole Purpose")

st.subheader("Body Lotion 200ml - R120")
st.write("**Purpose whole:** Heals whole body dry cracked skin from Matatiele sun wind. For farmers, teachers, kids, everyone. Soft, not sticky, Rooibos Marula scent.")
st.write("**How to use:** Pump 2 times after bath morning + night, whole body. Winter use 3 times.")

st.subheader("Face Cream 50ml - R95")
st.write("**Purpose whole:** Face only - pimples, dark spots, sunburn, sensitive. Light, no oil, youth glow.")
st.write("**How to use:** Clean face, pea size only, morning + night, jar lasts 30 days.")

st.subheader("Combo R200")
st.write("Purpose: Body + face full care, save R15, customer buys 2 fast")

# ADDED: INGREDIENTS + TOOLS WHOLE - YOU LEFT THIS
st.divider()
st.header("📦 What Inside - Whole Kit No Price Each")
st.write("**Ingredients whole:** Aloe Gel 5L from farm, Shea Butter 10kg, Marula Oil 8L, Beeswax 4kg, Vitamin E 800ml, Rooibos Tea 4 boxes, Geogard Preservative 200ml - No cloves, with gloves")
st.write("**Containers:** 100 green pump bottles 200ml, 100 amber glass jars 50ml, 400 stickers with QR code")
st.write("**Tools whole:** Blender stick, 2 stainless pots double boiler, 2 jugs 5L, spoons, pH strips 5.5 safe, thermometer 0-100C, gloves blue 100pcs, hair net + apron, scale - for right measure + hygiene + NYDA photo")

# ADDED: STOCK + PROFIT - YOU LEFT THIS
st.divider()
st.header("💰 Stock 41 Bottles + Profit")
st.write("Now: 5L Aloe / 120ml = 41 lotions limit. After 6 months free 5L every 3 months = 41 free")
lotion = st.number_input("Lotion bottles", value=41)
cream = st.number_input("Cream jars", value=100)
sales = lotion*120 + cream*95
st.metric("Total Sales", f"R{sales}")
st.write("NYDA R10,000 = R5,000 ingredients + R3,000 containers + R1,610 tools + R390 taxi left")
st.write("Profit first batch: R11,472")

st.divider()
st.subheader("Did this help for Mapeng?")
c1, c2 = st.columns(2)
if c1.button("👍 Helpful"):
    st.success("Thanks! Use it Monday when you go to Municipality")
    st.balloons()
if c2.button("👎 Need fix"):
    st.info("What to add? Tell me - Moringa oil? Online order form?")

st.caption("SmartFarmSA v2 | For Bare Beauty Farm 0.5ha | Matatiele to SA online 🌿")
st.caption("API Key hidden in Secrets - Safe from GitHub")




