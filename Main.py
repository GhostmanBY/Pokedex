from Menu import Menu
import customtkinter as ctk

def Jugar():
    root.destroy()
    Menu()

# Establece el modo de apariencia en oscuro
ctk.set_appearance_mode("dark")

# Crea la ventana principal
root = ctk.CTk()
root.geometry("800x600")
root.title("Pokewar")

# Define los colores inspirados en la Pokédex
bg_color = "#F4F4F4"  # Fondo blanco
header_color = "#CC0000"  # Rojo Pokédex para el encabezado
button_color = "#CC0000"  # Rojo Pokédex para el botón
button_hover_color = "#A80000"  # Rojo más oscuro para el botón al pasar el ratón
text_color = "#000000"  # Texto negro para buen contraste

# Aplica el color de fondo
root.configure(bg=bg_color)

# Encabezado (simula el diseño del encabezado de una Pokédex)
titulo_frame = ctk.CTkFrame(root, bg_color=header_color, height=100)
titulo_frame.pack(fill="x")

titulo = ctk.CTkLabel(titulo_frame, text="Pokewar", font=("Arial", 50), text_color="white", bg_color=header_color)
titulo.pack(pady=20)

# Botón de jugar
jugar = ctk.CTkButton(root, text="Jugar", font=("Arial", 20), command=Jugar, fg_color=button_color, hover_color=button_hover_color)
jugar.pack(pady=20)

# Pie de página
footer = ctk.CTkLabel(root, text="desarrollado por: \n GhostmanBY && Markbusking \n © 2024. Todos los derechos reservados.", font=("Arial", 15), text_color=text_color, bg_color=bg_color)
footer.pack(side="bottom", pady=20)

root.mainloop()
