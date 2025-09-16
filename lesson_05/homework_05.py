# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_values_small_list = [x for x in small_list if small_list.count(x) == 1]
print(unique_values_small_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

print(sum(small_list) / len(small_list))

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
big_list_has_duplicates = len(big_list) != len(set(big_list))
if big_list_has_duplicates:
    print("big_list has duplicates")
else:
    print("big_list has not duplicates")    

#print("big_list has duplicates" if len(big_list) != len(set(big_list)) else "big_list has no duplicates")

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":33, 'size': 12}
max_add_dict = max(add_dict.values())
print(max_add_dict)


# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
new_base_dict = dict(zip(base_dict.values(), base_dict.keys()))
print(new_base_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for k, v in base_dict.items():
    if k in add_dict:
        sum_dict[k] =f"{v} {add_dict[k]}"
    else:
        sum_dict[k] = v
for k, v in add_dict.items():
    if k not in sum_dict:
        sum_dict[k] = v        
print(sum_dict)        


# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_line = set(line)
print(set_line)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_sets = sum(set_1 ^ set_2)
print(sum_sets)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [6, 7, 8, 9, 10]
unique_elements = set(list_1) ^ set(list_2)
print(unique_elements)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

age_dict = {}

for name, age in person_list:
    start = (age // 10) * 10     # нижняя граница диапазона
    end = start + 9              # верхняя граница диапазона
    key = f"{start}-{end}"       # ключ словаря, например "20-29"
    
    if key not in age_dict:
        age_dict[key] = []
    age_dict[key].append(name)

print(age_dict)