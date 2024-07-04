#importacion de toda libreria necesaria
import os 
import random 
import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from tkinter import ttk

#Importacion de funciones de otros archivos
from Pokedex import serch_pokemon_num  
from Estadisticas import pokemones 
from Movimiento import seleccionar_movimiento, Tipo_movimiento, tipo_de_movimientos  
from Movimiento import Potencia_de_movimientos, Precicion_de_movimiento  
from Tabla_de_tipos import Tipos_pokemons, tipos_movimientos  
from Tabla_de_tipos import Eficacia

#Funcion para definir cual ataque se ara
def decicion_ataque(indice, Pokemon_J, Pokemon_R, labelB, labelJ):
    global PsA_Rival, PsA_Jugador
    if PsA_Rival <= 0 or PsA_Jugador <= 0:
        labelJ.place_forget()
        if PsA_Rival <= 0:#un mensaje o otro si gana el jugador o el bot
            labelB.configure(text="El jugador a ganado", font=("Arial", 14, "bold"), text_color="green")
            labelB.pack(padx=40, pady=10)
        else:
            labelB.configure(text="El Rival a ganado", font=("Arial", 14, "bold"), text_color="red")
            labelB.pack(padx=40, pady=10)
        return

    movimientos = [seleccionar_movimiento(Pokemon_J, 0), seleccionar_movimiento(Pokemon_J, 1), seleccionar_movimiento(Pokemon_J, 2), seleccionar_movimiento(Pokemon_J, 3)]
    movimiento = movimientos[indice]
    evacion_precicion(movimiento, Pokemon_J, Pokemon_R)
    porcentaje_de_acierto_J = precicion_calculo(movimiento, Pokemon_J, Pokemon_R)

    movimiento_B = movimiento_bot(Pokemon_R)
    porcentaje_de_acierto_B = precicion_calculo(movimiento_B, Pokemon_R, Pokemon_J)

    if pokemones[Pokemon_J]["vel"] > pokemones[Pokemon_R]["vel"]:
        precicion = random.uniform(0, 100) #numero random 
        #si el numero ramdom esta dentro del rango de la presicion del movimiento acierta si no falla
        if porcentaje_de_acierto_J >= precicion: 
            PsA_Rival -= Daño(movimiento, Pokemon_J, Pokemon_R) #para el jugador si acierta
        else:
            messagebox.showinfo("Precisión", "El movimiento falló") #para el jugador si falla

        precicion = random.uniform(0, 100)
        if porcentaje_de_acierto_B >= precicion:
            PsA_Jugador -= Daño(movimiento_B, Pokemon_R, Pokemon_J)
        else:
            messagebox.showinfo("Precisión", "El movimiento falló")
    else:
        precicion = random.uniform(0, 100)
        if porcentaje_de_acierto_B >= precicion:
            PsA_Jugador -= Daño(movimiento_B, Pokemon_R, Pokemon_J)
        else:
            messagebox.showinfo("Precisión", "El movimiento falló")

        precicion = random.uniform(0, 100)
        if porcentaje_de_acierto_J >= precicion:
            PsA_Rival -= Daño(movimiento, Pokemon_J, Pokemon_R)
        else:
            messagebox.showinfo("Precisión", "El movimiento falló")

    #llama a la funcion para actualizar los texto donde refleja la vida de los pokemons
    actualizar_ps(labelB, labelJ, Pokemon_R, Pokemon_J)

def actualizar_ps(labelB, labelJ, Pokemon_R, Pokemon_J):
    global PsA_Rival, PsA_Jugador
    vida_rival = pokemones[Pokemon_R]["hp"]
    vida_jugador = pokemones[Pokemon_J]["hp"]

    #verifica que mientras que los valores sean mayores cero actualiza los valores
    if labelB.winfo_exists(): 
        if PsA_Rival > 0:
            labelB.configure(text=f"{Pokemon_R}\nPS: {max(0, PsA_Rival)}/{vida_rival}", font=("Arial", 12, "bold"))
    if labelJ.winfo_exists():
        if PsA_Jugador > 0:
            labelJ.configure(text=f"{Pokemon_J}\nPS: {max(0, PsA_Jugador)}/{vida_jugador}", font=("Arial", 12, "bold"))

