# Настало время создать наш первый класс под названием Factory
# Ваша задача просто создать пустой класс, больше ничего внутри него делать не нужно

class Factory:
    pass

###

# Давайте создадим наш первый класс
# Вам необходимо создать класс Cat и внутри него два атрибута: name со значением 'Матроскин' и color со значением 'black'
# После этого создайте экземпляр класса и сохраните его в переменную my_cat

class Cat:
    name = 'Матроскин'
    color = 'black'

my_cat = Cat()

###

#  Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
# Пример работы с классом Lion

# simba = Lion()
# simba.roar() # печатает Rrrrrrr!!!

class Lion:
    def roar(self):
        print("Rrrrrrr!!!")

###
# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
# В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент - 
# значение, с которого начинается подсчет, по умолчанию равно 0
# Также нужно создать метод increment, который увеличивает счетчик на 1.
# Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>" 
# и метод reset,  который обнуляет экземпляр счетчика

class Counter:
    def start_from(self, value = 0):
        self.value = value       
    def increment(self):
        self.value +=1
    def display(self):
        print(f'Текущее значение счетчика= {self.value}')
    def reset(self):
        self.value = 0
        
###

# Создайте класс Point. У этого класса должны быть
# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса соответственно в атрибуты x и y 
# метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора. 
# В случае, если в данный метод передается не экземпляр класса Point необходимо вывести сообщение "Передана не точка"

class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, instance):
        if isinstance(instance, Point):
            return (((instance.x - self.x)**2) + ((self.y - instance.y)**2))**0.5
        else:
            print("Передана не точка")


###

# Создайте класс Laptop, у которого есть:
# конструктор __init__, принимающий 3 аргумента: brand, model, price 
# Также во время инициализации необходимо создать атрибут laptop_name - строковое значение, вида "<brand> <model>"
# И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.

class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'
        
laptop1 = Laptop('hp', '15-bw0xx', 57000)
laptop2 = Laptop('hp', 'pavillion gaming', 100500)

###


###

# Создайте класс Zebra, внутри которого есть метод which_stripe , 
# который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"

class Zebra():

    def __init__(self, count = 0):
        self.count = count

    def which_stripe(self):
        self.count += 1
        if self.count % 2 == 0:
            print("Полоска черная")
        else:
            print("Полоска белая")

###

# Создайте класс Person, у которого есть:
# конструктор __init__, принимающий 3 аргумента: first_name, last_name, age. 
# метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
# метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def is_adult(self):
        return True if self.age >= 18 else False

###


###
