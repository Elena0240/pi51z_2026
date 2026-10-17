#ЦИКЛ while

#Задача 1
number = int(input("введите число: "))
while number >=1:
    print(number)
    number -= 1

#Задача 2

number = int(input())
line = ""
while number != 0:
    line += str(number) + " "
    number = int(input())
print(line)

#Задача 3
line = input("введите строку: ")
while line != "":
    print(line)
    line = input("введите строку: ")

#Задача 4
t = float(input("Введите температуру: "))
while t !=0:
    if t < 15.5:
        print("ХОЛОДНО")
    elif t > 28:
        print("ЖАРКО")
    else:
        print("НОРМАЛЬНО")
    t = float(input("Введите температуру: "))

#Задача 5
password = input("Введите пароль: ")
repeat = input("Повторите пароль: ")
if len(password) < 8:
    print("Слишком короткий!")
elif password != repeat:
    print("Пароли не совпадают!")
else:
    print("ОК")

#Задача 6
password = input("Введите пароль: ")
repeat = input("Повторите пароль: ")
while len(password) < 8 or password != repeat or "123" in password:
    if len(password) <8:
        print("Слишком короткий!")
    elif password != repeat:
        print("Пароли не совпадают!")
    else:
        print("Пароль содержит 123!")
    password = input()
    repeat = input()
print("OK")

#Задача 7
number = int(input("Введите число: "))
total = 0
while number != 0:
    total += number
    number = int(input("Введите число: "))
    print(total)

#Задача 8
number = int(input("Введите число: "))
count = 0
while number > 0:
    count += 1
    number //= 10
print(count)

