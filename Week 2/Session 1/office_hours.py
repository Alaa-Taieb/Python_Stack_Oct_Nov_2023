
# def countdown(number):
#     my_list = []
#     for i in range(number, -1 , -1):
#         my_list.append(i)
#     return my_list


# new_list = [10,9,8,7,6,5,4,3,2,1,0]

# new_list = countdown(10) # [10,9,8,7,..0]

# print([10,9,8,7,6,5,4,3,2,1,0])
# print(countdown(10))

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    second_element = list[1]
    for number in list:
        if number > second_element:
            new_list.append(number)

    print(len(new_list))
    return new_list

result = values_greater_than_second([3])
print(result)


def length_and_value(size , value):
    my_list = []
    for i in range(size):
        my_list.append(value)
    return my_list

result = length_and_value(5 , 8)
print(result)