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
