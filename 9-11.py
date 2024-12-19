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

if __name__ == "__main__":
    x = [2, 3, 4]
    y = [5, 4, 3]
    print(same_numbers(x,y))