#Списки

#Задача 1
n = int(input("Сколько строк? "))
words = []
for i in range(n):
    words.append(input("Строка: "))
result = ""
for w in words:
    if result == "":
        result = w
    else:
        result = result + " " + w
print(result)