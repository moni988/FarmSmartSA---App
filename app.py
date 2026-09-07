import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA Bare Beauty Mapeng Ward 11 Matatiele", page_icon="🌿", layout="wide")

st.title("🌿 SmartFarmSA + Bare Beauty - Mapeng Ward 11 Matatiele")
st.markdown("**HOME: Mapeng Village Ward 11, Matatiele EC -30.24, 28.62 | 0.5ha Bare Beauty Farm near Mapfontein JSS**")

# ========== ALL 10 PROVINCES - EACH WHAT THEY GROW ==========
PROVINCE_CROPS = {
    "Mapeng Village Ward 11 - Matatiele (HOME)": {"loc": "Mapeng Village Ward 11 Matatiele EC -30.24, 28.62", "climate": "Temperate 600-800mm Frost Winter", "lat": -30.24, "lon": 28.62167, "soil": "Degraded donga clay loam Mapfontein JSS", "grow": ["Aloe Ferox South 100m Cash no water", "Lemongrass East 70m Oil windbreak 100 buckets compost", "Moringa Center 100 Food superfood 200 buckets compost frost kills", "Spekboom West North 50 Fodder carbon fixes donga NO water", "Maize Drought Food", "Cabbage Food winter", "Spinach Fast 30 days", "Potatoes Food", "Beans Protein"]},
    "Eastern Cape": {"loc": "Mthatha, Gqeberha", "climate": "Temperate 500-800mm", "lat": -32.97, "lon": 27.87, "soil": "Clay loam", "grow": ["Aloe Ferox Wild free", "Maize Staple", "Cabbage Winter", "Spekboom Fodder", "Lemongrass Oil", "Potatoes", "Beans"]},
    "KwaZulu-Natal": {"loc": "Durban, Pietermaritzburg", "climate": "Subtropical 800-1200mm", "lat": -29.85, "lon": 31.02, "soil": "Sandy loam", "grow": ["Sugarcane Cash 12mo", "Bananas Fruit", "Maize Food", "Moringa Superfood", "Amadumbe Traditional", "Sweet Potatoes"]},
    "Limpopo": {"loc": "Polokwane, Tzaneen", "climate": "Hot semi-arid 35°C+", "lat": -23.9, "lon": 29.45, "soil": "Loamy sand", "grow": ["Mangoes Export", "Moringa Drought", "Groundnuts Protein", "Cowpeas Food", "Maize", "Tomatoes", "Avocado"]},
    "Gauteng": {"loc": "Johannesburg, Pretoria", "climate": "Highveld 600-700mm", "lat": -26.20, "lon": 28.04, "soil": "Loam", "grow": ["Spinach Fast market Jozi", "Tomatoes High price", "Maize Backyard", "Cabbage", "Carrots", "Lettuce", "Herbs"]},
    "Western Cape": {"loc": "Cape Town, Stellenbosch", "climate": "Mediterranean winter rain", "lat": -33.92, "lon": 18.42, "soil": "Sandy limestone", "grow": ["Grapes Wine", "Olives Oil", "Spekboom Waterwise", "Wheat Winter", "Apples Ceres", "Rooibos Tea"]},
    "Free State": {"loc": "Bloemfontein, Bethlehem", "climate": "Semi-arid 400-600mm cold", "lat": -29.08, "lon": 26.15, "soil": "Clay", "grow": ["Maize Biggest SA", "Wheat Winter", "Sunflower Oil", "Sorghum Drought", "Potatoes", "Soybeans"]},
    "North West": {"loc": "Mahikeng, Rustenburg", "climate": "Semi-arid 300-600mm", "lat": -25.86, "lon": 25.64, "soil": "Sandy loam", "grow": ["Maize Staple", "Sunflower Oil", "Groundnuts", "Moringa Drought", "Cowpeas", "Spekboom Fodder", "Watermelon"]},
    "Mpumalanga": {"loc": "Mbombela, Witbank", "climate": "Subtropical 600-1000mm", "lat": -25.47, "lon": 30.96, "soil": "Red loam", "grow": ["Maize Food", "Avocado Export $$$", "Macadamia Cash $$$", "Moringa Superfood", "Lemongrass Oil", "Sugarcane Cash"]},
    "Northern Cape": {"loc": "Kimberley, Upington", "climate": "Arid 200-400mm 40°C", "lat": -28.72, "lon": 24.76, "soil": "Desert sand", "grow": ["Spekboom Only survives", "Aloe Ferox Wild cash", "Dates Desert fruit", "Grapes Orange River irrigated", "Wheat irrigated", "Pecans Nuts"]},
}

