# 1 задание 
def logger(func):
    def wrapper(*args, **kwargs):
        if kwargs:
            print(f"Вызов функции: {func.__name__} с аргументами: {args} {kwargs}")
        else: 
            print(f"Вызов функции: {func.__name__} с аргументами: {args}")
        return func(*args, **kwargs)
    return wrapper


@logger
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")


# 2 задание 
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Прямоугольник {self.width} x {self.height} '

    def __add__(self, other):
        return Rectangle(self.width + self.height, other.width + other.height)

rect1 = Rectangle(3, 4)  
rect2 = Rectangle(2, 5)  
rect3 = rect1 + rect2  

print(rect1)
print(rect2)
print(rect3)    
     

