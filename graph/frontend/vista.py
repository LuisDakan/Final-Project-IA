import tkinter as tk
from PIL import Image, ImageTk
import direction as d
import os
import random
import sys
import osmnx as om
import googlemaps
import math
sys.path.append(os.path.dirname(os.getcwd()))


import backend as bk


graf=bk.Graph()

VENTANA_ANCHO = 450
VENTANA_ALTO = 600
CARPETA_IMAGENES = "graphics"
CARPETA_COMIDA = os.path.join(CARPETA_IMAGENES, "food")  # Carpeta con imágenes aleatorias

# ==== Cargar imágenes automáticamente desde la carpeta food/ ====
IMAGENES_RESTAURANTES = [f for f in os.listdir(CARPETA_COMIDA) if f.lower().endswith(".jpg")]

def abrir_ventana_detalle(nombre_restaurante,index):
    detalle = tk.Toplevel()
    detalle.title(f"Detalles de {nombre_restaurante}")
    detalle.geometry("400x500")
    detalle.resizable(False, False)

    # ==== Fondo personalizado ====
    ruta_fondo = os.path.join(CARPETA_IMAGENES, "restaurant_background.png")
    fondo_img = Image.open(ruta_fondo).resize((400, 500))  # ancho = 400, alto = 500
    fondo_photo = ImageTk.PhotoImage(fondo_img)

    canvas = tk.Canvas(detalle, width=400, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=fondo_photo, anchor="nw")

    # ==== Imagen aleatoria del restaurante ====
    imagen_aleatoria = random.choice(IMAGENES_RESTAURANTES)
    ruta_imagen = os.path.join(CARPETA_COMIDA, imagen_aleatoria)



    img_rest = Image.open(ruta_imagen).resize((170, 230))  # ancho = 170, alto = 230
    rest_photo = ImageTk.PhotoImage(img_rest)

    canvas.create_image(200, 295, image=rest_photo, anchor="center")  # posición X = 200, Y = 295

    # ==== Título con nombre del restaurante ====
    canvas.create_text(200, 124, text=nombre_restaurante, font=("Helvetica", 16, "bold"), fill="white")

    # ==== Función de confirmar ====
    def confirmar_seleccion():
        print(f"Your order was placed: {nombre_restaurante}")
        detalle.destroy()
        #detalle.master.destroy()
        graf.print_path(graf.geo.general_rest_index[index])



    # ==== Botones con imágenes ====
    confirmar_img = ImageTk.PhotoImage(Image.open(os.path.join(CARPETA_IMAGENES, "order.png")).resize((60, 60)))
    regresar_img = ImageTk.PhotoImage(Image.open(os.path.join(CARPETA_IMAGENES, "last_exit.png")).resize((60, 60)))

    btn_confirmar = tk.Button(detalle, image=confirmar_img, command=confirmar_seleccion,
                              borderwidth=0, bg="#ffffff", highlightthickness=0)
    btn_regresar = tk.Button(detalle, image=regresar_img, command=detalle.destroy,
                             borderwidth=0, bg="#ffffff", highlightthickness=0)

    canvas.create_window(10, 490, window=btn_confirmar, anchor="sw")
    canvas.create_window(70, 490, window=btn_regresar, anchor="sw")

    # ==== Referencias para evitar garbage collection ====
    detalle.fondo_photo = fondo_photo
    detalle.rest_photo = rest_photo
    detalle.confirmar_img = confirmar_img
    detalle.regresar_img = regresar_img


def main(user_direction):

    global graf
    graf.set_source(user_direction)
    root = tk.Tk()
    root.title("Nearby Restaurants")
    root.geometry(f"{VENTANA_ANCHO}x{VENTANA_ALTO}")
    root.resizable(False, False)

    # ==== Fondo ====
    ruta_fondo = os.path.join(CARPETA_IMAGENES, "vista.png")
    fondo_img = Image.open(ruta_fondo).resize((VENTANA_ANCHO, VENTANA_ALTO))
    fondo_photo = ImageTk.PhotoImage(fondo_img)

    canvas = tk.Canvas(root, width=VENTANA_ANCHO, height=VENTANA_ALTO)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=fondo_photo, anchor="nw")

    # ==== Mostrar botones de restaurantes ====
    def mostrar_resultados():
        tot=4
        resultados=[]
        index=[]
        for distance,rest in graf.query_near_rest(tot):
            resultados.append(f"Rest. {graf.geo.get_info_rest(rest)}- {distance/1000:.5f} km")
            index.append(rest)
        y_inicial = 150
        for i, nombre in enumerate(resultados):
            btn = tk.Button(root, text=nombre, font=("Helvetica", 12, "bold"),
                            bg="#ffffff", fg="#000000", width=30, height=2, relief="raised",
                            command=lambda n=nombre,idx=i: abrir_ventana_detalle(n,index[idx]))
            canvas.create_window(VENTANA_ANCHO // 2, y_inicial + i * 80, window=btn)

    # ==== Botón salir ====
    def salir():
        root.destroy()
        d.main()

    # ==== Botón buscar resultados ====
    ruta_boton_buscar = os.path.join(CARPETA_IMAGENES, "search_view.png")
    btn_buscar_img = ImageTk.PhotoImage(Image.open(ruta_boton_buscar).resize((300, 60)))
    btn_buscar = tk.Button(root, image=btn_buscar_img, command=mostrar_resultados,
                           borderwidth=0, bg="#ffffff", highlightthickness=0)
    canvas.create_window(VENTANA_ANCHO // 2, 490, window=btn_buscar)

    # ==== Botón salir ====
    ruta_boton_salir = os.path.join(CARPETA_IMAGENES, "exit.png")
    btn_salir_img = ImageTk.PhotoImage(Image.open(ruta_boton_salir).resize((300, 60)))
    btn_salir = tk.Button(root, image=btn_salir_img, command=salir,
                          borderwidth=0, bg="#ffffff", highlightthickness=0)
    canvas.create_window(VENTANA_ANCHO // 2, VENTANA_ALTO - 50, window=btn_salir)

    # ==== Mantener referencias ====
    root.fondo_photo = fondo_photo
    root.btn_buscar_img = btn_buscar_img
    root.btn_salir_img = btn_salir_img

    root.mainloop()
