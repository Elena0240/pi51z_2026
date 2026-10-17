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
    