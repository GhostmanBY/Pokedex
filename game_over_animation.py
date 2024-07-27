import customtkinter as ctk
import time

def game_over():
    # Configuración de la ventana principal
    root = ctk.CTk()
    root.geometry("400x300")
    root.title("Game Over")
    root.configure(fg_color="black")  # Fondo negro para un aspecto retro

    # Crear el label para el texto "Game Over"
    game_over_label = ctk.CTkLabel(root, text="GAME OVER", font=("Press Start 2P", 36), text_color="red")
    game_over_label.place(relx=0.5, rely=0.5, anchor="center")

    # Función para hacer parpadear el texto
    def blink():
        for _ in range(5):  # Parpadea 5 veces
            game_over_label.configure(text_color="black")
            root.update()
            time.sleep(0.5)
            game_over_label.configure(text_color="red")
            root.update()
            time.sleep(0.5)
        root.after(2000, root.destroy)
    root.after(1000,blink)

    root.mainloop()