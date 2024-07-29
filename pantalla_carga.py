import customtkinter as ctk
from PIL import Image, ImageTk
import time
import threading

# Variables globales
loading_window = None
progress_bar = None
tip_label = None

def show_loading_screen(master, duration=3):
    global loading_window, progress_bar, tip_label
    
    loading_window = ctk.CTkToplevel(master)
    loading_window.title("Cargando...")
    loading_window.geometry("400x300")
    loading_window.configure(fg_color="#2C3E50")  # Fondo azul oscuro

    # Centrar la ventana de carga
    loading_window.update_idletasks()
    width = loading_window.winfo_width()
    height = loading_window.winfo_height()
    x = (loading_window.winfo_screenwidth() // 2) - (width // 2)
    y = (loading_window.winfo_screenheight() // 2) - (height // 2)
    loading_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Título
    title_label = ctk.CTkLabel(
        loading_window,
        text="Cargando...",
        font=("Roboto", 24, "bold"),
        text_color="#ECF0F1"
    )
    title_label.pack(pady=(20, 10))

    # Pokébola girando
    canvas = ctk.CTkCanvas(loading_window, width=100, height=100, bg="#2C3E50", highlightthickness=0)
    canvas.pack(pady=20)

    # Dibujar una Pokébola simple
    canvas.create_oval(10, 10, 90, 90, fill="red", outline="white", width=2)
    canvas.create_line(10, 50, 90, 50, fill="white", width=2)
    canvas.create_oval(40, 40, 60, 60, fill="white", outline="black", width=2)

    # Barra de progreso
    progress_bar = ctk.CTkProgressBar(loading_window, width=300)
    progress_bar.set(0)
    progress_bar.pack(pady=20)

    # Texto de consejo
    tip_label = ctk.CTkLabel(
        loading_window,
        text="Consejo: ¡Atrapa todos los Pokémon que puedas!",
        font=("Roboto", 12),
        text_color="#ECF0F1"
    )
    tip_label.pack(pady=10)

    # Iniciar animación y progreso
    threading.Thread(target=loading_animation, args=(canvas, duration), daemon=True).start()
    threading.Thread(target=update_progress_and_tip, args=(duration,), daemon=True).start()

def loading_animation(canvas, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(0, 360, 10):
            if loading_window is None or not loading_window.winfo_exists():
                return
            canvas.delete("all")
            canvas.create_arc(10, 10, 90, 90, start=i, extent=180, fill="red", outline="white", width=2)
            canvas.create_arc(10, 10, 90, 90, start=i+180, extent=180, fill="white", outline="white", width=2)
            canvas.create_oval(40, 40, 60, 60, fill="white", outline="black", width=2)
            loading_window.update()
            time.sleep(0.05)

def update_progress_and_tip(duration):
    tips = [
        "Consejo: ¡Atrapa todos los Pokémon que puedas!",
        "Consejo: Usa bayas para curar a tus Pokémon",
        "Consejo: Entrena duro para volverte un maestro Pokémon",
        "Consejo: Cada tipo de Pokémon tiene sus fortalezas y debilidades"
    ]
    start_time = time.time()
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        progress = min(elapsed / duration, 1.0)
        if loading_window is None or not loading_window.winfo_exists():
            return
        progress_bar.set(progress)
        tip_label.configure(text=tips[int(progress * len(tips)) % len(tips)])
        loading_window.update()
        time.sleep(0.1)
    if loading_window and loading_window.winfo_exists():
        loading_window.destroy()

def close_loading_screen():
    global loading_window
    if loading_window and loading_window.winfo_exists():
        loading_window.destroy()
    loading_window = None

# Ejemplo de uso:
# show_loading_screen(root, duration=5)
# close_loading_screen()
