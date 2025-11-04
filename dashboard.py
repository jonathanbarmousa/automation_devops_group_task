import streamlit as st
import pandas as pd
from get_api import get_weather_data

cities = {
    "Stockholm": {"lat": 59.3293, "lon": 18.0686},
    "Oslo": {"lat": 59.9139, "lon": 10.7522},
    "Köpenhamn": {"lat": 55.6761, "lon": 12.5683},
    "Helsingfors": {"lat": 60.1699, "lon": 24.9384},
    "Berlin": {"lat": 52.5200, "lon": 13.4050},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Rom": {"lat": 41.9028, "lon": 12.4964},
    "Warszawa": {"lat": 52.2297, "lon": 21.0122}
}

st.title("Weather Dashboard")
selected_city = st.selectbox("Välj stad", list(cities.keys()), index=0)
lat = cities[selected_city]["lat"]
lon = cities[selected_city]["lon"]

st.subheader(f"Dagliga väderdata för {selected_city}")

with st.spinner("Hämtar väderdata..."):
    df = get_weather_data(lat, lon)

st.dataframe(df, use_container_width=True)

st.line_chart(df.set_index("date")[["Max Temperatur (°C)", "Min Temperatur (°C)"]])