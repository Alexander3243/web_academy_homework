import os
import json
import datetime

d = datetime.datetime.now()
date = str(d.day) + "-" + str(d.month) + "-" + str(d.year)


# read new operation to db
def r_operation(user_id, today=False):
    if today:
        check_id = read_to_db(user_id=user_id, date=date)
        return check_id
    check_id = read_to_db(user_id=user_id, date=None)
    return check_id


def read_to_db(**read_operation):
    file_operation_history = os.path.join('history.json')

    def read_operation_in_db(user_id, data_today=None):
        with open(file_operation_history, 'r') as operation:
            list_operation = json.load(operation)
            if data_today == date:
                for user in list_operation:
                    if user['user_id'] == user_id and user['date'] == data_today:
                        print("-" * 10)
                        print(user["date"])
                        print("-" * 10)
                        for i in user["operation"]:
                            print(i)
            else:
                for user in list_operation:
                    if user['user_id'] == user_id:
                        print("-" * 10)
                        print(user["date"])
                        print("-" * 10)
                        for i in user["operation"]:
                            print(i)

    if read_operation_in_db(user_id=read_operation['user_id'], data_today=read_operation['date']):
        return True


# write new operation to db
def w_operation(operation, user_id):
    check_op = write_to_db(operation=operation, user_id=user_id)
    return check_op


def write_to_db(**check_operation):
    file_operation_history = os.path.join('history.json')

    def write_operation_in_db(op, user_id):
        if user_id == 0:
            return False
        with open(file_operation_history, 'r') as operation:
            list_operation = json.load(operation)
            for user in list_operation:
                if user['user_id'] == user_id and user['date'] == date:
                    user['operation'].append(op)
                    with open(file_operation_history, 'w+') as f:
                        json.dump(list_operation, f)
                        return True
            for user in list_operation:
                if user['user_id'] != user_id or user['date'] != date:
                    new_id = list_operation[-1]['id'] + 1
                    list_operation.append({"id": new_id,
                                           "date": date,
                                           "operation": [op],
                                           "user_id": user_id})
                    with open(file_operation_history, 'w+') as f:
                        json.dump(list_operation, f)
                        return True

    if write_operation_in_db(check_operation['operation'], check_operation['user_id']):
        return True
