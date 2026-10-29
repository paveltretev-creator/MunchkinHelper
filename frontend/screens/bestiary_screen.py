"""
Экран списка бестиария — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class BestiaryScreen(Screen):
    """Экран списка монстров"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
    
    def on_enter(self):
        """При входе на экран — загрузить список"""
        if self.controller:
            self.controller.load_bestiary()
    
    def on_back(self):
        """Вернуться на экран справочника"""
        if self.controller:
            self.controller.go_back()
    
    def on_search_text(self, text):
        """Обработчик изменения текста поиска"""
        if self.controller:
            self.controller.filter_bestiary()
    
    def on_filter_change(self, filter_value):
        """Обработчик изменения фильтра"""
        if self.controller:
            self.controller.filter_bestiary()
    
    def on_monster_click(self, monster_id):
        """Обработчик клика на монстра"""
        if self.controller:
            self.controller.open_monster_detail(monster_id)
    
    def update_monster_list(self, monsters):
        """Обновить список монстров в UI"""
        # Очищаем текущий список
        monsters_list = self.ids.monsters_list
        monsters_list.clear_widgets()
        
        if not monsters:
            from kivy.uix.label import Label
            label = Label(
                text='Монстры не найдены',
                font_size=24,
                color=(0.17, 0.09, 0.06, 1),
                size_hint_y=None,
                height=50
            )
            monsters_list.add_widget(label)
            return
        
        # Добавляем монстров в список
        for monster in monsters:
            from kivy.uix.button import Button
            btn = Button(
                text=monster['name'],
                font_size=24,
                bold=True,
                background_color=(0.82, 0.71, 0.55, 1),
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=60
            )
            btn.bind(on_press=lambda instance, mid=monster['id']: self.on_monster_click(mid))
            monsters_list.add_widget(btn)