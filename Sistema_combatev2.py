import tkinter as tk
from tkinter import messagebox
from customtkinter import *
import random

# Importaciones de los módulos necesarios
from Pokedex import serch_pokemon_num
from Estadisticas import pokemones
from Movimiento import seleccionar_movimiento, Tipo_movimiento, Potencia_de_movimientos, Precicion_de_movimiento, variacion, movimientos_de_Pokemons
from Tabla_de_tipos import Tipos_pokemons, tipos_movimientos, Eficacia

# Definición de colores Pokédex
POKE_RED = "#C84124"
POKE_BLUE = "#3B4CCA"
POKE_YELLOW = "#FFDE00"
POKE_BLACK = "#1E1E1E"
POKE_WHITE = "#FFFFFF"

def decicion_ataque(indice, Pokemon_J, Pokemon_R, label_oponente, label_jugador, historial_label):
    global PsA_Rival, PsA_Jugador
    
    if PsA_Rival <= 0 or PsA_Jugador <= 0:
        if PsA_Rival <= 0:
            historial_label.configure(text="¡El jugador ha ganado!", text_color="green")
        elif PsA_Jugador <= 0:
            historial_label.configure(text="¡El Rival ha ganado!", text_color="red")
        return

    movimientos = [seleccionar_movimiento(Pokemon_J, i) for i in range(4)]
    ataque = movimientos[indice]

    if Tipo_movimiento(ataque) not in ["Especial", "Fisico"]:
        evacion_precicion(ataque, Pokemon_J, Pokemon_R)
    else:
        porcentaje_de_acierto_J = precicion_calculo(ataque, Pokemon_J, Pokemon_R)
        movimiento_B = movimiento_bot(Pokemon_R)
        porcentaje_de_acierto_B = precicion_calculo(movimiento_B, Pokemon_R, Pokemon_J)

        if pokemones[Pokemon_J]["vel"] > pokemones[Pokemon_R]["vel"]:
            orden = [(Pokemon_J, ataque, porcentaje_de_acierto_J), (Pokemon_R, movimiento_B, porcentaje_de_acierto_B)]
        else:
            orden = [(Pokemon_R, movimiento_B, porcentaje_de_acierto_B), (Pokemon_J, ataque, porcentaje_de_acierto_J)]

        historial = ""
        for atacante, movimiento, precision in orden:
            precicion = random.uniform(0, 100)
            if precision >= precicion:
                if atacante == Pokemon_J:
                    daño = Daño(movimiento, Pokemon_J, Pokemon_R)
                    PsA_Rival -= daño
                    historial += f"{Pokemon_J} usó {movimiento} y causó {daño} de daño.\n"
                else:
                    daño = Daño(movimiento, Pokemon_R, Pokemon_J)
                    PsA_Jugador -= daño
                    historial += f"{Pokemon_R} usó {movimiento} y causó {daño} de daño.\n"
            else:
                historial += f"{atacante} falló al usar {movimiento}.\n"
        
        historial_label.configure(text=historial)
    
    actualizar_ps(label_oponente, label_jugador, Pokemon_R, Pokemon_J)

def actualizar_ps(label_oponente, label_jugador, Pokemon_R, Pokemon_J):
    global PsA_Rival, PsA_Jugador
    vida_rival = pokemones[Pokemon_R]["hp"]
    vida_jugador = pokemones[Pokemon_J]["hp"]

    label_oponente.configure(text=f"{Pokemon_R}\nPS: {max(0, PsA_Rival)}/{vida_rival}")
    label_jugador.configure(text=f"{Pokemon_J}\nPS: {max(0, PsA_Jugador)}/{vida_jugador}")

def precicion_calculo(ataque, pokemon_A, pokemon_D):
    P_movimiento = Precicion_de_movimiento[ataque]

    P_pokemon_A = pokemones[pokemon_A]["precicion"]
    
    E_pokemon_D = pokemones[pokemon_D]["evacion"]
    
    porcentaje_final = P_movimiento * (P_pokemon_A/E_pokemon_D)
    
    return float(porcentaje_final)

def movimiento_bot(pokemon_bot):
    movimiento = [seleccionar_movimiento(pokemon_bot, 0), seleccionar_movimiento(pokemon_bot, 1)]
    return random.choice(movimiento)

def evacion_precicion(movimiento, Pokemon_A, Pokemon_D):
    if Tipo_movimiento(movimiento) == "Alt_Precicion":
        if movimiento in variacion[Tipo_movimiento(movimiento)]: 
            pokemones[Pokemon_D]["precicion"] -= variacion[Tipo_movimiento(movimiento)][movimiento]    
    else:
        if movimiento in variacion[Tipo_movimiento(movimiento)]:
            pokemones[Pokemon_A]["evacion"] += variacion[Tipo_movimiento(movimiento)][movimiento]

def Daño(movimiento, Pokemon_A, Pokemon_D):

    N = 1
    
    if Tipo_movimiento(movimiento) == "Físico":
        A = pokemones[Pokemon_A]["atk"]
        D = pokemones[Pokemon_D]["def"]
    else:
        A = pokemones[Pokemon_A]["atkE"]
        D = pokemones[Pokemon_D]["defE"]

    P = Potencia_de_movimientos[movimiento]
    
    B = 1.5 if Tipos_pokemons[Pokemon_A] == tipos_movimientos[movimiento] else 1

    E = Eficacia(tipos_movimientos[movimiento], Tipos_pokemons[Pokemon_D])

    V = random.randint(85, 100)

    Damage = 0.01 * B * E * V * (((0.2 * N + 1) * A * P) / (25 * D) + 2)

    return int(Damage)



