#diccionario que tiene todas las estadisticas de todas las primeras evoluciones desde el numero 1 hasta el 89
#Exepcion de que toda evolucion no tiene estadistica debido a que esas se consiguien a raiz del pokemon original
pokemones = { 
    "Bulbasaur": {
        "pokedex": 1, "hp": 45, "atk": 49, "def": 49, "atkE": 65, "defE": 65, "vel": 45, "precicion": 3, "evacion": 3, "xp": 64,
    },
    "Ivysaur": {
        "pokedex": 2, "precicion": 3, "evacion": 3, "xp": 141,
    },
    "Venusaur": {
        "pokedex": 3, "precicion": 3, "evacion": 3, "xp": 208,
    },
    "Charmander": {
        "pokedex": 4, "hp": 39, "atk": 52, "def": 43, "atkE": 60, "defE": 50, "vel": 65, "precicion": 3, "evacion": 3, "xp": 65,
    },
    "Charmeleon": {
        "pokedex": 5, "precicion": 3, "evacion": 3, "xp": 142,
    },
    "Charizard": {
        "pokedex": 6, "precicion": 3, "evacion": 3, "xp": 209,
    },
    "Squirtle": {
        "pokedex": 7, "hp": 44, "atk": 48, "def": 65, "atkE": 50, "defE": 64, "vel": 43, "precicion": 3, "evacion": 3, "xp": 66,
    },
    "Wartortle": {
        "pokedex": 8, "precicion": 3, "evacion": 3, "xp": 143,
    },
    "Blastoise": {
        "pokedex": 9, "precicion": 3, "evacion": 3, "xp": 210,
    },
    "Caterpie": {
        "pokedex": 10, "hp": 45, "atk": 30, "def": 35, "atkE": 20, "defE": 20, "vel": 45, "precicion": 3, "evacion": 3, "xp": 53,
    },
    "Metapod": {
        "pokedex": 11, "precicion": 3, "evacion": 3, "xp": 72,
    },
    "Butterfree": {
        "pokedex": 12, "precicion": 3, "evacion": 3, "xp": 160,
    },
    "Weedle": {
        "pokedex": 13, "hp": 40, "atk": 35, "def": 30, "atkE": 20, "defE": 20, "vel": 50, "precicion": 3, "evacion": 3, "xp": 52,
    },
    "Kakuna": {
        "pokedex": 14, "precicion": 3, "evacion": 3, "xp": 71,
    },
    "Beedrill": {
        "pokedex": 15, "precicion": 3, "evacion": 3, "xp": 159,
    },
    "Pidgey": {
        "pokedex": 16, "hp": 40, "atk": 45, "def": 40, "atkE": 35, "defE": 35, "vel": 56, "precicion": 3, "evacion": 3, "xp": 55,
    },
    "Pidgeotto": {
        "pokedex": 17, "precicion": 3, "evacion": 3, "xp": 113,
    },
    "Pidgeot": {
        "pokedex": 18, "precicion": 3, "evacion": 3, "xp": 172,
    },
    "Rattata": {
        "pokedex": 19, "hp": 30, "atk": 56, "def": 35, "atkE": 25, "defE": 35, "vel": 72, "precicion": 3, "evacion": 3, "xp": 57,
    },
    "Raticate": {
        "pokedex": 20, "precicion": 3, "evacion": 3, "xp": 116,
    },
    "Spearow": {
        "pokedex": 21, "hp": 40, "atk": 60, "def": 30, "atkE": 31, "defE": 31, "vel": 70, "precicion": 3, "evacion": 3, "xp": 58,
    },
    "Fearow": {
        "pokedex": 22, "precicion": 3, "evacion": 3, "xp": 162,
    },
    "Ekans": {
        "pokedex": 23, "hp": 35, "atk": 60, "def": 44, "atkE": 40, "defE": 54, "vel": 55, "precicion": 3, "evacion": 3, "xp": 62,
    },
    "Arbok": {
        "pokedex": 24, "precicion": 3, "evacion": 3, "xp": 147,
    },
    "Pikachu": {
        "pokedex": 25, "hp": 35, "atk": 55, "def": 40, "atkE": 50, "defE": 50, "vel": 90, "precicion": 3, "evacion": 3, "xp": 82,
    },
    "Raichu": {
        "pokedex": 26, "precicion": 3, "evacion": 3, "xp": 122,
    },
    "Sandshrew": {
        "pokedex": 27, "hp": 50, "atk": 75, "def": 85, "atkE": 20, "defE": 30, "vel": 40, "precicion": 3, "evacion": 3,
    },
    "Sandslash": {
        "pokedex": 28, "precicion": 3, "evacion": 3,
    },
    "Nidoran♀": {
        "pokedex": 29, "hp": 55, "atk": 47, "def": 52, "atkE": 40, "defE": 40, "vel": 41, "precicion": 3, "evacion": 3,
    },
    "Nidorina": {
        "pokedex": 30, "precicion": 3, "evacion": 3,
    },
    "Nidoqueen": {
        "pokedex": 31, "precicion": 3, "evacion": 3,
    },
    "Nidoran♂": {
        "pokedex": 32, "hp": 46, "atk": 57, "def": 40, "atkE": 40, "defE": 40, "vel": 50, "precicion": 3, "evacion": 3,
    },
    "Nidorino": {
        "pokedex": 33, "precicion": 3, "evacion": 3,
    },
    "Nidoking": {
        "pokedex": 34, "precicion": 3, "evacion": 3,
    },
    "Clefairy": {
        "pokedex": 35, "hp": 70, "atk": 45, "def": 48, "atkE": 60, "defE": 65, "vel": 35, "precicion": 3, "evacion": 3,
    },
    "Clefable": {
        "pokedex": 36, "precicion": 3, "evacion": 3,
    },
    "Vulpix": {
        "pokedex": 37, "hp": 38, "atk": 41, "def": 40, "atkE": 50, "defE": 65, "vel": 65, "precicion": 3, "evacion": 3,
    },
    "Ninetales": {
        "pokedex": 38, "precicion": 3, "evacion": 3,
    },
    "Jigglypuff": {
        "pokedex": 39, "hp": 115, "atk": 45, "def": 20, "atkE": 45, "defE": 25, "vel": 20, "precicion": 3, "evacion": 3,
    },
    "Wigglytuff": {
        "pokedex": 40, "precicion": 3, "evacion": 3,
    },
    "Zubat": {
        "pokedex": 41, "hp": 40, "atk": 45, "def": 35, "atkE": 30, "defE": 40, "vel": 55, "precicion": 3, "evacion": 3,
    },
    "Golbat": {
        "pokedex": 42, "precicion": 3, "evacion": 3,
    },
    "Oddish": {
        "pokedex": 43, "hp": 45, "atk": 50, "def": 55, "atkE": 75, "defE": 65, "vel": 30, "precicion": 3, "evacion": 3,
    },
    "Gloom": {
        "pokedex": 44, "precicion": 3, "evacion": 3,
    },
    "Vileplume": {
        "pokedex": 45, "precicion": 3, "evacion": 3,
    },
    "Paras": {
        "pokedex": 46, "hp": 35, "atk": 70, "def": 55, "atkE": 45, "defE": 55, "vel": 25, "precicion": 3, "evacion": 3,
    },
    "Parasect": {
        "pokedex": 47, "precicion": 3, "evacion": 3,
    },
    "Venonat": {
        "pokedex": 48, "hp": 60, "atk": 55, "def": 50, "atkE": 40, "defE": 55, "vel": 45, "precicion": 3, "evacion": 3,
    },
    "Venomoth": {
        "pokedex": 49, "precicion": 3, "evacion": 3,
    },
    "Diglett": {
        "pokedex": 50, "hp": 10, "atk": 55, "def": 25, "atkE": 35, "defE": 45, "vel": 95, "precicion": 3, "evacion": 3,
    },
    "Dugtrio": {
        "pokedex": 51, "precicion": 3, "evacion": 3,
    },
    "Meowth": {
        "pokedex": 52, "hp": 40, "atk": 45, "def": 35, "atkE": 40, "defE": 40, "vel": 90, "precicion": 3, "evacion": 3,
    },
    "Persian": {
        "pokedex": 53, "precicion": 3, "evacion": 3,
    },
    "Psyduck": {
        "pokedex": 54, "hp": 50, "atk": 52, "def": 48, "atkE": 65, "defE": 50, "vel": 55, "precicion": 3, "evacion": 3,
    },
    "Golduck": {
        "pokedex": 55, "precicion": 3, "evacion": 3,
    },
    "Mankey": {
        "pokedex": 56, "hp": 40, "atk": 80, "def": 35, "atkE": 35, "defE": 45, "vel": 70, "precicion": 3, "evacion": 3,
    },
    "Primeape": {
        "pokedex": 57, "precicion": 3, "evacion": 3,
    },
    "Growlithe": {
        "pokedex": 58, "hp": 55, "atk": 70, "def": 45, "atkE": 70, "defE": 50, "vel": 60, "precicion": 3, "evacion": 3,
    },
    "Arcanine": {
        "pokedex": 59, "precicion": 3, "evacion": 3,
    },
    "Poliwag": {
        "pokedex": 60, "hp": 40, "atk": 50, "def": 40, "atkE": 40, "defE": 40, "vel": 90, "precicion": 3, "evacion": 3,
    },
    "Poliwhirl": {
        "pokedex": 61, "precicion": 3, "evacion": 3,
    },
    "Poliwrath": {
        "pokedex": 62, "precicion": 3, "evacion": 3,
    },
    "Abra": {
        "pokedex": 63, "hp": 25, "atk": 20, "def": 15, "atkE": 105, "defE": 55, "vel": 90, "precicion": 3, "evacion": 3,
    },
    "Kadabra": {
        "pokedex": 64, "precicion": 3, "evacion": 3,
    },
    "Alakazam": {
        "pokedex": 65, "precicion": 3, "evacion": 3,
    },
    "Machop": {
        "pokedex": 66, "hp": 70, "atk": 80, "def": 50, "atkE": 35, "defE": 35, "vel": 35, "precicion": 3, "evacion": 3,
    },
    "Machoke": {
        "pokedex": 67, "precicion": 3, "evacion": 3,
    },
    "Machamp": {
        "pokedex": 68, "precicion": 3, "evacion": 3,
    },
    "Bellsprout": {
        "pokedex": 69, "hp": 50, "atk": 75, "def": 35, "atkE": 70, "defE": 30, "vel": 40, "precicion": 3, "evacion": 3,
    },
    "Weepinbell": {
        "pokedex": 70, "precicion": 3, "evacion": 3,
    },
    "Victreebel": {
        "pokedex": 71, "precicion": 3, "evacion": 3,
    },
    "Tentacool": {
        "pokedex": 72, "hp": 40, "atk": 40, "def": 35, "atkE": 50, "defE": 100, "vel": 70, "precicion": 3, "evacion": 3,
    },
    "Tentacruel": {
        "pokedex": 73, "precicion": 3, "evacion": 3,
    },
    "Geodude": {
        "pokedex": 74, "hp": 40, "atk": 80, "def": 100, "atkE": 30, "defE": 30, "vel": 20, "precicion": 3, "evacion": 3,
    },
    "Graveler": {
        "pokedex": 75, "precicion": 3, "evacion": 3,
    },
    "Golem": {
        "pokedex": 76, "precicion": 3, "evacion": 3,
    },
    "Ponyta": {
        "pokedex": 77, "hp": 50, "atk": 85, "def": 55, "atkE": 65, "defE": 65, "vel": 90, "precicion": 3, "evacion": 3,
    },
    "Rapidash": {
        "pokedex": 78, "precicion": 3, "evacion": 3,
    },
    "Slowpoke": {
        "pokedex": 79, "hp": 90, "atk": 65, "def": 65, "atkE": 40, "defE": 40, "vel": 15, "precicion": 3, "evacion": 3,
    },
    "Slowbro": {
        "pokedex": 80, "precicion": 3, "evacion": 3,
    },
    "Magnemite": {
        "pokedex": 81, "hp":25, "atk":35, "def": 70, "atkE": 95, "defE": 55, "vel": 45, "precicion": 3, "evacion": 3,
    },
    "Magneton": {
        "pokedex": 82,"precicion": 3, "evacion": 3,
    },
    "Farfetch'd": {
        "pokedex": 83, "hp":52, "atk":90, "def": 55, "atkE": 58, "defE": 62, "vel": 60, "precicion": 3, "evacion": 3,
    },
    "doduo": {
        "pokedex": 84, "hp":35, "atk":85, "def": 45, "atkE": 35, "defE": 35, "vel": 75, "precicion": 3, "evacion": 3,
    },
    "Dodrio": {
        "pokedex": 85, "precicion": 3, "evacion": 3,
    },
    "Seel": {
        "pokedex": 86, "hp": 65, "atk": 45, "def": 55, "atkE": 45, "defE": 70, "vel": 45, "precicion": 3, "evacion": 3,
    },
    "Deowgon": {
        "pokedex": 87, "precicion": 3, "evacion": 3,
    },
    "Grimer": {
        "pokedex": 88, "hp": 80, "atk": 80, "def": 50, "atkE": 40, "defE": 50, "vel": 25, "precicion": 3, "evacion": 3,
    },
    "Muk": {
        "pokedex": 89, "precicion": 3, "evacion": 3,
    },
}
