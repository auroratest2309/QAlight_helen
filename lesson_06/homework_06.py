# Вправа 1: Проста математика
print("\n=== ВПРАВА 1: Калькулятор ===")
print("Створіть простий калькулятор для двох чисел і двох дій")
print("Підтримувані операції: +, -")

# Початок реалізації:
num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, ): ")
num2 = float(input("Введіть друге число: "))

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
else:
    print ("Incorrect action")    

# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")

password = str(input("Enter your password"))
if len(password) >= 8:
    print("Гарний пароль!")
else:
    print("Пароль повинен містити принаймні 8 символів")


# Вправа 3: Визначення високосного року
print("\n=== ВПРАВА 3: Високосний рік ===")
print("Рік є високосним, якщо:")
print("- Ділиться на 4 І не ділиться на 100")
print("- АБО ділиться на 400")

year = int(input("Enter year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Рік є високосним")
else:
    print("Рік не є високосним")


# Вправа 4: Лічильник голосних
print("\n=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")

text = input("Введіть текст: ").lower()
vowels = "аеиіїоуюя"
count = 0
for char in text:
        if char in vowels:
            count +=1 
print(f"Кількість голосних: {count}")

# код тут




# Вправа 5: Гра 
print("\n=== ВПРАВА 5: Гра ===")
"""
Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо колір прибульця green, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця yellow, надрукуйте, що гравець щойно заробив 10 балів.
Якщо колір прибульця red - надрукуйте, що гравець щойно заробив 15 балів.
Перевірте роботу гри самостійно, змінюючи значення alien_color
"""
alien_color = input(str("Enter color: (green, red, yellow): "))
if alien_color == "green":
    print("Ви щойно заробили 5 балів!")
elif alien_color == "yellow":
    print("Ви щойно заробили 10 балів!")
elif alien_color == "red":
    print("Ви щойно заробили 15 балів!")
else:
    alien_color != "yellow" and alien_color != "green" and alien_color != "red"
    print("Ви щось може i збили, але нічого не заробили :( спробуйте ще")

 


# Вправа 6: Піцерія *
print("\n=== ВПРАВА 6: Начинки для піци (pizza_topping) ===")
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
while True:
    pizza_topping = input("Введіть начинку для піци (або 'quit' для завершення): ").lower()
    if pizza_topping == "quit":
        print("Замовлення завершено")
        break
    else:
        print((f"Додаємо {pizza_topping} до вашої піци!"))
   



# Вправа 7: Зворотний порядок цифр
print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку")

number = input("Введіть число: ")
reversed_number = number[::-1]
print("У зворотному порядку:", reversed_number)


# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")

max_number = None

while True:
    current_number = int(input("Введіть число (0 — завершити): "))
    if current_number == 0:
        break
    if max_number is None or current_number > max_number:
        max_number = current_number

if max_number is None:
    print("Ви не ввели жодного числа.")
else:
    print(f"Найбільше число: {max_number}")



# Вправа 9: Виключення зі списку
print("\n=== ВПРАВА 9: Виключення зі списку ===")
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)

# Вправа 10: Вираз в один рядок
print("\n=== ВПРАВА 10: Вираз з умовою в один рядок ===")
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [n**2 for n in numbers if n % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]