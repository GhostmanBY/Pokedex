import customtkinter as ctk
from Menu import Menu

def Jugar():
    root.destroy()
    Menu()

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
root.geometry("600x800")
root.title("Pokewar")
root.configure(fg_color=BG_COLOR)

# Frame principal
main_frame = ctk.CTkFrame(root, fg_color=BG_COLOR)
main_frame.pack(fill="both", expand=True)

# Título del juego
title_label = ctk.CTkLabel(
    main_frame,
    text="POKEWAR",
    font=("Roboto", 60, "bold"),
    text_color=TEXT_COLOR
)
title_label.pack(pady=(100, 50))

# Función para crear botones
def create_button(parent, text, command):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=200,
        height=50,
        corner_radius=25,
        fg_color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font=("Roboto", 20)
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
    font=("Roboto", 12),
    text_color=TEXT_COLOR
)
footer.pack(side="bottom", pady=20)

root.mainloop()