import random
import threading

def big_sum(mas_a, mas_b):
    """
    Функция вычисляет сумму двух больших чисел, представленных в виде массивов цифр.

    :param mas_a: Массив цифр, представляющий первое большое число.
    :param mas_b: Массив цифр, представляющий второе большое число.
    :return: Массив цифр, представляющий сумму двух больших чисел.
    """
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a + int_mas_b
    mas_x = []
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    return mas_x[::-1]

def big_minus(mas_a, mas_b):
    """
    Функция вычисляет разность двух больших чисел, представленных в виде массивов цифр.

    :param mas_a: Массив цифр, представляющий первое большое число.
    :param mas_b: Массив цифр, представляющий второе большое число.
    :return: Массив цифр, представляющий разность двух больших чисел.
    """
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    z = int_mas_a - int_mas_b
    mas_x = []
    if z < 0:
        z = -z
        mas_x.append(-1)
    while z > 0:
        mas_x.append(z % 10)
        z //= 10
    mas_x.reverse()
    return mas_x[::-1]

def rotate90(matrix):
    """
    Функция поворачивает матрицу на 90 градусов по часовой стрелке.

    :param matrix: Исходная матрица.
    :return: Матрица, повернутая на 90 градусов по часовой стрелке.
    """
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate270(matrix):
    """
    Функция поворачивает матрицу на 90 градусов против часовой стрелки.

    :param matrix: Исходная матрица.
    :return: Матрица, повернутая на 90 градусов против часовой стрелки.
    """
    return [list(row) for row in list(zip(*matrix))[::-1]]

def same_numbers(mas_a, mas_b):
    """
    Функция проверяет, сколько у двух массивов общих чисел, включая перевернутые версии чисел.

    :param mas_a: Первый массив чисел.
    :param mas_b: Второй массив чисел.
    :return: Количество общих чисел в двух массивах.
    """
    k = 0
    for i in range(len(mas_a)):
        a = abs(mas_a[i])
        for j in range(len(mas_b)):
            b = abs(mas_b[j])
            if a == b:
                k += 1
    return k

def get_array(length):
    """
    Функция запрашивает у пользователя ввод массива заданной длины.

    :param length: Длина массива.
    :return: Массив, введенный пользователем.
    """
    a = []
    for i in range(length):
        a.append(int(input()))
    return a

def gen_array(length):
    """
    Функция генерирует массив случайных чисел заданной длины.

    :param length: Длина массива.
    :return: Массив случайных чисел.
    """
    a = []
    for i in range(length):
        a.append(random.randint(0, 10))
    return a

def get_matrix(length, width):
    """
    Функция запрашивает у пользователя ввод матрицы заданных размеров.

    :param length: Количество строк матрицы.
    :param width: Количество столбцов матрицы.
    :return: Матрица, введенная пользователем.
    """
    a = []
    for i in range(length):
        b = []
        for j in range(width):
            b.append(int(input()))
        a.append(b)
    return a

def gen_matrix(length, width):
    """
    Функция генерирует матрицу случайных чисел заданных размеров.

    :param length: Количество строк матрицы.
    :param width: Количество столбцов матрицы.
    :return: Матрица случайных чисел.
    """
    a = []
    for i in range(length):
        b = []
        for j in range(width):
            b.append(random.randint(0, 9))
        a.append(b)
    return a

def choice_mas():
    """
    Функция запрашивает у пользователя выбор способа создания массива (ввод вручную или генерация случайных чисел).

    :return: Массив, созданный выбранным способом.
    """
    while True:
        print("Gen - случайно сгенерировать массив, Get - ввести массив вручную")
        ch = input()
        if ch == 'Get':
            print("Введите длину массива")
            length = int(input())
            return get_array(length)
        elif ch == 'Gen':
            print("Введите длину массива")
            length = int(input())
            return gen_array(length)
        else:
            print("Неверный выбор")

def choice_matrix():
    """
    Функция запрашивает у пользователя выбор способа создания матрицы (ввод вручную или генерация случайных чисел).

    :return: Матрица, созданная выбранным способом.
    """
    while True:
        print("Gen - случайно сгенерировать матрицу, Get - ввести матрицу вручную")
        ch = input()
        if ch == 'Get':
            print("Введите длину матрицы")
            length = int(input())
            print("Введите ширину матрицы")
            width = int(input())
            return get_matrix(length, width)
        elif ch == 'Gen':
            print("Введите длину матрицы")
            length = int(input())
            print("Введите ширину матрицы")
            width = int(input())
            return gen_matrix(length, width)
        else:
            print("Неверный выбор")

def menu():
    """
    Функция обрабатывает выбор пункта меню и выполняет соответствующие действия.
    """
    while True:
        print("Задачи \n 1. Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих чисел. Также, число будет считаться общим, если оно входит в один массив, а в другом массиве находится его перевернутая версия. \n 2. Входные данные: матрица N на M. Требуется повернуть матрицу на 90 градусов против часовой или по часовой. \n 3. Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов. \n 4. Закончить работу программы")
        print("Выберите пункт меню")
        point = int(input())

        if point == 1:
            thread = threading.Thread(target=task_same_numbers)
        elif point == 2:
            thread = threading.Thread(target=task_rotate_matrix)
        elif point == 3:
            thread = threading.Thread(target=task_big_operations)
        elif point == 4:
            exit()
        else:
            print("Такого пункта нет!")
            continue

        thread.start()
        thread.join()

def task_same_numbers():
    mas_a = choice_mas()
    mas_b = choice_mas()
    print(same_numbers(mas_a, mas_b))

def task_rotate_matrix():
    mat = choice_matrix()
    print("Повернуть матрицу направо (1) или налево (2)")
    x = int(input())
    if x == 1:
        print(rotate90(mat))
    elif x == 2:
        print(rotate270(mat))
    else:
        print("Ошибка")

def task_big_operations():
    mas_a = choice_mas()
    mas_b = choice_mas()
    print("Сумма (1) или разность (2) массивов")
    x = int(input())
    if x == 1:
        print(big_sum(mas_a, mas_b))
    elif x == 2:
        print(big_minus(mas_a, mas_b))
    else:
        print("Такого пункта нет!")

if __name__ == "__main__":
    menu_thread = threading.Thread(target=menu)
    menu_thread.start()
    menu_thread.join()
