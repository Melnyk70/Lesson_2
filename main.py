# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
user_input = input("Введіть пʼятизначне ціле додатне число:")  # Нехай користувач надрукував 4
print(type(user_input))  # <class 'str'>
# print(user_input / 2)  # TypeError
number = int(user_input)
print(number % 10, end='')  # 5 цифра
print(number % 100 // 10, end='')  # 4 цифра
print(number % 1000 // 100, end='')  # 3 цифра
print(number % 10000 // 1000, end='')  # 2 цифра
print(number // 10000)  #1 цифра
