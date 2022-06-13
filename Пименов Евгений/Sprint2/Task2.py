with open('testExe.exe', 'rb') as f:
    symbols = f.read(2)
'''Вариант хороший, однако, для читаемости кода можно заменить * 2 ** 8 на битовый сдвиг влево на те же 8.'''
if hex(symbols[0] * 2 ** 8 + symbols[1])[2:] == '4d5a':
    '''Лучше расчитать значение hex(symbols[0] * 2 ** 8 + symbols[1])[2:] за пределами if, а то получается,
    что значение расчитывается 2 раза, проигрываем по времени работы в 2 раза.'''
    print(f'{hex(symbols[0] * 2 ** 8 + symbols[1])[2:]} {symbols.decode("utf-8")} - executable, OS Windows')
else:
    print(f'{hex(symbols[0] * 2 ** 8 + symbols[1])[2:]} {symbols.decode("utf-8")}- non-executable')