from run_operation import data_reg_operation, data_non_reg_operation
import registration
import authorization
import operation_history


check_first_answer = True
while check_first_answer:
    check_second_answer = True
    first_answer = input("Choice operation:"
                         "\n 1 - Sign in"
                         "\n 2 - Registration"
                         "\n 3 - Continue without registration"
                         "\n 4 - Exit \n")
    if first_answer == '1':
        id_user = authorization.authorization()
        while check_second_answer:
            sign_answer = input("Choice operation:"
                                "\n 1 - View operations for all time"
                                "\n 2 - View operations today"
                                "\n 3 - Calc"
                                "\n 4 - Exit \n")
            if sign_answer == "1":
                operation_history.r_operation(id_user)
            elif sign_answer == "2":
                operation_history.r_operation(id_user, today=True)
            elif sign_answer == "3":
                print("Result:", data_reg_operation(id_user))
            elif sign_answer == "4":
                check_second_answer = False
            else:
                print("Please enter correct answer")
    elif first_answer == '2':
        registration.register()
    elif first_answer == '3':
        print("Result:", data_non_reg_operation())
    elif first_answer == '4':
        check_first_answer = False
    else:
        print("Please enter correct answer")