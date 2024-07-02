Tipos_pokemons = {
    "Bulbasaur": "Planta", "Charmander": "Fuego", "Squirtle": "Agua"
} #Diccionario de los tipos de cada pokemon

tipos_movimientos = {
    "Ascuas": "Fuego", "Latigo cepa": "Planta", "Pistola agua": "Agua",
    "Placaje": "Normal",
} #diccionario de los tipos de cada ataque

Tipos_x2 = {
    "Planta": {"Agua"}, "Fuego": {"Planta"}, "Agua": {"Fuego"}    
} #Diccionario de todos los tipos que al atacar al otro son eficazes(x2)
Tipos_x1 = {
    "Normal": {"Roca"},
} #Diccionario de todos los tipos que al atacar al otro son neutros(x1)
Tipos_x05 = {
    "Planta": {"Planta", "Fuego"}, "Fuego": {"Fuego", "Agua"}, "Agua": {"Agua", "Planta"}
} #Diccionario de todos los tipos que al atacar al otro son resistentes(x0.5)

def Eficacia(Tipo_Atacante, Tipo_Defensor): #funcion para definir la eficacioa
    if Tipo_Defensor in Tipos_x2.get(Tipo_Atacante, []): #Dice que si Tipo del pokemon que resive el ataqe esta dentro del diccionario de x2(buscando en cada una de los sub indice) retorna 2
        return 2
    elif Tipo_Defensor in Tipos_x1.get(Tipo_Atacante, []): #Dice que si Tipo del pokemon que resive el ataqe esta dentro del diccionario de x1(buscando en cada una de los sub indice) retorna 1
        return 1
    elif Tipo_Defensor in Tipos_x05.get(Tipo_Atacante, []): #Dice que si Tipo del pokemon que resive el ataqe esta dentro del diccionario de x05(buscando en cada una de los sub indice) retorna 0.5
        return 0.5
    else:
        return 1 #en caso de que no este en ninguno de los 3 se retorna 1 para que no haya problemas con el calculo
