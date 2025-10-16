a = float(input("First Number: "))
b = float(input("Last Number: "))
op = input("Select Operation (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Cannot be devided by 0")
    else:
        print(a / b)
else:
    print("Option Not Available")
