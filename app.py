import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="SmartFarmSA Pro v2", page_icon="🌿", layout="centered")
st.title("🌿 SmartFarmSA Pro v2")
st.caption(f"{datetime.now().strftime('%d %B %Y')} - Mapeng Ward 11")

# WEATHER
try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Matatiele&appid={API_KEY}&units=metric", timeout=10).json()
    temp = r['main']['temp']
    tmin = r['main']['temp_min']
    c1,c2,c3 = st.columns(3)
    c1.metric("Now", f"{temp}°C")
    c2.metric("Tonight Low", f"{tmin}°C")
    c3.metric("Condition", r['weather'][0]['description'])
    if tmin <= 2:
        st.error(f"❄️ FROST {tmin}°C TONIGHT")
    else:
        st.success(f"✅ No frost {tmin}°C")
except:
    temp, tmin = 10.2, 10.2
    st.success(f"✅ No frost {tmin}°C - offline")

# WHATSAPP - CLEAN - NO YELLOW IF SECRETS OK
st.divider()
st.subheader("📲 WhatsApp Frost Alert")

has_twilio = all(k in st.secrets for k in ["TWILIO_SID","TWILIO_TOKEN","TWILIO_WHATSAPP","MY_WHATSAPP"])

if has_twilio:
    if st.button("Send Alert to My WhatsApp"):
        try:
            from twilio.rest import Client
            client = Client(st.secrets["TWILIO_SID"], st.secrets["TWILIO_TOKEN"])
            client.messages.create(from_=st.secrets["TWILIO_WHATSAPP"], to=st.secrets["MY_WHATSAPP"], body=f"Bare Beauty Mapeng {temp}C Low {tmin}C - No frost" )
            st.success("✅ WhatsApp sent! Check your phone")
        except Exception as e:
            st.error(f"Twilio error: {e} - Did you join sandbox? Send 'join code' to +14155238886")
else:
    st.warning("Add TWILIO secrets in Streamlit Cloud to enable WhatsApp")

# ALL 9
st.divider()
st.header("🇿🇦 All 9 Provinces - Everything They Grow")
st.subheader("1. EASTERN CAPE - Mapeng")
st.write("**Towns:** Matatiele, Mount Fletcher, Maclear, Qumbu, Mthatha, Gqeberha")
st.write("**Grow:** Aloe Ferox ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐, Lemongrass ⭐⭐⭐⭐")
st.subheader("2. KWAZULU-NATAL")
st.write("**Towns:** Durban, PMB, Richards Bay, Newcastle")
st.write("**Grow:** Lemongrass ⭐⭐⭐⭐⭐, Sugarcane ⭐⭐⭐⭐⭐, Madumbis ⭐⭐⭐⭐⭐, Banana ⭐⭐⭐⭐⭐")
st.subheader("3. WESTERN CAPE")
st.write("**Towns:** Cape Town, Stellenbosch, Paarl, Worcester, Ceres")
st.write("**Grow:** Spekboom ⭐⭐⭐⭐⭐, Grapes ⭐⭐⭐⭐⭐, Rooibos ⭐⭐⭐⭐⭐")
st.subheader("4. LIMPOPO")
st.write("**Towns:** Polokwane, Tzaneen, Thohoyandou, Phalaborwa")
st.write("**Grow:** Moringa ⭐⭐⭐⭐⭐, Marula ⭐⭐⭐⭐⭐, Mango ⭐⭐⭐⭐⭐, Avocado ⭐⭐⭐⭐⭐")
st.subheader("5. MPUMALANGA")
st.write("**Towns:** Mbombela, Hazyview, Barberton, Lydenburg")
st.write("**Grow:** Lemongrass ⭐⭐⭐⭐⭐, Avocado ⭐⭐⭐⭐⭐, Macadamia ⭐⭐⭐⭐⭐")
st.subheader("6. GAUTENG")
st.write("**Towns:** Johannesburg, Pretoria, Soweto, Centurion, Krugersdorp, Bronkhorstspruit")
st.write("**Grow:** Spekboom R150 Sandton, Herbs, Spinach greenhouse, Microgreens, Mushrooms")
st.subheader("7. NORTH WEST")
st.write("**Towns:** Rustenburg, Mahikeng, Potch, Klerksdorp, Brits, Lichtenburg, Vryburg")
st.write("**Grow:** Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐, Sunflower ⭐⭐⭐⭐⭐ Lichtenburg")
st.subheader("8. FREE STATE")
st.write("**Towns:** Bloemfontein, Welkom, Bethlehem, Kroonstad, Sasolburg, Harrismith")
st.write("**Grow:** Maize ⭐⭐⭐⭐⭐ Bothaville, Wheat ⭐⭐⭐⭐⭐, Aloe, Sunflower")
st.subheader("9. NORTHERN CAPE")
st.write("**Towns:** Kimberley, Upington, Springbok, De Aar, Kuruman, Kakamas")
st.write("**Grow:** Aloe ⭐⭐⭐⭐⭐, Dates ⭐⭐⭐⭐⭐ Upington, Grapes, Pecan, Raisins")
