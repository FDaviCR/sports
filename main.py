from kivy.config import Config
from kivy.core.window import Window

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Config.set('graphics', 'resizable', True)  # Permitir que a janela seja redimensionável
Config.set('graphics', 'borderless', False)  # Garantir que tenha borda para maximizar/minimizar
Config.set('graphics', 'fullscreen', 'fake')  # "fake" mantém a barra de tarefas visível

# Definir as telas no Python
class MenuScreen(Screen):
    pass

class Tela1(Screen):
    pass

class Tela2(Screen):
    pass

class Tela3(Screen):
    pass

# Gerenciar as telas
class GerenciadorDeTelas(ScreenManager):
    pass

# Carregar o arquivo KV
kv = Builder.load_file("menu.kv")

class MyApp(App):
    def build(self):
        Window.maximize()
        return kv

if __name__ == '__main__':
    MyApp().run()
