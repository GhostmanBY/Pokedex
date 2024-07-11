import tkinter as tk
from tkinter import messagebox
from customtkinter import *
import random
import copy

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


def decicion_ataque(indice, Pokemon_J, Pokemon_R, barra_oponente, barra_jugador, label_oponente, label_jugador, historial_label):
    global PsA_Rival, PsA_Jugador
    
    if PsA_Rival <= 0 or PsA_Jugador <= 0:
        if PsA_Rival <= 0:
            historial_label.configure(text="¡El jugador ha ganado!", text_color="green")
        elif PsA_Jugador <= 0:
            historial_label.configure(text="¡El Rival ha ganado!", text_color="red")
        return

    movimientos = [seleccionar_movimiento(Pokemon_J, i) for i in range(4)]
    ataque = movimientos[indice]

    porcentaje_de_acierto_J = precicion_calculo(ataque, Pokemon_J, Pokemon_R)
    movimiento_B = movimiento_bot(Pokemon_R)
    porcentaje_de_acierto_B = precicion_calculo(movimiento_B, Pokemon_R, Pokemon_J)

    # Determinar el orden de ataque según la velocidad
    if pokemones[Pokemon_J]["vel"] > pokemones[Pokemon_R]["vel"]:
        orden = [(Pokemon_J, ataque, porcentaje_de_acierto_J), (Pokemon_R, movimiento_B, porcentaje_de_acierto_B)]
    elif pokemones[Pokemon_J]["vel"] < pokemones[Pokemon_R]["vel"]:
        orden = [(Pokemon_R, movimiento_B, porcentaje_de_acierto_B), (Pokemon_J, ataque, porcentaje_de_acierto_J)]
    else:  # Velocidades iguales, decidir al azar
        if random.randint(1, 2) == 1:
            orden = [(Pokemon_J, ataque, porcentaje_de_acierto_J), (Pokemon_R, movimiento_B, porcentaje_de_acierto_B)]
        else:
            orden = [(Pokemon_R, movimiento_B, porcentaje_de_acierto_B), (Pokemon_J, ataque, porcentaje_de_acierto_J)]
    
    historial = ""
    for atacante, movimiento, precision in orden:
        precision_aleatoria = random.uniform(0, 100)
        if precision >= precision_aleatoria:
            if atacante == Pokemon_J:
                if Tipo_movimiento(movimiento) in ["Especial", "Fisico"]:
                    daño = Daño(movimiento, Pokemon_J, Pokemon_R, Jugador=True)
                    PsA_Rival -= daño
                    historial += f"{Pokemon_J} usó {movimiento} y causó {daño} de daño.\n"
                    # Verifica que animar_ataque esté definido
                    animar_ataque(label_oponente)
                else:
                    stat = evacion_precicion(movimiento, Pokemon_J, Pokemon_R, Jugador=True)
                    if stat == "Alt_Precicion":
                        stat = "precision"
                    elif stat == "Alt_Evacion":
                        stat = "evacion"

                    historial += f"{Pokemon_J} usó {movimiento} y afectó la {stat} de {Pokemon_R}.\n"
            else:
                if Tipo_movimiento(movimiento_B) in ["Especial", "Fisico"]:
                    daño = Daño(movimiento_B, Pokemon_R, Pokemon_J, Jugador=False)
                    PsA_Jugador -= daño
                    historial += f"{Pokemon_R} usó {movimiento_B} y causó {daño} de daño.\n"
                    # Verifica que animar_ataque esté definido
                    animar_ataque(label_jugador)
                else:
                    stat = evacion_precicion(movimiento_B, Pokemon_R, Pokemon_J, Jugador=False)
                    if stat == "Alt_Precicion":
                        stat = "precision"
                    elif stat == "Alt_Evacion":
                        stat = "evacion"
                        
                    historial += f"{Pokemon_R} usó {movimiento_B} y afectó la {stat} de {Pokemon_J}.\n"
        else:
            historial += f"{atacante} falló al usar {movimiento}.\n"
    
    historial_label.configure(text=historial)

    actualizar_ps(barra_oponente, barra_jugador, label_oponente, label_jugador, Pokemon_R, Pokemon_J)

