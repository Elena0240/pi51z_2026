#Кортежи

#Задача 1
n = int(input("Сколько чисел? "))
nums = []
for i in range(n):
    nums.append(int(input("Число: ")))

last = nums[-1]
found = False
for i in range(n - 1):
    for j in range(n - 1):
        if i != j and nums[i] * nums[j] == last:
            found = True

if found:
    print("ДА")
else:
    print("НЕТ")

#Задача 2
n = int(input("Сколько пар? "))
pairs = []
for i in range(n):
    line = input("Фамилия и оценка: ")
    pos = line.find(" ")
    surname = line[:pos]
    mark = int(line[pos+1:])
    pairs.append((surname, mark))
for p in pairs:
    print(p[0], p[1])
print()
for p in pairs:
    if p[1] == 4 or p[1] == 5:
        print(p[0], p[1])

#Задача 3
n = int(input("Сколько строк? "))

words = []
for i in range(n):
    word = input("Введите строку: ")
    words.append(word)
for w in sorted(words):
    print(w)

#Задача 4
n = int(input("Сколько строк? "))
words = []
for i in range(n):
    word = input("Введите строку: ")
    words.append(word)
for i in range(n - 1):
    for j in range(n - 1 - i):
        # Сравниваем кортежи: сначала длина, потом сама строка
        if (len(words[j]), words[j]) > (len(words[j+1]), words[j+1]):
            # Меняем местами через кортежное присваивание
            words[j], words[j+1] = words[j+1], words[j]
for w in words:
    print(w)

