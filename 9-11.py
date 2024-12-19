import random


def big_sum(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a + int_mas_b
    mas_x = []
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    return mas_x[::-1]


def big_minus(mas_a, mas_b):
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
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate270(matrix):
    return [list(row) for row in list(zip(*matrix))[::-1]]    

def same_numbers(mas_a, mas_b):
    k = 0
    for i in range(len(mas_a)):
        a = abs(mas_a[i])
        for j in range(len(mas_b)):
            b = abs(mas_b[j])
            if a == b:
                k += 1
    return k   

def get_array(lenght):
    a = []
    for i in range(lenght):
        a.append(int(input()))
    return a   

def gen_array(lenght):
    a = []
    for i in range(lenght):
        a.append(random.randint(0, 10))
    return a      

def get_matrix(lenght, wight):
    a = []
    for i in range(lenght):
        b = []
        for j in range(wight):
            b.append(int(input()))
        a.append(b)
    return a   

def gen_matrix(lenght, wight):
    a = []
    for i in range(lenght):
        b = []
        for j in range(wight):
            b.append(random.randint(0, 9))
        a.append(b)
    return a     

def choice_mas():
    while True:
        print("Gen - случайно сгенерировать массив, Get - ввести массив вручную")
        ch = input()
        if ch == 'Get':
            print("Введите длину массива")
            lenght = int(input())
            return get_array(lenght)
        elif ch == 'Gen':
            print("Введите длину массива")
            lenght = int(input())
            return gen_array(lenght)
        else:
            print("Неверный выбор")

def choice_matrix():
    while True:
        print("Gen - случайно сгенерировать матрицу, Get - ввести матрицу вручную")
        ch = input()
        if ch == 'Get':
            print("Введите длину матрицы")
            lenght = int(input())
            print("Введите ширину матрицы")
            width = int(input())
            return get_matrix(lenght,width)
        elif ch == 'Gen':
            print("Введите длину матрицы")
            lenght = int(input())
            print("Введите ширину матрицы")
            width = int(input())
            return gen_matrix(lenght, width)
        else:
            print("Неверный выбор")  

def menu(point):
    if point == 1:
        mas_a = choice_mas()
        mas_b = choice_mas()
        print(same_numbers(mas_a, mas_b))
        return

    if point == 2:
        mat = choice_matrix()
        print("Повернуть матрицу направо (1) или налево (2)")
        x = int(input())
        if x == 1:
            print(rotate90(mat))
        elif x == 2:
            print(rotate270(mat))
        else:
            print("Ошибка")
        return

    elif point == 3:
        mas_a = choice_mas()
        mas_b = choice_mas()
        print("Сумма (1) или разность (2) массивов")
        x = int(input())
        if x == 1:
            print(big_sum(mas_a, mas_b))
        elif x== 2:
            print(big_minus(mas_a, mas_b))
        else:
            print("Ошибка")   
        return 

    elif point == 4:
        exit()

    else:
        print("Такого пункта нет!")          

if __name__ == "__main__":
    while True:
        print("Задачи \n 1. Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих чисел. Также, число будет считаться общим, если оно входит в один массив, а в другом массиве находится его перевернутая версия. \n 2. Входные данные: матрица N на M. Требуется повернуть матрицу на 90 градусов против часовой или по часовой. \n 3. Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов. \n 4. Закончить работу программы")
        print("Выберите пункт меню")
        menu(int(input()))