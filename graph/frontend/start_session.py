import tkinter as tk
from PIL import Image, ImageTk
import direction as d
import os

# Tamaño de la ventana
VENTANA_ANCHO = 450
VENTANA_ALTO = 600

# Carpeta de imágenes
CARPETA_IMAGENES = "graphics"

def login_window(parent):
    login_root = tk.Toplevel(parent)
    login_root.title("Inicio de Sesión")
    login_root.geometry(f"{VENTANA_ANCHO}x{VENTANA_ALTO}")
    login_root.resizable(False, False)

    # ==== Fondo ====
    ruta_fondo = os.path.join(CARPETA_IMAGENES, "login.png")
    fondo_img = Image.open(ruta_fondo).resize((VENTANA_ANCHO, VENTANA_ALTO))
    fondo_photo = ImageTk.PhotoImage(fondo_img)

    canvas = tk.Canvas(login_root, width=VENTANA_ANCHO, height=VENTANA_ALTO)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=fondo_photo, anchor="nw")

    # ==== Función de login ====
    def hacer_login():
        login_root.destroy()
        parent.destroy()
        d.main()

    # ==== Botón (imagen) ====
    ruta_boton_login = os.path.join(CARPETA_IMAGENES, "start.png")
    boton_img = ImageTk.PhotoImage(Image.open(ruta_boton_login).resize((300, 60)))
    boton = tk.Button(login_root, image=boton_img, command=hacer_login, borderwidth=0, bg="#ffffff", highlightthickness=0)
    canvas.create_window(VENTANA_ANCHO // 2, VENTANA_ALTO - 50, window=boton)

    # ==== Mantener imágenes referenciadas ====
    login_root.fondo_photo = fondo_photo
    login_root.boton_img = boton_img

def main():
    root = tk.Tk()
    root.title("Gravo - Inicio")
    root.geometry(f"{VENTANA_ANCHO}x{VENTANA_ALTO}")
    root.resizable(False, False)

    # ==== Fondo ====
    ruta_fondo = os.path.join(CARPETA_IMAGENES, "start_session.png")
    fondo_img = Image.open(ruta_fondo).resize((VENTANA_ANCHO, VENTANA_ALTO))
    fondo_photo = ImageTk.PhotoImage(fondo_img)

    canvas = tk.Canvas(root, width=VENTANA_ANCHO, height=VENTANA_ALTO)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=fondo_photo, anchor="nw")

    # ==== Funciones ====
    def exit_app():
        root.destroy()

    def login():
        login_window(root)  # Abre la ventana personalizada

    # ==== Botones con imagen ====
    ruta_boton_login = os.path.join(CARPETA_IMAGENES, "begin.png")
    ruta_boton_exit = os.path.join(CARPETA_IMAGENES, "exit.png")
    btn_login_img = ImageTk.PhotoImage(Image.open(ruta_boton_login).resize((300, 60)))
    btn_exit_img = ImageTk.PhotoImage(Image.open(ruta_boton_exit).resize((300, 60)))

    btn_login = tk.Button(root, image=btn_login_img, command=login, borderwidth=0, bg="#ffffff", highlightthickness=0)
    btn_exit = tk.Button(root, image=btn_exit_img, command=exit_app, borderwidth=0, bg="#ffffff", highlightthickness=0)

    canvas.create_window(VENTANA_ANCHO // 2, VENTANA_ALTO - 150, window=btn_login)
    canvas.create_window(VENTANA_ANCHO // 2, VENTANA_ALTO - 80, window=btn_exit)

    # ==== Mantener referencias ====
    root.fondo_photo = fondo_photo
    root.btn_login_img = btn_login_img
    root.btn_exit_img = btn_exit_img

    root.mainloop()

if __name__ == "__main__":
    main()
