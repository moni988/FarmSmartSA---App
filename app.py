import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA 9 Provinces", page_icon="🌿", layout="centered")
st.title("Bare Beauty Botanicals - 9 Provinces FULL")
st.caption(f"{datetime.now().strftime('%d %B %Y')} - Mapeng Ward 11")

# --- WEATHER ALERTS ---
st.header("Live Weather + Solutions")
try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Matatiele&appid={API_KEY}&units=metric", timeout=10).json()
    temp = r['main']['temp']; tmin = r['main']['temp_min']; tmax = r['main']['temp_max']; humidity = r['main']['humidity']
    st.metric("Matatiele Now", f"{temp} C Low {tmin} C High {tmax} C")
    if tmin <= 2:
        st.error(f"FROST {tmin}C - Cover Moringa center + Lemongrass east with plastic + dry grass")
    if tmax >= 32:
        st.error(f"HEAT {tmax}C - Water 6am, shade Lemongrass")
except:
    st.info("Weather offline - If 2C frost cover Moringa Lemongrass")

st.divider()

# --- 9 PROVINCES DROPDOWN - FIX FOR PHONE ---
st.header("Select Province - See Full Detail")
province = st.selectbox("Choose Province", 
["1 EASTERN CAPE Mapeng - Your Home", 
 "2 KZN Durban PMB", 
 "3 WESTERN CAPE Cape Town", 
 "4 LIMPOPO Polokwane", 
 "5 MPUMALANGA Nelspruit", 
 "6 GAUTENG Joburg Pretoria", 
 "7 NORTH WEST Rustenburg", 
 "8 FREE STATE Bloemfontein", 
 "9 NORTHERN CAPE Kimberley"])

if province.startswith("1 EASTERN"):
    st.subheader("1. EASTERN CAPE Mapeng Ward 11 - YOUR FARM")
    st.write("Climate: -4C frost Jun Jul, 28C summer, rain 600mm")
    st.write("Soil: Loam sandy rocky west north pH 6.0")
    st.write("Farm 0.5ha: South 100 Aloe, East 70m Lemongrass, West North 50 Spekboom, Center 100 Moringa")
    st.write("Frost: Cover Moringa Lemongrass nightly May Aug plastic bottle, Aloe Spekboom ok -5C")
    st.write("Market: Matatiele R120 lotion R95 cream, NYDA loves EC")
    st.write("Water: Summer 3 days, Winter 7 days")

elif province.startswith("2 KZN"):
    st.subheader("2. KZN Durban PMB")
    st.write("Climate: 30C hot humid no frost rain 1000mm")
    st.write("Soil: Acid sandy pH 5.5 needs compost")
    st.write("Best: Lemongrass 2m fast, Moringa 3m 1 year, Aloe rots plant on mound")
    st.write("Frost: No frost good for Moringa Lemongrass all year")
    st.write("Problem: Too much rain Aloe rot Solution mound south side")
    st.write("Market: Durban tourists R150 lotion, Moringa powder R200 per 100g")

elif province.startswith("3 WESTERN"):
    st.subheader("3. WESTERN CAPE Cape Town Stellenbosch")
    st.write("Climate: Winter rain summer dry wind 10m/s frost 0C Ceres")
    st.write("Soil: Sandy acid pH 5.0 add lime")
    st.write("Best: Spekboom carbon R50 per tree, Rooibos, Aloe Mossel Bay, Lemongrass needs irrigation")
    st.write("Frost: Spekboom ok -5C, Aloe cover, Lemongrass pot inside")
    st.write("Problem: Wind Solution Spekboom hedge west side windbreak")
    st.write("Market: Green market R180 lotion tourists love QR")

elif province.startswith("4 LIMPOPO"):
    st.subheader("4. LIMPOPO Polokwane Giyani")
    st.write("Climate: Very hot 38C no frost rain 400mm drought")
    st.write("Soil: Red sandy pH 7.5 alkaline")
    st.write("Best: Moringa king 4m, Marula, Aloe, Lemongrass needs daily water")
    st.write("Frost: No frost Moringa never dies")
    st.write("Problem: Drought Solution mulch 10cm thick")
    st.write("Market: Moringa powder R250, Aloe gel R100 per litre")

elif province.startswith("5 MPUMALANGA"):
    st.subheader("5. MPUMALANGA Nelspruit Hazyview")
    st.write("Climate: 32C humid rain 800mm mist best soil SA")
    st.write("Soil: Loam rich pH 6.0")
    st.write("Best: Lemongrass oil 1% best province, Moringa 3m, all 4 crops good")
    st.write("Frost: Lowveld no frost Highveld -2C cover Moringa")
    st.write("Problem: Weeds fast Solution Lemongrass thick row stops weeds")
    st.write("Market: Lodges R200 cream Kruger tourists")

elif province.startswith("6 GAUTENG"):
    st.subheader("6. GAUTENG Joburg Pretoria Soweto")
    st.write("Climate: Cold -5C frost winter, 30C summer, hail Nov")
    st.write("Soil: Clay pH 6.5 bad drainage")
    st.write("Best: Spekboom pots R80 mall balcony, Aloe pot, Moringa pot inside winter, Lemongrass pot")
    st.write("Frost: -5C kills Moringa MUST pot bring inside Jun Jul greenhouse")
    st.write("Problem: Hail Solution shade cloth 50%")
    st.write("Market: Richest R180 lotion R120 cream Courier")

elif province.startswith("7 NORTH"):
    st.subheader("7. NORTH WEST Rustenburg Mahikeng")
    st.write("Climate: Dry 36C drought frost -3C")
    st.write("Soil: Sandy Kalahari pH 7.0 poor")
    st.write("Best: Aloe Ferox wild area, Spekboom, Moringa needs water")
    st.write("Frost: -3C Aloe ok Spekboom ok cover Moringa Lemongrass")
    st.write("Problem: Mining dust Solution Spekboom hedge dust filter")
    st.write("Market: Mines workers R120 dry skin Sun City lodges")

elif province.startswith("8 FREE"):
    st.subheader("8. FREE STATE Bloemfontein Bethlehem")
    st.write("Climate: Coldest -8C frost snow 35C summer")
    st.write("Soil: Clay loam pH 7.0")
    st.write("Best: Aloe hardy survives -8C with plastic, Spekboom, Moringa dies outside pot only")
    st.write("Frost: Worst -8C Solution tunnel R2000 plastic or Moringa inside house Oct Apr")
    st.write("Problem: Frost kills Lemongrass Moringa Solution grow Aloe Spekboom only outside")
    st.write("Market: Farmers Aloe gel cattle wounds R80 litre")

else:
    st.subheader("9. NORTHERN CAPE Kimberley Upington")
    st.write("Climate: Hottest 40C coldest -6C desert rain 200mm")
    st.write("Soil: Sand desert pH 8.0 alkaline poor")
    st.write("Best: Aloe desert king, Spekboom desert, Moringa borehole, Lemongrass impossible")
    st.write("Frost: -6C night Aloe Spekboom ok Moringa pot inside")
    st.write("Problem: No water Solution Spekboom lives 1 year no water")
    st.write("Market: Big Hole tourists R150 sunburn")

st.divider()
st.header("Profit 41 Bottles")
lotion = st.number_input("Lotion 200ml", value=41)
cream = st.number_input("Cream 50ml", value=100)
sales = lotion*120 + cream*95
st.metric("Profit", f"R{sales - (lotion*28 + cream*18)}")

st.write("Bare Beauty - No Cloves With Gloves - All 9 provinces now visible")
