from art import logo
print(logo)

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
   return n1 / n2
proceed = True
while proceed:
    n1=int(input("What's the first number?"))
    op=input("Pick an operation: + - * / ")
    n2=int(input("What's the second number?"))
    if op=="+":
        result=add(n1,n2)
    elif op=="-":
        result=sub(n1,n2)
    elif op=="*":
        result=mul(n1,n2)
    elif op=="/":
        result=div(n1,n2)

    print(f"{n1} {op} {n2} = {result} ")

    to_continue=input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation\t").lower()
    if to_continue=="n":
        proceed = False



