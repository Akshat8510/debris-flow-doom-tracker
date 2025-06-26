import streamlit as st
from streamlit_folium import st_folium
import folium
import random

st.set_page_config(layout="wide")
st.title("🔥 Click-Based Debris Flow Predictor – Bring the Doom")

# Initial map setup
start_coords = [31.705, 76.9326]
m = folium.Map(location=start_coords, zoom_start=8)

# Color/risk mapping
risk_levels = {
    "Low": {"color": "green", "comments": ["Chill zone 😎", "You're safe... for now!", "No landslides, just landsights 🌄"]},
    "Medium": {"color": "orange", "comments": ["Slight chaos ☁️", "Could go either way 🤷‍♂️", "You’re flirting with nature"]},
    "High": {"color": "red", "comments": ["RUN. NOW. 🏃‍♀️💨", "Why did you even click here?!", "Kaboom incoming! 💥"]}
}

def get_risk_level():
    return random.choice(list(risk_levels.keys()))

# Store click info
clicked_data = st_folium(m, width=1000, height=600)

# Process click
if clicked_data and clicked_data.get("last_clicked"):
    lat = clicked_data["last_clicked"]["lat"]
    lon = clicked_data["last_clicked"]["lng"]
    
    # Generate risk
    level = get_risk_level()
    color = risk_levels[level]["color"]
    message = random.choice(risk_levels[level]["comments"])
    
    # Add a dramatic popup marker
    folium.Marker(
        location=[lat, lon],
        popup=f"💀 {level} Risk: {message}",
        tooltip="🔥 You clicked here!",
        icon=folium.Icon(color=color)
    ).add_to(m)

    # Show again with updated marker
    st_folium(m, width=1000, height=600)

    # Also show on sidebar/panel
    with st.sidebar:
        st.header("📍 Risk Report")
        st.success(f"Location: `{lat:.4f}, {lon:.4f}`")
        st.warning(f"⚠️ Risk Level: `{level}`")
        st.info(f"💬 Comment: {message}")
else:
    st.info("🖱️ Click on the map to drop chaos. We'll warn you instantly.")

