# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число
# и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

print("Введите вещественное или целое число: ")
num = float(input())
sum = 0
if num < 0:
    num = num * (-1)

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f"Сумма цифр числа {num} = {sumNums(num)}")

