def option():
    print("1 for Addition \n")
    print("2 for Subtract \n")
    print("3 for Multiplication \n")
    print("4 for Division \n")
    print("5 for Answer \n")
    x=int(input("Enter the Operation which you have to perform : "))
    return x

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

a=int(input("Enter the first Number : "))

while True:
    y=option()
    if y==1:
        b=int(input("Enter the second Number : "))
        a=add(a,b)
        print(a)
    elif y==2:
        b=int(input("Enter the second Number : "))
        a=subtract(a,b)
        print(a)
    elif y==3:
        b=int(input("Enter the second Number : "))
        a=multiply(a,b)
        print(a)
    elif y==4:
        b=int(input("Enter the second Number : "))
        a=divide(a,b)
        print(a)
    else:
        print("Exit Succesfully :) ")
        break
print("Final Answer is ",a)