import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="FarmSmartSA 9-Module", page_icon="🌿", layout="wide")
st.title("🌿 FarmSmartSA - 9 Module System")
st.caption(f"Matatiele Mapeng Ward 11 | {datetime.now().strftime('%d %B %Y')} | Green+Gold+White")

# --- SECRETS ---
try:
    API_KEY = st.secrets["WEATHER_API_KEY"]
except:
    API_KEY = "b6a9082fddf3edfdb3c8903722f60c71"

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "🌤️ 7-Day Weather", "🌍 All Provinces", "🌿 Plant Scanner", "🌱 Soil Scanner",
    "📚 Soil Library", "👨‍🌾 Ask Expert", "🛰️ OSINT", "🚨 Disaster Alerts", "💰 Business"
])

# MODULE 1: 7-DAY WEATHER WHOLE WEEK
with tab1:
    st.header("🌤️ 7-Day Weather - All Access")
    province_coords = {
        "Eastern Cape - Matatiele": (-30.3396, 28.7992),
        "KZN - Durban": (-29.8587, 31.0218),
        "Western Cape - Cape Town": (-33.9249, 18.4241),
        "Limpopo - Polokwane": (-23.9045, 29.4689),
        "Mpumalanga - Nelspruit": (-25.4753, 30.9694),
        "Gauteng - Johannesburg": (-26.2041, 28.0473),
        "North West - Rustenburg": (-25.6678, 27.2419),
        "Free State - Bloemfontein": (-29.0852, 26.1596),
        "Northern Cape - Kimberley": (-28.7282, 24.7499)
    }
    selected_prov = st.selectbox("Choose Province for 7-Day", list(province_coords.keys()))
    lat, lon = province_coords[selected_prov]

    col_a, col_b = st.columns(2)
    with col_a:
        # OpenWeather 7-Day
        st.subheader("OpenWeatherMap 7-Day")
        url_ow = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&units=metric&appid={API_KEY}"
        try:
            r = requests.get(url_ow, timeout=10).json()
            for day in r['daily'][:7]:
                date = datetime.fromtimestamp(day['dt']).strftime('%a %d %b')
                st.write(f"**{date}**: {day['weather'][0]['description']} | {day['temp']['min']}°C - {day['temp']['max']}°C | Rain {day.get('pop',0)*100:.0f}% | Humidity {day['humidity']}%")
        except:
            st.warning("Add WEATHER_API_KEY in Secrets for OpenWeather 7-day. Using Open-Meteo backup below.")

    with col_b:
        # Open-Meteo Free - Uses SAWS model (No Key Needed)
        st.subheader("SAWS-based Free API (Open-Meteo)")
        url_om = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability,precipitation_sum,wind_speed_10m_max,weathercode&timezone=Africa/Johannesburg&forecast_days=7"
        try:
            d = requests.get(url_om, timeout=10).json()
            for i in range(7):
                date = d['daily']['time'][i]
                st.write(f"**{date}**: Max {d['daily']['temperature_2m_max'][i]}°C / Min {d['daily']['temperature_2m_min'][i]}°C | Rain {d['daily']['precipitation_probability'][i]}% | {d['daily']['precipitation_sum'][i]}mm")
        except Exception as e:
            st.error(f"Weather offline: {e}")

# MODULE 2: ALL 9 PROVINCES
with tab2:
    st.header("🌍 All 9 Provinces - What Grows Where")
    st.info("Your base: 0.5ha PTO Mapeng Ward 11 - South=Aloe, East=Lemongrass, West/North=Spekboom, Center=Moringa")
    provinces_data = {
        "Eastern Cape": "Aloe Ferox ⭐⭐⭐⭐⭐ (south rocky), Spekboom ⭐⭐⭐⭐⭐, Lemongrass ⭐⭐⭐, Moringa ⭐⭐⭐ | Soil: Sandy loam | Delivery R20 same day Matatiele Market/Taxi Rank/JSS",
        "KZN": "Lemongrass ⭐⭐⭐⭐⭐, Moringa ⭐⭐⭐⭐⭐ | Soil: Red loam humid | Market: Durban tourists R120 | Delivery R100 Paxi",
        "Western Cape": "Spekboom ⭐⭐⭐⭐⭐, Aloe ⭐⭐⭐⭐⭐, Rooibos | Soil: Sandy windy | Market: Eco shops R200 | Delivery R100",
        "Limpopo": "Moringa ⭐⭐⭐⭐⭐, Marula oil source cheaper | Soil: Sandy very hot | Delivery R100",
        "Mpumalanga": "Lemongrass ⭐⭐⭐⭐⭐ essential oils | Soil: Loam subtropical | Market: Kruger tourists | Delivery R100",
        "Gauteng": "Spekboom pots, Aloe frost hardy | Soil: Clay frost -5°C | Best SELL Sandton R150 | Delivery R100",
        "North West": "Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐ | Soil: Sandy dry | Market: Mines dry skin | Delivery R100",
        "Free State": "Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐ | Soil: Clay -10°C frost | Only frost survivors | Delivery R100",
        "Northern Cape": "Aloe ⭐⭐⭐⭐⭐, Spekboom ⭐⭐⭐⭐⭐ | Soil: Desert | No water needed | Delivery R100"
    }
    for prov, info in provinces_data.items():
        with st.expander(prov):
            st.write(info)

# MODULE 3: PLANT SCANNER
with
