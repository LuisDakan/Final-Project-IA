import os
import tkinter as tk
from tkinterhtml import HtmlFrame
import googlemaps
from datetime import datetime
from flask import Flask, render_template

gmaps = googlemaps.Client(key=os.getenv("API_KEY_GOOGLE"))

direccion="Sobre Av. División del Norte y Tehuantepec, código 2, Escandón II Secc, 06100 Ciudad de México, CDMX, Mexico"
resultado=gmaps.geocode(direccion)

# Extrae la latitud y longitud del resultado
if resultado:
    ubicacion = resultado[0]['geometry']['location']
    latitud = ubicacion['lat']
    longitud = ubicacion['lng']
    print(f"Latitud: {latitud}, Longitud: {longitud}")
else:
    print("No se encontraron resultados para la dirección proporcionada.")