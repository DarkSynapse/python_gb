# Первая задача
# https://drive.google.com/file/d/181rYfuFaGt8HE7kMZyH2tLQPYHUSPm3G/view?usp=sharing

x = int(input("Введите целое 3х значное число = " ))

n1 = x // 100
n2 = x % 10
n3 = x % 100 // 10

print("сумма числел = " f'{n1 + n2 + n3}')
