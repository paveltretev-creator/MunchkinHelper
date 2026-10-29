from controllers.auth_controller import AuthController
from controllers.main_controller import MainController
from controllers.game_controller import GameController
from controllers.catalog_controller import CatalogController
from controllers.bestiary_controller import BestiaryController
from controllers.monster_detail_controller import MonsterDetailController
from controllers.races_classes_controller import RacesClassesController
from controllers.race_class_detail_controller import RaceClassDetailController
from controllers.register_controller import RegisterController

__all__ = [
    'AuthController', 'MainController', 'GameController',
    'CatalogController', 'BestiaryController', 'MonsterDetailController',
    'RacesClassesController', 'RaceClassDetailController', 'RegisterController'
]