import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('notebooks/vehicles_us.csv') # leer los datos

# Encabezado de la aplicación
st.title('Análisis de Datos de Vehículos')
st.header('Exploración de Datos de Anuncios de Venta de Coches')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

scatter_button = st.button('Construir scatterplot')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un scatterplot para el conjunto de datos')
    
    # Crear un scatterplot
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Scatterplot de Odometer vs Price")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)