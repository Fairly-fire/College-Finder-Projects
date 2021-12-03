__________ = FillTheMissingPlacesUsingYourLogic #comment this line out otherwise you'd get an error
def add(a,b):
    __________
    print(f"The sum of {a} and {b} is {__________}") #formatted strings

def subtract(a,b):
    __________
    print(f"The result of subtracting {b} from {a} is {__________}")

def multiply(a,b):
    __________
    print(f"The multiplication of {a} and {b} is {__________}")

def division(a,b):
    __________
    print(f"The sum of {a} and {b} is {__________}")

# accepting multiple inputs in a single
number1,operator,number2 = map(str, input("Enter your equation: ")__________) # 8 / 9
number1 = int(number1)
number2 = int(number2)

# shift+alt+down

if operator == __________:
    add(number1,number2)
    
elif operator == __________:
    subtract(number1,number2)
    
elif operator == __________:
    multiply(number1,number2)
    
elif operator == __________:
    division(number1,number2)
    
else:
    print("Invalid Typo Error! Type something like - 8 / 4")
    

# add a function here which accepts the modulus operator '%' - 10%3 == 1
