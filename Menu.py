from Pokedex import serch_pokemon_name #impoorta desde Pokedex la funcion serch_pokemon_name
from Pokedex import serch_pokemon_num #impoorta desde Pokedex la funcion serch_pokemon_num
from Estadisticas import pokemones #importa desde Estadisticas los diccionarios de Hp, Atk, Def, AtkE, DefE, Vel
from Tabla_de_tipos import Tipos_pokemons #importa desde Tabla_de_tipos el diccionario de Tipos_pokemons
from Sistema_combatev2 import Pelea #importa desde Sistema_de_combate la funcion de combate
from tkinter import *

def Menu():
    root = Tk()
    root.title("Menu")

    #Funciones de consola
    def limpiar_consola():
        root.destroy()
        Menu()

    PokemonJ = None

    def seleccionar_pokemon():
        nonlocal PokemonJ
        Id = ID_entry.get().capitalize()
        if Id.capitalize() == "Nombre":
            pokemon = Pokemon_entry.get()
            PokemonJ = serch_pokemon_name(pokemon)
        elif Id.capitalize() == "Pokedex":
            pokemon_num = int(Pokemon_entry.get())
            PokemonJ = serch_pokemon_num(pokemon_num)

    def ver_estadisticas():
        if PokemonJ:
            Nivel = 1
            Tipo_P = Tipos_pokemons[PokemonJ]
            Hp_P = pokemones[PokemonJ]["hp"]
            Atk_P = pokemones[PokemonJ]["atk"]
            Def_P = pokemones[PokemonJ]["def"]
            AtkE_P = pokemones[PokemonJ]["atkE"]
            DefE_P = pokemones[PokemonJ]["defE"]
            Vel_P = pokemones[PokemonJ]["vel"]

            estadisticas_label = Label(root, text=f"El pokemon que elijio es: {PokemonJ}\nLas esta disticas de su pokemon son:\nNivel {Nivel}\nTipo = {Tipo_P}\nPs = {Hp_P}\nAtk = {Atk_P} \nDef = {Def_P}\nAtkE = {AtkE_P}\nDefE = {DefE_P}\nVel = {Vel_P}")
            estadisticas_label.pack()
        else:
            error_label = Label(root, text="Tiene que elejir un pokemon primero")
            error_label.pack()

    def ir_a_combate():
        if PokemonJ:
            Pelea(PokemonJ)
        else:
            error_label = Label(root, text="Tiene que elegir un pokemon primero")
            error_label.pack()
    def salir():
        root.destroy()

    ID_label = Label(root, text="Como va a elejir el pokemon por nombre o por numero de pokedex?(nombre/pokedex): ")
    ID_label.pack()
    ID_entry = Entry(root)
    ID_entry.pack()

    Pokemon_label = Label(root, text="Ingrese el nombre del pokemon o el numero: ")
    Pokemon_label.pack()
    Pokemon_entry = Entry(root)
    Pokemon_entry.pack()

    seleccionar_pokemon_button = Button(root, text="Seleccionar Pokemon", command=seleccionar_pokemon)
    seleccionar_pokemon_button.pack()

    ver_estadisticas_button = Button(root, text="Ver Estadisticas", command=ver_estadisticas)
    ver_estadisticas_button.pack()

    ir_a_combate_button = Button(root, text="Ir a un combate", command=ir_a_combate)
    ir_a_combate_button.pack()

    salir_button = Button(root, text="Salir", command=salir)
    salir_button.pack()

    root.mainloop()



