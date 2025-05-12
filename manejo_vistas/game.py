import arcade
import random # todo: lo usaremos para hacer posiciones aleatorias
import os # Pa' verificar el directorio de trabajo

# ----------------11/Mayo/2025 : Creacion del Juego-----------------------
class GameView(arcade.View):
    # todo: Inicializaremos el init 
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)  # Fondo negro
        # Inicializa tus elementos del juego aquí
        self.carro = None  # Placeholder para el jugador
        self.lista_carro = None # todo: Lista para dibujar al jugador o bueno al carro
        self.lista_obstaculos = None # todo: lista para los obstaculos
        self.tiempo_ultimo_obstaculo = 0 # todo: Temporizador en segundos
        self.velocidad_carro = 0

    def setup(self):
        """Configura los elementos iniciales del juego."""
        # Aquí puedes inicializar sprites, listas de sprites, física, etc.
        self.lista_carro = arcade.SpriteList()
        self.lista_obstaculos = arcade.SpriteList()

        # Verifica el directorio de trabajo actual
        current_dir = os.getcwd()
        print(f"Directorio de trabajo actual: {current_dir}")

        # Carro del jugador (usamos recursos/carroverde.png)
        try:
            # Primero intenta con ruta absoluta
            self.carro = arcade.Sprite(
                filename=r"C:\Users\aleja\Desktop\ARCADE PROJECT\recursos\carroverde.png"
                # Quitamos scale pa' probar
            )
            if self.carro.texture:
                print("Carro verde tiene textura cargada correctamente.")
            else:
                print("Carro verde cargado, pero no tiene textura.")
            print("Carro verde cargado correctamente con ruta absoluta.")
        except FileNotFoundError as e:
            print(f"Error con ruta absoluta: No se encontró carroverde.png. Detalle: {e}")
            try:
                self.carro = arcade.Sprite(
                    filename="recursos/carroverde.png"
                )
                if self.carro.texture:
                    print("Carro verde tiene textura cargada correctamente.")
                else:
                    print("Carro verde cargado, pero no tiene textura.")
                print("Carro verde cargado correctamente con ruta relativa.")
            except FileNotFoundError as e:
                print(f"Error con ruta relativa: No se encontró carroverde.png. Detalle: {e}")
                self.carro = arcade.SpriteSolidColor(width=50, height=30, color=arcade.color.GREEN)
            except Exception as e:
                print(f"Error con ruta relativa: {e}")
                self.carro = arcade.SpriteSolidColor(width=50, height=30, color=arcade.color.GREEN)
        except Exception as e:
            print(f"Error al cargar carroverde.png con ruta absoluta: {e}")
            self.carro = arcade.SpriteSolidColor(width=50, height=30, color=arcade.color.GREEN)
        # todo: Posicionamiento del carro
        self.carro.center_x = self.window.width / 2
        self.carro.center_y = 100
        self.lista_carro.append(self.carro)

    def on_show_view(self):
        """Se ejecuta cuando la vista del juego se muestra."""
        self.setup()

    def on_draw(self):
        """Dibuja los elementos del juego en cada frame."""
        self.clear()
        # Fondo negro ya está seteado, no dibujamos nada más
        # Dibuja tus elementos aquí
        self.lista_carro.draw()
        self.lista_obstaculos.draw()

    def on_update(self, delta_time):
        """Actualiza la lógica del juego."""
        # Actualiza movimiento, colisiones, etc.
        # todo: Actualizamos posicion y evitamos que el carro se salga de la pantalla
        self.carro.center_x += self.velocidad_carro * delta_time
        if self.carro.left < 0:
            self.carro.left = 0
        if self.carro.right > self.window.width:
            self.carro.right = self.window.width
        
        # todo: Generacion de obstaculos
        self.tiempo_ultimo_obstaculo += delta_time
        if self.tiempo_ultimo_obstaculo > 2.0:
            self.crear_obstaculo() 
            self.tiempo_ultimo_obstaculo = 0
        
        # todo: Actualizar la posicion de los obstaculos
        for obstaculo in self.lista_obstaculos:
            obstaculo.center_y -= 200 * delta_time # todo: Velocidad de caida 200 pixeles por segundo
            # todo: eliminar obstaculos que salen en la pantalla apa
            if obstaculo.top < 0:
                obstaculo.remove_from_sprite_lists()
        
        # todo: Revisa colisiones entre el carro y los obstaculos
        lista_choques = arcade.check_for_collision_with_list(self.carro, self.lista_obstaculos)
        if lista_choques:
            print("!ALA VRG !, GAME OVER") # todo: que mamada jajajajjaja, hay vemos que pedo

    def crear_obstaculo(self):
        """Crea un nuevo obstáculo en la parte superior de la pantalla."""
        try:
            # Primero intenta con ruta absoluta
            obstaculo = arcade.Sprite(
                filename=r"C:\Users\aleja\Desktop\ARCADE PROJECT\recursos\carroazul.png"
                # Quitamos scale pa' probar
            )
            if obstaculo.texture:
                print("Carro azul tiene textura cargada correctamente.")
            else:
                print("Carro azul cargado, pero no tiene textura.")
            print("Carro azul cargado correctamente con ruta absoluta.")
        except FileNotFoundError as e:
            print(f"Error con ruta absoluta: No se encontró carroazul.png. Detalle: {e}")
            try:
                obstaculo = arcade.Sprite(
                    filename="recursos/carroazul.png"
                )
                if obstaculo.texture:
                    print("Carro azul tiene textura cargada correctamente.")
                else:
                    print("Carro azul cargado, pero no tiene textura.")
                print("Carro azul cargado correctamente con ruta relativa.")
            except FileNotFoundError as e:
                print(f"Error con ruta relativa: No se encontró carroazul.png. Detalle: {e}")
                obstaculo = arcade.SpriteSolidColor(width=30, height=30, color=arcade.color.BLUE)
            except Exception as e:
                print(f"Error con ruta relativa: {e}")
                obstaculo = arcade.SpriteSolidColor(width=30, height=30, color=arcade.color.BLUE)
        except Exception as e:
            print(f"Error al cargar carroazul.png con ruta absoluta: {e}")
            obstaculo = arcade.SpriteSolidColor(width=30, height=30, color=arcade.color.BLUE)
        # todo: Posiciona el obstáculo en una posición X aleatoria arriba, pe
        obstaculo.center_x = random.randint(0, self.window.width)
        obstaculo.center_y = self.window.height
        self.lista_obstaculos.append(obstaculo)

    def on_key_press(self, key, modifiers):
        """Maneja las teclas presionadas."""
        # todo: Controla el movimiento del carro, pe
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.velocidad_carro = -300  # todo: Mueve a la izquierda (300 píxeles/segundo)
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.velocidad_carro = 300  # todo: Mueve a la derecha
        if key == arcade.key.ESCAPE:
            arcade.exit()  # todo: Cierra la ventana al presionar ESC, pe

    def on_key_release(self, key, modifiers):
        """Maneja las teclas liberadas."""
        # todo: Detiene el movimiento cuando se sueltan las teclas, pe
        if key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.velocidad_carro = 0