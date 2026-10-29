"""
Munchkin Helper - Главное окно приложения (фронтенд)
Точка входа: инициализация App и ScreenManager
"""
import os
import sys

BACKEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'height', 720)

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screens import (
    LoginScreen, MainScreen, GameScreen, CatalogScreen,
    BestiaryScreen, MonsterDetailScreen,
    RacesClassesScreen, RaceClassDetailScreen, RegisterScreen
)
from controllers import (
    AuthController, MainController, GameController, CatalogController,
    BestiaryController, MonsterDetailController,
    RacesClassesController, RaceClassDetailController, RegisterController
)
KV_FILE = os.path.join(os.path.dirname(__file__), 'main.kv')
Builder.load_file(KV_FILE)


class MunchkinApp(App):
    def build(self):
        Window.title = "Munchkin Helper"
        
        sm = ScreenManager()
        
        # Экран авторизации
        login_screen = LoginScreen(name='login')
        auth_controller = AuthController(login_screen)
        login_screen.controller = auth_controller
        sm.add_widget(login_screen)

        # Экран регистрации
        register_screen = RegisterScreen(name='register')
        register_controller = RegisterController(register_screen)
        register_screen.controller = register_controller
        sm.add_widget(register_screen)
        
        # Главный экран
        main_screen = MainScreen(name='main')
        main_controller = MainController(main_screen)
        main_screen.controller = main_controller
        main_screen.controller_session = auth_controller
        sm.add_widget(main_screen)
        
        # Экран новой игры
        game_screen = GameScreen(name='game')
        game_controller = GameController(game_screen)
        game_screen.controller = game_controller
        sm.add_widget(game_screen)

        # Экран справочника
        catalog_screen = CatalogScreen(name='catalog')
        catalog_controller = CatalogController(catalog_screen)
        catalog_screen.controller = catalog_controller
        sm.add_widget(catalog_screen)

        # Экран бестиария
        bestiary_screen = BestiaryScreen(name='bestiary')
        bestiary_controller = BestiaryController(bestiary_screen)
        bestiary_screen.controller = bestiary_controller
        sm.add_widget(bestiary_screen)
        
        # Экран детального описания монстра
        monster_detail_screen = MonsterDetailScreen(name='monster_detail')
        monster_detail_controller = MonsterDetailController(monster_detail_screen)
        monster_detail_screen.controller = monster_detail_controller
        sm.add_widget(monster_detail_screen)
        
        # Экран рас и классов
        races_classes_screen = RacesClassesScreen(name='races_classes')
        races_classes_controller = RacesClassesController(races_classes_screen)
        races_classes_screen.controller = races_classes_controller
        sm.add_widget(races_classes_screen)
        
        # Экран детального описания расы/класса
        race_class_detail_screen = RaceClassDetailScreen(name='race_class_detail')
        race_class_detail_controller = RaceClassDetailController(race_class_detail_screen)
        race_class_detail_screen.controller = race_class_detail_controller
        sm.add_widget(race_class_detail_screen)

        sm.current = 'login'
        
        return sm


if __name__ == '__main__':
    MunchkinApp().run()