print("Test!!")

#### first function
def myFirstAddFunction(x, y):
    sum = x + y
    return sum

### second function
def simpleCalculator(x, y, operator):
    value = ""
    if (operator == "+"):
        value = x + y
    elif (operator == "-"):
        value = x - y
    elif (operator == "*"):
        value = x * y
    elif (operator == "/"):
        value = x / y
    else:
        value = "INVALID"
        
    if value % 1 == 0:
        return int(value)
    return value


#print(myFirstAddFunction(3,4))
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operator: ")

res = simpleCalculator(num1, num2, op)

print(res)