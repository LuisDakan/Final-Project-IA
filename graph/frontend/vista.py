import tkinter as tk
from tkinter import messagebox
import direction as d

def main(user_direction):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Resultados Cercanos")
    root.geometry("400x300")

    # Frame para la sección de "Resultados Más Cercanos"
    frame_results = tk.Frame(root)
    frame_results.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Título de la sección
    label_title = tk.Label(frame_results, text="Resultados Más Cercanos", font=("Arial", 14, "bold"))
    label_title.pack(pady=5)

    # Listbox para mostrar la lista de resultados
    listbox_results = tk.Listbox(frame_results, font=("Arial", 12))
    listbox_results.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Frame para los botones de acción
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=10)

    def buscar_resultados():
    # Este es un ejemplo de resultados; en una aplicación real, aquí se 
    # invocaría la lógica para obtener los resultados más cercanos.
        resultados = [
            "Restaurante A - 0.5 km",
            "Cafetería B - 0.8 km",
            "Tienda C - 1.0 km",
        ]
    # Limpiar los resultados previos
        listbox_results.delete(0, tk.END)
        for resultado in resultados:
            listbox_results.insert(tk.END, resultado)

    def salir():
        root.destroy()
        d.main()

    # Botón para simular la búsqueda de resultados
    btn_buscar = tk.Button(frame_buttons, text="Buscar", font=("Arial", 12, "bold"), command=buscar_resultados, bg="lightgreen")
    btn_buscar.pack(side=tk.LEFT, padx=10)

    # Botón para salir de la aplicación
    btn_salir = tk.Button(frame_buttons, text="Salir", font=("Arial", 12, "bold"), command=salir, bg="tomato")
    btn_salir.pack(side=tk.LEFT, padx=10)

    root.mainloop()