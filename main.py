class Store:
    def __init__(self, name, address):
        """Инициализация магазина с его названием, адресом и пустым ассортиментом."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаление товара из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Получение цены товара по его названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновление цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

# Создание объектов класса Store
store1 = Store("Магазин №1", "ул. Пушкина, 10")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("Магазин №2", "ул. Лермонтова, 15")
store2.add_item("oranges", 0.85)
store2.add_item("grapes", 1.2)

store3 = Store("Магазин №3", "ул. Чехова, 20")
store3.add_item("pears", 0.6)
store3.add_item("mangoes", 1.5)

# Пример использования методов
print(store1.get_price("apples"))  # Выводит: 0.5
store1.update_price("apples", 0.55)
print(store1.get_price("apples"))  # Выводит: 0.55
store1.remove_item("bananas")
print(store1.get_price("bananas"))  # Выводит: None