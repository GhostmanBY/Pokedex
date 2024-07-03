import os 
import random 
import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from tkinter import ttk

from Pokedex import serch_pokemon_num  
from Estadisticas import pokemones 
from Movimiento import seleccionar_movimiento, Tipo_movimiento  
from Movimiento import movimientos_de_Pokemons
from Movimiento import Potencia_de_movimientos, Precicion_de_movimiento  
from Tabla_de_tipos import Tipos_pokemons, tipos_movimientos  
from Tabla_de_tipos import Eficacia

set_appearance_mode("dark")

def decicion_ataque(indice, Pokemon_J, Pokemon_R, labelB, labelJ):
    global PsA_Rival, PsA_Jugador
    if PsA_Rival <= 0 or PsA_Jugador <= 0:
        labelJ.place_forget()
        labelB.configure(text="El combate ha terminado", font=("Arial", 14, "bold"), text_color="red")
        labelB.pack(padx=40, pady=10)
        return

    movimientos = movimientos_de_Pokemons[Pokemon_J]
    movimiento = movimientos[indice]

    movimiento_B = movimiento_bot(Pokemon_R)

    if pokemones[Pokemon_J]["vel"] > pokemones[Pokemon_R]["vel"]:
        precicion = random.randint(0, 100)
        if Precicion_de_movimiento[movimiento] >= precicion:
            PsA_Rival -= Daño(movimiento, Pokemon_J, Pokemon_R)
        else:
            messagebox.showinfo("Precisión", "El movimiento falló")

        precicion = random.randint(0, 100)
        if Precicion_de_movimiento[movimiento_B] >= precicion:
            PsA_Jugador -= Daño(movimiento_B, Pokemon_R, Pokemon_J)
        else:
            messagebox.showinfo("Precisión", "El movimiento falló")
    else:
        precicion = random.randint(0, 100)
        if Precicion_de_movimiento[movimiento_B] >= precicion:
            PsA_Jugador -= Daño(movimiento_B, Pokemon_R, Pokemon_J)
        else:
            messagebox.showinfo("Precisión", "El movimiento falló")

        precicion = random.randint(0, 100)
        if Precicion_de_movimiento[movimiento] >= precicion:
            PsA_Rival -= Daño(movimiento, Pokemon_J, Pokemon_R)
        else:
            messagebox.showinfo("Precisión", "El movimiento falló")

    actualizar_ps(labelB, labelJ, Pokemon_R, Pokemon_J)

def actualizar_ps(labelB, labelJ, Pokemon_R, Pokemon_J):
    global PsA_Rival, PsA_Jugador
    vida_rival = pokemones[Pokemon_R]["hp"]
    vida_jugador = pokemones[Pokemon_J]["hp"]

    if labelB.winfo_exists():
        if PsA_Rival > 0:
            labelB.configure(text=f"{Pokemon_R}\nPS: {max(0, PsA_Rival)}/{vida_rival}", font=("Arial", 12, "bold"))
    if labelJ.winfo_exists():
        if PsA_Jugador > 0:
            labelJ.configure(text=f"{Pokemon_J}\nPS: {max(0, PsA_Jugador)}/{vida_jugador}", font=("Arial", 12, "bold"))

def movimiento_bot(pokemon_bot):
    movimientos = movimientos_de_Pokemons[pokemon_bot]
    seleccion = random.choice(movimientos)
    return seleccion

def Daño(movimiento, Pokemon_A, Pokemon_D):
    N = 1

    if Tipo_movimiento(movimiento) == "Físico":
        A = pokemones[Pokemon_A]["atk"]
        D = pokemones[Pokemon_D]["def"]
    else:
        A = pokemones[Pokemon_A]["atkE"]
        D = pokemones[Pokemon_D]["defE"]

    P = Potencia_de_movimientos[movimiento]

    if Tipos_pokemons[Pokemon_A] == tipos_movimientos[movimiento]:
        B = 1.5
    else:
        B = 1

    E = Eficacia(tipos_movimientos[movimiento], Tipos_pokemons[Pokemon_D])

    V = random.randint(85, 100)

    Damage = 0.01 * B * E * V * (((0.2 * N + 1) * A * P) / (25 * D) + 2)

    return int(Damage)

def Pelea(Pokemon):
    global PsA_Rival, PsA_Jugador
    # pokemon del rival
    num = [1, 4, 7]
    R = random.choice(num)
    Pokemon_Rival = serch_pokemon_num(R)

    PsA_Rival = pokemones[Pokemon_Rival]["hp"]  # rival(bot)
    PsA_Jugador = pokemones[Pokemon]["hp"]  # jugador

    vida_rival = pokemones[Pokemon_Rival]["hp"]
    vida_jugador = pokemones[Pokemon]["hp"]

    root = tk.Tk()
    root.title("Sistema de combate Pokémon")
    root.geometry("600x500")
    root.configure(bg="#f0f0f0")

    frame_batalla = CTkFrame(master=root, height=300, width=550, fg_color="#e6e6e6", corner_radius=10)
    frame_batalla.place(relx=0.5, rely=0.3, anchor="center")
    
    text_name_B = CTkLabel(master=frame_batalla, text=f"{Pokemon_Rival}\nPS: {PsA_Rival}/{vida_rival}", text_color="black", font=("Arial", 14, "bold"))
    text_name_B.place(relx=0.8, rely=0.2, anchor="center")

    text_name_J = CTkLabel(master=frame_batalla, text=f"{Pokemon}\nPS: {PsA_Jugador}/{vida_jugador}", text_color="black", font=("Arial", 14, "bold"))
    text_name_J.place(relx=0.2, rely=0.8, anchor="center")

    frame_historial = CTkFrame(master=root, height=100, width=550, fg_color="#d9d9d9", corner_radius=10)
    frame_historial.place(relx=0.5, rely=0.65, anchor="center")

    title_historial = CTkLabel(master=frame_historial, text="Historial:", text_color="black", font=("Arial", 12, "bold"))
    title_historial.place(relx=0.02, rely=0.1)

    text_historial = CTkLabel(master=frame_historial, text=(f"Tu {Pokemon} se va a enfrentar a un {Pokemon_Rival}"), text_color="black", font=("Arial", 12))
    text_historial.place(relx=0.5, rely=0.5, anchor="center")
    
    frame_Botones = CTkFrame(master=root, height=100, width=550, fg_color="#c2c2c2", corner_radius=10)
    frame_Botones.place(relx=0.5, rely=0.9, anchor="center")

    movimientos = movimientos_de_Pokemons[Pokemon]

    # Iteramos sobre cada movimiento y creamos un botón
    for idx, movimiento in enumerate(movimientos):
        boton = CTkButton(
            master=frame_Botones,
            text=movimiento,
            height=40,
            width=120,
            text_color="white",
            corner_radius=5,
            command=lambda idx=idx: decicion_ataque(idx, Pokemon, Pokemon_Rival, text_name_B, text_name_J)
        )
        boton.place(relx=0.25 + 0.5 * idx, rely=0.5, anchor="center")

    root.mainloop()

# Llamada a la función principal
Pelea("Squirtle")  # Puedes cambiar "Bulbasaur" por el Pokémon que desees
