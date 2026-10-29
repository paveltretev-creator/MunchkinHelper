"""
Экран детального описания монстра — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class MonsterDetailScreen(Screen):
    """Экран полного описания монстра"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
    
    def on_back(self):
        """Вернуться на экран списка бестиария"""
        if self.controller:
            self.controller.go_back()
    
    def update_monster_info(self, monster_data):
        """Обновить информацию о монстре в UI"""
        if monster_data:
            self.ids.monster_name.text = monster_data.get('name', '')
            self.ids.monster_type.text = f"Тип: {monster_data.get('type', '')}"
            self.ids.monster_level.text = f"Уровень: {monster_data.get('level', 0)}"
            self.ids.monster_description.text = monster_data.get('description', 'Описание отсутствует')
            self.ids.monster_quirk.text = monster_data.get('quirk', 'Непотребство отсутствует')
            self.ids.monster_xp.text = f"Даёт уровней: {monster_data.get('xp_reward', 0)}"
            self.ids.monster_treasure.text = f"Даёт сокровищ: {monster_data.get('treasure_reward', 0)}"