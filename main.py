# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
print("Внесіть чотирьохзначне число:", end=" ")
user_input = input()  # Нехай користувач надрукував 4
print(type(user_input))  # <class 'str'>
print(user_input / 2)  # TypeError
number = int(user_input)
print(number / 2)  # Виведе 2
