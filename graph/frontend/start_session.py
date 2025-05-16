import tkinter as tk
from tkinter import messagebox
import direction as d

def main():

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gravo - Inicio de Sesión")
    root.geometry("300x250")

    # Frame para los botones
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=20)

    btn_options = {
        "width": 12,
        "height": 2,
        "font": ("Arial", 12, "bold"),
        "bg": "lightblue",
        "fg": "black",
        "bd": 3,
        "relief": "raised"
    }
    def exit_app():
        root.destroy()

    def login():
        messagebox.showinfo("Login", f"Bienvenido usuario!")
        root.destroy()
        d.main()
    # Botón "Entrar"
    btn_login = tk.Button(frame_buttons, text="Entrar", command=login,**btn_options)
    btn_login.pack(side=tk.LEFT, padx=10)

    # Botón "Exit"
    btn_exit = tk.Button(frame_buttons, text="Exit", command=exit_app,**btn_options)
    btn_exit.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__=="__main__":
    main()

