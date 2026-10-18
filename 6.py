#TRUE и FALSE. BREAK и CONTINUE

#Задача 1
n = int(input("Сколько строк ввести? "))
found = False
for i in range(n):
    text = input("Введите строку: ")
    if "кот" in text or "Кот" in text: 
        found = True
if found:
    print("МЯУ")
else:
    print("НЕТ")

#Задача 2
n = int(input("Сколько строк ввести? "))
found = False
for i in range(n):
    text = input("Введите строку: ")
    if "кот" in text or "Кот" in text: 
        found = True
        break
if found:
    print("МЯУ")
else:
    print("НЕТ")

#Задача 3
cat = -1
counter = 0
while True:
    text = input("Введите строку (или СТОП): ")
    if text == "СТОП":
        break
    counter += 1
    if ("кот" in text or "Кот" in text) and cat == -1:
        cat = counter 
print(cat)

#Задача 4
cat = 0
index = -1
counter = 0
while True:
    text = input("Введите строку: ")
    if text == "СТОП":
        break
    counter += 1 
    if "кот" in text or "Кот" in text:
        cat += 1
        if index == -1:
            index = counter
print(cat, index)

#Задача 5
a = int(input("Введите начало (а): "))
b = int(input("Введите конец (b): "))
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

#Задача 6
total = 0
count = 0
result = -1
while True:
    number = int(input("Введите число (0 для выхода): "))
    if number == 0:
        break
    total += number
    count += 1
    if total >= 10 and result == -1:
        result = count -1
print(result)

#Задача 7
n = int(input("Сколько строк вводить? "))
for i in range(n):
    text = input("Введите строку: ")
    if "плохо" in text:
        continue
    print(text)

#Задача 8
cat = False
while True:
    text = input("Введите строку (или СТОП): ")
    if text == "СТОП":
        break
    if "пёс" in text or "Пёс" in text:
        cat = False
    elif "кот" in text or "Кот" in text:
        cat = True
if cat:
    print("МЯУ")
else:
    print("НЕТ")
