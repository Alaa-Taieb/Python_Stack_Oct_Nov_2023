def function_name():
    print("Basic Function")
    print("Basic Function")
    print("Basic Function")
    print("Basic Function")

def function_2(parameter_1 = "Placeholder 1", parameter_2 = True):
    print(f"Parameter 1: {parameter_1} End of line")
    print(f"Parameter 2: {parameter_2}")
    print("Parameter 1: " + parameter_1 + " End of line" )

# function_2("hello" , False)


def greet(name):
    return f"Hello {name}"

print(greet("Alaa"))
# print("Hello Alaa") => Hello Alaa