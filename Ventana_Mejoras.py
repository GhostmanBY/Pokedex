from customtkinter import *
from tkinter import messagebox, StringVar
from PIL import Image, ImageTk
import requests
from io import BytesIO
import json
from Pokedex import serch_pokemon_name, serch_pokemon_num
from Estadisticas import pokemones
from Tabla_de_tipos import Tipos_pokemons
from test import Pelea

letra = "Mono Space", 28, "bold"

POKE_RED = "#CC0000"
POKE_BLUE = "#3B4CCA"
POKE_YELLOW = "#FFDE00"
POKE_BLACK = "#1E1E1E"
POKE_WHITE = "#FFFFFF"

def obtener_imagen_pokemon(nombre, tamaño=(200, 200)):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}/"
    respuesta = requests.get(url)
    datos = respuesta.json()
    imagen_url = datos['sprites']['front_default']
    
    respuesta = requests.get(imagen_url)
    img = Image.open(BytesIO(respuesta.content))
    img = img.resize(tamaño)
    
    return ImageTk.PhotoImage(img)

def actualizar_json(pokemon, stat, valor):
    with open('info_run.json', 'r+') as f:
        data = json.load(f)
        if pokemon not in data:
            data[pokemon] = {}
        data[pokemon][stat] = valor
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def mejoras(PokemonJ, N):
    root = CTk(fg_color="grey")
    root.geometry("250x100")
    root.title("Eleccion")
    
    def volver():
        root.destroy()

    def mejorar():
        if PokemonJ:
            ventana_estadisticas = CTkToplevel(root)
            ventana_estadisticas.geometry("500x500")
            ventana_estadisticas.title(f"Estadísticas de {PokemonJ}")
            ventana_estadisticas.configure(fg_color=POKE_WHITE)

            Nivel = N 
            Tipo_P = Tipos_pokemons[PokemonJ]
            stats = pokemones[PokemonJ]

            # Frame principal
            main_frame = CTkFrame(ventana_estadisticas, fg_color=POKE_WHITE)
            main_frame.pack(padx=20, pady=20, fill="both", expand=True)

            # Título y tipo
            CTkLabel(main_frame, text=f"{PokemonJ}", font=("Helvetica", 24, "bold"), text_color=POKE_RED).pack(pady=(0, 1))
            CTkLabel(main_frame, text=f"Tipo: {Tipo_P}", font=("Helvetica", 16), text_color=POKE_BLUE).pack(pady=(0, 1))
            CTkLabel(main_frame, text=f"Nivel: {Nivel}", font=("Helvetica", 16), text_color=POKE_BLUE).pack(pady=(0, 1))

            # Imagen del Pokémon
            try:
                imagen_poke = obtener_imagen_pokemon(PokemonJ, tamaño=(150, 150))
                CTkLabel(main_frame, image=imagen_poke, text="").pack(pady=(0, 1))
            except Exception:
                CTkLabel(main_frame, text="Imagen no disponible", text_color=POKE_BLACK).pack(pady=(0, 5))

            # Frame para las estadísticas
            stats_frame = CTkFrame(main_frame, fg_color=POKE_WHITE)
            stats_frame.pack(fill="x", padx=5, pady=5)

            # Mostrar estadísticas en dos columnas
            stats_labels = ["HP", "Ataque", "Defensa", "Ataque Esp", "Defensa Esp", "Velocidad"]
            stats_keys = ["hp", "atk", "def", "atkE", "defE", "vel"]

            def aumentar_stat(key):
                stats[key] += 1
                actualizar_json(PokemonJ, key, stats[key])
                stat_labels[key].configure(text=f"{stats[key]}")

            stat_labels = {}
            for i, (label, key) in enumerate(zip(stats_labels, stats_keys)):
                row = i // 2
                col = i % 2
                
                frame = CTkFrame(stats_frame, fg_color=POKE_YELLOW)
                frame.grid(row=row, column=col*2, padx=10, pady=5, sticky="ew")
                
                CTkLabel(frame, text=f"{label}:", font=("Helvetica", 14, "bold"), text_color=POKE_BLUE).pack(side="left", padx=5)
                stat_labels[key] = CTkLabel(frame, text=f"{stats[key]}", font=("Helvetica", 14), text_color=POKE_BLACK)
                stat_labels[key].pack(side="left", padx=5)
                
                CTkButton(stats_frame, text="+", command=lambda k=key: aumentar_stat(k), width=30, height=30).grid(row=row, column=col*2+1, padx=(0, 10), pady=5)

            stats_frame.grid_columnconfigure(0, weight=1)
            stats_frame.grid_columnconfigure(1, weight=0)
            stats_frame.grid_columnconfigure(2, weight=1)
            stats_frame.grid_columnconfigure(3, weight=0)

    text = CTkLabel(master=root, text="Elija su opcion", text_color="black", font=letra)
    text.pack()

    boton_continuar = CTkButton(master= root, text="Continuar", command=volver, height=50, width=100)
    boton_continuar.place(relx=0.25, rely=0.65, anchor="center")
    
    boton_mejorar = CTkButton(master= root, text="Mejorar", command=mejorar, height=50, width=100)
    boton_mejorar.place(relx=0.75, rely=0.65, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    mejoras("Charmander", 5)
