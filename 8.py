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

#Задача 7
s = input("Введите строку: ")
result = ""
for ch in s:
    if result == "":
        result = str(ord(ch))
    else:
        result = result + ", " + str(ord(ch))
print(result)

#Задача 8

word = input("Слово: ")
prev = word
while True:
    word = input("Следующее слово: ")
    if word[0] != prev[-1]:
        print(word)
        break
    prev = word

#Задача 9
string = input("Введите строку: ")
vowels = "аеёиоуыэюя"
count = 0
for i in string:
    if i in vowels:
        count = count + 1
print(count)

#Задача 10
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
step = int(input("Шаг сдвига: "))
string = input("Введите строку: ")
result = ""
for i in string:
    if i in alphabet:
        pos = alphabet.find(i)
        new_pos = (pos + step) % 33
        result = result + alphabet[new_pos]
    else:
        result = result + i
print(result)

#Часть 2: Срезы

#Задача 11
string = input("Введите строку: ")
print(string[::-1])

#Задача 12
string = input("Введите строку: ")
print(string[:3], s[-3:])

#Задача 13
string = input("Введите строку: ")
if string[:2] == "Не" or string[:2] == "не":
    print(string[2:])
else:
    print(string)

#Задача 14
string = input("Введите строку: ")
print(string[::2])

#Задача 15
n = int(input("Максимальная длина: "))
s = input("Введите строку: ")
if len(s) > n:
    print(s[:n - 3] + "...")
else:
    print(s)

#Задача 16
string = input("Введите строку: ")
if string == string[::-1]:
    print("ДА")
else:
    print("НЕТ")

#Задача 17
word1 = input("Первое слово: ")
word2 = input("Второе слово: ")
bulls = 0
cows = 0
for i in range(len(w1)):
    if word1[i] == word2[i]:
        bulls = bulls + 1
    elif word1[i] in word2:
        cows = cows + 1
print("Быки:", bulls)
print("Коровы:", cows)