from abc import ABC, abstractmethod

class HotBeverage(ABC):
    
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments(): 
            self.add_condiments()

    def boil_water(self):
        print("Кипячение воды...")

    def pour_in_cup(self):
        print("Переливание в чашку...")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def customer_wants_condiments(self):
        return True

class Tea(HotBeverage):
    def brew(self):
        print("Заваривание чайного пакетика...")

    def add_condiments(self):
        print("Добавление лимона...")

class Coffee(HotBeverage):
    def brew(self):
        print("Пропускание кофе через фильтр...")

    def add_condiments(self):
        print("Добавление сахара и молока...")

    def customer_wants_condiments(self):
        return False

if __name__ == "__main__":
    print("--- Готовим Чай ---")
    tea = Tea()
    tea.prepare_recipe()

    print("\n--- Готовим Кофе ---")
    coffee = Coffee()
    coffee.prepare_recipe()
