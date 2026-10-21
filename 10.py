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
        if (len(words[j]), words[j]) > (len(words[j+1]), words[j+1]):
            words[j], words[j+1] = words[j+1], words[j]
for w in words:
    print(w)

#Задача 5
n = int(input("Сколько чисел Фибоначчи вывести? "))
a = 1
b = 1
for i in range(n):
    print(a)
    a, b = b, a + b

#Задача 6
n = int(input("Сколько чисел? "))
nums = []
for i in range(n):
    nums.append(int(input("Число: ")))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)

#Задача 7
n = int(input("Сколько чисел? "))
nums = []
for i in range(n):
    nums.append(int(input("Число: ")))
unique_nums = set(nums)
print(len(unique_nums))

#Задача 8
n = int(input("Сколько пар чисел? "))
for i in range(n):
    line = input("Введите пару чисел: ")
    pos = line.find(" ")
    a = int(line[:pos])
    b = int(line[pos+1:])
    if a > b:
        a, b = b, a
    print(a, b)

#Задача 9
n = int(input("Сколько человек? "))
people = []
for i in range(n):
    line = input("Фамилия и рост: ")
    pos = line.find(" ")
    surname = line[:pos]
    height = int(line[pos+1:])
    people.append((surname, height))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if people[j][1] < people[j+1][1]:
            people[j], people[j+1] = people[j+1], people[j]
for p in people:
    print(p[0], p[1])