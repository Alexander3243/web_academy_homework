from operation import add, sub, mul, truediv, sin, cos, tg, ctg


def check_type_num(a):
    if "." in a and a[-1] == "0":
        return int(float(a))
    elif "." in a:
        return float(a)
    return int(a)


def data_non_reg_operation():
    while True:
        try:
            num1 = check_type_num(input("Enter first number:\n"))
            op_ = input("Enter operation, you can only use:  \"+\", \"-\", \"*\", \"/\"\n")
            num2 = check_type_num(input("Enter second number:\n"))
            if op_ == "+":
                return add(num1, num2)
            elif op_ == "-":
                return sub(num1, num2)
            elif op_ == "*":
                return mul(num1, num2)
            elif op_ == "/":
                return truediv(num1, num2)
        except Exception:
            print("Please enter correct data")


def data_reg_operation(id_user_):
    while True:
        try:
            operators_ = "sin,cos,tg,ctg"
            num1 = check_type_num(input("Enter first number:\n"))
            op_ = input("Enter operation, you can use: \"+\", \"-\", \"*\", \"/\", \"sin\", \"cos\", \"tg\", \"ctg\" \n")
            if op_ not in operators_:
                num2 = check_type_num(input("Enter second number:\n"))
                if op_ == "+":
                    return add(num1, num2, id_user_)
                elif op_ == "-":
                    return sub(num1, num2, id_user_)
                elif op_ == "*":
                    return mul(num1, num2, id_user_)
                elif op_ == "/":
                    return truediv(num1, num2, id_user_)
            else:
                if op_ == "sin":
                    return sin(num1, id_user_)
                elif op_ == "cos":
                    return cos(num1, id_user_)
                elif op_ == "tg":
                    return tg(num1, id_user_)
                elif op_ == "ctg":
                    return ctg(num1, id_user_)
        except Exception:
            print("Please enter correct data")
