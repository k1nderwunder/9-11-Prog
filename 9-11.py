import random


def big_sum(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a + int_mas_b
    mas_x = []
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    return mas_x


def big_minus(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    z = int_mas_a - int_mas_b
    mas_x = []
    while z > 0:
        mas_x.append(z % 10)
        z //= 10
    mas_x.reverse()
    return mas_x

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
        return gen_matrix(lenght,width)
    else:
        print("Неверный выбор")    

if __name__ == "__main__":
    print(choice_mas())
    print(choice_matrix())