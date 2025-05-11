import os
import tkinter as tk
from tkinterhtml import HtmlFrame
import googlemaps
from datetime import datetime
from flask import Flask, render_template

gmaps = googlemaps.Client(key=os.getenv("API_KEY_GOOGLE"))

coordenadas=(19.4034471, -99.1710897)

resultado = gmaps.reverse_geocode(coordenadas)

# Extrae la dirección del resultado
if resultado:
    direccion = resultado[0]['formatted_address']
    print(f"Dirección: {direccion}")
else:
    print("No se encontraron resultados para las coordenadas proporcionadas.")