def big_sum(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a + int_mas_b
    mas_x = []
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    return mas_x

if __name__ == "__main__":
    x = [2, 3, 4]
    y = [4, 3, 2]
    print(big_sum(x,y))
    print(432 + 234)