#ЦИКЛ while

#Задача 1
number = int(input())
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