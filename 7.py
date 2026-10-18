#МНОЖЕСТВА

#Задача 1
n = int(input("Сколько строк вы будете вводить? "))
words = set()

for i in range(n):
    word = input(f"Введите слово {i + 1}: ")
    words.add(word)

print("Количество уникальных слов:", len(words))

#Задача 2
n = int(input("Сколько городов уже есть? "))
cities = set()

for i in range(n):
    city = input(f"Введите город {i + 1}: ")
    cities.add(city)

new_city = input("Какой город хотите проверить? ")

if new_city in cities:
    print("Результат: TRY ANOTHER")
else:
    print("Результат: OK")

#Задача 3
list1 = set()
list2 = set()

while True:
    text = input()
    if text == "":
        break
    list1.add(text)

while True:
    text = input()
    if text == "":
        break
    list2.add(text)

common = list1 & list2

if len(common) > 0:
    for num in common:
        print(num, end=" ")
    print()
else:
    print("EMPTY")

#Задача 4
m = int(input("Сколько учеников изучают английский? "))
english = set()
for i in range(m):
    name = input("Введите фамилию: ")
    english.add(name)
n = int(input("Сколько учеников изучают немецкий? "))
german = set()
for i in range(n):
    name = input("Введите фамилию: ")
    german.add(name)

only_one = english.symmetric_difference(german)

if len(only_one) > 0:
    print("Ученики, изучающие только один язык:", len(only_one))
else:
    print("NO")