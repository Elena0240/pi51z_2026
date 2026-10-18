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

#Задача 5
m = int(input("Сколько книг в библиотеке? "))
books = set()

for i in range(m):
    name = input("Название книги: ")
    books.add(name)

n = int(input("Сколько книг в списке? "))

for i in range(n):
    name = input("Какая книга нужна? ")
    if name in books:
        print("YES")
    else:
        print("NO")

#Задача 6
m = int(input("Сколько было уроков? "))
all_students = set()
for i in range(m):
    k = int(input("Сколько учеников на уроке? "))
    lesson_students = set()
    for j in range(k):
        name = input("Введите фамилию: ")
        lesson_students.add(name)   
    if i == 0:
        all_students = lesson_students
    else:
        all_students = all_students & lesson_students
for name in all_students:
    print(name)

#Задача 7
n = int(input("Сколько всего сотрудников? "))
names = set()
duplicates = set()
for i in range(n):
    name = input("Введите фамилию: ")
    if name in names:
        duplicates.add(name)
    else:
        names.add(name)
print("Количество однофамильцев:", len(duplicates))