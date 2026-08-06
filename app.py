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
