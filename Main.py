import json
import os
import customtkinter as ctk
from PIL import Image
from Menu import Menu, obtener_imagen_pokemon
from Estadisticas import pokemones
from test import Pelea
import threading
import time

loading_window = None
progress_bar = None
tip_label = None
loading_completed = False

def show_loading_screen(master):
    global loading_window, progress_bar, tip_label, loading_completed
    
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
    loading_completed = False
    threading.Thread(target=loading_animation, args=(canvas,), daemon=True).start()
    threading.Thread(target=update_progress_and_tip, daemon=True).start()

def loading_animation(canvas):
    global loading_completed
    while not loading_completed:
        for i in range(0, 360, 10):
            if loading_completed:
                return
            if loading_window is None or not loading_window.winfo_exists():
                return
            canvas.delete("all")
            canvas.create_arc(10, 10, 90, 90, start=i, extent=180, fill="red", outline="white", width=2)
            canvas.create_arc(10, 10, 90, 90, start=i+180, extent=180, fill="white", outline="white", width=2)
            canvas.create_oval(40, 40, 60, 60, fill="white", outline="black", width=2)
            loading_window.update()
            time.sleep(0.05)

def update_progress_and_tip():
    global loading_completed
    tips = [
        "Consejo: ¡Atrapa todos los Pokémon que puedas!",
        "Consejo: Usa bayas para curar a tus Pokémon",
        "Consejo: Entrena duro para volverte un maestro Pokémon",
        "Consejo: Cada tipo de Pokémon tiene sus fortalezas y debilidades"
    ]
    progress = 0
    while not loading_completed:
        if loading_window is None or not loading_window.winfo_exists():
            return
        progress = min(progress + 0.01, 0.99)  # Mantener la barra en 99% hasta que la carga esté completa
        progress_bar.set(progress)
        tip_label.configure(text=tips[int(progress * len(tips)) % len(tips)])
        loading_window.update()
        time.sleep(0.1)

def close_loading_screen():
    global loading_window, loading_completed
    loading_completed = True
    if loading_window and loading_window.winfo_exists():
        loading_window.destroy()
    loading_window = None

def cargar_info_guardada():
    filename = "info_run.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, "r") as archivo:
                data = json.load(archivo)
                if data:
                    return list(data.keys())[0]
        except json.JSONDecodeError:
            print(f"Error al leer {filename}.")
    return None

def guardar_info(pokemon_nombre,ventana = None):
    if pokemon_nombre in pokemones:
        stats = pokemones[pokemon_nombre]
        info_pokemon = {
            'nombre': pokemon_nombre,
            'hp': stats['hp'],
            'ataque': stats['atk'],
            'defensa': stats['def'],
            'ataque_esp': stats['atkE'],
            'defensa_esp': stats['defE'],
            'velocidad': stats['vel'],
            'precision': stats['precicion'],
            'evacion': stats['evacion'],
            'xp': 0
        }
        
        filename = "info_run.json"
        all_pokemon_info = {pokemon_nombre: info_pokemon}
        
        try:
            with open(filename, "w") as archivo:
                json.dump(all_pokemon_info, archivo, indent=4)
            print(f"Información guardada para {pokemon_nombre}")
        except IOError as e:
            print(f"Error al escribir en {filename}: {e}")
        ventana.withdraw()
        Pelea(pokemon_nombre)

