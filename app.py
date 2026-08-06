import streamlit as st

# Page setup with color
st.set_page_config(page_title="FarmSmartSA", page_icon="🌾", layout="wide")

# Add some color with CSS
st.markdown("""
    <style>
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }
    h1 {
        color: #1B5E20;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌾 FarmSmartSA")
st.write("Weather and farming tips for SA farmers")

# Show an image of South Africa farming
st.image("IMG-20260805-WA4690.jpg", caption="Powered by Farmers, Built for App SA")
# FARMING TIPS SECTION
st.subheader("🌱 Today's Farming Tips")

col1, col2 = st.columns(2)

with col1:
    st.info("**Watering Tip**\n\nMorning is best! Water between 6am-9am.")

with col2:
    st.success("**Soil Tip**\n\nCheck soil 2 inches down. If dry, water.")

st.warning("**Weather Watch**\n\nMulch around crops to keep roots cool.")

st.divider()
# ALL 9 PROVINCES
provinces = [
    "Gauteng", "KwaZulu-Natal", "Western Cape", "Eastern Cape", 
    "Limpopo", "Mpumalanga", "North West", "Free State", "Northern Cape"
]
province = st.selectbox("Select Province", provinces)

if st.button("Get Tips"):
    st.success(f"🌱 Farming tips for {province}")
    
    if province == "KwaZulu-Natal":
        st.write("- Plant sugarcane and maize in summer")
        st.write("- Watch for heavy rains and flooding")
        st.write("- Test soil for acidity")
    elif province == "Western Cape":
        st.write("- Grape and wine farming season")
        st.write("- Irrigation important - watch water levels")
        st.write("- Plant wheat in winter")
    elif province == "Limpopo":
        st.write("- Citrus and avocado farming")
        st.write("- Prepare for hot, dry conditions")
        st.write("- Irrigate early morning")
    else:
        st.write("- Check weather forecast daily")
        st.write("- Test soil moisture")
        st.write("- Watch for pests and diseases")
        import requests

st.markdown("---")
st.subheader("🌤️ Live Weather for " + province)

API_KEY = "b6a9082fddf3edfdb3c8903722f60c71"

city_map = {
    "Gauteng": "Johannesburg",
    "KwaZulu-Natal": "Durban",
    "Western Cape": "Cape Town",
    "Eastern Cape": "Gqeberha",
    "Limpopo": "Polokwane",
    "Mpumalanga": "Nelspruit",
    "North West": "Rustenburg",
    "Free State": "Bloemfontein",
    "Northern Cape": "Kimberley"
}

city = city_map[province]
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    st.metric("Temperature", f"{temp}°C")
    st.write(f"**Condition:** {desc}")
except:
    st.info("Weather loading... Key activates in 20 min or check internet")
