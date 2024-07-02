from Pokedex import serch_pokemon_name # importa desde Pokedex la función serch_pokemon_name
from Pokedex import serch_pokemon_num # importa desde Pokedex la función serch_pokemon_num
from Estadisticas import pokemones # importa desde Estadisticas los diccionarios de Hp, Atk, Def, AtkE, DefE, Vel
from Tabla_de_tipos import Tipos_pokemons # importa desde Tabla_de_tipos el diccionario de Tipos_pokemons
from Sistema_combatev2 import Pelea # importa desde Sistema_de_combate la función de combate
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def Menu():
    root = ctk.CTk()
    root.geometry("600x400")
    root.title("Menu")

    # Definir colores
    bg_color = "#3b3b3b"
    fg_color = "#f2f2f2"
    primary_color = "#ff3b30"
    secondary_color = "#1e1e1e"

    root.configure(bg=bg_color)

    # Funciones de consola
    def limpiar_consola():
        root.destroy()
        Menu()

    PokemonJ = None

    def seleccionar_pokemon():
        nonlocal PokemonJ
        Id = ID_var.get()
        if Id == "Nombre":
            pokemon = Pokemon_entry.get()
            PokemonJ = serch_pokemon_name(pokemon)
        elif Id == "Pokedex":
            pokemon_num = int(Pokemon_entry.get())
            PokemonJ = serch_pokemon_num(pokemon_num)
        messagebox.showinfo("Pokemon", message=f"El pokemon elegido es: {PokemonJ}")

    def ver_estadisticas():
        ventana_estadisticas = ctk.CTkToplevel()
        ventana_estadisticas.geometry("300x200")
        ventana_estadisticas.title("Estadisticas")
        ventana_estadisticas.configure(bg=bg_color)

        if PokemonJ:
            Nivel = 1
            Tipo_P = Tipos_pokemons[PokemonJ]
            Hp_P = pokemones[PokemonJ]["hp"]
            Atk_P = pokemones[PokemonJ]["atk"]
            Def_P = pokemones[PokemonJ]["def"]
            AtkE_P = pokemones[PokemonJ]["atkE"]
            DefE_P = pokemones[PokemonJ]["defE"]
            Vel_P = pokemones[PokemonJ]["vel"]

            estadisticas_label = ctk.CTkLabel(
                ventana_estadisticas,
                text=f"""El pokemon que eligió es: {PokemonJ}
Las estadísticas de su pokemon son:
Nivel: {Nivel}
Tipo: {Tipo_P}
PS: {Hp_P}
Atk: {Atk_P}
Def: {Def_P}
AtkE: {AtkE_P}
DefE: {DefE_P}
Vel: {Vel_P}""",
                font=("Helvetica", 14),
                fg_color=secondary_color,
                text_color=fg_color
            )
            estadisticas_label.pack(padx=20, pady=20)
        else:
            error_label = ctk.CTkLabel(
                ventana_estadisticas, 
                text="Tiene que elegir un pokemon primero",
                font=("Helvetica", 14),
                fg_color=secondary_color,
                text_color=primary_color
            )
            error_label.pack(padx=20, pady=20)

    def ir_a_combate():
        if PokemonJ:
            Pelea(PokemonJ)
        else:
            error_label = ctk.CTkLabel(root, text="Tiene que elegir un pokemon primero", fg_color=secondary_color, text_color=primary_color)
            error_label.pack(padx=10, pady=10)

    def salir():
        root.destroy()

    def actualizar_pokemon_label(*args):
        if ID_var.get() == "Nombre":
            Pokemon_label.configure(text="Ingrese el nombre del pokemon")
        else:
            Pokemon_label.configure(text="Ingrese el número de Pokedex del pokemon")

    ID_var = StringVar(value="Nombre")
    ID_var.trace("w", actualizar_pokemon_label)
    ID_menu = ctk.CTkOptionMenu(root, variable=ID_var, values=["Nombre", "Pokedex"])
    ID_menu.pack(padx=10, pady=10)
    ID_menu.configure(font=("Helvetica", 14), fg_color=primary_color)

    Pokemon_label = ctk.CTkLabel(root, text="Ingrese el nombre del pokemon", font=("Helvetica", 14), fg_color=secondary_color, text_color=fg_color)
    Pokemon_label.pack(padx=10, pady=10)
    Pokemon_entry = ctk.CTkEntry(root, font=("Helvetica", 14), fg_color=secondary_color, text_color=fg_color)
    Pokemon_entry.pack(padx=10, pady=10)
    Pokemon_entry.bind("<Return>", lambda event: seleccionar_pokemon())  # Agrega este

    seleccionar_pokemon_button = ctk.CTkButton(root, text="Seleccionar Pokemon", command=seleccionar_pokemon, font=("Helvetica", 14), fg_color=primary_color)
    seleccionar_pokemon_button.pack(padx=10, pady=10)

    ver_estadisticas_button = ctk.CTkButton(root, text="Ver Estadísticas", command=ver_estadisticas, font=("Helvetica", 14), fg_color=primary_color)
    ver_estadisticas_button.pack(padx=10, pady=10)

    ir_a_combate_button = ctk.CTkButton(root, text="Ir a un combate", command=ir_a_combate, font=("Helvetica", 14), fg_color=primary_color)
    ir_a_combate_button.pack(padx=10, pady=10)

    salir_button = ctk.CTkButton(root, text="Salir", command=salir, font=("Helvetica", 14), fg_color=primary_color)
    salir_button.pack(padx=10, pady=10)

    root.mainloop()

Menu()
