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

# Создайте класс SoccerPlayer, у которого есть:

# конструктор __init__, принимающий 2 аргумента: name, surname. 
# Также во время инициализации необходимо создать 2 атрибута экземпляра: goals и assists - 
# общее количество голов и передач игрока, изначально оба значения должны быть 0


# метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение равно единице. 
# Метод должен увеличить общее количество забитых голов игрока на переданное значение;

# метод make_assist, который принимает количество передач, сделанных игроком за матч, по умолчанию данное значение равно единице. 
# Метод должен увеличить общее количество сделанных передач игроком на переданное значение;

# метод statistics, который вывод на экран статистику игрока в виде:
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>

class SoccerPlayer:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0
        
    def score(self, goals=1):
        self.goals += goals
    
    def make_assist(self, assists=1):
        self.assists += assists
    
    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

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

# Создайте класс Dog, у которого есть:
# конструктор __init__, принимающий 2 аргумента: name, age. 
# метод description, который возвращает строку в виде "<name> is <age> years old"
# метод speak принимающий один аргумент, который возвращает строку вида "<name> says <sound>";

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        self.sound = sound
        return f"{self.name} says {self.sound}"

###

# Ваша задача реализовать класс Stack, у которого есть:

# метод __init__  создаёт новый пустой стек. Параметры данный метод не принимает. 
# Создает атрибут экземпляра values, где будут в дальнейшем хранятся элементы стека в виде списка (list), 
# изначально при инициализации задайте значение атрибуту values равное пустому списку;

# метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает.

# метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. Стек изменяется. 
# Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "Empty Stack";

# метод peek() возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется. 
# Если элементов в стеке нет, распечатайте сообщение "Empty Stack", верните None после этого;

# метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.

# метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число.


class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)
    
    def pop(self):
        return self.values.pop() if self.values else print("Empty Stack")

    def peek(self):
        return self.values[-1] if self.values else print("Empty Stack")

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

###

# Создайте класс UserMail, у которого есть:

# конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес. 
# Их необходимо сохранить в экземпляр как атрибуты login и __email (обратите внимание, защищенный атрибут)

# метод геттер get_email, которое возвращает защищенный атрибут __email ;

# метод сеттер set_email, которое принимает в виде строки новую почту. 
# Метод должен проверять, что в новой почте есть только один символ @ и после нее есть точка. 
# Если данные условия выполняются, новая почта сохраняется в атрибут __email, в противном случае выведите сообщение "Ошибочная почта";

# создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email

class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str) and value.count('@') == 1 and '.' in value[value.find('@'):]:
            self.__email = value
        else:
            print("Ошибочная почта")

    email = property(get_email, set_email)
    
###

# Создайте класс Money, у которого есть:

# конструктор __init__, принимающий 2 аргумента: dollars, cents. По входным аргументам вам необходимо создать атрибут экземпляра total_cents. 

# свойство геттер dollars, которое возвращает количество имеющихся долларов;

# свойство сеттер dollars, которое принимает целое неотрицательное число - количество долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение центов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error dollars";

# свойство геттер cents, которое возвращает количество имеющихся центов;

# свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100 - 
# количество центов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение долларов должно сохранятся. 
# В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error cents";

#метод __str__ (информация по данному методу), который возвращает строку вида "Ваше состояние составляет {dollars} долларов {cents} центов". 
# Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами

class Money:
    
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.total_cents % 100
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 < value < 100:
            self.total_cents = (self.total_cents - self.total_cents % 100) + value
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов ' \
               f'{self.cents} центов'

###

# Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

# конструктор __init__, принимающий произвольное количество аргументов. 
# Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;

# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
# "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию;
# "Пустой вектор", если наш вектор не хранит в себе значения

class Vector:
    
    def __init__(self, *args):
        self.values = [x for x in args if isinstance(x, int)]  # только целые числа

    def __str__(self):
        if self.values:
            return f"Вектор{tuple(sorted(self.values))}"  # по возрастанию
        return "Пустой вектор"

###

###

###

###

###

###

###
