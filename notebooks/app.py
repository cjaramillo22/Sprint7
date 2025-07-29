#1. Importar librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el CSV desde la ruta local
car_data = pd.read_csv('C:/Users/carlo/OneDrive/Escritorio/Proyecto Sprint 7/vehicles_us.csv')

# Título de la aplicación
st.header("Cuadro de Mandos de Vehículos en USA")

# Botón 1: Histograma del odómetro
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches (kilometraje).')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón 2: Gráfico de dispersión odómetro vs precio
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre el precio del vehículo y su kilometraje (odómetro).')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

    ####################

    import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el CSV desde la ruta local
car_data = pd.read_csv('C:/Users/carlo/OneDrive/Escritorio/Proyecto Sprint 7/vehicles_us.csv')

# Título de la aplicación
st.header("Cuadro de Mandos de Vehículos en EE. UU.")

# Casilla de verificación 1: Histograma del odómetro
show_hist = st.checkbox('Construir histograma del odómetro')

if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches (kilometraje).')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación 2: Gráfico de dispersión odómetro vs precio
show_scatter = st.checkbox('Construir gráfico de dispersión odómetro vs precio')

if show_scatter:
    st.write('Relación entre el precio del vehículo y su kilometraje (odómetro).')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)