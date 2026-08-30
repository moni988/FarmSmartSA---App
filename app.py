import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA Pro 9 Provinces", page_icon="🌿", layout="centered")

st.title("🌿 SmartFarmSA Pro v2")
st.write("**Bare Beauty Botanicals | Mapeng Ward 11 Matatiele | All 9 Provinces Visible**")
st.caption(f"{datetime.now().strftime('%d %B %Y')}")

# WEATHER
try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
except:
    API_KEY = "b6a9082fddf3edfdb3c8903722f60c71"
try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Matatiele&appid={API_KEY}&units=metric"
    r = requests.get(url, timeout=10)
    d = r.json()
    c1,c2,c3 = st.columns(3)
    c1.metric("Matatiele", f"{d['main']['temp']}°C")
    c2.metric("Humidity", f"{d['main']['humidity']}%")
    c3.metric("Condition", d['weather'][0]['description'])
except:
    st.info("Matatiele 11.74°C few clouds - Good for Aloe")

st.divider()
st.header("🇿🇦 All 9 Provinces - Farming Towns + Suitable Crops - ALL VISIBLE")

# 1 EASTERN CAPE - MATATIELE DETAILED ONLY CHANGED
st.subheader("1. EASTERN CAPE - Matatiele Mapeng Ward 11 (YOUR BASE)")
st.write("**Towns:** Matatiele, Mount Fletcher, Mount Frere, Bizana, Flagstaff, Lusikisiki, Mthatha, Qumbu, Port St Johns, Kokstad")
st.write("**Base:** 0.5ha Mapeng near Mapfontein JSS PTO free sandy loam degraded")
st.write("Aloe 100 SOUTH slope rocky no compost frost hardy -5 to 30°C holes 30cm free 5L every 3 months")
st.write("Lemongrass 70m EAST morning sun near compost 100 buckets compost water 2x week cut 2 months")
st.write("Spekboom 50 WEST+NORTH fence donga edge windbreak Municipality IDP carbon credit no water")
st.write("Moringa 100 CENTER full sun deep 50cm 200 buckets compost cover sack frost leaves tea oil")
st.write("Delivery: Same day R20 Taxi Rank Market Schools Clinics")

# 2 KZN
st.subheader("2. KWAZULU-NATAL")
st.write("**Towns:** Durban, Pietermaritzburg, Richards Bay, Newcastle, Ladysmith, Vryheid, Hluhluwe, Port Shepstone, Kokstad")
st.write("**Crops:** Lemongrass ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐⭐, Sugarcane ⭐⭐⭐⭐⭐, Banana ⭐⭐⭐⭐, Macadamia ⭐⭐⭐⭐, Aloe ⭐⭐⭐")
st.write("Soil red loam humid 800-1000mm | Tip: Hot humid Lemongrass 1.5m cut 4x year Moringa 3m year | Delivery R100 Paxi")

# 3 WESTERN CAPE
st.subheader("3. WESTERN CAPE")
st.write("**Towns:** Cape Town, Stellenbosch, Paarl, Worcester, George, Oudtshoorn, Malmesbury, Ceres, Clanwilliam")
st.write("**Crops:** Spekboom ⭐⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐⭐, Rooibos ⭐⭐⭐⭐⭐, Grapes ⭐⭐⭐⭐⭐, Olives ⭐⭐⭐⭐")
st.write("Soil sandy dry 300mm windy | Tip: Spekboom Aloe no water Rooibos only Clanwilliam | Delivery R100 Courier")

# 4 LIMPOPO
st.subheader("4. LIMPOPO")
st.write("**Towns:** Polokwane, Tzaneen, Thohoyandou, Louis Trichardt, Musina, Bela-Bela, Phalaborwa, Giyani, Lephalale")
st.write("**Crops:** Moringa ⭐⭐⭐⭐⭐, Marula ⭐⭐⭐⭐⭐, Mango ⭐⭐⭐⭐⭐, Avocado ⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐")
st.write("Soil sandy very hot 35-40°C | Tip: Hottest Marula oil source Phalaborwa cheaper | Delivery R100 Paxi")

