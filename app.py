import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="FarmSmart SA", page_icon="🌾", layout="centered")

st.title("🌾 FarmSmart SA")
st.write("Get smart farming tips + live weather for your South African province")

# Province selector
province_list = [
    "Gauteng", "KwaZulu-Natal", "Western Cape", "Eastern Cape", 
    "Limpopo", "Mpumalanga", "North West", "Free State", "Northern Cape"
]
province = st.selectbox("Select Province", province_list)

# Get Tips Button
if st.button("Get Tips", type="primary"):
    
    st.subheader(f"🌱 Farming Tips for {province}")
    
    if province == "Gauteng":
        st.write("- Maize and vegetable farming season")
        st.write("- Monitor for frost in winter")
        st.write("- Water early morning or late afternoon")
    elif province == "KwaZulu-Natal":
        st.write("- Sugarcane and banana farming")
        st.write("- Watch for heavy rains and flooding")
        st.write("- Test soil for acidity")
    elif province == "Western Cape":
        st.write("- Grape and wine farming season")
        st.write("- Irrigation important - watch water")
        st.write("- Plant wheat in winter")
    elif province == "Limpopo":
        st.write("- Citrus and avocado farming")
        st.write("- Prepare for hot, dry conditions")
        st.write("- Irrigate early morning")
    elif province == "Eastern Cape":
        st.write("- Livestock and sheep farming")
        st.write("- Prepare for coastal winds")
        st.write("- Plant drought-resistant crops")
    elif province == "Mpumalanga":
        st.write("- Citrus, nuts and subtropical fruits")
        st.write("- Watch for summer storms")
        st.write("- Good soil for maize")
    elif province == "North West":
        st.write("- Sunflower and maize farming")
        st.write("- Prepare for dry conditions")
        st.write("- Soil conservation important")
    elif province == "Free State":
        st.write("- Maize and wheat belt")
        st.write("- Watch for hail storms")
        st.write("- Good grazing for livestock")
    elif province == "Northern Cape":
        st.write("- Grape and date farming with irrigation")
        st.write("- Very hot and dry - conserve water")
        st.write("- Windbreaks important")
    else:
        st.write("- Check weather forecast daily")
        st.write("- Test soil moisture")
        st.write("- Watch for pests and diseases")

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
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            st.metric("Temperature", f"{temp}°C")
            st.write(f"**Condition:** {desc}")
            st.write(f"**Humidity:** {humidity}%")
        else:
            st.warning(f"Could not get weather. Error: {data.get('message')}")
            
    except Exception as e:
        st.info("Weather loading... Key activates in 20 min or check internet")

st.markdown("---")
st.caption("Built with FarmSmart SA | Data from OpenWeatherMap")




