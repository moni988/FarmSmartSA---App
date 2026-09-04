import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA Pro v2", page_icon="🌿", layout="centered")

st.title("🌿 SmartFarmSA Pro v2")
st.caption(f"{datetime.now().strftime('%d %B %Y')} - Mapeng Ward 11")

# --- WEATHER ONLY TRY ---
try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Matatiele&appid={API_KEY}&units=metric"
    d = requests.get(url, timeout=10).json()
    temp = d['main']['temp']
    tmin = d['main']['temp_min']
    c1,c2,c3 = st.columns(3)
    c1.metric("Now", f"{temp}°C")
    c2.metric("Tonight Low", f"{tmin}°C")
    c3.metric("Condition", d['weather'][0]['description'])
    if tmin <= 2:
        st.error(f"❄️ FROST {tmin}°C TONIGHT - COVER Moringa!")
        frost = f"FROST {tmin}C"
    else:
        st.success(f"✅ No frost {tmin}°C")
        frost = f"Good {temp}C"
except Exception as e:
    temp = 11.7
    tmin = 2.5
    frost = "Check"
    st.info("Matatiele 11.7°C few clouds - using offline")

# --- WHATSAPP ALWAYS VISIBLE - NOT INSIDE TRY ---
st.divider()
st.subheader("📲 WhatsApp Frost Alert")
try:
    from twilio.rest import Client
    TW_SID = st.secrets["TWILIO_SID"]
    TW_TOK = st.secrets["TWILIO_TOKEN"]
    TW_FROM = st.secrets["TWILIO_WHATSAPP"]
    TW_TO = st.secrets["MY_WHATSAPP"]
    if st.button("Send Alert to My WhatsApp"):
        client = Client(TW_SID, TW_TOK)
        client.messages.create(from_=TW_FROM, to=TW_TO, body=f"🌱 Bare Beauty Mapeng {temp}°C Low {tmin}°C {frost}")
        st.success("✅ WhatsApp sent!")
except:
    st.warning("Add TWILIO secrets in Streamlit Cloud to enable WhatsApp")

# --- ALL 9 ALWAYS VISIBLE ---
st.divider()
st.header("🇿🇦 All 9 Provinces - Everything They Grow")

st.subheader("1. EASTERN CAPE - Mapeng")
st.write("**Towns:** Matatiele, Mount Fletcher, Maclear, Qumbu, Mthatha, Gqeberha")
st.write("**Grow:** Aloe Ferox ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐, Lemongrass ⭐⭐⭐⭐, Maize, Cabbage, Spinach, Pineapple")

st.subheader("2. KWAZULU-NATAL")
st.write("**Towns:** Durban, Pietermaritzburg, Richards Bay, Newcastle, Port Shepstone")
st.write("**Grow:** Lemongrass ⭐⭐⭐⭐⭐, Sugarcane ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐, Madumbis ⭐⭐⭐⭐⭐, Banana ⭐⭐⭐⭐⭐, Mango, Avocado, Macadamia")

st.subheader("3. WESTERN CAPE")
st.write("**Towns:** Cape Town, Stellenbosch, Paarl, Worcester, Ceres, Clanwilliam")
st.write("**Grow:** Spekboom ⭐⭐⭐⭐⭐, Grapes Wine ⭐⭐⭐⭐⭐, Olives ⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐⭐, Rooibos ⭐⭐⭐⭐⭐, Apples Ceres")

st.subheader("4. LIMPOPO")
st.write("**Towns:** Polokwane, Tzaneen, Thohoyandou, Phalaborwa, Giyani, Lephalale")
st.write("**Grow:** Moringa ⭐⭐⭐⭐⭐, Marula ⭐⭐⭐⭐⭐, Mango ⭐⭐⭐⭐⭐, Avocado ⭐⭐⭐⭐⭐, Litchi, Tomato, Baobab")

st.subheader("5. MPUMALANGA")
st.write("**Towns:** Mbombela, Hazyview, Barberton, Lydenburg, White River")
st.write("**Grow:** Lemongrass ⭐⭐⭐⭐⭐, Avocado ⭐⭐⭐⭐⭐, Macadamia ⭐⭐⭐⭐⭐, Mango ⭐⭐⭐⭐⭐, Citrus, Sugarcane")

st.subheader("6. GAUTENG")
st.write("**Towns:** Johannesburg, Pretoria, Soweto, Centurion, Krugersdorp, Bronkhorstspruit, Vereeniging, Randfontein")
st.write("**Grow:** Spekboom ⭐⭐⭐⭐⭐ pots R150 Sandton, Herbs ⭐⭐⭐⭐⭐, Spinach greenhouse ⭐⭐⭐⭐, Aloe pots, Microgreens ⭐⭐⭐⭐⭐, Mushrooms, Lemongrass ⭐⭐⭐")
st.write("Soil clay Highveld frost -5°C | Tip: SELL Sandton biggest market | Delivery R100 Courier R50 same day JHB")

st.subheader("7. NORTH WEST")
st.write("**Towns:** Rustenburg, Mahikeng, Potchefstroom, Klerksdorp, Brits, Lichtenburg, Vryburg, Zeerust, Hartbeespoort")
st.write("**Grow:** Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐, Sunflower ⭐⭐⭐⭐⭐ Lichtenburg, Maize ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐, Groundnuts")
st.write("Soil sandy dry 400-500mm | Tip: Sunflower capital | Delivery R100 Paxi")

st.subheader("8. FREE STATE")
st.write("**Towns:** Bloemfontein, Welkom, Bethlehem, Kroonstad, Sasolburg, Harrismith, Phuthaditjhaba, Bothaville, Parys")
st.write("**Grow:** Maize ⭐⭐⭐⭐⭐ Bothaville, Wheat ⭐⭐⭐⭐⭐ Bethlehem, Aloe ⭐⭐⭐⭐⭐, Sunflower ⭐⭐⭐⭐⭐, Soya, Potatoes, Cherries Ficksburg, Spekboom ⭐⭐⭐⭐")
st.write("Soil clay loam cold -10°C frost | Tip: coldest only Aloe Spekboom survive | Delivery R100 Paxi")

st.subheader("9. NORTHERN CAPE")
st.write("**Towns:** Kimberley, Upington, Springbok, De Aar, Kuruman, Kakamas, Prieska, Sutherland, Colesberg")
st.write("**Grow:** Aloe ⭐⭐⭐⭐⭐, Dates ⭐⭐⭐⭐⭐ Upington Orange River, Grapes ⭐⭐⭐⭐ Kakamas, Pecan ⭐⭐⭐⭐⭐, Raisins ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐")
st.write("Soil desert 40°C+ 100-300mm | Tip: Dates Orange River irrigation | Delivery R100 Courier")

st.divider()
st.write("Body Lotion 200ml R120 | Face Cream 50ml R95 | Whole Kit R9,610 =41 bottles: Aloe 5L Shea 10kg Marula 8L Beeswax 4kg Vit E 800ml Rooibos 4 boxes Geogard 200ml +100 pumps 100 amber 50ml +Blender 2 pots 2 jugs spoons pH 5.5 thermometer gloves hair net apron scale")
st.caption("All 9 Visible No Dropdown | Bare Beauty Farm Mapeng Ward 11")