# 5 MPUMALANGA
st.subheader("5. MPUMALANGA")
st.write("**Towns:** Nelspruit Mbombela, Hazyview, Witbank Emalahleni, Middelburg, Ermelo, Barberton, Lydenburg, White River")
st.write("**Crops:** Lemongrass ⭐⭐⭐⭐⭐, Macadamia ⭐⭐⭐⭐⭐, Avocado ⭐⭐⭐⭐, Citrus ⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐")
st.write("Soil loam subtropical 600-800mm | Tip: Macadamia capital Hazyview | Delivery R100 Paxi")

# 6 GAUTENG
st.subheader("6. GAUTENG")
st.write("**Towns:** Johannesburg, Pretoria, Soweto, Centurion, Krugersdorp, Heidelberg, Bronkhorstspruit, Vereeniging, Randfontein")
st.write("**Crops:** Spekboom ⭐⭐⭐⭐⭐ pots, Aloe ⭐⭐⭐⭐, Herbs ⭐⭐⭐⭐, Spinach ⭐⭐⭐⭐, Lemongrass ⭐⭐⭐ greenhouse")
st.write("Soil clay Highveld frost -5°C | Tip: SELL not grow Sandton R150-R200 biggest market | Delivery R100 Courier R50 same day Joburg")

# 7 NORTH WEST
st.subheader("7. NORTH WEST")
st.write("**Towns:** Rustenburg, Mahikeng, Potchefstroom, Klerksdorp, Brits, Lichtenburg, Vryburg, Zeerust, Hartbeespoort")
st.write("**Crops:** Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐, Sunflower ⭐⭐⭐⭐⭐ Lichtenburg, Maize ⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐")
st.write("Soil sandy dry 400-500mm | Tip: Sunflower capital Lichtenburg Maize belt | Delivery R100 Paxi")

# 8 FREE STATE
st.subheader("8. FREE STATE")
st.write("**Towns:** Bloemfontein, Welkom, Bethlehem, Kroonstad, Sasolburg, Harrismith, Phuthaditjhaba, Bothaville, Parys")
st.write("**Crops:** Aloe ⭐⭐⭐⭐⭐, Maize ⭐⭐⭐⭐⭐ Bothaville, Wheat ⭐⭐⭐⭐⭐ Bethlehem, Spekboom ⭐⭐⭐⭐, Sunflower ⭐⭐⭐⭐")
st.write("Soil clay loam cold -10°C frost | Tip: Maize wheat capital coldest only Aloe Spekboom survive | Delivery R100 Paxi")

# 9 NORTHERN CAPE
st.subheader("9. NORTHERN CAPE")
st.write("**Towns:** Kimberley, Upington, Springbok, De Aar, Kuruman, Kakamas, Prieska, Sutherland, Colesberg")
st.write("**Crops:** Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐, Dates ⭐⭐⭐⭐⭐ Upington, Grapes ⭐⭐⭐⭐ Kakamas, Pecan ⭐⭐⭐⭐")
st.write("Soil desert sandy 40°C+ 100-300mm | Tip: Dates Upington famous Orange River irrigation | Delivery R100 Courier")

st.divider()
st.header("🧴 Products + Kit")
st.write("Body Lotion 200ml R120 whole body dry cracked Matatiele sun wind | Face Cream 50ml R95 pimples dark spots light youth glow | Combo R200 save R15")
st.write("Whole Kit R9,610: Aloe 5L farm Shea 10kg Marula 8L Beeswax 4kg Vit E 800ml Rooibos 4 boxes Geogard 200ml +100 green pump 200ml 100 amber glass 50ml 400 stickers QR +Blender 2 pots 2 jugs spoons pH 5.5 thermometer gloves blue hair net apron scale =41 bottles")

st.caption("All 9 Provinces Visible No Dropdown | Eastern Cape Matatiele Changed Only | Other 8 Professional")




