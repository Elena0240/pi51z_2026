#Методы split и join. Списочные выражения

#Задача 1
text = input("Введите текст: ")
words = text.split()
print(" ".join(words[::3]))

#Задача 2
line = input("Введите числа через пробел: ")
print(" ".join(["*" * int(x) for x in line.split()]))

#Задача 3

line = input("Введите числа через пробел: ")
nums = [int(x) for x in line.split()]
result = [x ** 2 for x in nums if x % 2 != 0 and (x ** 2) % 10 != 9]
print(" ".join([str(r) for r in result]))

#Задача 4
line = input("Введите числа через пробел: ")
nums = [int(x) for x in line.split()]
result = [x ** 2 for x in nums if x % 2 != 0 and (x ** 2) % 10 != 9]
print(" ".join([str(r) for r in result]))

#Задача 5
line = input("Введите строки через пробел: ")
words = line.split()
print("[" + ", ".join(['"' + w + '"' for w in words]) + "]")

#Задача 6
lines = []
while True:
    line = input("Строка рецепта (Enter — конец): ")
    if line == "":
        break
    if "лук" not in line.split():
        lines.append(line)
print(", ".join(lines))

#Задача 7
text = input("Введите строку: ")
print("\n".join(text.split()))

#Задача 8
url = input("Введите URL: ")
params = url.split("?")[1].split("&")
for p in params:
    if p.startswith("q="):
        print(p.split("=")[1])
        break