def precicion_calculo(movimiento, pokemon_A, pokemon_D):
    P_movimiento = Precicion_de_movimiento[movimiento]

    P_pokemon_A = pokemones[pokemon_A]["precicion"]

    E_pokemon_D = pokemones[pokemon_D]["evacion"]

    porcentaje_final = P_movimiento * (P_pokemon_A/E_pokemon_D)

    return float(porcentaje_final)

#Elije de forma alatoria el movimiento del bot 
def movimiento_bot(pokemon_bot):
    movimiento = [seleccionar_movimiento(pokemon_bot, 0), seleccionar_movimiento(pokemon_bot, 1), seleccionar_movimiento(pokemon_bot, 2), seleccionar_movimiento(pokemon_bot, 3)]
    seleccion = random.choice(movimiento)
    return seleccion

def evacion_precicion(movimiento,Pokemon_A, Pokemon_D):
    if tipo_de_movimientos[movimiento] == "Alt_Precicion":
        if movimiento in tipo_de_movimientos[movimiento]["P-1"]: 
            v_A = pokemones[Pokemon_D]["precicion"]
        
            v_A -= 1    
    else:
        if movimiento in tipo_de_movimientos[movimiento]["E-1"]:
            v_A = pokemones[Pokemon_A]["evacion"]
            
            v_A += 1
            
#Calcula el daño con la formula de los juegos originales
def Daño(movimiento, Pokemon_A, Pokemon_D):
    N = 1

    #dependiendo del tipo del ataque elije las stats corespondientes
    if Tipo_movimiento(movimiento) == "Físico":
        A = pokemones[Pokemon_A]["atk"]
        D = pokemones[Pokemon_D]["def"]
    else:
        A = pokemones[Pokemon_A]["atkE"]
        D = pokemones[Pokemon_D]["defE"]

    P = Potencia_de_movimientos[movimiento]
    
    #si el tipo del ataque es igual al del pokemon o no se le asigna el bonus correspondiente
    if Tipos_pokemons[Pokemon_A] == tipos_movimientos[movimiento]:
        B = 1.5
    else:
        B = 1

    #utiliza el tipo del movimiento para saber si el mismo tiene mas o menos eficacia 
    E = Eficacia(tipos_movimientos[movimiento], Tipos_pokemons[Pokemon_D])

    V = random.randint(85, 100) #valor ramdompara la cuenta

    #calculo final
    Damage = 0.01 * B * E * V * (((0.2 * N + 1) * A * P) / (25 * D) + 2)

    return int(Damage)

def Pelea(Pokemon):
    #declaracion de variable globales para usar los mismo variables en todos lados
    global PsA_Rival, PsA_Jugador, tempjugador, tempbot
    global Pokemon_Rival
    global vida_jugador, vida_rival
    
    #pokemon del rival (seleccion alatoria)
    num = [1, 4, 7]
    R = random.choice(num)
    Pokemon_Rival = serch_pokemon_num(R)

    #vida actual y total de los pokemons
    PsA_Rival = pokemones[Pokemon_Rival]["hp"]  # rival(bot)
    PsA_Jugador = pokemones[Pokemon]["hp"]  # jugador
    vida_rival = pokemones[Pokemon_Rival]["hp"]
    vida_jugador = pokemones[Pokemon]["hp"]

    #crea la ventana de batalla
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

    # Creación dinámica de botones de ataque
    j = -1 #fijate como queres acomodar esta inicializacion por que queda raro aca
    for i in range(4):
        move = seleccionar_movimiento(Pokemon, i)
        button = CTkButton(
            master=frame_Botones,
            text=move,
            height=40,
            width=120,
            text_color="white",
            corner_radius=5,
            command=lambda idx=i: decicion_ataque(idx, Pokemon, Pokemon_Rival, text_name_B, text_name_J)
        )
        if i < 2:
            button.place(relx=0.25 + 0.5*i, rely=0.25, anchor="center")
        elif i > 1:
            j += 1
            button.place(relx=0.25 + 0.5*j, rely=0.75, anchor="center")

    root.mainloop()

# Llamada a la función principal
Pelea("Charmander")  # Puedes cambiar "Charmander" por el Pokémon que desees