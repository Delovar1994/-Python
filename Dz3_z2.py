def max_num(a, b, c):
    num_list = [a,b,c]
    max_n = (max(num_list))
    return max_n
num_1 = int (input('Первое число: '))
num_2 = int (input('Второе число: '))
num_3 = int (input('Третье число: '))
result = max_num(num_1, num_2, num_3)
print('Максимальное число из введеных вами: {}'.format(result))