def actualizar_ps(barra_oponente, barra_jugador, label_oponente, label_jugador, Pokemon_R, Pokemon_J):
    global PsA_Rival, PsA_Jugador
    vida_rival = pokemones[Pokemon_R]["hp"]
    vida_jugador = pokemones[Pokemon_J]["hp"]

    label_oponente.configure(text=f"{Pokemon_R}\nPS: {max(0, PsA_Rival)}/{vida_rival}")
    label_jugador.configure(text=f"{Pokemon_J}\nPS: {max(0, PsA_Jugador)}/{vida_jugador}")

    # Actualizar barras de vida
    porcentaje_rival = max(0, min(PsA_Rival / vida_rival, 1))
    porcentaje_jugador = max(0, min(PsA_Jugador / vida_jugador, 1))
    
    barra_oponente.configure(progress_color=get_health_color(porcentaje_rival))
    barra_jugador.configure(progress_color=get_health_color(porcentaje_jugador))
    
    barra_oponente.set(porcentaje_rival)
    barra_jugador.set(porcentaje_jugador)

def animar_ataque(label):
    original_pos = label.place_info()
    for _ in range(3):
        label.place(x=int(original_pos['x'])+5, y=int(original_pos['y'])-5)
        label.update()
        label.after(50)
        label.place(x=int(original_pos['x'])-5, y=int(original_pos['y'])+5)
        label.update()
        label.after(50)
    label.place(x=int(original_pos['x']), y=int(original_pos['y']))

def get_health_color(percentage):
    if percentage > 0.5:
        return "green"
    elif percentage > 0.2:
        return "yellow"
    else:
        return "red"
    
def precicion_calculo(ataque, pokemon_A, pokemon_D):
    P_movimiento = Precicion_de_movimiento[ataque]

    P_pokemon_A = pokemones[pokemon_A]["precicion"]
    
    E_pokemon_D = pokemones[pokemon_D]["evacion"]
    
    porcentaje_final = P_movimiento * (P_pokemon_A/E_pokemon_D)
    
    return float(porcentaje_final)

def movimiento_bot(pokemon_bot):
    movimiento = [seleccionar_movimiento(pokemon_bot, i) for i in range(4)]
    return random.choice(movimiento)

def evacion_precicion(movimiento, Pokemon_A, Pokemon_D, Jugador=True):
    if Tipo_movimiento(movimiento) == "Alt_Precicion":
        if movimiento in variacion[Tipo_movimiento(movimiento)]:
            if Jugador == True:
                clon_stats[Pokemon_D]["precicion"] -= variacion[Tipo_movimiento(movimiento)][movimiento]
            else:
                pokemones[Pokemon_D]["precicion"] -= variacion[Tipo_movimiento(movimiento)][movimiento]
    else:
        if movimiento in variacion[Tipo_movimiento(movimiento)]:
            if Jugador == True:
                clon_stats[Pokemon_A]["evacion"] += variacion[Tipo_movimiento(movimiento)][movimiento]
            else:
                pokemones[Pokemon_A]["evacion"] += variacion[Tipo_movimiento(movimiento)][movimiento]
    return Tipo_movimiento(movimiento)

def Daño(movimiento, Pokemon_A, Pokemon_D, Jugador=True):

    N = 1
    
    if Tipo_movimiento(movimiento) == "Físico":
        if Jugador == True:
            A = pokemones[Pokemon_A]["atk"] #Ataque Físico Jugador
            D = clon_stats[Pokemon_A]["atk"] #Defensa Física alterada o no Bot
        else:
            A = clon_stats[Pokemon_A]["atk"] #Ataque Físico alterado o no Bot
            D = pokemones[Pokemon_D]["def"] #Defensa Física Jugador
    else:
        if Jugador == True:
            A = pokemones[Pokemon_A]["atkE"] #Ataque Especial Jugador
            D = clon_stats[Pokemon_A]["atkE"] #Defensa Especial alterada o no Bot
        else:
            A = clon_stats[Pokemon_A]["atkE"] #Ataque Especial alterado o no Bot
            D = pokemones[Pokemon_D]["defE"] #Defensa Especial Jugador

    P = Potencia_de_movimientos[movimiento]
    
    B = 1.5 if Tipos_pokemons[Pokemon_A] == tipos_movimientos[movimiento] else 1

    E = Eficacia(tipos_movimientos[movimiento], Tipos_pokemons[Pokemon_D])

    V = random.randint(85, 100)

    Damage = 0.01 * B * E * V * (((0.2 * N + 1) * A * P) / (25 * D) + 2)

    return int(Damage)