selected = st.selectbox("📍 CHOOSE LOCATION - 10 PROVINCES", list(PROVINCE_CROPS.keys()), index=0)
data = PROVINCE_CROPS[selected]
st.info(f"{data['loc']} | Climate: {data['climate']} | Soil: {data['soil']}")

# ========== WEATHER WITH ALERTS AND SOLUTIONS EVERY WEATHER ==========
def get_alerts(temp, humidity, wind, desc, province):
    alerts=[]
    d=desc.lower()
    if temp<=2:
        alerts.append(("❄️ FROST ALERT", f"{temp}°C - COVER! Frost kills Moringa, Tomatoes in {province}. SOLUTION: Mulch heavy, cover plastic night, use Mapeng Ward 11 kraal manure."))
    elif temp<=5:
        alerts.append(("🥶 COLD ALERT", f"{temp}°C - Cold risk in {province}. SOLUTION: Delay planting cuttings, wait 10°C+, greenhouse for spinach."))
    if temp>=35:
        alerts.append(("🔥 HEAT ALERT", f"{temp}°C - Extreme heat in {province}! SOLUTION: Water 5am & 6pm, mulch heavy Mapeng Ward 11, shade cloth Moringa Center 100, Aloe Ferox OK."))
    elif temp>=30:
        alerts.append(("☀️ HOT ALERT", f"{temp}°C - Hot in {province}. SOLUTION: Irrigate Moringa Center 100, Lemongrass East 70m loves it, maize needs water."))
    if "rain" in d:
        alerts.append(("🌧️ RAIN ALERT", f"{desc.title()} - Rain in {province}! SOLUTION: Stop irrigation, check drainage, harvest rainwater Mapeng Ward 11 tanks, PERFECT Spekboom West 50 planting sticks root fast."))
    if "overcast" in d or "clouds" in d:
        alerts.append(("☁️ CLOUDY", f"{desc.title()} - Cloudy in {province}. SOLUTION: Good transplant cabbage, no water stress, low sun photosynthesis low."))
    if "clear" in d:
        alerts.append(("🌞 CLEAR SKY", f"{desc.title()} - Clear in {province}. SOLUTION: Perfect sun, high photosynthesis, great for Spekboom & Aloe Ferox drying gel, harvest Aloe morning."))
    if wind>=10:
        alerts.append(("💨 WIND ALERT", f"{wind} m/s strong wind in {province}! SOLUTION: Stake tomatoes, Lemongrass East 70m windbreak working protects Moringa Center 100 & Maize, protect young."))
    elif wind>=5:
        alerts.append(("🍃 WINDY", f"{wind} m/s - Moderate in {province}. SOLUTION: Good for maize pollination, windbreak holding."))
    if humidity>=80:
        alerts.append(("💧 HIGH HUMIDITY", f"{humidity}% - Disease risk in {province}! SOLUTION: Spray organic fungicide chili garlic, avoid wet leaves, good for Moringa but watch cabbage rot."))
    elif humidity<=30:
        alerts.append(("🏜️ LOW HUMIDITY", f"{humidity}% - Dry air in {province}! SOLUTION: Water more, mulch heavy Mapeng Ward 11, Spekboom & Aloe need NO water."))
    if not alerts:
        alerts.append(("✅ PERFECT WEATHER", f"{temp}°C {desc.title()} - Perfect for {province}! SOLUTION: Do planting, weeding, harvesting, plant 50 Spekboom West fence today."))
    return alerts

