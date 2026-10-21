#Методы split и join. Списочные выражения

#Задача 1
text = input("Введите текст: ")
words = text.split()
print(" ".join(words[::3]))

#Задача 2
line = input("Введите числа через пробел: ")
print(" ".join(["*" * int(x) for x in line.split()]))