def Pelea(Pokemon):
    global PsA_Rival, PsA_Jugador, Pokemon_Rival, vida_jugador, vida_rival, clon_stats
    num = [1, 4, 7]
    R = random.choice(num)
    Pokemon_Rival = serch_pokemon_num(R)
    clon_stats = copy.deepcopy(pokemones)

    PsA_Rival = pokemones[Pokemon_Rival]["hp"]
    PsA_Jugador = pokemones[Pokemon]["hp"]
    vida_rival = pokemones[Pokemon_Rival]["hp"]
    vida_jugador = pokemones[Pokemon]["hp"]

    root = CTk()
    root.geometry("400x500")
    root.title("Combate Pokémon")

    main_frame = CTkFrame(master=root, height=500, width=400, fg_color=POKE_RED, corner_radius=0)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    batalla_frame = CTkFrame(master=main_frame, height=320, width=300, fg_color="#AEA499", border_width=5, border_color="black")
    batalla_frame.place(relx=0.5, rely=0.35, anchor="center")

    barra_R = CTkProgressBar(master=batalla_frame, width=100, height=20, border_width=1, border_color="black", progress_color="green")
    barra_R.place(relx=0.8, rely=0.15, anchor="center")
    barra_R.set(1)

    label_R = CTkLabel(master=batalla_frame, text=f"{Pokemon_Rival}\nPS: {PsA_Rival}/{vida_rival}", text_color="#3E3934")
    label_R.place(relx=0.8, rely=0.25, anchor="center")

    barra_J = CTkProgressBar(master=batalla_frame, width=100, height=20, border_width=1, border_color="black", progress_color="green")
    barra_J.place(relx=0.2, rely=0.55, anchor="center")
    barra_J.set(1)

    label_J = CTkLabel(master=batalla_frame, text=f"{Pokemon}\nPS: {PsA_Jugador}/{vida_jugador}", text_color="#3E3934")
    label_J.place(relx=0.2, rely=0.65, anchor="center")

    ataques_frame = CTkFrame(master=batalla_frame, height=100, width=300, fg_color="#82786D", corner_radius=10)
    ataques_frame.place(relx=0.5, rely=0.84, anchor="center")

    opciones = [seleccionar_movimiento(Pokemon, i) for i in range(4)]
    global seleccion
    seleccion = 0

    def actualizar_opciones(ataques_frame):
        for i in range(2):
            for j in range(2):
                idx = i * 2 + j
                if idx < 4:
                    if idx == seleccion:
                        btn = CTkButton(ataques_frame, text=opciones[idx], fg_color="gray", hover_color=POKE_BLUE, 
                                        command=lambda idx=idx: seleccionar_opcion(idx), height=40, width=130)
                    else:
                        btn = CTkButton(ataques_frame, text=opciones[idx], fg_color="#999999", hover_color=POKE_BLUE,
                                        command=lambda idx=idx: seleccionar_opcion(idx), height=40, width=130)
                    btn.grid(row=i, column=j, padx=5, pady=2)

    def tecla_arriba(event):
        global seleccion
        if seleccion > 1:
            seleccion -= 2
        actualizar_opciones(ataques_frame)

    def tecla_abajo(event):
        global seleccion
        if seleccion < 2:
            seleccion += 2
        actualizar_opciones(ataques_frame)

    def tecla_izquierda(event):
        global seleccion
        if seleccion % 2 == 1:
            seleccion -= 1
        actualizar_opciones(ataques_frame)

    def tecla_derecha(event):
        global seleccion
        if seleccion % 2 == 0 and seleccion < 3:
            seleccion += 1
        actualizar_opciones(ataques_frame)

    def tecla_enter(event):
        decicion_ataque(seleccion, Pokemon, Pokemon_Rival, barra_R, barra_J, label_R, label_J, battle_log)

    def seleccionar_opcion(idx):
        global seleccion
        seleccion = idx
        tecla_enter(None)
    
    def salir(event):
        root.destroy()
        
    historial_frame = CTkFrame(master=main_frame, height=120, width=260, fg_color="#C0C0C0", bg_color="black", border_width=5, border_color="black")
    historial_frame.place(relx=0.5, rely=0.82, anchor="center")
    
    battle_log = CTkLabel(historial_frame, 
                          text=f"Tu {Pokemon} se va a enfrentar a un {Pokemon_Rival}",
                          font=("Arial", 12), 
                          text_color="black", 
                          wraplength=220,
                          width=240,
                          height=100)
    battle_log.place(relx=0.5, rely=0.5, anchor="center")

    actualizar_opciones(ataques_frame)
    root.bind("<Up>", tecla_arriba)
    root.bind("<Down>", tecla_abajo)
    root.bind("<Left>", tecla_izquierda)
    root.bind("<Right>", tecla_derecha)
    root.bind("<Return>", tecla_enter)
    root.bind("<z>", tecla_enter)
    root.bind("<Escape>", salir)
    root.bind("<x>", salir)
    
    root.mainloop()

# Las demás funciones permanecen igual

# Llamada a la función principal
if __name__ == "__main__":
    Pelea("Charmander")