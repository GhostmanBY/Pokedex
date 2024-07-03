# Diccionario de los tipos de ataques
tipo_de_movimientos = {
    "Especial": ["Ascuas", "Pistola agua", "Rayo", "Psíquico"],
    "Fisico": ["Latigo cepa", "Placaje", "Llamarada", "Puño Fuego", "Golpe Karate", "Cuchillada", "Hoja Afilada"],
    "Alt_Precicion": ["Ataque arena"],
    "Alt_Evacion": ["Doble equipo", "Onda Trueno", "Hipnosis"],
} 

def Tipo_movimiento(movimiento): # función para saber el tipo de ataque que se ingresó
    for tipo, movimientos in tipo_de_movimientos.items(): # va buscando en cada item del diccionario de tipos de movimiento
        if movimiento.capitalize() in movimientos: # verifica si el movimiento ingresado está en el tipo que está en el for 
            return tipo # si es verdadero, retorna el tipo que es el movimiento
    return None # en caso de que no exista, devuelve None

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
    "Bulbasaur": ["Latigo cepa", "Placaje", "Hoja Afilada"],
    "Charmander": ["Ascuas", "Placaje", "Llamarada", "Puño Fuego"],
    "Squirtle": ["Pistola agua", "Placaje", "Surf"],
    "Pikachu": ["Rayo", "Onda Trueno", "Placaje"],
    "Machop": ["Golpe Karate", "Placaje", "Puño Fuego"],
    "Abra": ["Psíquico", "Hipnosis", "Doble equipo"],
    "Sandshrew": ["Ataque arena", "Placaje", "Cuchillada"],
    "Gengar": ["Hipnosis", "Psíquico", "Doble equipo"],
    "Eevee": ["Placaje", "Ataque arena", "Doble equipo"]
}

def seleccionar_movimiento(pokemon, i): # función para identificar los movimientos de cada Pokémon
    movimientos = list(movimientos_de_Pokemons.get(pokemon, [])) # le asigna a movimientos la lista completa de los movimientos del Pokémon recibido
    if movimientos: # verifica si el Pokémon tiene movimientos
        if 0 <= i < len(movimientos): # verifica si el índice está dentro del rango de movimientos disponibles
            return movimientos[i] # en caso verdadero, retorna el movimiento en la posición indicada por i
        else:
            return None # si el índice está fuera de rango, retorna None
    return None # en caso de que no tenga ningún movimiento, retorna None
