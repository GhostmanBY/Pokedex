tipo_de_movimientos = {
    "Especial":["Ascuas", "Pistola agua"],
    "Fisico":["Latigo cepa", "Placaje"],
    "Alt_Precicion":["Ataque arena"],
    "Alt_Evacion":["Doble equipo"],
} #diccionario de los tipos de ataques

def Tipo_movimiento(movimiento): #funcion para saber el tipo de ataque que se ingreso
    for tipo, movimientos in tipo_de_movimientos.items(): #va buscando en cada item del diccionario de tipos de movimiento
        if movimiento.capitalize() in movimientos: #verifica si el movimiento ingresa esta en el tipo que esta el for 
            return tipo #si es verdadero retorna el tipo que es el movimiento
    return None #en caso de que no exista devuelva None

Potencia_de_movimientos = {
    "Ascuas": 40, "Pistola agua": 40, "Latigo cepa": 45, "Placaje": 40,
    "Doble equipo": 1, "Ataque arena": 1
} #Diccionario de potencia de cada movimiento
Precicion_de_movimiento = {
    "Ascuas": 80, "Pistola agua": 80, "Latigo cepa": 80, "Placaje": 100,
    "Doble equipo": 100, "Ataque arena": 100
} #diccionario de precicion de cada movimiento

movimientos_de_Pokemons = {
    "Bulbasaur": {"Latigo cepa", "Placaje"}, "Charmander": {"Ascuas", "Placaje"}, "Squirtle": {"Pistola agua", "Placaje"}
} #Movimientos de cada pokemon

def seleccionar_movimiento(pokemon, i): #funcion para identificar los movimiento de cada pokemon
    movimientos = list(movimientos_de_Pokemons.get(pokemon, [])) #le asigana a movimiento la lista completa de los movimientos del pokemon resivido
    if movimientos: #verifica si el pokemon tiene movimientos
        return movimientos[i] #en caso verdadero retorna el movimiento en la posicion indicada por i
    return None #en caso de que no tenga ningun movimiento retorna None
