import tkinter as tk
from PIL import Image, ImageTk
import start_session as ss
import vista as v
import os

# Tamaño de la ventana
VENTANA_ANCHO = 450
VENTANA_ALTO = 600
CARPETA_IMAGENES = "graphics"

def main():
    root = tk.Tk()
    root.title("Gravo - Dirección")
    root.geometry(f"{VENTANA_ANCHO}x{VENTANA_ALTO}")
    root.resizable(False, False)

    # ====== Fondo ======
    ruta_fondo = os.path.join(CARPETA_IMAGENES, "direction.png")  # Usa tu imagen de fondo aquí
    fondo_img = Image.open(ruta_fondo).resize((VENTANA_ANCHO, VENTANA_ALTO))
    fondo_photo = ImageTk.PhotoImage(fondo_img)

    canvas = tk.Canvas(root, width=VENTANA_ANCHO, height=VENTANA_ALTO)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=fondo_photo, anchor="nw")

    # ====== Campo para ingresar dirección ======
    entry_address = tk.Entry(root, font=("Helvetica", 14), width=30, justify="center")
    canvas.create_window(VENTANA_ANCHO // 2, VENTANA_ALTO // 2, window=entry_address)

    # ====== Funciones ======
    def submit_address():
        address = entry_address.get()
        if address.strip() == "":
            # Aquí podrías hacer una alerta más bonita si lo deseas
            print("Por favor, ingresa una dirección.")
        else:
            root.destroy()
            v.main(address)

    def exit_app():
        root.destroy()
        ss.main()

    # ====== Botones ======
    ruta_boton_enviar = os.path.join(CARPETA_IMAGENES, "search.png")     # Imagen para botón enviar
    ruta_boton_salir = os.path.join(CARPETA_IMAGENES, "exit.png")      # Imagen para botón volver/salir

    btn_send_img = ImageTk.PhotoImage(Image.open(ruta_boton_enviar).resize((180, 45)))
    btn_exit_img = ImageTk.PhotoImage(Image.open(ruta_boton_salir).resize((300, 60)))

    btn_send = tk.Button(root, image=btn_send_img, command=submit_address,
                         borderwidth=0, bg="#ffffff", highlightthickness=0)
    btn_exit = tk.Button(root, image=btn_exit_img, command=exit_app,
                         borderwidth=0, bg="#ffffff", highlightthickness=0)

    canvas.create_window(VENTANA_ANCHO // 2, VENTANA_ALTO - 250, window=btn_send)
    canvas.create_window(VENTANA_ANCHO // 2, VENTANA_ALTO - 50, window=btn_exit)

    # ====== Referencias para evitar que se liberen ======
    root.fondo_photo = fondo_photo
    root.btn_send_img = btn_send_img
    root.btn_exit_img = btn_exit_img

    root.mainloop()
