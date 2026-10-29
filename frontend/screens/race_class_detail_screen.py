"""
Экран детального описания расы или класса — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class RaceClassDetailScreen(Screen):
    """Экран полного описания расы или класса"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
    
    def on_back(self):
        """Вернуться на экран списка"""
        if self.controller:
            self.controller.go_back()
    
    def update_info(self, item_data):
        """Обновить информацию в UI"""
        if item_data:
            self.ids.item_type_label.text = item_data.get('type_label', '')
            self.ids.item_name.text = item_data.get('name', '')
            self.ids.ability_1.text = item_data.get('ability_1', '—')
            self.ids.ability_2.text = item_data.get('ability_2', '—')
            self.ids.epic_ability_1.text = item_data.get('epic_ability_1', '—')
            self.ids.epic_ability_2.text = item_data.get('epic_ability_2', '—')