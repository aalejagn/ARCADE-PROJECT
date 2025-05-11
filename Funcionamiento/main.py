import arcade
from arcade.gui import UIManager, UIFlatButton
from arcade.gui.widgets.layout import UIAnchorLayout



#!----------------11/Mayo/2025 : Creacion del Menu-----------------------
SCREEN_TITLE = "Retro Racing - Menú Principal"

class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)
        self.title = None  # Inicializamos el título

    def setup(self):
        """Configura el menú con el sistema UI de Arcade."""
        self.ui_manager.clear()  # Cambiado de purge_ui_elements() a clear()

        # --- Título ---
        
        self.title = arcade.Text(
            # Texto a mostrar (cadena)
            "RETRO RACING",
            
            # Posición X (centrado horizontalmente)
            self.window.width // 2,  
            
            # Posición Y (65% de la altura de la pantalla)
            self.window.height * 0.65,
            
            # Color del texto (usando constantes predefinidas de arcade)
            # Alternativas: arcade.color.GOLD, arcade.color.NEON_CARROT, arcade.color.ELECTRIC_CRIMSON
            arcade.color.BLACK_LEATHER_JACKET,
            
            # Tamaño de fuente en píxeles (80 es grande para títulos)
            100,
            
            # Alineación horizontal ('center', 'left' o 'right')
            anchor_x="center",
            
            # Negrita (True/False)
            bold=True,
            
            # Nombre de la fuente (puede ser una cadena o tupla con fuentes alternativas)
            # Fuentes recomendadas para estilo retro:
            # - "Kenney Future" (descargable gratis de kenney.nl)
            # - "Press Start 2P" (ideal para 8-bit)
            # - "Agency FB" (estilo años 80)
            font_name=("Agency FB")  # Tupla de fuentes alternativas
        )
        self.title.draw()  # Luego el texto principal
        

        anchor_layout = UIAnchorLayout(
            size_hint=(1, 1)  # Ocupa toda la pantalla
        )  # ¡Paréntesis cerrado aquí!
        self.ui_manager.add(anchor_layout)
        
        # --- Botones centrales ---
        # Lista de tuplas que define los botones principales del menú:
        # Cada tupla contiene (texto_del_botón, función_a_ejecutar_al_presionar)
        button_options = [
            ("UN JUGADOR", self.start_single_player),  # Botón para modo un jugador
            ("MULTIJUGADOR", self.start_multiplayer),  # Botón para modo multijugador
            ("CONFIGURACIONES", self.open_settings)    # Botón para ajustes del juego
        ]
        
        # Bucle que crea y posiciona cada botón central
        for i, (text, action) in enumerate(button_options):
            # Crea un botón plano con:
            button = UIFlatButton(
                text=text,       # Texto que muestra el botón
                width=300,       # Ancho en píxeles
                height=60        # Alto en píxeles
            )
            # Asigna la función que se ejecutará al hacer clic
            button.on_click = action

            # Añade el botón al layout de anclaje con:
            anchor_layout.add(
                child=button,       # El botón a añadir
                anchor_x="center_x", # Anclaje horizontal al centro
                anchor_y="center_y", # Anclaje vertical al centro
                align_y=(-i * 80)   # Posición vertical (-80px por cada botón para espaciado)
            )
            
        # --- Botón Skines ---
        # Crea un botón especial para skins/customización:
        skin_button = UIFlatButton(
            text="SKINS",   # Texto del botón
            width=140,      # Ancho más pequeño que los botones centrales
            height=50       # Alto más pequeño que los botones centrales
        )
        # Asigna la función para abrir menú de skins
        skin_button.on_click = self.open_skins

        # Posiciona el botón de skins en:
        anchor_layout.add(
            child=skin_button,  # El botón a posicionar
            anchor_x="right",   # Anclaje al lado derecho
            anchor_y="bottom",  # Anclaje a la parte inferior
            align_x=-20,       # Margen derecho de 20px
            align_y=20         # Margen inferior de 20px
        )

        # --- Botón Créditos ---
        # Crea un botón para mostrar los créditos del juego:
        credits_button = UIFlatButton(
            text="CRÉDITOS",  # Texto del botón
            width=140,        # Mismo tamaño que botón de skins
            height=50
        )
        # Asigna la función para mostrar créditos
        credits_button.on_click = self.open_credits

        # Posiciona el botón de créditos en:
        anchor_layout.add(
            child=credits_button,  # El botón a posicionar
            anchor_x="left",       # Anclaje al lado izquierdo
            anchor_y="bottom",     # Anclaje a la parte inferior
            align_x=20,           # Margen izquierdo de 20px
            align_y=20            # Margen inferior de 20px (igual que skins)
        )

    def on_show_view(self):
            """Método que se ejecuta automáticamente cuando esta vista (menú) se muestra.
            Realiza dos acciones esenciales:
            1. self.setup() - Prepara/recarga todos los elementos del menú
            2. self.ui_manager.enable() - Activa el sistema de interfaz de usuario para que responda a eventos"""
            self.setup()
            self.ui_manager.enable()

    def on_hide_view(self):
            """Método que se ejecuta automáticamente cuando esta vista (menú) se oculta.
            Realiza una acción crítica:
            1. self.ui_manager.disable() - Desactiva el sistema de interfaz para liberar recursos
            y evitar que siga procesando eventos cuando no es visible"""
            self.ui_manager.disable()

    def on_draw(self):
            """Método que se ejecuta en cada frame para dibujar todos los elementos gráficos.
            Sigue un orden de renderizado específico:
            1. self.clear() - Limpia la pantalla con el color de fondo establecido
            2. if self.title: - Verificación de seguridad para asegurar que el título existe
            self.title.draw() - Dibuja el texto del título principal
            3. self.ui_manager.draw() - Dibuja todos los elementos de la interfaz (botones, etc.)
            
            Nota: El orden es importante para que los elementos se superpongan correctamente"""
            self.clear()
            if self.title:  # Verificamos que el título exista
                self.title.draw()
            self.ui_manager.draw()

    # Funciones de botones (mantenemos el event aunque no se use)
    def start_single_player(self, event=None):
        print("Iniciando un jugador...")

    def start_multiplayer(self, event=None):
        print("Iniciando multijugador...")

    def open_settings(self, event=None):
        print("Abriendo configuraciones...")

    def open_skins(self, event=None):
        print("Abriendo skines...")

    def open_credits(self, event=None):
        print("Mostrando créditos...")

def main():
    window = arcade.Window(
        fullscreen=True,
        title=SCREEN_TITLE,
        resizable=False)  # Evita redimensionamiento
    menu_view = MainMenu()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()