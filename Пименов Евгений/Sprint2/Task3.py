import re
with open('Code.txt', 'r') as f:
    func = f.read()
if func == '':
    print('Закиньте вашу функцию в Code.txt')
    exit()
vars = []
lists = []
'''Регулярки отличные, однако их можно упростить (\w хранит в себе a-zA-Z0-9_ поэтому \d не нужен,
как и вообще второй класс \w\d).'''
vars.append(re.findall(r'[\w][\w\d]+(?=\s*[\,\)])', func[:func.index(':')]))  # аргументы на вход
'''Код можно немного реорганизовать, чтобы не включать переменные-списки в общий массив vars, 
для этого придется разделить for в конце на 2 отдельных, однако количество итераций от этого не увеличится.
От этого код станет более читабельным и логически структурированным, 
а в массиве vars не будут хранится повторные значения, следовательно, выйграем по памяти.'''
vars.append(re.findall(r'[\w][\w\d]+(?=\s*\=)', func))  # создаваемые переменные
lists.append(re.findall(r'[\w][\w\d]+(?=\s*\=\[)', func))  # создаваемые списки
count_var = 1
count_list = 1
for i in vars:
    for var in i:
        if var not in str(lists):
            func = str(func).replace(str(var), 'a' + str(count_var))
            count_var += 1
        else:
            func = str(func).replace(str(var), 'R' + str(count_list))
            count_list += 1
print(func)

'''Итог:
    Отличный код. Стоит посмотреть в сторону оптимизации и читабельности.
    А также, стоит разделять код на функции - это хороший тон.'''
