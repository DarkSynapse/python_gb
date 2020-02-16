# Девятая задача
# https://drive.google.com/file/d/1nNEjO0fZvkT0Ndksa9WKrlgf1LSsSoCK/view?usp=sharing

print("Введите три разных числа: ")

a = int(input())
b = int(input())
c = int(input())

if b < a < c or c < a < b:
    print("Среднее: ", a)
elif a < b < c or c < b < a:
    print("Среднее: ", b)
else:
    print("Среднее: ", c)