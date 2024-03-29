import streamlit as st
import requests
import altair as alt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Visualisation Playground", layout="wide")
st.title("Visualisation Playground")

############################################################################
st.header("Using the Metrics Label")
cities = ['London', 'Salt Lake City', 'New Jersey', 'Orlando']

with st.expander("Weather Metrics"):
    with st.spinner('Loading Weather Data'):
        city_cols = st.columns(4)
        for i, city in enumerate(cities):
            if city not in st.session_state:
                city_url = city.replace(" ", "_")
                st.session_state[city] = requests.get(f"https://wttr.in/{city_url}?format=%t").text

            city_cols[i].metric(label=f"{city} Temperature", value=st.session_state[city])
            
    st.snow()
    
############################################################################
# Generate sample data for scatterplots
np.random.seed(42)
n = 100
data = pd.DataFrame({
    'x': np.random.randn(n),
    'y': np.random.randn(n),
    'c': np.random.randint(0, 2, n)
})
st.write('data generated')

# Altair charts
st.header("Altair Charts")
scatter_plot = alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    color='c:N'
)
st.altair_chart(scatter_plot, use_container_width=True)

# Seaborn charts
st.header("Seaborn Charts")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='x', y='y', hue='c', ax=ax)
ax.set_facecolor('none')
st.pyplot(fig)

# Matplotlib charts
st.header("Matplotlib Charts")
fig, ax = plt.subplots()
scatter = ax.scatter(data['x'], data['y'], c=data['c'], cmap='viridis')
legend1 = ax.legend(*scatter.legend_elements(), title="Categories")
ax.add_artist(legend1)
st.pyplot(fig)

# Plotly Chart
st.subheader("Plotly Charts")
# Create a scatter plot using Plotly
fig = px.scatter(data, x='x', y='y', color='c')
st.plotly_chart(fig)