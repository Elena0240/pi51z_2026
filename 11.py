#Методы split и join. Списочные выражения

#Задача 1
text = input("Введите текст: ")
words = text.split()
print(" ".join(words[::3]))