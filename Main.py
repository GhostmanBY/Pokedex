import json
import customtkinter as ctk
from PIL import Image
from Menu import Menu, obtener_imagen_pokemon
from Estadisticas import pokemones

def guardar_info(pokemon_nombre):
    if pokemon_nombre in pokemones:
        stats = pokemones[pokemon_nombre]
        info_pokemon = {
            'nombre': pokemon_nombre,
            'hp': stats['hp'],
            'ataque': stats['atk'],
            'defensa': stats['def'],
            'ataque_esp': stats['atkE'],
            'defensa_esp': stats['defE'],
            'velocidad': stats['vel'],
            'xp': 0
        }
        print(f"Información guardada para {pokemon_nombre}")
        with open("info_run.json","w",) as archivo:
            json.dump(info_pokemon,archivo,indent=4)
        Menu()  # Llamar a la función Menu después de guardar la información

def Jugar():
    root.withdraw()  # Ocultar la ventana principal en lugar de destruirla
    seleccion_ventana = ctk.CTkToplevel()
    seleccion_ventana.geometry("800x600")
    seleccion_ventana.title("Selección de Pokémon")

    titulo = ctk.CTkLabel(seleccion_ventana, text="Selecciona tu primer pokémon", font=("Roboto", 28, "bold"), text_color=TEXT_COLOR)
    titulo.pack(pady=(30, 20))

    frame_pokemones = ctk.CTkFrame(seleccion_ventana, fg_color="transparent")
    frame_pokemones.pack(expand=True)

    def crear_boton_pokemon(pokemon_nombre):
        frame = ctk.CTkFrame(frame_pokemones, fg_color="transparent")
        frame.pack(side="left", padx=20)

        foto_poke = obtener_imagen_pokemon(pokemon_nombre)
        imagen = ctk.CTkLabel(frame, image=foto_poke, text="")
        imagen.pack()

        boton = ctk.CTkButton(
            frame,
            text=f"Elegir {pokemon_nombre}",
            command=lambda: guardar_info(pokemon_nombre),
            width=150,
            height=40,
            corner_radius=20,
            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
            text_color=TEXT_COLOR,
            font=("Roboto", 16)
        )
        boton.pack(pady=10)

    crear_boton_pokemon("Bulbasaur")
    crear_boton_pokemon("Charmander")
    crear_boton_pokemon("Squirtle")

    boton_volver = ctk.CTkButton(
        seleccion_ventana,
        text="Volver al Menú Principal",
        command=lambda: [seleccion_ventana.destroy(), root.deiconify()],
        width=200,
        height=40,
        corner_radius=20,
        fg_color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font=("Roboto", 16)
    )
    boton_volver.pack(pady=20)

# Configuración general
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Colores
BG_COLOR = "#2C3E50"  # Azul oscuro
BUTTON_COLOR = "#3498DB"  # Azul claro
BUTTON_HOVER_COLOR = "#2980B9"  # Azul más oscuro para hover
TEXT_COLOR = "#ECF0F1"  # Blanco grisáceo

# Crear ventana principal
root = ctk.CTk()
root.geometry("800x600")
root.title("Pokewar")
root.configure(fg_color=BG_COLOR)

# Frame principal
main_frame = ctk.CTkFrame(root, fg_color=BG_COLOR)
main_frame.pack(fill="both", expand=True)

# Título del juego
title_label = ctk.CTkLabel(
    main_frame,
    text="POKEWAR",
    font=("Roboto", 72, "bold"),
    text_color=TEXT_COLOR
)
title_label.pack(pady=(80, 50))

# Función para crear botones
def create_button(parent, text, command):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=250,
        height=60,
        corner_radius=30,
        fg_color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font=("Roboto", 24)
    )

# Botones
jugar_button = create_button(main_frame, "Jugar", Jugar)
jugar_button.pack(pady=20)

opciones_button = create_button(main_frame, "Opciones", lambda: print("Opciones"))
opciones_button.pack(pady=20)

salir_button = create_button(main_frame, "Salir", root.quit)
salir_button.pack(pady=20)

# Pie de página
footer = ctk.CTkLabel(
    main_frame,
    text="Desarrollado por: GhostmanBY && Markbusking\n© 2024. Todos los derechos reservados.",
    font=("Roboto", 14),
    text_color=TEXT_COLOR
)
footer.pack(side="bottom", pady=20)

root.mainloop()
