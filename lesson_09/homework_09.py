# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_ab(a,b):
    return a + b
a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(sum_ab(a,b))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avr(numbers):
    return (sum(numbers)/len(numbers))
numbers = []
while True:
    s = input("Enter number (0 finish): ".strip())
    try:
        n = int(s)
    except ValueError:
        print("Enter integer number")
        continue    
    if n == 0:
        break
    numbers.append(n) 
print("Average",avr(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def revers(s)
"""
def revers(s):
    return s[::-1]
string = input("Enter line")
print(revers(string))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def biggest_word(words):
    return (max(words, key = len))
words = []
while True:
    word = input("Enter word ('.' to finish): ")
   
    if word == ".":
        break
    else:
        words.append(word) 
print(biggest_word(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""print("\n=== ВПРАВА 1: Калькулятор ===")
print("Створіть простий калькулятор для двох чисел і двох дій")
print("Підтримувані операції: +, -")"""

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    else:
        return "Невідома операція"
    
# task 8
"""print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")"""
def check_password(password):
    if len(password) >=8:
        return("Accepted")
    else:
        return("Min len should be 8 symbols")
    

# task 9
""" print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку") """

def reverse_number(num):
    return str(num)[::-1]

n = input("Enter number: ")
print(reverse_number(n))


# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
def even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]
numbers = [1,2,3,4,5,6,7,8,9]
print (even_squares(numbers))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""