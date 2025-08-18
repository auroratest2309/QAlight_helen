#tuple незмінні значення

sing_element_tuple = (42,)

mixed_tuple = (1, 'hello', 3.14, True)
#mixed_tuple = 1, 'hello', 3.14, True

first = mixed_tuple[0]
last = mixed_tuple[-1]
print(first, last)
print(mixed_tuple.count('hello'))

#my_tuple = (1,2,3,2,4,2,5)
#index_of_2_2 = my_tuple.index(2, index_of_2_2 + 1)
#print("index_of_2_2", index_of_2_2)

my_tuple = (1,2,3,2,4,2,5,6,7,8,9,0)
subset = my_tuple[2:7]
print(subset)
subset_2 = my_tuple[2:8:2]
print(subset_2)

one, two, thre, four = mixed_tuple
print("four vals", one, two,)

#list

my_list_2 = [1, 2, 4, 'a', 'b', 'c']
print(my_list_2[0])
print(my_list_2[-1])

my_list = [1,2,3,4,5,6,7,8,9,10]
subset = my_list[2:7]
print(subset)
subset_2 = my_list[2:8:2]
print(subset_2)

my_list.append(4)
print(my_list)

small = [0,1,2,3,4]
*one, two, thre = small
print("3 vals small", one, two, thre)
one, *two, thre = small
print("3 vals small", one, two, thre)

numbers = [1,2,3,4,5,7,2,4,2,0]
numbers.sort()
print("numbers", numbers) # сортирует, ничего не возвращает

sorted_list = sorted(numbers)
print(sorted_list) #сортирует и не перезаписывает

#set
