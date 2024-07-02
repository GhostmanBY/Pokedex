import os #importa os para usar cls y pause
import random #importa random para que se pueda usar numeors randoms
import tkinter as tk
from customtkinter import CTkTextbox

from Pokedex import serch_pokemon_num #desde el archivo pokedex importa la funcion serch_pokemon_num
from Estadisticas import pokemones #desde el archivo estadisticas importa Hp, Atk, Def, AtkE, DefE, Vel los cuales son diccionarios
from Movimiento import seleccionar_movimiento, Tipo_movimiento #desde el archivo Movimiento importa seleccionar_movimiento, Tipo_movimiento las cuales son funciones
from Movimiento import Potencia_de_movimientos, Precicion_de_movimiento #desde el archivo Movimiento importa Potencia_de_movimientos, Precicion_de_movimiento las cuales son diccionarios
from Tabla_de_tipos import Tipos_pokemons, tipos_movimientos #desde el archivo Tabla_de_tipos importa Tipos_pokemons, tipos_movimientos las cuales son diccionarios
from Tabla_de_tipos import Eficacia #desde el archivo Tabla_de_tipos importa Eficacia la cual es una funcion

def cls_pause(): #esta funcion solo es para juntar el system pause y cls
    if os.name == "nt":
        os.system("cls")
        os.system("pause")
    else:
        os.system("clear")
        input("Press Enter to continue...")

def movimiento_R(pokemon_bot): #esta funcion selecciona de forma alatoria el movimiento del rival 
    movimiento = [seleccionar_movimiento(pokemon_bot, 0), seleccionar_movimiento(pokemon_bot, 1)] #mete en una lista los movimiento del rival
    seleccion = random.choice(movimiento) #genera un numero alatorio y le da ese valor como posicion dentro de la lista
    return seleccion #retorna el nombre del movimiento

def Daño(movimiento, Pokemon_J, Pokemon_R): #Funcion para calcular el daño tanto del jugador como del rival(bot)

    N = 1 #variable del nivel del pokemon 
    
    if Tipo_movimiento(movimiento) == "Fisco": #if para saber si es un ataque especial o fisico, lo cual evalua desde el archivo Tabla_de_tipos
        A = pokemones[Pokemon_J]["atk"] #toma el ataque del pokemon atacante, desde el archivo Estadistica
        D = pokemones[Pokemon_R]["def"] #toma la defensa del pokemon defensor, desde el archivo Estadistica
    else: #caso en el que sea especial
        A = pokemones[Pokemon_J]["atkE"] #toma el ataque especial del pokemon atacante, desde el archivo Estadistica
        D = pokemones[Pokemon_R]["defE"] #toma la defensa especial del pokemon defensor, desde el archivo Estadistica

    P = Potencia_de_movimientos[movimiento] #toma la potencia del movimiento respectivo, desde el archivo Movimiento

    if Tipos_pokemons[Pokemon_J] == tipos_movimientos[movimiento]: #if para saber si el tipo del ataque es igual al del pokemon, lo evalua desde el archivo Tabla_de_tipos
        B = 1.5 #caso verdadero
    else:
        B = 1 #caso falso

    E = Eficacia(tipos_movimientos[movimiento], Tipos_pokemons[Pokemon_R]) #Esta funcion evalua que eficiencia tiene el mocimiento contra el tipo del pokemon del rival

    V = random.randint(85, 100) #genera un numero alatorio el cual se usa para el calculo
    
    Damage = 0.01 * B * E * V * (((0.2 * N + 1) * A * P) / (25 * D) + 2) #hace el respectivo calculo de daño
    
    return int(Damage) #retorn la cantidad de puntos de vida que se le va a restar al pokemon del rival
    

