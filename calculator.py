#calculator to work with it 
import math

history = []
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def devision(a,b):
    if b==0:
        return"Error : Division by zero"
    return a/b
def power(a,b):
    return a**b
def square_root(a,b):
    if a<0:
        return"Error: Negative number"
    return math.sqrt(a)

def show_menu():
    print("\n----PYTHON CALCULATOR----")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.Square Root")
    print("7.View History")
    print("8.Exit")
while True:
    show_menu()
    choise = input("enter choise(1-8)")

    if choise =='8':
        print ("Thnaks for using shivam's calculator ")
        break
    if choise=='7':
        print("\n---Calculator History")
        for item in history:
            print(item)
        continue
    try:
        if choise in ['1','2','3','4','5']:
            a = float(input("Enter first number : "))
            b = float(input("enter second number: "))

        if choise == '1':
            result =add(a,b)
            operation = f"{a}+{b} = {result}" 
        elif choise =='2':
            result = subtract(a,b)
            operation =f"{a}-{b}={result}"
        elif choise =='3':
            result = multiplication(a,b)
            operation=f"{a}*{b}={result}"
        elif choise =='4':
            result = devision(a,b)
            operation=f"{a}/{b}={result}"
        elif choise =='5':
            result=power(a,b)
            operation=f"{a}^{b}={result}"
        elif choise=='6':
            a = float(input( "enter number: "))
            result=square_root(a)
            operation =f"√{a} = {result}"
        else:
            print("invalid choise")
            continue
        print("result",result)
        history.append(operation)
    except ValueError:
        print("Error: Invalid input")
                  
                  
                  
