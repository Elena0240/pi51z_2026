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