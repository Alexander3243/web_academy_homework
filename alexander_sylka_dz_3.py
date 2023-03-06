"""
1. Напишіть функцію, яка приймає слово у нижньому регістрі і повертає слово з першою великою буквою.
Введіть рядок слів через пропуск у нижньому регістрі і застосуйте створену функцію для отримання результату
як у вихідних даних.

Вхідні дані:

jived fox nymph grabs quick waltz

Вихідні дані:

Jived Fox Nymph Grabs Quick Waltz
"""

def first_capital_letter(text: str) -> str:
    return text.title()


"""
2. Дано дійсне додатне число a і ціле число n, яке може набувати додатних і від’ємних значень.
Напишіть функцію для обчислення an. Стандартною функцією піднесення до степеня і оператором ** користуватися не можна.

 Вхідні дані:

 2
 1
 2
-1
 2
 1
 2
-1

 Вихідні дані:

 2.0
 0.5
"""


def calc_degree(num1, num2):
    result = 1.0
    if num2 > 0:
        for i in range(num2):
            result *= num1
        return result
    elif num2 < 0:
        for i in range(abs(num2)):
            result *= num1
        return float(1 / result)
    return result


list_numbers = []

# enter numbers one by one ('Enter' - close program)
while True:
    num = input()
    if num == '':
        break
    list_numbers.append(num)

i = 0
while len(list_numbers) - 1 > i:
    print(calc_degree(float(list_numbers[i]), int(list_numbers[i + 1])))
    i += 2

"""
3. Напишіть функцію, яка отримує значення середньомісячної кількості опадів по місяцях (в мм) і повертає
загальний обсяг опадів протягом року, середньорічну кількість опадів, назви місяців та значення з найвищим та
найменшим числом опадів протягом року.
Вхідні дані:

22 22 24 49 72 98 101 82 51 40 36 24
Вихідні дані:

(621.0, 51.75, (101.0, 'July'), (22.0, 'January'))
"""


def precipitation(nums):
    month = {1: "January",
             2: "February",
             3: "March",
             4: "April",
             5: "May",
             6: "June",
             7: "July",
             8: "August",
             9: "September",
             10: "October",
             11: "November",
             12: "December"}

    total_p = sum(nums)
    avg_p = sum(nums) / 12
    max_p = max(nums), month[nums.index(max(nums))+1]
    min_p = min(nums), month[nums.index(min(nums))+1]

    return "({}, {}, {}, {})".format(total_p, avg_p, max_p, min_p)


data = list(map(float, input().split()))

"""
4. Написати функцію для перевірки правильності введеної дати. Функція приймає 3 аргументи - день, місяць та рік і
повертає True, якщо така дата є в календарі, і False в протилежному випадку.
Вхідні дані:

04
03
2029

33
11
2019

Вихідні дані:

True

False
"""


# checking the number of days in february
def check_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return 29
    elif y % 400 == 0 and y % 100 == 0:
        return 29
    elif y % 100 == 0:
        return 28
    return 28


