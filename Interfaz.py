from Sistema_de_captura import Listado_pokemons_cap_gen1
from Sistema_de_captura import parametros
from customtkinter import *

set_appearance_mode("dark")

Fuente_T = ("Arial", 20, "bold")
Fuente_P = ("Arial", 25, "bold")

ventana_main = CTk()
ventana_main.geometry("250x250")
ventana_main.title("Parametros")

def submit():
    global Rc, b
    Rc = Listado_pokemons_cap_gen1[entry_pokemon.get()]
    b = parametros(entry_pokeball.get(), entry_Estado.get(), int(entry_PsM.get()), int(entry_PsA.get()), Rc)
    if b != 1:
        Ventana_extra = CTkToplevel()
        Ventana_extra.title("Cap")

        mensaje = CTkLabel(master=Ventana_extra, text=f"El porsentaje de captuara es\n {float(b):.2f}%", text_color="white")
        mensaje.place(relx=0.5, rely=0.5, anchor="center")
    else:
        Ventana_extra = CTkToplevel()
        Ventana_extra.title("Cap")

        mensaje = CTkLabel(master=Ventana_extra, text=f"El Pokemona se va a atrapar", text_color="white")
        mensaje.place(relx=0.5, rely=0.5, anchor="center")
    
global text_pokemon, entry_pokemon
text_pokemon = CTkLabel(master=ventana_main, text="Pokémon", text_color="white", font=Fuente_T)
text_pokemon.place(relx=0.2, rely=0.1, anchor="center")

entry_pokemon = CTkEntry(master=ventana_main, placeholder_text="Caterpie")
entry_pokemon.place(relx=0.7, rely=0.1, anchor="center")

global text_pokeball, entry_pokeball
text_pokeball = CTkLabel(master=ventana_main, text="PokeBall", text_color="white", font=Fuente_T)
text_pokeball.place(relx=0.187, rely=0.25, anchor="center")

entry_pokeball = CTkEntry(master=ventana_main, placeholder_text="Pokeball")
entry_pokeball.place(relx=0.7, rely=0.26, anchor="center")

global text_PsM, entry_PsM
text_PsM = CTkLabel(master=ventana_main, text="PsMax", text_color="white", font=Fuente_T)
text_PsM.place(relx=0.145, rely=0.41, anchor="center")

entry_PsM = CTkEntry(master=ventana_main, placeholder_text="12")
entry_PsM.place(relx=0.7, rely=0.42, anchor="center")

global text_PsA, entry_PsA
text_PsA = CTkLabel(master=ventana_main, text="PsAct", text_color="white", font=Fuente_T)
text_PsA.place(relx=0.130, rely=0.58, anchor="center")

entry_PsA = CTkEntry(master=ventana_main, placeholder_text="1")
entry_PsA.place(relx=0.7, rely=0.58, anchor="center")

global text_Estado, entry_Estado
text_Estado = CTkLabel(master=ventana_main, text="Estado", text_color="white", font=Fuente_T)
text_Estado.place(relx=0.150, rely=0.75, anchor="center")

entry_Estado = CTkEntry(master=ventana_main, placeholder_text="Dormido")
entry_Estado.place(relx=0.7, rely=0.75, anchor="center")

global button_enviar
button_enviar = CTkButton(master=ventana_main, text="Enviar", command=submit)
button_enviar.place(relx=0.5, rely=0.92, anchor="center")
ventana_main.mainloop()

