# Given a list as an input, return the biggest value inside it.

# [2,8,4,6,14,4]

# IN MY HEAD: I am considering 14 as the biggest number

def find_max(number_list):
    max = number_list[0]
    for i in range(1 , len(number_list)):
        if max < number_list[i]:
            max = number_list[i]
    return max



# Gives a number than add it to list
# If user gives the letter s we stop and calculate

last_item = False
my_list = []
while not(last_item):
    
    number = input("Can you please enter the next number ('s' mean stop): ")
    if (number != 's'):
        my_list.append(int(number))
    else:
        last_item = True
    

print(my_list)
print(f"The biggest number in this loop is :{find_max(my_list)}")