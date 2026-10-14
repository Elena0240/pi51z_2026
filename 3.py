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

#Задача 
text = input()
total_kopecks = len(text) * 40
rubles = total_kopecks // 100
kopecks = total_kopecks % 100
print(rubles, "p.", kopecks, "коп.")