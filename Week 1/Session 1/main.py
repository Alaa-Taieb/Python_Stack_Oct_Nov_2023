# This a python comment. [Single line]

"""
    This is a multi-line comment in Python
    1
    2
    3
    4
    ...
"""

# Printing to the console
# print("Hello World!")


# Variables
variable_name = "Some value"

# Integer (int)
my_integers = 10

# String
my_string = "Hello, Python!"

# Boolean
my_boolean = False

# List
my_list = [1,2,3,4,5]

my_list.append(6)

my_list[0] = 10
print(my_list)

# print(my_list)

my_dictionary = {
    "name": "example_name",
    "age": 35,
    "address": "example_address"
}

my_dictionary["email"] = "example@gmail.com"

# Tuples
my_tuple = ("apple" , "Lemon" , "banana")

print(my_tuple[1])

my_list2 = list(my_tuple)
my_list2[1] = "Cherry"
my_list2.append("Orange")
my_tuple = tuple(my_list2)

print(my_tuple)

# [1,2,3,4,5,"apple","Lemon","Banana"]

# Unpacking tuples
coordinates = (54.52165 , 1.315485)
latitude, longitude = coordinates
print("Latitude: ", latitude)
print("longitude: ", longitude)


my_integers = 10
if my_integers < 8:
    print("Number is less than 8")
    print("Number is less than 8")
elif my_integers == 8:
    print("My integer is equal to 8")
else:
    print("Number is larger than 8")

print("Hello")

# for i in range(1,6,1):
#     print(i)

# print("My list length = ", len(my_list))

for i in range(6):
    my_list.append(i)

print(my_list)
# for i in range(5):
#     print(i)

# for key in my_dictionary.keys():
#     print(my_dictionary[key])

# for item in my_list:
#     print("my_list item  = ", item)

# print(my_list)

variable = range(5)
# [0,1,2,3,4]
new_list = [5,7,4,55,22,8.5]

for i in new_list:
    my_list.append(i)

print(my_list)