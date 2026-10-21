#Кортежи

#Задача 1
n = int(input("Сколько чисел? "))
nums = []
for i in range(n):
    nums.append(int(input("Число: ")))

last = nums[-1]
found = False
for i in range(n - 1):
    for j in range(n - 1):
        if i != j and nums[i] * nums[j] == last:
            found = True

if found:
    print("ДА")
else:
    print("НЕТ")