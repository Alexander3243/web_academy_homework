import os
import json


def authorization():
    repeat_auth = True
    # user = None

    while repeat_auth:
        login = input('Login: ')
        password = input('Password: ')
        check_id = write_to_db(login=login, password=password)
        if check_id:
            print('You are logged in')
            repeat_auth = False
            return check_id


def write_to_db(**check_user):
    file = os.path.join('users.json')

    def check_user_in_db(login, password):
        nonlocal file
        find_pas = True

        with open(file, 'r') as users:
            list_users = json.load(users)
            while find_pas:
                for user in list_users:
                    if user['login'] == login:
                        if user['password'] == password:
                            find_pas = False
                            return user['id']
                else:
                    print("Wrong login or password")
                    return False

    check_user = check_user_in_db(login=check_user['login'], password=check_user['password'])
    if check_user:
        return check_user
    return False
