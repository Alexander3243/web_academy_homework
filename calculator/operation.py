import math
from operation_history import w_operation


def add(a, b, id_user=0):
    res = a + b
    w_operation("{}+{}={}".format(a, b, res), id_user)
    return res


def sub(a, b, id_user=0):
    res = a - b
    w_operation("{}-{}={}".format(a, b, res), id_user)
    return res


def mul(a, b, id_user=0):
    res = a * b
    w_operation("{}-{}={}".format(a, b, res), id_user)
    return res


def truediv(a, b, id_user=0):
    res = a / b
    w_operation("{}-{}={}".format(a, b, res), id_user)
    return res


# For autorization users
def sin(a, id_user=0):
    res = math.sin(a)
    w_operation("sin({})={}".format(a, res), id_user)
    return res


def cos(a, id_user=0):
    res = math.cos(a)
    w_operation("cos({})={}".format(a, res), id_user)
    return res


def tg(a, id_user=0):
    res = math.tan(a)
    w_operation("tg({})={}".format(a, res), id_user)
    return res


def ctg(a, id_user=0):
    res = 1 / math.tan(a)
    w_operation("ctg({})={}".format(a, res), id_user)
    return res
