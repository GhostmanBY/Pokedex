# Diccionario de los tipos de ataques
tipo_de_movimientos = {
    "Especial": ["Ascuas", "Pistola agua", "Rayo", "Psíquico"],
    "Fisico": ["Latigo cepa", "Placaje", "Llamarada", "Puño Fuego", "Golpe Karate", "Cuchillada", "Hoja Afilada"],
    "Alt_Precicion": ["Ataque arena"],
    "Alt_Evacion": ["Doble equipo"]
}

def Tipo_movimiento(movimiento): # función para saber el tipo de ataque que se ingresó
    for tipo, movimientos in tipo_de_movimientos.items(): # va buscando en cada item del diccionario de tipos de movimiento
        if movimiento.capitalize() in movimientos: # verifica si el movimiento ingresado está en el tipo que está en el for 
            return tipo # si es verdadero, retorna el tipo que es el movimiento
    return None # en caso de que no exista, devuelve None

variacion = {
    "Alt_Precicion": {
        "Ataque arena": 1,
    },
    "Alt_Evacion": {
        "Doble equipo": 1,
    },
}

# Diccionario de potencia de cada movimiento
Potencia_de_movimientos = {
    "Ascuas": 40, "Pistola agua": 40, "Latigo cepa": 45, "Placaje": 40,
    "Doble equipo": 0, "Ataque arena": 0, "Rayo": 90, "Onda Trueno": 0,
    "Llamarada": 110, "Surf": 90, "Hoja Afilada": 55, "Puño Fuego": 75,
    "Golpe Karate": 50, "Cuchillada": 70, "Psíquico": 90, "Hipnosis": 0
}

# Diccionario de precisión de cada movimiento
Precicion_de_movimiento = {
    "Ascuas": 100, "Pistola agua": 100, "Latigo cepa": 100, "Placaje": 100,
    "Doble equipo": 100, "Ataque arena": 100, "Rayo": 100, "Onda Trueno": 90,
    "Llamarada": 85, "Surf": 100, "Hoja Afilada": 95, "Puño Fuego": 100,
    "Golpe Karate": 100, "Cuchillada": 100, "Psíquico": 100, "Hipnosis": 60
}

# Movimientos de cada Pokémon
movimientos_de_Pokemons = {
    "Bulbasaur": ["Latigo cepa", "Placaje", "Ataque arena", "Doble equipo" ], "Charmander": ["Llamarada", "Placaje", "Doble equipo", "Ataque arena"], "Squirtle": ["Pistola agua", "Placaje", "Ataque arena","Doble equipo"]
} #Movimientos de cada pokemon

def seleccionar_movimiento(pokemon, i): #funcion para identificar los movimiento de cada pokemon
    try:
        movimientos = list(movimientos_de_Pokemons.get(pokemon, [i])) #le asigana a movimiento la lista completa de los movimientos del pokemon resivido
        if movimientos: #verifica si el pokemon tiene movimientos
            return movimientos[i] #en caso verdadero retorna el movimiento en la posicion indicada por i
        print(movimientos[i])
        return None #en caso de que no tenga ningun movimiento retorna None
    except:
        return None