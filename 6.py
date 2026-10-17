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