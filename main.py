import os

def cln_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def cln_num(x):
    return int(x) if x.is_integer() else x

def calculator(a, b, op):
    try:
        first_num = cln_num(float(a))
        last_num = cln_num(float(b))
    except ValueError:
        return "\n!Input must be a Number"

    if op in ("/", "//", "%") and last_num == 0:
        return "\n!Can't be divided by 0"

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "%": lambda x, y: x % y,
        "//": lambda x, y: x // y,
        "**": lambda x, y: x ** y
    }

    result = operations.get(op, lambda x, y: "\n!Unknown operator")(first_num, last_num)
    
    if isinstance(result, (int, float)):
        return f"\nResult: {first_num} {op} {last_num} = {cln_num(result)}"
    return result

def main():
    while True:
        cln_screen()
        print("===== PYTHON CALCULATOR =====")
        a = input("First Number: ")
        b = input("Last Number: ")
        print("=== Select Operator ===")
        op = input("+, -, *, **, /, //, %: ")

        result = calculator(a, b, op)
        print(result)
        is_continue = input("\n!Continue? (y/n): ").lower()

        if is_continue == "n":
            print("\n!Goodbye...")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n!Goodbye...")
    except Exception as e:
        print("\n!Error: ", e)

