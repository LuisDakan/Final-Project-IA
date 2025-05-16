import tkinter as tk
from tkinter import messagebox
import start_session as ss
import vista as v
# La función submit_address se define dentro de main para capturar entry_address por cierre


def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ingresa tu Dirección")
    root.geometry("350x180")

    # Etiqueta para indicar al usuario
    label = tk.Label(root, text="Ingresa tu dirección:", font=("Arial", 12))
    label.pack(pady=10)

    # Campo de entrada para la dirección
    entry_address = tk.Entry(root, width=40, font=("Arial", 12))
    entry_address.pack(pady=5)

    # Definir submit_address dentro de main para capturar entry_address
    def submit_address():
        address = entry_address.get()
        if address.strip() == "":
            messagebox.showwarning("Advertencia", "Por favor, ingresa una dirección")
        else:
            user_address = address
            root.destroy()
            v.main(user_address)
            


    def exit_app():
        root.destroy()
        ss.main()
    # Frame para los botones de acción
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=10)

    # Botón para enviar la dirección
    btn_submit = tk.Button(frame_buttons, text="Enviar", command=submit_address ,font=("Arial", 12, "bold"), bg="lightgreen", fg="black", bd=2, relief="raised")
    btn_submit.pack(side=tk.LEFT, padx=10)

    # Botón para salir de la aplicación
    btn_exit = tk.Button(frame_buttons, text="Salir", command=exit_app, font=("Arial", 12, "bold"), bg="tomato", fg="black", bd=2, relief="raised")
    btn_exit.pack(side=tk.LEFT, padx=10)

    root.mainloop()

