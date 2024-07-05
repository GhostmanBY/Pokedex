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
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("800x600")
    root.title("Pokédex")

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
            ventana_estadisticas.geometry("400x300")
            ventana_estadisticas.title(f"Estadísticas de {PokemonJ}")

            Nivel = 1
            Tipo_P = Tipos_pokemons[PokemonJ]
            stats = pokemones[PokemonJ]

            frame = ctk.CTkFrame(ventana_estadisticas)
            frame.pack(padx=20, pady=20, fill="both", expand=True)

            ctk.CTkLabel(frame, text=f"Estadísticas de {PokemonJ}", font=("Helvetica", 18, "bold")).pack(pady=10)
            ctk.CTkLabel(frame, text=f"Nivel: {Nivel}").pack()
            ctk.CTkLabel(frame, text=f"Tipo: {Tipo_P}").pack()
            
            for stat, value in stats.items():
                ctk.CTkLabel(frame, text=f"{stat.upper()}: {value}").pack()

    def ir_a_combate():
        if PokemonJ:
            root.withdraw()
            Pelea(PokemonJ)

    def actualizar_pokemon_label(*args):
        if ID_var.get() == "Nombre":
            Pokemon_label.configure(text="Ingrese el nombre del Pokémon")
        else:
            Pokemon_label.configure(text="Ingrese el número de Pokédex")

    # Marco principal
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Título
    ctk.CTkLabel(main_frame, text="Pokédex", font=("Helvetica", 24, "bold")).pack(pady=10)

    # Frame para la selección del Pokémon
    select_frame = ctk.CTkFrame(main_frame)
    select_frame.pack(pady=10, padx=10, fill="x")

    ID_var = StringVar(value="Nombre")
    ID_var.trace("w", actualizar_pokemon_label)
    ID_menu = ctk.CTkOptionMenu(select_frame, variable=ID_var, values=["Nombre", "Pokedex"])
    ID_menu.pack(side="left", padx=5)

    Pokemon_label = ctk.CTkLabel(select_frame, text="Ingrese el nombre del Pokémon")
    Pokemon_label.pack(side="left", padx=5)

    Pokemon_entry = ctk.CTkEntry(select_frame)
    Pokemon_entry.pack(side="left", padx=5, expand=True, fill="x")
    Pokemon_entry.bind("<Return>", lambda event: seleccionar_pokemon())

    seleccionar_pokemon_button = ctk.CTkButton(select_frame, text="Buscar", command=seleccionar_pokemon)
    seleccionar_pokemon_button.pack(side="left", padx=5)

    # Frame para la imagen del Pokémon
    image_frame = ctk.CTkFrame(main_frame)
    image_frame.pack(pady=10)

    foto = ctk.CTkLabel(image_frame, text="", width=300, height=300)
    foto.pack()

    # Frame para los botones
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.pack(pady=10, fill="x")

    ver_estadisticas_button = ctk.CTkButton(button_frame, text="Ver Estadísticas", command=ver_estadisticas, state="disabled")
    ver_estadisticas_button.pack(side="left", padx=5, expand=True)

    ir_a_combate_button = ctk.CTkButton(button_frame, text="Ir a un combate", command=ir_a_combate, state="disabled")
    ir_a_combate_button.pack(side="left", padx=5, expand=True)

    salir_button = ctk.CTkButton(button_frame, text="Salir", command=root.quit)
    salir_button.pack(side="left", padx=5, expand=True)

    root.mainloop()

if __name__ == "__main__":
    Menu()