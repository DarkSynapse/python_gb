# Восьмая задача
# https://drive.google.com/file/d/18CnooQl73nRGgH5j8GKJjx8zpJiHrtLt/view?usp=sharing

x = int(input("Введите год в формате XXXX = "))
if x % 4 != 0:
    print("Год не високосный")
elif x % 100 == 0:
    if x % 400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")
else:
    print("Год Високосный")