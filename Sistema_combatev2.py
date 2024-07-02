import os 
import random 
import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from tkinter import ttk

from Pokedex import serch_pokemon_num  
from Estadisticas import pokemones 
from Movimiento import seleccionar_movimiento, Tipo_movimiento  
from Movimiento import Potencia_de_movimientos, Precicion_de_movimiento  
from Tabla_de_tipos import Tipos_pokemons, tipos_movimientos  
from Tabla_de_tipos import Eficacia

def decicion_ataque(indice, Pokemon_J, Pokemon_R, labelB,labelJ):
    global PsA_Rival, PsA_Jugador

    movimientos = [seleccionar_movimiento(Pokemon_J, 0), seleccionar_movimiento(Pokemon_J, 1)]
    movimiento = movimientos[indice]

    movimiento_B =movimiento_bot(Pokemon_R)

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
    labelB.configure(text=PsA_Rival)
    labelJ.configure(text=PsA_Jugador)


def movimiento_bot(pokemon_bot):
    movimiento = [seleccionar_movimiento(pokemon_bot, 0), seleccionar_movimiento(pokemon_bot, 1)]
    seleccion = random.choice(movimiento)
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
    #pokemon del rival
    num = [1, 4, 7]
    R = random.choice(num)
    Pokemon_Rival = serch_pokemon_num(R)

    PsA_Rival = pokemones[Pokemon_Rival]["hp"]  # rival(bot)
    PsA_Jugador = pokemones[Pokemon]["hp"]  # jugador

    vida_rival = pokemones[Pokemon_Rival]["hp"]
    vida_jugador = pokemones[Pokemon]["hp"]
    tempjugador = (f"{Pokemon}\nPs{PsA_Jugador}/{vida_jugador}")
    tempbot = (f"{Pokemon_Rival}\nPs{PsA_Rival}/{vida_rival}")

    root = tk.Tk()
    root.title("Sistema de combate")
    root.geometry("500x500")

    frame_batalla = CTkFrame(master=root, height=300, width=550, fg_color="black")
    frame_batalla.place(relx=-0.01, rely=0)
    
    text_name_B = CTkLabel(master=frame_batalla, text=tempbot, text_color="white")
    text_name_B.place(relx=0.1, rely=0.1, anchor="center")

    text_name_J = CTkLabel(master=frame_batalla, text=tempjugador, text_color="white")
    text_name_J.place(relx=0.1, rely=0.4, anchor="center")

    frame_historial = CTkFrame(master=root,height=150, width=550, fg_color="black")
    frame_historial.place(relx=-0.01, rely=0.35)

    title_historial = CTkLabel(master=frame_historial, text="Historial:", text_color="white")
    title_historial.place(relx=0.02, rely=0.1)

    text_historial = CTkLabel(master=frame_historial, text=(f"Tu {Pokemon} se va a enfrentar a un {Pokemon_Rival}"), text_color="white")
    text_historial.place(relx=0.28, rely=0.35, anchor="center")
    
    frame_Botones = CTkFrame(master=root, height=180, width=550, fg_color="green")
    frame_Botones.place(relx=-0.01, rely=0.65)

    button_ataque1 = CTkButton(master=frame_Botones, text="Ataque 1", height=90, width=275, text_color="white", corner_radius=0, command= lambda: decicion_ataque(0, Pokemon, Pokemon_Rival,text_name_B, text_name_J))
    button_ataque1.place(relx=0, rely=0)

    button_ataque2 = CTkButton(master=frame_Botones, text="Ataque 2", height=90, width=275, text_color="white", corner_radius=0, command= lambda: decicion_ataque(1, Pokemon, Pokemon_Rival,text_name_B, text_name_J))
    button_ataque2.place(relx=0.45, rely=0)

    button_ataque3 = CTkButton(master=frame_Botones, text="Ataque 3", height=90, width=275, text_color="white", corner_radius=0, command= lambda: decicion_ataque(2, Pokemon, Pokemon_Rival,text_name_B, text_name_J))
    button_ataque3.place(relx=0, rely=0.5)

    button_ataque4 = CTkButton(master=frame_Botones, text="Ataque 4", height=90, width=275, text_color="white", corner_radius=0, command= lambda: decicion_ataque(3, Pokemon, Pokemon_Rival, text_name_B, text_name_J))
    button_ataque4.place(relx=0.45, rely=0.5)

    root.mainloop()