def Pelea(Pokemon):
    global PsA_Rival, PsA_Jugador, Pokemon_Rival, vida_jugador, vida_rival
    num = [1, 4, 7]
    R = random.choice(num)
    Pokemon_Rival = serch_pokemon_num(R)

    PsA_Rival = pokemones[Pokemon_Rival]["hp"]
    PsA_Jugador = pokemones[Pokemon]["hp"]
    vida_rival = pokemones[Pokemon_Rival]["hp"]
    vida_jugador = pokemones[Pokemon]["hp"]

    root = CTk()
    root.geometry("350x400")
    root.title("Combate")

    main_frame = CTkFrame(master=root, height=400, width=350, fg_color=POKE_RED, corner_radius=0)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    batalla_frame = CTkFrame(master=main_frame, height=260, width=250, fg_color="#AEA499", border_width=5, border_color="black")
    batalla_frame.place(relx=0.5, rely=0.35, anchor="center")

    pokemon_R = CTkLabel(master=batalla_frame, text=f"{Pokemon_Rival}\n{PsA_Rival}/{vida_rival}", text_color="#3E3934")
    pokemon_R.place(relx=0.8, rely=0.15, anchor="center")

    pokemon_J = CTkLabel(master=batalla_frame, text=f"{Pokemon}\n{PsA_Jugador}/{vida_jugador}", text_color="#3E3934")
    pokemon_J.place(relx=0.2, rely=0.55, anchor="center")

    ataques_frame = CTkFrame(master=batalla_frame, height=90, width=240, fg_color="#82786D", corner_radius=0)
    ataques_frame.place(relx=0.5, rely=0.81, anchor="center")


    opciones = [seleccionar_movimiento(Pokemon, 0), seleccionar_movimiento(Pokemon, 1), seleccionar_movimiento(Pokemon, 2), seleccionar_movimiento(Pokemon, 3)]
    global seleccion
    seleccion = 0

    def actualizar_opciones(ataques_frame):
        # Calcular la cantidad de botones por columna
        num_filas = (4 + 1) // 2  # Asegura que la última fila tenga 2 botones si es impar
        for i in range(num_filas):
            for j in range(2):  # Dos columnas
                idx = i * 2 + j
                if idx < 4:
                    if idx == seleccion:
                        btn = CTkButton(ataques_frame, text=opciones[idx], fg_color="gray", command=lambda idx=idx: seleccionar_opcion(idx), height=40, width=110)
                    else:
                        btn = CTkButton(ataques_frame, text=opciones[idx], fg_color="#999999",command=lambda idx=idx: seleccionar_opcion(idx), height=40, width=110)
                    btn.grid(row=i, column=j, padx=5, pady=2)

    def tecla_arriba(event, ataques_frame):
        global seleccion
        if seleccion > 1:
            seleccion -= 2
        actualizar_opciones(ataques_frame)

    def tecla_abajo(event, ataques_frame):
        global seleccion
        if seleccion < 4 - 2:
            seleccion += 2
        actualizar_opciones(ataques_frame)

    def tecla_izquierda(event, ataques_frame):
        global seleccion
        if seleccion % 2 == 1:
            seleccion -= 1
        actualizar_opciones(ataques_frame)

    def tecla_derecha(event, ataques_frame):
        global seleccion
        if seleccion % 2 == 0 and seleccion + 1 < 4:
            seleccion += 1
        actualizar_opciones(ataques_frame)

    def tecla_enter(event, seleccion, Pokemon, Pokemon_Rival, pokemon_R, pokemon_J, battle_log):
        decicion_ataque(seleccion, Pokemon, Pokemon_Rival, pokemon_R, pokemon_J, battle_log)

    def seleccionar_opcion(idx):
        global seleccion
        seleccion = idx
        tecla_enter(None)
    
    def salir(event):
        root.destroy()
        
    historial_frame = CTkFrame(master=main_frame, height=100, width=220, fg_color="#C0C0C0", bg_color="black", border_width=5, border_color="black")
    historial_frame.place(relx=0.5, rely=0.79, anchor="center")
    
    battle_log = CTkLabel(historial_frame, 
                          text=f"Tu {Pokemon} se va a enfrentar a un {Pokemon_Rival}",
                          font=("Arial", 12), 
                          text_color="black", 
                          wraplength=180,
                          width=10,  # Ancho fijo
                          height=10)  # Alto fijo
    battle_log.place(relx=0.5, rely=0.5, anchor="center")

    actualizar_opciones(ataques_frame)
    root.bind("<Up>", lambda event: tecla_arriba(event, ataques_frame))
    root.bind("<Down>", lambda event: tecla_abajo(event, ataques_frame))
    root.bind("<Left>", lambda event: tecla_izquierda(event, ataques_frame))
    root.bind("<Right>", lambda event: tecla_derecha(event, ataques_frame))
    root.bind("<Return>", lambda event: tecla_enter(event, seleccion, Pokemon, Pokemon_Rival, pokemon_R, pokemon_J, battle_log))
    root.bind("<z>", lambda event: tecla_enter(event, seleccion, Pokemon, Pokemon_Rival, pokemon_R, pokemon_J, battle_log))
    root.bind("<Escape>", lambda event: salir(event))
    root.bind("<x>", lambda event: salir(event))
    
    root.mainloop()

# Llamada a la función principal
if __name__ == "__main__":
    Pelea("Charmander")