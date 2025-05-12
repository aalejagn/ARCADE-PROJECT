import arcade
from manejo_vistas.menu import MainMenu

# ----------------11/Mayo/2025 : Inicialización del Juego-----------------------
SCREEN_TITLE = "Retro Racing - Menú Principal"

def main():
    window = arcade.Window(
        # TODO: Modificare el tamaño para que no se expanda a pantalla completa
        width=1280,
        height = 720,
        title=SCREEN_TITLE,
        resizable=False)  # Evita redimensionamiento
    menu_view = MainMenu()
    window.show_view(menu_view)
    arcade.run()
if __name__ == "__main__":
    main()