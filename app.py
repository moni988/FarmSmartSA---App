import Streamlit as st
    st.set_page_config(page_title="FarmSmartSA", page_icon="🌾")
    st.title("🌾 FarmSmartSA")
    st.write("Weather and farming tips for SA farmers")
    
    province = st.selectbox("Select Province", ["Gauteng", "KZN", "Western Cape", "Eastern Cape", "Free State"])
    
    if st.button("Get Tips"):
        st.success(f"Farming tips for {province}:")
        st.write("- Check weather forecast this week")
        st.write("- Test soil moisture before planting")
        st.write("- Watch for pests after rain")
