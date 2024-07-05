import tkinter as tk
from customtkinter import *
from PIL import Image
import requests
from io import BytesIO
import random

# Asegúrate de que estos imports sean correctos y que los archivos estén en la ubicación adecuada
from Pokedex import serch_pokemon_num
from Estadisticas import pokemones
from Movimiento import seleccionar_movimiento, Tipo_movimiento, Potencia_de_movimientos, Precicion_de_movimiento, variacion
from Tabla_de_tipos import Tipos_pokemons, tipos_movimientos, Eficacia

# Definición de colores Pokédex
POKE_RED = "#CC0000"
POKE_BLUE = "#3B4CCA"
POKE_YELLOW = "#FFDE00"
POKE_BLACK = "#1E1E1E"
POKE_WHITE = "#FFFFFF"

def obtener_imagen_pokemon(nombre, es_jugador=False, tamaño=(150, 150)):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}/"
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        if es_jugador:
            imagen_url = datos['sprites']['back_default']
        else:
            imagen_url = datos['sprites']['front_default']
        
        respuesta = requests.get(imagen_url)
        img = Image.open(BytesIO(respuesta.content))
        img = img.resize(tamaño)
        
        return CTkImage(light_image=img, dark_image=img, size=tamaño)
    except Exception as e:
        print(f"Error al obtener la imagen del Pokémon {nombre}: {e}")
        return None

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
    root.title("Sistema de combate Pokémon")
    root.geometry("800x700")
    set_appearance_mode("dark")

    # Main frame
    main_frame = CTkFrame(root, fg_color=POKE_BLACK)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Battle frame
    battle_frame = CTkFrame(main_frame, fg_color=POKE_RED, corner_radius=15)
    battle_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Opponent Pokemon frame
    opponent_frame = CTkFrame(battle_frame, fg_color=POKE_WHITE, corner_radius=10)
    opponent_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    foto_r = obtener_imagen_pokemon(Pokemon_Rival, tamaño=(150, 150))
    if foto_r:
        opponent_image = CTkLabel(opponent_frame, image=foto_r, text="")
        opponent_image.pack(side=tk.RIGHT, padx=10, pady=10)

    opponent_info = CTkLabel(opponent_frame, text=f"{Pokemon_Rival}\nPS: {PsA_Rival}/{vida_rival}", 
                             font=("Arial", 14, "bold"), text_color=POKE_BLACK)
    opponent_info.pack(side=tk.LEFT, padx=10, pady=10)

    # Player Pokemon frame
    player_frame = CTkFrame(battle_frame, fg_color=POKE_WHITE, corner_radius=10)
    player_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    foto_j = obtener_imagen_pokemon(Pokemon, es_jugador=True, tamaño=(150, 150))
    if foto_j:
        player_image = CTkLabel(player_frame, image=foto_j, text="")
        player_image.pack(side=tk.LEFT, padx=10, pady=10)

    player_info = CTkLabel(player_frame, text=f"{Pokemon}\nPS: {PsA_Jugador}/{vida_jugador}", 
                           font=("Arial", 14, "bold"), text_color=POKE_BLACK)
    player_info.pack(side=tk.RIGHT, padx=10, pady=10)

    # Battle log frame
    log_frame = CTkFrame(main_frame, fg_color=POKE_BLUE, corner_radius=10, height=100)
    log_frame.pack(fill=tk.X, padx=10, pady=10)

    log_title = CTkLabel(log_frame, text="Historial de batalla:", font=("Arial", 12, "bold"), text_color=POKE_YELLOW)
    log_title.pack(anchor="w", padx=10, pady=5)

    battle_log = CTkLabel(log_frame, text=f"Tu {Pokemon} se va a enfrentar a un {Pokemon_Rival}", 
                          font=("Arial", 12), text_color=POKE_WHITE, wraplength=700)
    battle_log.pack(padx=10, pady=5)

    # Buttons frame
    buttons_frame = CTkFrame(main_frame, fg_color=POKE_YELLOW, corner_radius=10)
    buttons_frame.pack(fill=tk.X, padx=10, pady=10)

    for i in range(4):
        button = CTkButton(
            master=buttons_frame,
            text=seleccionar_movimiento(Pokemon, i),
            height=40,
            width=180,
            fg_color=POKE_RED,
            text_color=POKE_WHITE,
            hover_color=POKE_BLUE,
            corner_radius=5,
            command=lambda i=i: decicion_ataque(i, Pokemon, Pokemon_Rival, opponent_info, player_info, battle_log)
        )
        button.grid(row=i//2, column=i%2, padx=10, pady=5, sticky="nsew")

    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)

    root.mainloop()

# Llamada a la función principal
if __name__ == "__main__":
    Pelea("Charmander")  # Puedes cambiar "Charmander" por el Pokémon que desees
