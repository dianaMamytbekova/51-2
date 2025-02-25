# class 

class Person:
    # Это функция конструктор 
    def __init__(self, name, age):
        # Аттрибуты класса 
        self.name = name 
        self.age = age 
    # self - Это ссылка на экземпляр класса   
    # Метод класса    
    def instroduce(self):
        print(f'Hi I`m  {self.name}')


# class OBJ - Экземпляр класса
diana = Person('Diana', 18)        
diana.instroduce()


# print(type(diana))
# print(type(12345))
# print(type('hello'))

class Hero: # Родительский класс

    def __init__(self, name, hp, lvl):
        self.name = name 
        self.hp = hp 
        self.lvl = lvl

    def action(self):
        print(f'{self.name} делает базовое действие')    


# naofume = Hero('NaoFume', 100, 3)


class ShiledHero(Hero):  #Дочерний класс
    pass


# class -- CamelCase
# переменных методов функций -- snakeCase



        