def create_selection_window():
    
    global loading_completed
    
    def load_pokemon_images():
        pokemon_images = {}
        for pokemon in ["Bulbasaur", "Charmander", "Squirtle"]:
            pokemon_images[pokemon] = obtener_imagen_pokemon(pokemon)
        return pokemon_images

    def setup_selection_window(pokemon_images):
        global loading_completed
        
        seleccion_ventana = ctk.CTkToplevel(root)
        seleccion_ventana.geometry("800x600")
        seleccion_ventana.title("Selección de Pokémon")

        titulo = ctk.CTkLabel(seleccion_ventana, text="Selecciona tu primer pokémon", font=("Roboto", 28, "bold"), text_color=TEXT_COLOR)
        titulo.pack(pady=(30, 20))

        frame_pokemones = ctk.CTkFrame(seleccion_ventana, fg_color="transparent")
        frame_pokemones.pack(expand=True)

        def crear_boton_pokemon(pokemon_nombre):
            frame = ctk.CTkFrame(frame_pokemones, fg_color="transparent")
            frame.pack(side="left", padx=20)

            imagen = ctk.CTkLabel(frame, image=pokemon_images[pokemon_nombre], text="")
            imagen.pack()

            boton = ctk.CTkButton(
                frame,
                text=f"Elegir {pokemon_nombre}",
                command=lambda pn=pokemon_nombre: guardar_info(pn, ventana=seleccion_ventana),
                width=150,
                height=40,
                corner_radius=20,
                fg_color=BUTTON_COLOR,
                hover_color=BUTTON_HOVER_COLOR,
                text_color=TEXT_COLOR,
                font=("Roboto", 16)
            )
            boton.pack(pady=10)

        for pokemon in pokemon_images:
            crear_boton_pokemon(pokemon)

        boton_volver = ctk.CTkButton(
            seleccion_ventana,
            text="Volver al Menú Principal",
            command=lambda: [seleccion_ventana.destroy(), root.deiconify()],
            width=200,
            height=40,
            corner_radius=20,
            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
            text_color=TEXT_COLOR,
            font=("Roboto", 16)
        )
        boton_volver.pack(pady=20)

        # Indicar que la carga ha terminado y cerrar la pantalla de carga
        loading_completed = True
        close_loading_screen()
        seleccion_ventana.deiconify()

    # Mostrar pantalla de carga
    show_loading_screen(root)
    
    # Cargar imágenes y crear ventana de selección en segundo plano
    threading.Thread(target=lambda: [
        images := load_pokemon_images(),
        root.after(0, lambda: setup_selection_window(images))
    ], daemon=True).start()

def Jugar():
    root.withdraw()
    create_selection_window()

# Configuración general
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Colores
BG_COLOR = "#2C3E50"  # Azul oscuro
BUTTON_COLOR = "#3498DB"  # Azul claro
BUTTON_HOVER_COLOR = "#2980B9"  # Azul más oscuro para hover
TEXT_COLOR = "#ECF0F1"  # Blanco grisáceo

# Crear ventana principal
root = ctk.CTk()
root.geometry("800x600")
root.title("Pokewar")
root.configure(fg_color=BG_COLOR)

# Frame principal
main_frame = ctk.CTkFrame(root, fg_color=BG_COLOR)
main_frame.pack(fill="both", expand=True)

# Título del juego
title_label = ctk.CTkLabel(
    main_frame,
    text="POKEWAR",
    font=("Roboto", 72, "bold"),
    text_color=TEXT_COLOR
)
title_label.pack(pady=(80, 50))

# Función para crear botones
def create_button(parent, text, command):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=250,
        height=60,
        corner_radius=30,
        fg_color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font=("Roboto", 24)
    )

pokemon_guardado = cargar_info_guardada()
def continuar():
    # Verificar si hay información guardada
    if pokemon_guardado:
        root.destroy()
        Pelea(pokemon_guardado)
    else:
        messagebox.showinfo("Aviso", "No hay una partida guardada. Por favor, juega primero.")




continuar_button = create_button(main_frame, "Continuar", continuar)
continuar_button.pack(pady=20)

jugar_button = create_button(main_frame, "Jugar", Jugar)
jugar_button.pack(pady=20)

opciones_button = create_button(main_frame, "Opciones", lambda: print("Opciones"))
opciones_button.pack(pady=20)

salir_button = create_button(main_frame, "Salir", root.quit)
salir_button.pack(pady=20)

# Pie de página
footer = ctk.CTkLabel(
    main_frame,
    text="Desarrollado por: GhostmanBY && Markbusking\n© 2024. Todos los derechos reservados.",
    font=("Roboto", 14),
    text_color=TEXT_COLOR
)
footer.pack(side="bottom", pady=20)

root.mainloop()