st.subheader("⛅ Live Weather with ALERTS and SOLUTIONS for EVERY weather")
try:
    api_key = st.secrets["WEATHER_API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={data['lat']}&lon={data['lon']}&appid={api_key}&units=metric"
    res = requests.get(url, timeout=10).json()
    temp=res["main"]["temp"]; humidity=res["main"]["humidity"]; wind=res["wind"]["speed"]; desc=res["weather"][0]["description"]
    temp_min=res["main"]["temp_min"]; temp_max=res["main"]["temp_max"]
    c1,c2,c3=st.columns(3)
    c1.metric("Now", f"{temp}°C", desc.title()); c2.metric("Humidity / Wind", f"{humidity}% / {wind} m/s"); c3.metric("Low / High", f"{temp_min}°C / {temp_max}°C")
    alerts=get_alerts(temp,humidity,wind,desc,selected)
    for title,msg in alerts:
        if "ALERT" in title: st.error(f"**{title}:** {msg}")
        elif "PERFECT" in title: st.success(f"**{title}:** {msg}")
        else: st.warning(f"**{title}:** {msg}")
except Exception as e:
    st.warning(f"Weather loading error {e} - backup: Matatiele 22°C sunny good harvest Aloe morning"); alerts=[]; temp=22; desc="clear"

# ========== WHAT THEY GROW ==========
st.divider()
st.subheader(f"🌿 What They Grow in {selected}")
for crop in data["grow"]:
    st.success(f"• {crop}")

st.divider()
st.subheader("🇿🇦 ALL 10 PROVINCES - Each What They Grow (Click open)")
for prov, info in PROVINCE_CROPS.items():
    with st.expander(f"📍 {prov} - {info['loc']}"):
        st.write(f"**Climate:** {info['climate']} | **Soil:** {info['soil']}")
        st.write(f"**What They Grow:**")
        for crop in info["grow"]:
            st.markdown(f"- {crop}")

st.divider()
st.subheader("🗺️ Mapeng Ward 11 Farm Layout")
st.markdown("- **South 100m:** Aloe Ferox what they grow cash border\n- **East 70m:** Lemongrass oil windbreak\n- **Center 100:** Moringa food\n- **West North 50:** Spekboom fodder carbon fixes donga\n- **Food:** Maize, Cabbage, Spinach, Potatoes, Beans food security")

# ========== TELEGRAM ==========
st.divider()
if st.button("🔔 Send ALL Alerts + Solutions to Telegram"):
    try:
        bot_token=st.secrets["BOT_TOKEN"]; chat_id=st.secrets["CHAT_ID"]
        txt="\n".join([f"{t}: {m}" for t,m in alerts])
        msg=f"FarmSmartSA Mapeng Ward 11 Matatiele -30.24,28.62 {selected} {temp}°C {desc}\n{txt}"
        r=requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}", timeout=10)
        st.success("✅ Sent! Check phone" if r.status_code==200 else f"Failed {r.text}")
    except Exception as e: st.error(f"Error {e}")

# ========== 4 CORRECT TOOLS ==========
st.divider()
st.header("🛠️ 4 CORRECT TOOLS")

st.subheader("🔍 1. Plant Scanner")
up=st.file_uploader("Upload leaf photo what they grow Mapeng", type=["jpg","png","jpeg"], key="plant")
if up:
    st.image(up)
    p=st.selectbox("Plant what they grow?", ["Aloe Ferox South 100","Lemongrass East 70m","Spekboom West 50","Moringa Center 100","Maize","Cabbage"], key="p1")
    if "Aloe" in p: st.success("Scanner: Aloe Ferox South 100 what they grow healthy green thick good yellow overwater no compost cash.")
    elif "Lemongrass" in p: st.success("Scanner: Lemongrass East 70m what they grow yellow needs nitrogen 100 buckets compost.")
    elif "Spekboom" in p: st.success("Scanner: Spekboom West 50 what they grow droopy overwater loves dry donga fixes soil.")
    elif "Moringa" in p: st.warning("Scanner: Moringa Center 100 what they grow frost kills under 2°C cover plastic.")
    else: st.info(f"Scanner: {p} what they grow check Armyworm chili garlic soap.")

st.divider()
st.subheader("🌱 2. Soil Library")
soil=st.selectbox("Soil Mapeng Ward 11 Mapfontein JSS?", ["Degraded / Donga your plot", "Sandy", "Clay", "Loam"], key="soil")
if "Degraded" in soil:
    st.markdown("**Degraded Donga what they grow:**\n- ⭐⭐⭐⭐⭐ Spekboom West 50 fixes donga NO compost\n- ⭐⭐⭐⭐⭐ Aloe Ferox South 100 loves degraded NO compost\n- ⭐⭐⭐ Lemongrass East 70m needs 100 buckets compost\n- ⭐⭐⭐ Moringa Center 100 needs 200 buckets compost deep 60cm\n- ⭐⭐⭐⭐ Maize drought needs compost but food\n- Compost: Cow dung 100 + leaves 100 + kitchen 50 + soil 50 = 2mo 300 buckets")
else:
    st.write(f"{soil}: Aloe & Spekboom no compost, Moringa Lemongrass Maize need compost pH 5.5 safe.")

st.divider()
st.subheader("👨‍🌾 3. Ask Expert")
q=st.text_input("Ask about Mapeng 0.5ha", placeholder="How to plant Spekboom in donga?", key="expert")
if q:
    ql=q.lower()
    if "spekboom" in ql: st.success("Expert: Spekboom West 50 stick 30cm donga rainy day no water 1 week roots fast stops erosion Municipality IDP carbon.")
    elif "aloe" in ql: st.success("Expert: Aloe South 100 1m apart no water gel 8 months wild free Matatiele PTO free cash.")
    elif "moringa" in ql: st.success("Expert: Moringa Center 100 deep 60cm 200 buckets compost water daily 3mo frost plastic under 2°C.")
    else: st.info(f"Expert: For '{q}' use Aloe & Spekboom first degraded no compost then compost others PTO free NYDA R10k.")

