"""
Контроллер справочника — бизнес-логика навигации
"""


class CatalogController:
    """Логика экрана справочника"""
    
    def __init__(self, screen):
        self.screen = screen
        self._previous_screen = 'main'  # По умолчанию возвращаемся на главный
    
    def set_previous_screen(self, screen_name: str):
        """Запомнить, откуда пришли"""
        self._previous_screen = screen_name
    
    def go_back(self):
        """Вернуться на предыдущий экран"""
        print(f'Возврат на экран: {self._previous_screen}')
        self.screen.manager.current = self._previous_screen
    
    def open_bestiary(self):
        """Открыть бестиарий (заглушка)"""
        self.screen.show_message('Раздел "Бестиарий" — в разработке')
        print('Открытие бестиария')
    
    def open_races_classes(self):
        """Открыть расы/классы (заглушка)"""
        self.screen.show_message('Раздел "Расы/Классы" — в разработке')
        print('Открытие рас/классов')
    
    def show_rules_placeholder(self):
        """Показать заглушку правил"""
        self.screen.show_message('Раздел "Правила" — в разработке')
        print('Открытие правил')

    def open_bestiary(self):
        """Открыть бестиарий"""
        print('Открытие бестиария')
        bestiary_screen = self.screen.manager.get_screen('bestiary')
        bestiary_screen.controller.load_bestiary()
        self.screen.manager.current = 'bestiary'

    def open_races_classes(self):
        """Открыть расы/классы"""
        print('Открытие рас/классов')
        races_classes_screen = self.screen.manager.get_screen('races_classes')
        races_classes_screen.controller.load_races_and_classes()
        self.screen.manager.current = 'races_classes'