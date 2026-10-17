#Цикл for

#Задача 1
n = int(input("Введите число n: "))
for i in range(n + 1):
    print(i)

#Задача 2
n = int(input("Введите число n: "))
for i in range(n + 1):
    print(i, end="")
print()

#Задача 3
text = input("Введите строку: ")
n = int(input("Сколько раз вывести: "))
for i in range(1, n + 1):
    print(i, text)

#Задача 4
n = int(input("Введите число для отсчета: "))
for i in range(n, -1, -1):
    print(i)
print("Пуск!")

#Задача 5
n = int(input("Введите число n: "))
for i in range(n + 1):
    print("Куб числа", i, "равен", i **3)

#Задача 6
n = int(input("Введите число для факториала: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

#Задача 7
n = int(input("Сколько чисел вводить? "))
total = 0
for i in range(n):
    number = int(input("Введите число: "))
    total += number
print(total)

#Задача 8
n = int(input("Сколько чисел выводить? "))
product = 1
for i in range(n):
    number = int(input("Введите число: "))
    if number !=0:
        product *= number
print(product)

#Задача 9
n = int(input("Введите число: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

#Задача 10
n = int(input("Введите число n: "))
total = 0
for i in range(1, n + 1):
    number = int(input("Введите число: "))
    if i % 2 != 0:
        total += number
    else:
        total -= number
print(total)