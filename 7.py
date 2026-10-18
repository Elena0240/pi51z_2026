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