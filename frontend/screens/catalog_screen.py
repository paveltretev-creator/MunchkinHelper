"""
Экран справочника — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class CatalogScreen(Screen):
    """Экран справочника"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
    
    def on_back(self):
        """Вернуться на предыдущий экран"""
        if self.controller:
            self.controller.go_back()
    
    def on_bestiary(self):
        """Перейти в бестиарий (заглушка)"""
        if self.controller:
            self.controller.open_bestiary()
    
    def on_races_classes(self):
        """Перейти в расы/классы (заглушка)"""
        if self.controller:
            self.controller.open_races_classes()
    
    def on_rules(self):
        """Показать заглушку правил"""
        if self.controller:
            self.controller.show_rules_placeholder()
    
    def show_message(self, message: str):
        """Показать информационное сообщение"""
        self.ids.message_label.text = message