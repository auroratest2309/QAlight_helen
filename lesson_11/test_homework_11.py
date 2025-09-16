
"""
Тести для файлу tasks.py
Запуск: pytest test_tasks.py
"""
import pytest
#import sys
import math
#from pathlib import Path

"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""
def add(a,b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-2, -3) == -5
    assert add(0, 3) == 3
    assert add(-5,0) == -5


"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""
def is_even (n):
    return n % 2 == 0

def test_is_even():
    assert is_even (2) is True
    assert is_even (0) is True
    assert is_even (-4) is True
    assert is_even (3) is False
    assert is_even (-7) is False
   

    # TODO: додай тести для функції is_even
   


"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""
def reverse_string(s):
    return s[::-1]

def test_reverse_string():
    assert reverse_string ("Hello") == "olleH"
    assert reverse_string ("A") == "A"
    assert reverse_string ("") == ""


    # TODO: додай тести для функції reverse_string



"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""
def find_min(nums):
    return min(nums)
   

def test_find_min():
    assert find_min([1, 2, 8, 99, 1001]) == 1
    assert find_min([8]) == 8
    assert find_min([-1, -2, -8, -99, -1001]) == -1001

    # TODO: додай тести для функції find_min


"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""
def contains_substring(s, sub):
    return sub in s

def test_contains_substring():
    assert contains_substring ("Hello word", "word") is True
    assert contains_substring ("Hello word", "python") is False
    assert contains_substring ("Hello word", "") is True
    assert contains_substring ("", "word") is False

    # TODO: додай тести для функції contains_substring



"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""
def test_factorial():
    assert math.factorial(0) == 1
    assert math.factorial(1) == 1
    assert math.factorial(5) ==120

    # TODO: додай тести для функції factorial
  


"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""
def div(a,b):
    return a / b
def test_divide():
    assert div(10, 2) == 5
    assert div(20, -5) == -4
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
    # TODO: додай тести для функції divide



"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""
def is_palindrome(s):
    return s == s[::-1]
def test_is_palindrome():
    assert is_palindrome("level") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
    # TODO: додай тести для функції is_palindrome



"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""
def sum_list(nums):
    return sum(nums)

def test_sum_list():
    assert sum_list([1,2,3,4,5]) == 15
    assert sum_list([0,-1,-2,-5]) == -8
    assert sum_list([]) == 0
    # TODO: додай тести для функції sum_list



"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""
def to_upper(s):
    return (s.upper())


def test_to_upper():
    assert to_upper("hello") == "HELLO"
    assert to_upper("PYTHON") == "PYTHON"
    assert to_upper("") == ""

    # TODO: додай тести для функції to_upper

