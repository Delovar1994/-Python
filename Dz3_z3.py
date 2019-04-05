def len_max(*args):
    max_len = max(args, key = len)
    return max_len
args_1 = input('Ввод строки: ')
args_2 = input('Ввод строки: ')
args_3 = input('Ввод строки: ')
args_4 = input('Ввод строки: ')
result = len_max(args_1, args_2)
print('Самой длинной строкой является: : {}'.format(result))