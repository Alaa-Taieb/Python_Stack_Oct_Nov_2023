# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 5 => 120
# 1 * 2 = 2
# 2 * 3 = 6 
# 6 * 4 = 24
# 24 * 5 = 120
# factorial(5) 

def factorial(num):
    f = 1
    for i in range(2, num + 1):
        f *= i
    return f

def rec_factorial(n):
    if n == 1:
        return 1
    return n * rec_factorial(n - 1)

# fact(3) => 3 * (2) => 6
# 

# number *= 2    | number = number * 2

def factorial_5():
    number = 1
    number *= 2
    number *= 3
    number *= 4
    number *= 5

    return number
    

print(factorial(7))