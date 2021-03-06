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

# свойство сеттер dollars, которое принимает целое неотрицательное число - количество долларов и устанавливает при помощи него новое значение в 
# атрибут экземпляра total_cents, при этом значение центов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, 
# нужно печатать на экран сообщение "Error dollars";

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

# Создайте класс Robot, у которого есть:

# атрибут класса population. В этом атрибуте будет хранится общее количество роботов, изначально принимает значение 0;

# конструктор __init__, принимающий 1 аргумент name. Данный метод должен сохранять атрибут name и печатать сообщение вида 
# "Робот <name> был создан". Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;

# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"

# метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"

# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def destroy(self):
        print(f"Робот {self.name} был уничтожен")
        Robot.population -= 1

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{Robot.population}, вот сколько нас еще осталось")   
        
###

# Создайте класс Person, у которого есть:

# конструктор __init__, принимающий 3 аргумента: name, surname, gender. 
# Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". 
# Если в атрибут gender передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"

# переопределить метод __str__ следующим образом: 
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>

class Person:
    
    def __init__ (self, name, surname, gender = 'male'):
        self.name = name
        self.surname = surname
        if gender == 'female':
            self.gender = 'female'
        elif gender == '' or gender == 'male':
            self.gender = 'male'
        else:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        if self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'

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

# Создайте класс City, у которого есть:

# конструктор __init__, принимающий единственный аргумент - название города. Вам необходимо сохранить его в качестве атрибута экземпляра name, 
# причем вам нужно преобразовать переданное имя города таким образом, чтобы первая буква каждого слова была заглавной, 
# а остальные оказались строчными (пример "new york" - > "New York")
 
# переопределить метод __str__ таким образом, чтобы он возвращал имя города

# переопределить метод __bool__ так, чтобы он возвращал False, если название города заканчивается 
# на любую гласную букву латинского алфавита (a, e, i, o, u), в противном случае True

class City:
    
    def __init__(self, city):
        self.name = city.title()
        
    def __str__(self):
        return self.name
    
    def __bool__(self):
        if self.name[-1] in "aeiou":
            return False
        return True

###

# Сейчас вам нужно создать класс Quadrilateral (четырехугольник), в котором есть:

# конструктор __init__. Он должен сохранять в экземпляр класса два атрибута: width и height. 
# При этом в сам метод __init__ может передаваться один аргумент(тогда в width и height присваивать это одно одинаковое значение, 
# тем самым делать квадрат), либо два аргумента( первый идет в атрибут width, второй - в height)

# переопределить метод __str__ следующим образом: 
# если width и height одинаковые, возвращать строку "Куб размером <width>х<height>
# в противном случае, возвращать строку "Прямоугольник размером <width>х<height>

# переопределить метод __bool__ так, чтобы он возвращал True, если объект является кубом, и False в противном случае


class Quadrilateral:

    def __init__(self, *args):
        if len(args) == 1:
            self.width = self.height = args[0]
        else:
            self.width = args[0]
            self.height = args[1]

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height

###

# Ваша задача создать пустые классы Vehicle Car Plane Boat RaceCar, которые находятся в следующей иерархии:
# https://ucarecdn.com/0ccef0e2-a223-4620-9382-5e7015485613/
# Класс Vehicle является базовым классом, от которого наследуются все остальные.
# Необходимо написать только определение классов

class Vehicle:
    pass

class Car(Vehicle):
    pass

class RaceCar(Car):
    pass

class Plane(Vehicle):
    pass

class Boat(Vehicle):
    pass

###

# Создайте класс NewInt, который унаследован от целого типа int, то есть мы будем унаследовать поведение целых чисел и значит экземплярам 
# нашего класса будут поддерживать те же операции, что и целые числа.

# Дополнительно в классе NewInt нужно создать:

# метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2), обозначающее сколько раз нужно продублировать данное число. 
# Метод repeat должен возвращать новое число, продублированное n раз;

# метод to_bin, который возвращает двоичное представление числа в виде числа (может пригодиться функция bin)

class NewInt(int):
    
    def repeat(self, value=2):
        return int(str(self) * value)
    
    def to_bin(self):
        return int(bin(self)[2:])

###
