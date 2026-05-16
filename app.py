import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIG
st.set_page_config(
    page_title="Uber/Ola Ride Analytics",
    layout="wide"
)

# CSS

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(
        135deg,
        #0f0f0f,
        #1a1a1a,
        #111111
    );
    color: white;
}

/* DASHBOARD TITLE */
.main-title {
    font-size: 45px;
    font-weight: bold;
    color: #FFD700;
    text-align: center;
    margin-bottom: 30px;
    text-shadow: 2px 2px 15px rgba(255,215,0,0.5);
}

/* KPI CARDS */
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    transition: 0.3s ease-in-out;
}

/* KPI HOVER EFFECT */
[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 35px rgba(255,215,0,0.25);
}

/* CHART CONTAINER */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* SUBHEADINGS */
h2, h3 {
    color: #FFD700;
    font-weight: bold;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #111111;
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: black;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

/* BUTTON HOVER */
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #FFA500, #FFD700);
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #111;
}

::-webkit-scrollbar-thumb {
    background: #FFD700;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    '<div class="main-title">🚖 Uber/Ola Ride Analytics Dashboard</div>',
    unsafe_allow_html=True
)

# LOAD DATA
df = pd.read_csv("sample_uber_data.csv")

# KPI SECTION
total_revenue = df['fare_amount'].sum()
total_trips = len(df)
avg_rating = df['driver_rating'].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Trips", total_trips)
col3.metric("Avg Driver Rating", round(avg_rating, 2))

# PEAK BOOKING HOURS
st.subheader("📊 Peak Booking Hours")

hour_chart = df.groupby('hour').size().reset_index(name='rides')

fig = px.bar(
    hour_chart,
    x='hour',
    y='rides',
    title='Peak Booking Hours'
)

st.plotly_chart(fig, use_container_width=True)

# VEHICLE TYPE ANALYSIS
st.subheader("🚗 Vehicle Type Distribution")

vehicle_chart = px.pie(
    df,
    names='vehicle_type',
    title='Vehicle Distribution'
)

st.plotly_chart(vehicle_chart, use_container_width=True)

# RIDE STATUS
st.subheader("❌ Ride Status Analysis")

status_chart = px.pie(
    df,
    names='ride_status',
    title='Ride Status'
)

st.plotly_chart(status_chart, use_container_width=True)

# GEO MAP
st.subheader("🌍 Ride Hotspots")

map_data = df.rename(columns={
    'pickup_latitude': 'lat',
    'pickup_longitude': 'lon'
})

st.map(map_data[['lat', 'lon']])