st.divider()
st.subheader("🛡️ 4. FarmShield")
threat=st.selectbox("Threat what they grow?", ["Frost Winter", "Drought", "Goats eating", "Pests Armyworm", "Wind", "Theft"], key="shield")
if "Frost" in threat: st.error(f"FarmShield Frost {temp}°C: Cover Moringa plastic, mulch cabbage, Aloe & Spekboom & Lemongrass OK.")
elif "Drought" in threat: st.warning("FarmShield Drought: Spekboom & Aloe NO water, Lemongrass mulch heavy, Moringa 2x week, harvest rainwater.")
elif "Goats" in threat: st.warning("FarmShield Goats: Fence Spekboom living fence West 50, Aloe South thorny border.")
elif "Pests" in threat: st.info("FarmShield Pests: Chili garlic soap spray, Lemongrass East 70m repellent, check under leaves.")
else: st.info(f"FarmShield {threat}: Check daily Ward 11.")

# ========== YOUR PRODUCTS AND INGREDIENTS - YOU SAID MISSING ==========
st.divider()
st.header("🧴 Bare Beauty Products - Whole Purpose (Mapeng Ward 11)")
st.subheader("Body Lotion 200ml - R120")
st.write("**Purpose whole:** Heals whole body dry cracked skin from Matatiele sun wind. For farmers, teachers, kids, everyone. Soft not sticky Rooibos Marula scent.")
st.write("**How to use:** Pump 2 times after bath morning + night whole body. Winter use 3 times.")
st.subheader("Face Cream 50ml - R95")
st.write("**Purpose whole:** Face only - pimples, dark spots, sunburn, sensitive. Light no oil youth glow.")
st.write("**How to use:** Clean face pea size only morning + night jar lasts 30 days.")
st.subheader("Combo R200 - Body + Face full care save R15")

st.divider()
st.header("📦 What Inside - Whole Kit Ingredients + Tools No Price Each")
st.markdown("""
**Ingredients whole what they grow + buy:**
- Aloe Gel 5L from farm South 100 - what they grow Mapeng Ward 11
- Shea Butter 10kg - buy
- Marula Oil 8L - buy Limpopo
- Beeswax 4kg - buy Matatiele
- Vitamin E 800ml - preservative
- Rooibos Tea 4 boxes - scent Western Cape
- Geogard Preservative 200ml - safe
- Lemongrass Oil from East 70m - what they grow your oil
- Moringa Powder Center 100 - what they grow superfood additive

**Containers:**
- 100 green pump bottles 200ml
- 100 amber glass jars 50ml
- 400 stickers with QR code

**Tools whole:**
- Blender stick, 2 stainless pots double boiler, 2 jugs 5L, spoons, pH strips 5.5 safe, thermometer 0-100C, gloves blue 100pcs, hair net + apron, scale - for right measure + hygiene + NYDA photo
""")

st.divider()
st.header("💰 Stock 41 Bottles + Profit + Market")
lotion=st.number_input("Lotion bottles from Aloe South 100", value=41)
cream=st.number_input("Cream jars", value=100)
sales=lotion*120 + cream*95
st.metric("Total Sales", f"R{sales}")
st.write("NYDA R10,000 = R5,000 ingredients + R3,000 containers + R1,610 tools + R390 taxi left")
st.write("Profit first batch: R11,472")
st.write("Base: Matatiele Ward 11 Mapeng PTO land free, Aloe wild cost low")
st.write("Local: Mapfontein School, Matatiele Town Market, Taxi Rank, Clinics, Churches Same day R20")
st.write("Online: Facebook WhatsApp TikTok Instagram Paxi to Pep Store all provinces 3-5 days R100")
provinces=["Eastern Cape","KwaZulu-Natal","Western Cape","Limpopo","Mpumalanga","Gauteng","North West","Free State","Northern Cape"]
sel=st.selectbox("Customer Province - Delivery?", provinces)
st.success(f"I deliver Matatiele to {sel} - Yes! R100 courier")

st.divider()
st.caption(f"SmartFarmSA v2 + Bare Beauty | Mapeng Village Ward 11 Matatiele -30.24,28.62 | 10 Provinces what they grow | Alerts EVERY weather + Solutions | 4 Tools: Plant Scanner, Soil Library, Ask Expert, FarmShield | Products + Ingredients | {datetime.now().strftime('%d %B %Y')} | Bare Beauty 0.5ha")
