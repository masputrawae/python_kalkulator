def cln_num(x):
    return int(x) if x.is_integer() else x

def calculator(a, b, op):
    try:
        first_num = cln_num(float(a))
        last_num = cln_num(float(b))
    except ValueError:
        return "\n!Input must be a Number"

    result = 0

    if op == "+":
        result = first_num + last_num
    elif op == "-":
        result = first_num - last_num
    elif op == "*":
        result = first_num * last_num
    elif op == "/":
        if last_num == 0:
            return "\n!Cannot be divided by 0"
        else:
            result = first_num / last_num
    else:
        return "\n!The selected operation is not available"
    
    return f"\nResult: {first_num} {op} {last_num} = {cln_num(result)}"

def main():
    print("=== Python Kalkulator ===")
    a = input("First Number: ")
    b = input("Last Number: ")
    op = input("Select Operation (+, -, *, /): ")

    result = calculator(a, b, op)
    print(result)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n!Error: ", e)


