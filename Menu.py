import customtkinter as ctk
from tkinter import messagebox, StringVar
from PIL import Image, ImageTk
import requests
from io import BytesIO
from Pokedex import serch_pokemon_name, serch_pokemon_num
from Estadisticas import pokemones
from Tabla_de_tipos import Tipos_pokemons
from Sistema_combatev2 import Pelea

def obtener_imagen_pokemon(nombre, tamaño=(200, 200)):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}/"
    respuesta = requests.get(url)
    datos = respuesta.json()
    imagen_url = datos['sprites']['front_default']
    
    respuesta = requests.get(imagen_url)
    img = Image.open(BytesIO(respuesta.content))
    img = img.resize(tamaño)
    
    return ImageTk.PhotoImage(img)

def Menu():
    # Definición de la paleta de colores Pokémon
    POKE_RED = "#CC0000"
    POKE_BLUE = "#3B4CCA"
    POKE_YELLOW = "#FFDE00"
    POKE_BLACK = "#1E1E1E"
    POKE_WHITE = "#FFFFFF"

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")
    root.title("Pokédex")
    root.configure(fg_color=POKE_RED)

    PokemonJ = None

    def seleccionar_pokemon():
        nonlocal PokemonJ
        Id = ID_var.get()
        pokemon = Pokemon_entry.get()
        
        try:
            if Id == "Nombre":
                PokemonJ = serch_pokemon_name(pokemon)
            elif Id == "Pokedex":
                PokemonJ = serch_pokemon_num(int(pokemon))
            
            if PokemonJ:
                messagebox.showinfo("Pokémon", message=f"El Pokémon elegido es: {PokemonJ}")
                foto_poke = obtener_imagen_pokemon(PokemonJ, tamaño=(300, 300))
                foto.configure(image=foto_poke)
                foto.image = foto_poke
                ver_estadisticas_button.configure(state="normal")
                ir_a_combate_button.configure(state="normal")
            else:
                messagebox.showerror("Error", "Pokémon no encontrado")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para la Pokédex")



    def ver_estadisticas():
        if PokemonJ:
            ventana_estadisticas = ctk.CTkToplevel(root)
            ventana_estadisticas.geometry("500x400")
            ventana_estadisticas.title(f"Estadísticas de {PokemonJ}")
            ventana_estadisticas.configure(fg_color=POKE_WHITE)

            Nivel = 50  # Asumimos un nivel predeterminado de 50
            Tipo_P = Tipos_pokemons[PokemonJ]
            stats = pokemones[PokemonJ]

            # Frame principal
            main_frame = ctk.CTkFrame(ventana_estadisticas, fg_color=POKE_WHITE)
            main_frame.pack(padx=20, pady=20, fill="both", expand=True)

            # Título y tipo
            ctk.CTkLabel(main_frame, text=f"{PokemonJ}", font=("Helvetica", 24, "bold"), text_color=POKE_RED).pack(pady=(0, 5))
            ctk.CTkLabel(main_frame, text=f"Tipo: {Tipo_P}", font=("Helvetica", 16), text_color=POKE_BLUE).pack(pady=(0, 10))

            # Imagen del Pokémon
            try:
                imagen_poke = obtener_imagen_pokemon(PokemonJ, tamaño=(150, 150))
                ctk.CTkLabel(main_frame, image=imagen_poke, text="").pack(pady=(0, 10))
            except Exception:
                ctk.CTkLabel(main_frame, text="Imagen no disponible", text_color=POKE_BLACK).pack(pady=(0, 10))

            # Frame para las estadísticas
            stats_frame = ctk.CTkFrame(main_frame, fg_color=POKE_WHITE)
            stats_frame.pack(fill="x", padx=10, pady=10)

            # Mostrar estadísticas en dos columnas
            stats_labels = ["HP", "Ataque", "Defensa", "Ataque Esp.", "Defensa Esp.", "Velocidad"]
            stats_keys = ["hp", "atk", "def", "atkE", "defE", "vel"]

            for i, (label, key) in enumerate(zip(stats_labels, stats_keys)):
                row = i // 2
                col = i % 2
                
                frame = ctk.CTkFrame(stats_frame, fg_color=POKE_YELLOW)
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
                
                ctk.CTkLabel(frame, text=f"{label}:", font=("Helvetica", 14, "bold"), text_color=POKE_BLUE).pack(side="left", padx=5)
                ctk.CTkLabel(frame, text=f"{stats[key]}", font=("Helvetica", 14), text_color=POKE_BLACK).pack(side="right", padx=5)

            stats_frame.grid_columnconfigure(0, weight=1)
            stats_frame.grid_columnconfigure(1, weight=1)

            # Nivel
            ctk.CTkLabel(main_frame, text=f"Nivel: {Nivel}", font=("Helvetica", 16, "bold"), text_color=POKE_BLUE).pack(pady=(10, 0))

            # Botón para cerrar
            ctk.CTkButton(main_frame, text="Cerrar", command=ventana_estadisticas.destroy, 
                        fg_color=POKE_RED, hover_color=POKE_BLUE, text_color=POKE_WHITE).pack(pady=(20, 0))

    def ir_a_combate():
        Pelea(PokemonJ)

    def actualizar_pokemon_label(*args):
        if ID_var.get() == "Nombre":
            Pokemon_label.configure(text="Ingrese el nombre del Pokémon")
        else:
            Pokemon_label.configure(text="Ingrese el número de Pokédex")

    # Marco principal
    main_frame = ctk.CTkFrame(root, fg_color=POKE_WHITE)
    main_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Título
    ctk.CTkLabel(main_frame, text="Pokédex", font=("Helvetica", 24, "bold"), text_color=POKE_RED).pack(pady=10)

    # Frame para la selección del Pokémon
    select_frame = ctk.CTkFrame(main_frame, fg_color=POKE_WHITE)
    select_frame.pack(pady=10, padx=10, fill="x")

    ID_var = StringVar(value="Nombre")
    ID_var.trace("w", actualizar_pokemon_label)
    ID_menu = ctk.CTkOptionMenu(select_frame, variable=ID_var, values=["Nombre", "Pokedex"], 
                                fg_color=POKE_BLUE, button_color=POKE_BLUE, button_hover_color=POKE_YELLOW)
    ID_menu.pack(side="left", padx=5)

    Pokemon_label = ctk.CTkLabel(select_frame, text="Ingrese el nombre del Pokémon", text_color=POKE_BLACK)
    Pokemon_label.pack(side="left", padx=5)

    Pokemon_entry = ctk.CTkEntry(select_frame, fg_color=POKE_WHITE, text_color=POKE_BLACK, border_color=POKE_BLUE)
    Pokemon_entry.pack(side="left", padx=5, expand=True, fill="x")
    Pokemon_entry.bind("<Return>", lambda event: seleccionar_pokemon())

    seleccionar_pokemon_button = ctk.CTkButton(select_frame, text="Buscar", command=seleccionar_pokemon, 
                                               fg_color=POKE_BLUE, hover_color=POKE_YELLOW, text_color=POKE_WHITE)
    seleccionar_pokemon_button.pack(side="left", padx=5)
    seleccionar_pokemon_button.bind("<Return>", lambda event: seleccionar_pokemon())

    # Frame para la imagen del Pokémon
    image_frame = ctk.CTkFrame(main_frame, fg_color=POKE_WHITE)
    image_frame.pack(pady=10)

    foto = ctk.CTkLabel(image_frame, text="", width=300, height=300)
    foto.pack()

    # Frame para los botones
    button_frame = ctk.CTkFrame(main_frame, fg_color=POKE_WHITE)
    button_frame.pack(pady=10, fill="x")

    ver_estadisticas_button = ctk.CTkButton(button_frame, text="Ver Estadísticas", command=ver_estadisticas, state="disabled", 
                                            fg_color=POKE_BLUE, hover_color=POKE_YELLOW, text_color=POKE_WHITE)
    ver_estadisticas_button.pack(side="left", padx=5, expand=True)

    ir_a_combate_button = ctk.CTkButton(button_frame, text="Ir a un combate", command=ir_a_combate, state="disabled", 
                                        fg_color=POKE_BLUE, hover_color=POKE_YELLOW, text_color=POKE_WHITE)
    ir_a_combate_button.pack(side="left", padx=5, expand=True)

    salir_button = ctk.CTkButton(button_frame, text="Salir", command=root.quit, 
                                 fg_color=POKE_RED, hover_color=POKE_YELLOW, text_color=POKE_WHITE)
    salir_button.pack(side="left", padx=5, expand=True)

    root.mainloop()

if __name__ == "__main__":
    Menu()