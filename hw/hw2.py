import random

class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} выполняет действие!"

    def attack(self):
        return f"{self.name} атакует!"

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if random.random() <= self.precision:
                return f"{self.name} успешно попал! Осталось стрел: {self.arrows}"
            else:
                return f"{self.name} промахнулся! Осталось стрел: {self.arrows}"
        return f"{self.name} не может атаковать, стрел нет!"

    def rest(self):
        self.arrows += 5
        return f"{self.name} отдыхает и пополняет стрелы! Теперь их {self.arrows}"

    def status(self):
        return f"Герой: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision:.2f}"


archer = Archer("Воин888", 100, 10, 0.8)


print(archer.status())
print(archer.attack())
print(archer.rest())
print(archer.status())



# Второй варинат без random
class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 0.5:
                return f"{self.name} успешно попал! Осталось стрел: {self.arrows}"
            else:
                return f"{self.name} промахнулся! Осталось стрел: {self.arrows}"
        return f"{self.name} не может атаковать, стрел нет!"

    def rest(self):
        self.arrows += 5
        return f"{self.name} отдыхает и пополняет стрелы! Теперь их {self.arrows}"

    def status(self):
        return f"Герой: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"

archer = Archer("Воин999", 100, 10, 0.8)
print(archer.status())
print(archer.attack())
print(archer.rest())
print(archer.status())