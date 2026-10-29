"""
Контроллер списка рас и классов — бизнес-логика
"""
from app.database import SessionLocal
from app.services.catalog_service import CatalogService


class RacesClassesController:
    """Логика экрана списка рас и классов"""
    
    def __init__(self, screen):
        self.screen = screen
        self._all_items = []
    
    def load_races_and_classes(self):
        """Загрузить расы и классы из БД"""
        db = SessionLocal()
        try:
            catalog = CatalogService(db)
            
            # Загружаем расы
            races = catalog.races_list()
            self._all_items = [
                {
                    'id': r.id_race,
                    'type': 'race',
                    'type_label': 'Раса',
                    'name': r.name,
                    'ability_1': r.ability_1,
                    'ability_2': r.ability_2,
                    'epic_ability_1': r.epic_ability_1,
                    'epic_ability_2': r.epic_ability_2,
                }
                for r in races
            ]
            
            # Загружаем классы
            classes = catalog.classes_list()
            self._all_items.extend([
                {
                    'id': c.id_class,
                    'type': 'class',
                    'type_label': 'Класс',
                    'name': c.name,
                    'ability_1': c.ability_1,
                    'ability_2': c.ability_2,
                    'epic_ability_1': c.epic_ability_1,
                    'epic_ability_2': c.epic_ability_2,
                }
                for c in classes
            ])
            
            # Сортируем по имени
            self._all_items.sort(key=lambda x: x['name'])
            
            self.filter_list()
        except Exception as e:
            print(f'Ошибка загрузки рас и классов: {e}')
        finally:
            db.close()
    
    def filter_list(self):
        """Фильтрация по поисковому запросу"""
        search_text = self.screen.ids.search_input.text.strip().lower()
        
        if search_text:
            filtered = [item for item in self._all_items if search_text in item['name'].lower()]
        else:
            filtered = self._all_items
        
        self.screen.update_list(filtered)
    
    def open_detail(self, item_id, item_type):
        """Открыть экран с детальным описанием"""
        item = next((i for i in self._all_items if i['id'] == item_id and i['type'] == item_type), None)
        
        if item:
            detail_screen = self.screen.manager.get_screen('race_class_detail')
            detail_screen.controller.set_item_data(item)
            self.screen.manager.current = 'race_class_detail'
    
    def go_back(self):
        """Вернуться на экран справочника"""
        self.screen.manager.current = 'catalog'