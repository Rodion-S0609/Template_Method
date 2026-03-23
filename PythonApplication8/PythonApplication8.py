from abc import ABC, abstractmethod

class AirportCheck(ABC):
    
    def check_passenger(self):
        self.show_ticket()
        self.security_scan()
        self.passport_control() 
        self.vlog_from_airport() 
        self.boarding()

    def show_ticket(self):
        print("1. Регистрация: Билет проверен, багаж сдан.")

    def security_scan(self):
        print("2. Безопасность: Проход через рамку и сканирование сумок.")

    @abstractmethod
    def passport_control(self):
        pass

    def boarding(self):
        print("4. Посадка: Выход на гейт и посадка в самолет.\n")

    def vlog_from_airport(self):
        pass

class DomesticFlight(AirportCheck):
    def passport_control(self):
        print("3. Паспортный контроль: Проверка внутреннего ID (быстрый процесс).")

class InternationalFlight(AirportCheck):
    def passport_control(self):
        print("3. Таможня: Проверка загранпаспорта, визы и декларации.")

    def vlog_from_airport(self):
        print("   [Bonus] Пассажир снимает сторис: 'Улетаю в отпуск!'")

if __name__ == "__main__":
    print("=== ПУТЕШЕСТВИЕ ПО СТРАНЕ ===")
    traveler1 = DomesticFlight()
    traveler1.check_passenger()

    print("=== ПУТЕШЕСТВИЕ ЗА ГРАНИЦУ ===")
    traveler2 = InternationalFlight()
    traveler2.check_passenger()