def pelea(Pokemon): #funcion de "interfaz de juego"
    
    root = tk.Tk()
    root.title("Sistema de combate")
    root.geometry("500x500")

    batalla = CTkTextbox(root, height=300, width=500)
    batalla.pack()



    num = [1, 4, 7] #lista de pokemon disponibles
    R = random.choice(num) #numero dentro del rango de la lista
    Pokemon_Rival = serch_pokemon_num(R) #pokemon a raiz del numero generado 

    print(f"Tu {Pokemon} se va a enfrentar a un {Pokemon_Rival}") #mensaje que informa al jugador contra que pokemon va a luchar
    global PsA_Rival, PsA_Jugador #definicion global de los puntos de vida de cada pokemon
    PsA_Rival = pokemones[Pokemon_Rival]["hp"] #rival(bot)
    PsA_Jugador = pokemones[Pokemon]["hp"] #jugador
    
    vida_rival = pokemones[Pokemon_Rival]["hp"]
    vida_jugador = pokemones[Pokemon]["hp"]
    tempjugador = (f"{Pokemon}\nPs{PsA_Jugador}/{vida_jugador}")
    tempbot = (f"\n\n\n{Pokemon_Rival}\nPs{PsA_Rival}/{vida_rival}")
    while PsA_Jugador > 0 and PsA_Rival > 0: #este while determina que hasta que no se llegue a 0 de vida de un de los dos pokemons no se termina el combate
        batalla.insert("0.0", text=tempbot) #muestra al pokemon del rival(bot)
        batalla.insert("0.0", text=tempjugador) #muestra al pokemon del Jugador

        print("Elija un movimiento: ") #da un mensaje indicativo
        movimiento = input(f"\n{seleccionar_movimiento(Pokemon, 1)}\n\n{seleccionar_movimiento(Pokemon, 0)}\nEleccion: ") #muestra los ataques correspondientes del pokemon del jugador
        movimiento_bot = movimiento_R(Pokemon_Rival) #manda el pokemon del rival(bot) a la funcion de seleccion de movimiento dle mismo

        if pokemones[Pokemon]["vel"] > pokemones[Pokemon_Rival]["vel"]: #este if es para determinar que pokemon ataca primero que otro
            precicion = random.randint(0, 100) #genera numero random el cual hace de precicion
            #print(f"La precicion fue de {precicion}") #esto es para hacer pruebas de la precicion
            #este if contiguo es para la precicion del jugador
            if Precicion_de_movimiento[movimiento] >= precicion: #evalua si el numero random esta en el rango de chanse del movimeinto
                PsA_Rival -= Daño(movimiento, Pokemon, Pokemon_Rival) #Luego si la precicion esta dentro del rango se ejecuta el calculo de daño del jugador
            else: #caso falso en precicion
                print("Su movimiento a fallado") #mensaje demostrativo
            #divicion de if
            # El contiguio hace lo mismo que el de ariba pero para el pokemon enemigo 
            precicion = random.randint(0, 100)
            #print(f"La precicion fue de {precicion}") #esto es para hacer pruebas de la precicion
            if Precicion_de_movimiento[movimiento_bot] >= precicion:    
                PsA_Jugador -= Daño(movimiento_bot, Pokemon_Rival, Pokemon)
            else:
                print("El movimiento del rival fallo")
        else: #este caso falso es para el if principal donde se ve que pokemon es mas rapido
            #todo lo que esta aca dentro es lo mismo que arriba pero invierte el orde de jugadores
            precicion = random.randint(0, 100)
            #print(f"La precicion fue de {precicion}") #esto es para hacer pruebas de la precicion
            if Precicion_de_movimiento[movimiento_bot] >= precicion:    
                PsA_Jugador -= Daño(movimiento_bot, Pokemon_Rival, Pokemon)
            else:
                print("El movimiento del rival fallo")

            precicion = random.randint(0, 100)
            #print(f"La precicion fue de {precicion}") #esto es para hacer pruebas de la precicion
            if Precicion_de_movimiento[movimiento] >= precicion:        
                PsA_Rival -= Daño(movimiento, Pokemon, Pokemon_Rival)
            else:
                print("Su movimiento a fallado")
        cls_pause()#da una pausa para ver si fallo o no el ataque y despues borra para que se vuelva a ver la interfaz
    #if para dar un mensaje una vez que se termina el combate
    if PsA_Rival <= 0:
        print(f"FELIDADES TU {Pokemon} GANO")
    else: 
        print(f"Tu {Pokemon} a perdido")
    #comandos de consola 
    cls_pause()
    root.mainloop()

def combate(Pokemon): #funcion para empezar el combate 
    root = tk.Tk()
    root.title("Sistema de combate")
    root.geometry("500x500")

    batalla = CTkTextbox(root, height=300, width=500)
    batalla.insert("0.0", "BIENVENIDO AL SISTEMA DE COMBATE")
    batalla.pack()


    root.mainloop()

    num = [1, 4, 7] #lista de pokemon disponibles
    R = random.choice(num) #numero dentro del rango de la lista
    Pokemon_Rival = serch_pokemon_num(R) #pokemon a raiz del numero generado 

    print(f"Tu {Pokemon} se va a enfrentar a un {Pokemon_Rival}") #mensaje que informa al jugador contra que pokemon va a luchar
    global PsA_Rival, PsA_Jugador #definicion global de los puntos de vida de cada pokemon
    PsA_Rival = pokemones[Pokemon_Rival]["hp"] #rival(bot)
    PsA_Jugador = pokemones[Pokemon]["hp"] #jugador
    cls_pause() #comandos de consola
    pelea(Pokemon, Pokemon_Rival, PsA_Jugador, PsA_Rival) #manda los parametros a la funcion de pelea

# l = "Bulbasaur"
# pelea(l)