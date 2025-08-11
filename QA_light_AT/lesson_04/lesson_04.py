line = "apple,orange,banana,grape"
parts = line.split(',', 2)
print (parts)

print(line.startswith("orange"))
print(line.startswith("apple"))
print(line.endswith("banana"))
print(line.endswith("grape"))

user_input = "Hello ALL" 
small_ui = user_input.lower()
print(user_input, small_ui)
big_ui = user_input.upper()

title_ui = user_input.title()
print(title_ui)

capi_ui = user_input.capitalize()
print(capi_ui)

swap_ui = user_input.swapcase()
print(user_input, swap_ui)

vers_for_strip = "   Show must   go on!    "
strip_1 = vers_for_strip.strip()
print(f"|{vers_for_strip}|{strip_1}")

vers_for_strip_2 = "zzooovvv Show must   go on!  vvvooozzz"
strip_2 = vers_for_strip_2.strip("z").strip("o").strip("v").strip()
print(f"|{strip_2}")


str_list = ["apple","orange","banana","grape"]
joined_str = ','.join(str_list)
print(joined_str)

number = int("123")
print(number, type(number))
pi = float("3.242596")
print(pi, type(pi))
data_vals = "11,2,3,44,5"
data_list = data_vals.split(",")
print(data_list)

" " == True
"" == '' == """""" == False