#УСЛОВНЫЙ ОПЕРАТОР

#Задача 1
word = input()
print(word, "? Конечно, помню, ведь мы проходили это на прошлом занятии!")

#Задача 2
name = input()
if name == "Python":
    print("ДА")
else:
    print("НЕТ")

#Задача 3
name = input()
print(name * 4)

#Задача 4
text = input()
if "кот" in text:
    print("МЯУ")
else:
    print("ГАВ")

#Задача 5
text1 = input()
text2 = input()
text3 = input()
if text1 == "раз" and text2 == "два" and text3 == "три":
    print("ГОРИ")
else:
    print("НЕ ГОРИ")

#Задача 6
text1 = input()
text2 = input()
text3 = input()
if (text1 == "раз" or text1 == "1") and (text2 == "два" or text2 == "2") and (text3 == "три" or text3 == "3"):
   print("ГОРИ")
else:
   print("НЕ ГОРИ") 

#Задача 7
answer1 = input("Ты любишь активный отдых? (да/нет): ")
answer2 = input("Ты любишь узнавать что-то новое? (да/нет): ")
if answer1 == "да" and answer2 == "да":
    print("Ты - Путешественник. ")
elif answer1 == "да" and answer2 == "нет":
    print("Движение - это жизнь.")
elif answer1 == "нет" and answer2 == "да":
    print("Ты очень любознательный!")
else:
    print("Ты - любитель поспать.")