def check_data(n):
    day = n[0]
    month = n[1]
    year = n[2]

    months_days = {1: 31, 2: check_year(year), 3: 31, 4: 30, 5: 31,
                   6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if year > 0 and len(str(year)) == 4 and 0 < month <= 12 and 0 < day <= months_days[month]:
        return True
    return False


# enter 3 numbers in one line with a space ('Enter' - close program)
while True:
    nums = list(map(int, input().split()))
    if len(nums) != 3:
        break
    print(check_data(nums))

"""
5. На стадіоні є три категорії місць для сидіння: місця класу A коштують a грошових одиниць, місця
класу B коштують b грошових одиниць, а місця класу C - c грошових одиниць. Напишіть першу функцію, яка запитує
скільки продано квитків на кожний клас місць, і другу функцію, яка відображає суму отриманого доходу від продажу
квитків на кожен клас окремо і загалом. Формати введення і виведення такі, як у вхідних і
вихідних даних. a = 20.50 b = 15.75 c = 10.55

Вхідні дані:
A
45
B
30
C
15

Вихідні дані:

({'A': 922.5, 'B': 472.5, 'C': 158.25}, 1553.25)
"""


def total_sell_tickets(a, b, c):
    price_a = 20.50
    price_b = 15.75
    price_c = 10.55
    categories_places = {'A': a * price_a, 'B': b * price_b, 'C': c * price_c}
    return categories_places, sum(categories_places.values())


def sell_tickets(c1_a, c2_a, c3_a):
    return total_sell_tickets(c1_a, c2_a, c3_a)


category1 = input()
cat1_amount = int(input())
category2 = input()
cat2_amount = int(input())
category3 = input()
cat3_amount = int(input())

print(sell_tickets(cat1_amount, cat2_amount, cat3_amount))

"""
6. Напишіть функцію, яка отримує послідовність балів (цілі числа) і повертає буквенну інтерпретацію числових балів
на основі наступної шкали оцінок:
90-100 - A
80-89 - B
70-79 - C
60-69 - D
Нижче 60 - F

Вхідні дані:

60 80 64 45 35 87 90 95 91 64 78 (їх може n)
Вихідні дані:

{'A': [90, 95, 91], 'B': [80, 87], 'C': [78], 'D': [60, 64, 64], 'F': [45, 35]}
"""


def rating(*args):

    dict_ratings = {"A": [], "B": [], "C": [], "D": [], "F": []}

    for i in args:
        if 90 <= i <= 100:
            dict_ratings["A"].append(i)
        elif 80 <= i <= 89:
            dict_ratings["B"].append(i)
        elif 70 <= i <= 79:
            dict_ratings["C"].append(i)
        elif 60 <= i <= 69:
            dict_ratings["D"].append(i)
        elif 60 > i:
            dict_ratings["F"].append(i)
    return dict_ratings


print(rating(*list(map(int, input().split()))))

"""
7. Напишіть функцію для сортування рядка в алфавітному порядку без врахування регістру літер.

Вхідні дані:

JavaScript
Python
Вихідні дані:

aaciJprStv
hnoPty
"""


def sort_alpha(line):
    result = ""
    for i in sorted(line.upper()):
        if i in line:
            result += i
        else:
            result += i.lower()
    return result

print(sort_alpha(input()))

"""
8. Напишіть функцію для сортування рядка слів, розділених пропусками, за довжиною слів в порядку зростання.

Вхідні дані:

Ruby Python Go JavaScript Java
Вихідні дані:

Go Java Ruby Python JavaScript

"""

def sort_words(sentence):
    return sorted(sorted(sentence), key=len)

print(*sort_words(input().split()))

"""
9. Дано список кортежів, кожен з яких містить два значення: назва фільму (рядок) і рейтинг (дійсне число).
Напишіть функцію(ї) для сортування кортежів в порядку зростання рейтингу.

Вхідні дані:

[('Toy Story 4', 8.2) , ('Captain Marvel', 7.0) , ('Aladdin', 7.4) , ('Avengers: Endgame', 8.7)]
Вихідні дані:

[('Captain Marvel', 7.0), ('Aladdin', 7.4), ('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]
"""


def sort_movie(t):
    return sorted(t, key=lambda x: x[1])

movies = eval(input())

print(sort_movie(movies))

"""
10. Напишіть функцію для знаходження кількість повторень елементів у послідовності, які вводяться через кому в один
рядок, і виведіть список пар «елемент- кількість повторень» в порядку спадання кількості повторень як у вихідних даних.
Вхідні дані:

1,2,3,4,3,3,2,4,5,6,1,2,3,4,6,1,2,3,4,6,6
Вихідні дані:

[(3, 5), (2, 4), (4, 4), (6, 4), (1, 3), (5, 1)]
"""


def sort_line(s):
    data_list = [(int(i), s.count(i)) for i in set(s)]
    sort_list = sorted(data_list, key=lambda x: (x[1], 1 - x[0]), reverse=True)
    return sort_list


print(sort_line(input().split(",")))

