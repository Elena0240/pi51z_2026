#Строки как коллекция
#Часть 1:Индексация

#Задача 1
word = input("Введите слово: ")
if len(word) < 5:
    print("НЕТ")
else:
    print(word[4])

#Задача 2
word = input("Введите слово: ")
if word[0] == "а":
    print("ДА")
else:
    print("НЕТ")

#Задача 3
word = input("Введите слово: ")
print(word[-1])

#3адача 4
word1 = input("Первое слово: ")
word2 = input("Второе слово: ")
if word1[-1] == word2[0]:
    print("ВЕРНО")
else:
    print("НЕВЕРНО")

#Задача 5
word = input("Введите слово: ")
for letter in word:
    print(letter)

#Задача 6
word = input("Введите слово: ")
n = int(input("Введите номер буквы: "))
if n < 1 or n > len(word):
    print("ОШИБКА")
else:
    print(word[n - 1])