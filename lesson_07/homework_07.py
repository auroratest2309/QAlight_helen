"""
### Робота з файлами та папками — завдання

1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here
from pathlib import Path

with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!")

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("\nLearning file operations.")
"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Кількість символів у файлі:", len(content))
"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
import os

# створюємо папку "data", якщо її ще немає
os.makedirs("data", exist_ok=True)

# створюємо файл notes.txt всередині папки
with open("data/notes.txt", "w", encoding="utf-8") as f:
    f.write("My first note.")
"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
files = os.listdir("data")
print("Файли в папці data:", files)
"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
with open("data/notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("data/copy.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Вміст успішно скопійовано у copy.txt")
"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
# створимо два файли з текстом
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("Це файл А\n")

with open("b.txt", "w", encoding="utf-8") as f:
    f.write("А це файл B\n")

# об’єднаємо їх у новий файл
with open("ab.txt", "w", encoding="utf-8") as f_out:
    for filename in ["a.txt", "b.txt"]:
        with open(filename, "r", encoding="utf-8") as f_in:
            f_out.write(f_in.read())

print("Файл ab.txt створено і містить вміст a.txt та b.txt")
"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
with open("data/notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

if "note" in content:
    print("Знайдено")
else:
    print("Не знайдено")