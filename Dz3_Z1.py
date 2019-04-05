def info (name, age, city):
    result = '{}, {} год(а), проживанет в городе {}'.format(name, age, city)
    return result

name = input('Сообщите ваше имя: ')
age = input('Сколько вам лет? ')
city = input('В каком городе вы проживаете? ')

result = info(name, age, city)
print(result)