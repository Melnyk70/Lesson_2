# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
x = 1
print(id(x)) # Виведе 4382794560. Для кожного запуску кода це значення – різне
x = 2 # Перевизначення, тобто змінна змінила адресу у памʼяті
print(id(x)) # Виведе 4382794592, тобто іншу клітину памʼяті

l = [1, 2, 3] # Це змінна типу list, який є змінюванним
print(l) # Виведе [1, 2, 3]
print(id(l)) # Виведе 4377070080. Для кожного запуску кода це значення – різне
l.append(4)
print(l) # Виведе [1, 2, 3, 4]
print(id(l)) # Виведе 4377070080. Таке ж саме значення