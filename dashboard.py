import streamlit as st
import pandas as pd

st.title("Energy Data Dashboard")

# Dummy data example
data = {
    "timestamp": ["2025-06-09T17:07:25", "2025-06-09T17:12:26"],
    "site_id": ["site_001", "site_002"],
    "energy_generated_kwh": [120.5, 98.3],
    "energy_consumed_kwh": [100.2, 110.1],
}
df = pd.DataFrame(data)
df["net_energy_kwh"] = df["energy_generated_kwh"] - df["energy_consumed_kwh"]

st.dataframe(df)
st.line_chart(df.set_index("timestamp")[["energy_generated_kwh", "energy_consumed_kwh", "net_energy_kwh"]])
