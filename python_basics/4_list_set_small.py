# Маленькие задачи

# Дан список a и кортеж b. Сконкатенируйте два этих объекта. Что получится?

a=[1,2,3,4]
b = {5,6,7,8}
a + b

#Traceback (most recent call last):
#  File "<pyshell#6>", line 1, in <module>
#    a + b
#TypeError: can only concatenate list (not "set") to list

###

# Пользователь вводит длину списка. Заполнить список нулями, кроме первого и последнего элементов, которые должны быть равны единице.

array_len = int(input())
array = [0 for x in range(array_len)]
array[0] = 1
array[-1] = 1
print(array)

###

# Пользователь вводит длину списка. Заполнить список нулями и единицами, при этом данные значения чередуются, начиная с нуля.

array_len = int(input())
array = [i%2 for i in range(array_len)]
print(array)

###

# Дан список чисел. Определите, каких чисел в списке больше: которые делятся на первый элемент списка или которые делятся на последний элемент списка.

list_numbers = input()
div_first = 0
div_last = 0
first_number = list_numbers[0]
last_number = list_numbers[-1]


###

# Дан список. Найдите сумму чисел списка, которые стоят на четных местах.

list_numbers = input()
array_numbers = [int(elem) for elem in list_numbers.split()]
for num in array_numbers:
  if int(num)%2 == 0:
       print(num, end=' ')

###

# Дан список. В данном списке найти максимальное количество одинаковых элементов.
