#МНОЖЕСТВА

#Задача 1
n = int(input("Сколько строк вы будете вводить? "))
words = set()

for i in range(n):
    word = input(f"Введите слово {i + 1}: ")
    words.add(word)

print("Количество уникальных слов:", len(words))