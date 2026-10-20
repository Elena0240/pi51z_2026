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

#Задача 2
n = int(input("Сколько строк? "))
words = []
for i in range(n):
    words.append(input("Строка: "))
query = input("Поисковый запрос: ")
for w in words:
    if query in w:
        print(w)

#Задача 3
n = int(input("Сколько чисел? "))
nums = []
for i in range(n):
    nums.append(int(input("Число: ")))
out = ""
for i in range(n - 1):
    s = nums[i] + nums[i + 1]
    if out == "":
        out = str(s)
    else:
        out = out + " " + str(s)
print(out)

#Задача 4
n = int(input("Сколько строк? "))
words = []
for i in range(n):
    words.append(input("Строка: "))
for i in range(n - 1, -1, -1):
    print(words[i])