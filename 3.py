#ПРОСТЫЕ ВСТРОЕННЫЕ ФУНКЦИИ

#Задача 1
number1 = int(input())
number2 = int(input())
print(number1 + number2)

#Задача 2
number1 = float(input())
number2 = float(input())
print(number1 + number2)

#Задача 3
word = input()
print("Слово", word, "имеет длину", len(word))

#Задача 4
number = float(input())
if number > 0:
    print("+")
elif number < 0:
    print("-")
else:
    print("0")

#Задача 5
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
print(days_per_year * hours_per_day * minutes_per_hour)

#Задача 6
text = input()
total_kopecks = len(text) * 40
rubles = total_kopecks // 100
kopecks = total_kopecks % 100
print(rubles, "p.", kopecks, "коп.")

#Задача 7
number1 = int(input())
number2 = int(input())
number1, number2 = number2, number1
print(number1)
print(number2)

#Задача 8
number =float(input())
print(abs(number))

#Задача 9
number1 = int(input())
number2 = int(input())
print(number1 // number2)
print(number1 % number2)

#Задача 10
number1 = int(input())
number2 = int(input())
operation = input()
if operation == "+":
 print(number1 + number2)
elif operation == "-":
 print(number1 - number2)
elif operation == "*":
 print(number1 * number2)
elif operation == "/":
   if number2 == 0:
      print("ОШИБКА")
   else:
      print(number1 / number2)
else:
   print("ОШИБКА")
   

