def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

should_continue=True

while should_continue:
    num1=int(input("What's the first number: "))
    also_continue=True
    value = 0

    while also_continue:
        print(" + \n - \n * \n / ")

        op=input("Pick an operator: ")

        num2=int(input("Whats the next number: "))


        if op=="+":
            value=add(num1,num2)
        elif op=="-":
            value = sub(num1, num2)
        elif op=="*":
            value = mul(num1, num2)
        elif op=="/":
            value = div(num1, num2)
        else:
            print("Invalid operator")

        print(f"{num1} {op} {num2} = {value}")
        num1=value

        yorn=input(f"Type 'y' to continue calculating with {value}, or type 'n' start a new calculation, or type 'exit' to exit the calculation : ")
        if yorn=='exit':
            also_continue=False
            should_continue = False

        elif yorn!="y":
            also_continue = False



