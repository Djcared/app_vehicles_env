import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Título de la app
st.header("Dashboard de anuncios de venta de coches")

# Cargar datos
car_data = pd.read_csv("C:\\Users\\User\\Desktop\\Nueva carpeta\\vehicles_us.csv")

# Casillas de verificación
build_histogram = st.checkbox('Construir histograma del odómetro')
build_scatter = st.checkbox('Construir gráfico de dispersión (precio vs odómetro)')

if build_histogram:
    st.write('Histograma del odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Gráfico de dispersión: Precio vs Odómetro')
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs Odómetro'
    )
    st.plotly_chart(fig, use_container_width=True)