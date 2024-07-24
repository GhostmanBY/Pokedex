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
    "Venusaur": [
        "Tera Explosión",
        "Placaje",
        "Venganza",
        "Rayo Solar"
    ],
    "Pidgey": [
        "Furia",
        "Picoteo",
        "Tajo Aéreo",
        "Mimético"
    ],
    "Pidgeotto": [
        "Don Natural",
        "Picoteo",
        "Retribución",
        "Vendaval"
    ],
    "Kakuna": [
        "Fortaleza",
        "Picadura",
        "Disparo Demora",
        "Defensa Férrea"
    ],
    "Beedrill": [
        "Demolición",
        "Golpe Roca",
        "Viento Afín",
        "Picotazo"
    ],
    "Metapod": [
        "Picadura",
        "Defensa Férrea",
        "Electrotela",
        "Fortaleza"
    ],
    "Pidgeot": [
        "Ataque Aéreo",
        "Sonámbulo",
        "Vendaval",
        "Despejar"
    ],
    "Raticate": [
        "Bomba Lodo",
        "Furia",
        "Esfuerzo",
        "Mimético"
    ],
    "Wartortle": [
        "Disparo Lodo",
        "Tera Explosión",
        "Bostezo",
        "Viento Hielo"
    ],
    "Charizard": [
        "Tormenta Arena",
        "Cara Susto",
        "Falso Tortazo",
        "Golpe Roca"
    ],
    "Ivysaur": [
        "Hoja Afilada",
        "Somnífero",
        "Látigo Cepa",
        "Latigazo"
    ],
    "Weedle": [
        "Picotazo Veneno",
        "Disparo Demora",
        "Picadura",
        "Electrotela"
    ],
    "Squirtle": [
        "Pistola agua",
        "Placaje",
        "Doble equipo",
        "Ataque arena"
    ],
    "Caterpie": [
        "Ronquido",
        "Placaje",
        "Disparo Demora",
        "Picadura"
    ],
    "Charmeleon": [
        "Rapidez",
        "Eco Voz",
        "Tóxico",
        "Pulso Dragón"
    ],
    "Bulbasaur": [
        "Latigo cepa",
        "Placaje",
        "Doble equipo",
        "Ataque arena"
    ],
    "Butterfree": [
        "Teletransporte",
        "Beso Drenaje",
        "Don Natural",
        "Dulce Aroma"
    ],
    "Charmander": [
        "Ascuas",
        "Placaje",
        "Doble equipo",
        "Ataque arena"
    ],
    "Blastoise": [
        "Antiaéreo",
        "Viento Hielo",
        "Puño Dinámico",
        "Refuerzo"
    ],
    "Rattata": [
        "Sonámbulo",
        "Rayo Burbuja",
        "Voltio Cruel",
        "Venganza"
    ],
    "Fearow": [
        "Ciclón",
        "Falso Tortazo",
        "Don Natural",
        "Ronquido"
    ],
    "Spearow": [
        "Ataque Ala",
        "Golpe Aéreo",
        "Ataque Aéreo",
        "Don Natural"
    ],
    "Pikachu": [
        "Frustración",
        "Refuerzo",
        "Retribución",
        "Antojo"
    ],
    "Arbok": [
        "Ladrón",
        "Poder Oculto",
        "Divide Dolor",
        "Terratemblor"
    ],
    "Sandslash": [
        "Onda Certera",
        "Contoneo",
        "Confidencia",
        "Furia"
    ],
    "Nidoking": [
        "Supersónico",
        "Foco Energía",
        "Daño Secreto",
        "Onda Tóxica"
    ],
    "Sandshrew": [
        "Superdiente",
        "Imagen",
        "Confidencia",
        "Agilidad"
    ],
    "Nidoran-f": [
        "Púas Tóxicas",
        "Arañazo",
        "Ladrón",
        "Venganza"
    ],
    "Ekans": [
        "Trapicheo",
        "Acua Cola",
        "Eructo",
        "Atizar"
    ],
    "Nidoqueen": [
        "Avalancha",
        "Reflejo",
        "Trampa Rocas",
        "Cabezazo"
    ],
    "Clefable": [
        "Hiperrayo",
        "Lanzamiento",
        "Frustración",
        "Rayo Meteórico"
    ],
    "Raichu": [
        "Voltiocambio",
        "Detección",
        "Chispazo",
        "Golpe Roca"
    ],
    "Nidoran-m": [
        "Contoneo",
        "Bomba Lodo",
        "Excavar",
        "Don Natural"
    ],
    "Clefairy": [
        "Puño Certero",
        "Sonámbulo",
        "Antojo",
        "Golpe Roca"
    ],
    "Nidorino": [
        "Retribución",
        "Refuerzo",
        "Contraataque",
        "Puya Nociva"
    ],
    "Jigglypuff": [
        "Giro Bola",
        "Danza Lluvia",
        "Velo Sagrado",
        "Tera Explosión"
    ],
    "Vulpix": [
        "Rugido",
        "Paranormal",
        "Pulso Umbrío",
        "Maldición"
    ],
    "Ninetales": [
        "Anulación",
        "Bola Sombra",
        "Otra Vez",
        "Sonámbulo"
    ],
    "Nidorina": [
        "Golpes Furia",
        "Cola Férrea",
        "Rayo",
        "Trueno"
    ],
    "Golbat": [
        "Robo",
        "Gigaimpacto",
        "Niebla",
        "Ladrón"
    ],
    "Wigglytuff": [
        "Puño Hielo",
        "Vasta Fuerza",
        "Día Soleado",
        "Megapuño"
    ],
    "Vileplume": [
        "Energibola",
        "Acoso",
        "Refuerzo",
        "Bomba Germen"
    ],
    "Venonat": [
        "Polvo Ira",
        "Destello",
        "Cañon",
        "Aguante"
    ],
    "Oddish": [
        "Brillo Mágico",
        "Hoja Mágica",
        "Retribución",
        "Luz Lunar"
    ],
    "Zubat": [
        "Aguante",
        "Ala Bis",
        "Respiro",
        "Golpe Aéreo"
    ],
    "Dugtrio": [
        "Bomba Fango",
        "Tierra Viva",
        "Paliza",
        "Golpe Cuerpo"
    ],
    "Venomoth": [
        "Somnífero",
        "Viento Aciago",
        "Rapidez",
        "Frustración"
    ],
    "Diglett": [
        "Sacrificio",
        "Legado",
        "Alboroto",
        "Arañazo"
    ],
    "Parasect": [
        "Golpe Mordaza",
        "Hiperrayo",
        "Ladrón",
        "Cañon"
    ],
    "Gloom": [
        "Frustración",
        "Desarrollo",
        "Luz Lunar",
        "Carga Tóxica"
    ],
    "Meowth": [
        "Hipnosis",
        "Castigo",
        "Vendetta",
        "Más Psique"
    ],
    "Persian": [
        "Bofetón Lodo",
        "Desahogo",
        "Golpe Cabeza",
        "Daño Secreto"
    ],
    "Paras": [
        "Estoicismo",
        "Abatidoras",
        "Chirrido",
        "Golpes Furia"
    ],
    "Mankey": [
        "Rayo",
        "Furia",
        "Don Natural",
        "Golpe Bis"
    ],
    "Psyduck": [
        "Disparo Lodo",
        "Excavar",
        "Furia",
        "Pantalla de Luz"
    ],
    "Golduck": [
        "Más Psique",
        "Bostezo",
        "Danza Lluvia",
        "Hidrobomba"
    ],
    "Primeape": [
        "Demolición",
        "Sumisión",
        "Treparrocas",
        "Rayo"
    ],
    "Growlithe": [
        "Rastreo",
        "Cara Susto",
        "Carantoña",
        "Golpe Cuerpo"
    ],
    "Poliwhirl": [
        "Descanso",
        "Confidencia",
        "Cañon",
        "Puño Hielo"
    ],
    "Arcanine": [
        "Ronquido",
        "Doble Equipo",
        "Lanzallamas",
        "Derribo"
    ],
    "Poliwag": [
        "Neblina",
        "Niebla",
        "Tóxico",
        "Hidropulso"
    ],
    "Poliwrath": [
        "Onda Vacío",
        "Golpe Cuerpo",
        "Hidroariete",
        "Bofetón Lodo"
    ],
    "Alakazam": [
        "Frustración",
        "Onda Certera",
        "Hiperrayo",
        "Confusión"
    ],
    "Kadabra": [
        "Psicorrayo",
        "Cambiadefensa",
        "Tóxico",
        "Reciclaje"
    ],
    "Abra": [
        "Brillo Mágico",
        "Seducción",
        "Metrónomo",
        "Intercambio"
    ],
    "Bellsprout": [
        "Tera Explosión",
        "Niebla Clara",
        "Gigadrenado",
        "Hierba Lazo"
    ],
    "Tentacruel": [
        "Ronquido",
        "Danza Lluvia",
        "Ácido",
        "Vendetta"
    ],
    "Machop": [
        "Puño Hielo",
        "Profecía",
        "Tumba Rocas",
        "Imitación"
    ],
    "Weepinbell": [
        "Desarme",
        "Constricción",
        "Hierba Lazo",
        "Rapidez"
    ],
    "Victreebel": [
        "Abrir Senda",
        "Paralizador",
        "Constricción",
        "Maldición"
    ],
    "Machoke": [
        "Vendetta",
        "Sustituto",
        "Fuerza",
        "Refuerzo"
    ],
    "Tentacool": [
        "Hidroariete",
        "Ácido",
        "Seducción",
        "Manto Espejo"
    ],
    "Golem": [
        "Puño Incremento",
        "Golpe Cuerpo",
        "Contoneo",
        "Metrónomo"
    ],
    "Machamp": [
        "Descanso",
        "Puntapié",
        "Terremoto",
        "Puño Trueno"
    ],
    "Geodude": [
        "Calcinación",
        "Maldición",
        "Antiaéreo",
        "Retribución"
    ],
    "Graveler": [
        "Doble Filo",
        "Poder Oculto",
        "Poder Pasado",
        "Puño Certero"
    ],
    "Ponyta": [
        "Furia",
        "Nitrocarga",
        "Látigo",
        "Ronquido"
    ],
    "Slowbro": [
        "Frustración",
        "Llamarada",
        "Surf",
        "Protección"
    ],
    "Slowpoke": [
        "Psíquico",
        "Juego Sucio",
        "Danza Lluvia",
        "Tera Explosión"
    ],
    "Rapidash": [
        "Mimético",
        "Cuerno Certero",
        "Agilidad",
        "Cuchilla Solar"
    ],
    "Farfetchd": [
        "Confidencia",
        "Falso Tortazo",
        "Detección",
        "Cuchilla Solar"
    ],
    "Magnemite": [
        "Rayo",
        "Reflejo",
        "Electrotela",
        "Ronquido"
    ],
    "Magneton": [
        "Confidencia",
        "Sustituto",
        "Reflejo",
        "Electrocañón"
    ],
    "Seel": [
        "Acua Aro",
        "chilling-water",
        "ice-spinner",
        "Contoneo"
    ],
    "Dodrio": [
        "Danza Espada",
        "Doble Filo",
        "Golpe Aéreo",
        "pounce"
    ],
    "Dewgong": [
        "Aguante",
        "Triple Axel",
        "Alboroto",
        "Viento Hielo"
    ],
    "Doduo": [
        "Seducción",
        "Sustituto",
        "Supersónico",
        "Golpe Aéreo"
    ],
    "Cloyster": [
        "Allanador Férreo",
        "Cuerno Certero",
        "chilling-water",
        "Chuzos"
    ],
    "Grimer": [
        "Gigadrenado",
        "Excavar",
        "Contoneo",
        "Escupir"
    ],
    "Muk": [
        "Cañon",
        "Gigaimpacto",
        "Descanso",
        "Danza Lluvia"
    ],
    "Shellder": [
        "Confidencia",
        "Sonámbulo",
        "Tera Explosión",
        "Tenaza"
    ],
    "Haunter": [
        "Viento Hielo",
        "Danza Lluvia",
        "Golpe Bajo",
        "Poder Oculto"
    ],
    "Gastly": [
        "Autodestrucción",
        "Descanso",
        "Robo",
        "Zona Extraña"
    ],
    "Gengar": [
        "Puño Certero",
        "Tinieblas",
        "Cabezazo",
        "Venganza"
    ],
    "Hypno": [
        "Patada Baja",
        "Imitación",
        "Triataque",
        "Puño Dinámico"
    ],
    "Onix": [
        "Lanzarrocas",
        "Dragoaliento",
        "Roca Afilada",
        "Tumba Rocas"
    ],
    "Drowzee": [
        "Golpe Cabeza",
        "Psicoonda",
        "Intercambio",
        "Puntapié"
    ],
    "Krabby": [
        "Malicioso",
        "Tumba Rocas",
        "Danza Lluvia",
        "Atizar"
    ],
    "Voltorb": [
        "Sonámbulo",
        "Cañon",
        "Onda Trueno",
        "Aguante"
    ],
    "Kingler": [
        "Escaldar",
        "Hidroariete",
        "Corte",
        "Atracción"
    ],
    "Exeggcute": [
        "Adaptación",
        "Bomba Lodo",
        "Psicocarga",
        "Lluevehojas"
    ],
    "Cubone": [
        "Cola Férrea",
        "Canto Mortal",
        "Rayo Burbuja",
        "Ronquido"
    ],
    "Exeggutor": [
        "Espacio Raro",
        "Mazazo",
        "Protección",
        "Reflejo"
    ],
    "Hitmonchan": [
        "A Bocajarro",
        "Patada Baja",
        "Pat. Salto Alta",
        "Furia"
    ],
    "Electrode": [
        "Daño Secreto",
        "Eco Metálico",
        "Furia",
        "Derribo"
    ],
    "Koffing": [
        "Mismo Destino",
        "Psicorrayo",
        "Polución",
        "Bomba Lodo"
    ],
    "Hitmonlee": [
        "Vastaguardia",
        "Cabezazo",
        "A Bocajarro",
        "Tera Explosión"
    ],
    "Marowak": [
        "Aguante",
        "Aguzar",
        "Gigaimpacto",
        "Foco Energía"
    ],
    "Lickitung": [
        "Lanzamiento",
        "Ladrón",
        "Bofetón Lodo",
        "Don Natural"
    ],
    "Weezing": [
        "Electrocañón",
        "Doble Equipo",
        "Retribución",
        "Sonámbulo"
    ],
    "Rhydon": [
        "Viento Hielo",
        "Rayo Hielo",
        "Demolición",
        "Surf"
    ],
    "Rhyhorn": [
        "Fuerza Equina",
        "Ataque Arena",
        "Día Soleado",
        "Lanzallamas"
    ],
    "Tangela": [
        "Azote",
        "Bomba Lodo",
        "Lluevehojas",
        "Día Soleado"
    ],
    "Chansey": [
        "Contoneo",
        "Ventisca",
        "Viento Hielo",
        "Intercambio"
    ],
    "Kangaskhan": [
        "Puño Dinámico",
        "Paliza",
        "Protección",
        "Rayo Hielo"
    ],
    "Horsea": [
        "Bote",
        "Cascada",
        "Niebla Clara",
        "Furia Dragón"
    ],
    "Seaking": [
        "Imagen",
        "Derribo",
        "Azote",
        "Golpe Cabeza"
    ],
    "Goldeen": [
        "Ventisca",
        "Sonámbulo",
        "Confidencia",
        "Hidropulso"
    ],
    "Seadra": [
        "Doble Filo",
        "Pantalla de Humo",
        "Salpicadura",
        "Poder Oculto"
    ],
    "Ditto": [
        "Transformación"
    ],
    "Mr-mime": [
        "Electrocañón",
        "Campo de Niebla",
        "Bofetón Lodo",
        "Intercambio"
    ],
    "Staryu": [
        "Barrera",
        "Cascada",
        "Más Psique",
        "Confidencia"
    ],
    "Pinsir": [
        "Refuerzo",
        "Corte",
        "Tijera X",
        "Corpulencia"
    ],
    "Starmie": [
        "Onda Trueno",
        "Reducción",
        "Ronquido",
        "Giro Bola"
    ],
    "Scyther": [
        "Agilidad",
        "Ala de Acero",
        "Frustración",
        "Tijera X"
    ],
    "Tauros": [
        "Surf",
        "Poder Oculto",
        "Llamarada",
        "Tumba Rocas"
    ],
    "Magmar": [
        "Venganza",
        "Ronquido",
        "Sumisión",
        "Cambiafuerza"
    ],
    "Magikarp": [
        "Salpicadura",
        "Bote",
        "Placaje",
        "Azote"
    ],
    "Electabuzz": [
        "Rapidez",
        "Puño Trueno",
        "Antojo",
        "Campo Eléctrico"
    ],
    "Jynx": [
        "Pantalla de Luz",
        "Psicocorte",
        "Eco Voz",
        "Atracción"
    ],
    "Lapras": [
        "Fuerza",
        "Gruñido",
        "Dragoaliento",
        "Aguante"
    ],
    "Jolteon": [
        "Cañon",
        "Abrir Senda",
        "Copión",
        "Colmillo Rayo"
    ],
    "Eevee": [
        "Imagen",
        "Gruñido",
        "Ataque Arena",
        "Vozarrón"
    ],
    "Gyarados": [
        "Tormenta Arena",
        "Cola Férrea",
        "Alboroto",
        "Golpe Cabeza"
    ],
    "Flareon": [
        "Golpe Cuerpo",
        "Avivar",
        "Derribo",
        "Última Baza"
    ],
    "Omanyte": [
        "Ladrón",
        "Cascada",
        "Cornada",
        "Atizar"
    ],
    "Vaporeon": [
        "Copión",
        "Doble Patada",
        "Doble Rayo",
        "Danza Lluvia"
    ],
    "Porygon": [
        "Teletransporte",
        "Cabezazo",
        "Electrocañón",
        "Descanso"
    ],
    "Omastar": [
        "Aguante",
        "Granizo",
        "Retribución",
        "Seducción"
    ],
    "Kabutops": [
        "Acua Cola",
        "Golpe Aéreo",
        "Sísmico",
        "Retribución"
    ],
    "Zapdos": [
        "Doble Rayo",
        "Ataque Aéreo",
        "Picotazo",
        "Sustituto"
    ],
    "Aerodactyl": [
        "Maldición",
        "Mordisco",
        "Aguzar",
        "Lanzallamas"
    ],
    "Snorlax": [
        "Daño Secreto",
        "Golpe Cuerpo",
        "Viento Hielo",
        "Puño Incremento"
    ],
    "Dragonair": [
        "Descanso",
        "chilling-water",
        "Llamarada",
        "Pistola Agua"
    ],
    "Dratini": [
        "Protección",
        "Enfado",
        "Ciclón",
        "Cañon"
    ],
    "Moltres": [
        "Tóxico",
        "Ala Bis",
        "Confidencia",
        "Aguzar"
    ],
    "Mew": [
        "Bola Sombra",
        "Colmillo Hielo",
        "Desquite",
        "Día de Pago"
    ],
    "Kabuto": [
        "Giro Rápido",
        "Poder Pasado",
        "Desarme",
        "Disparo Lodo"
    ],
    "Mewtwo": [
        "Tinieblas",
        "Día Soleado",
        "Maldición",
        "Terremoto"
    ],
    "Articuno": [
        "Refuerzo",
        "Doble Rayo",
        "Rugido",
        "Hiperrayo"
    ],
    "Dragonite": [
        "Viento Cortante",
        "Puño Trueno",
        "Sonámbulo",
        "Tajo Aéreo"
    ]
} #Movimientos de cada pokemon

def seleccionar_movimiento(pokemon, i): #funcion para identificar los movimiento de cada pokemon
    try:
        movimientos = movimientos_de_Pokemons[pokemon][i] #le asigana a movimiento la lista completa de los movimientos del pokemon resivido
        if movimientos: #verifica si el pokemon tiene movimientos
            return movimientos #en caso verdadero retorna el movimiento en la posicion indicada por i
        #print(movimientos[i])
        return None #en caso de que no tenga ningun movimiento retorna None
    except:
        return None