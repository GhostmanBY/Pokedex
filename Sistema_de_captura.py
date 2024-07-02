Listado_pokemons_cap_gen1 = {
    "Caterpie":255, "Weedle":255, "Pidgey":255, "Rattata":255, "Spearow":255, 
    "Ekans":255, "Sandshrew":255, "Zubat":255, "Oddish":255, "Diglett":255, "Meowth":255, 
    "Poliwag":255, "Bellsprout":255, "Geodude":255, "Krabby":255, "Horsea":255, "Goldeen":255, 
    "Staryu":255, "Magikarp":255, "Nidoran♀":235, "Nidoran♂":235, "Abra":200, "Pikachu":190, 
    "Vulpix":190, "Paras":190, "Venonat":190,"Psyduck":190, "Mankey":190, "Growlithe":190, 
    "Tentacool":190, "Ponyta":190, "Slowpoke":190, "Magnemite":190, "Doduo":190, "Seel":190, 
    "Grimer":190, "Shellder":190,"Gastly":190, "Drowzee":190, "Voltorb":190, "Cubone":190, 
    "Koffing":190, "Machop":180, "Jigglypuff":170, "Clefairy":150, "Raticate":127, "Metapod":120, 
    "Kakuna":120, "Pidgeotto":120, "Nidorina":120,"Nidorino":120, "Gloom":120, "Poliwhirl":120, 
    "Weepinbell":120, "Graveler":120, "Rhyhorn":120, "Kadabra":100, "Fearow":90, "Arbok":90, 
    "Sandslash":90, "Golbat":90, "Persian":90, "Machoke":90, "Haunter":90, "Exeggcute":90, 
    "Raichu":75, "Ninetales":75, "Parasect":75, "Venomoth":75, "Golduck":75, "Primeape":75, 
    "Arcanine":75, "Slowbro":75, "Dewgong":75, "Muk":75, "Hypno":75, "Marowak":75, 
    "Seadra":75, "Tentacruel":60, "Rapidash":60, "Magneton":60, "Cloyster":60, "Kingler":60, 
    "Electrode":60, "Weezing":60, "Rhydon":60, "Seaking":60, "Starmie":60, "Wigglytuff":50, 
    "Dugtrio":50, "Alakazam":50, "Bulbasaur":45, "Ivysaur":45, "Venusaur":45, "Charmander":45, 
    "Charmeleon":45, "Charizard":45, "Squirtle":45, "Wartortle":45, "Blastoise":45, "Butterfree":45, 
    "Beedrill":45, "Pidgeot":45, "Nidoqueen":45, "Nidoking":45, "Vileplume":45, "Poliwrath":45, 
    "Victreebel":45, "Golem":45, "Farfetch'd":45, "Dodrio":45,"Gengar":45, "Onix":45, 
    "Exeggutor":45,"Hitmonlee":45, "Hitmonchan":45, "Lickitung":45, "Tangela":45, "Kangaskhan":45, 
    "Mr. Mime":45,"Scyther":45, "Jynx":45, "Electabuzz":45, "Magmar":45, "Pinsir":45, 
    "Tauros":45, "Gyarados":45, "Lapras":45, "Eevee":45, "Vaporeon":45,"Jolteon":45, 
    "Flareon":45, "Porygon":45, "Omanyte":45, "Omastar":45, "Kabuto":45, "Kabutops":45, 
    "Aerodactyl":45,"Dratini":45, "Dragonair":45, "Dragonite":45, "Mew":45,"Ditto":35, 
    "Chansey":30,"Snorlax":25, "Clefable":25, "Articuno":3, "Zapdos":3, "Moltres":3, 
    "Mewtwo":3,
    "Lumineon": 75
    } #diccionario en orden decendente del ratio de captura de cada pokemon de la primera generacion

def parametros(PokeBall, Bonos, PsM, PsA, Rc): #funcion para calcular el ratio de captura
    #if de cuanto multiplicador tiene cada pokeball
    if PokeBall.capitalize() == "Pokeball":
        Rb = 1
    elif PokeBall.capitalize() == "Superball":
        Rb = 1.5
    elif PokeBall.capitalize() == "Ultraball":
        Rb = 2
    elif PokeBall.capitalize() == "Mallaball":
        Rb = 3

    #if de cuanto multiplicador tiene cada estado
    if Bonos.capitalize() == "Dormido":
        Be = 2
    elif Bonos.capitalize() == "Congelado":
        Be = 1.5
    elif Bonos.capitalize() == "Paralizado":
        Be = 1.5
    elif Bonos.capitalize() == "Quemado":
        Be = 1.5
    elif Bonos.capitalize() == "Envenenado":
        Be = 1.5
    elif Bonos.capitalize() == "Ninguno":
        Be = 1
    
    #cuenta de ratio de captura
    a = (((3 * PsM - 2 * PsA) * Rc * Rb)/(3 * PsM))*Be
    b = 1 #valor de b para el caso verdadero
    if a >= 255: #evalua si a es mayor a 255
        return b #si es verdadero entonces retorna b con valor igual 1
    elif a < 255: #caso falso
        b = a/2.55 #a al ser menor a 255 se divide por 2.55 lo que da un porsentaje del resultado de a
        return b #lo que es retornado con el valor de b