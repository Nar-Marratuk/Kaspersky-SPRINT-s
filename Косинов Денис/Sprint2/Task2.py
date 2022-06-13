a = input()
with open(a, 'rb') as f:
    '''Избыточное чтение файла.
    Здесь читается весь файл, а потом вырезаются первые 2 байта, 
    однако можно просто считать из файла 2 байта.'''
    text = f.read()[:2]
    if text == b'MZ':
        '''Вывод не корректный. Требуется вывести первые 2 байта файла, а тут всегда выводится MZ, 
        вне зависимости от файла'''
        print("4D5A"+" "+"MZ"+" "+'executable, OS Windows')
    else:
        print("4D5A"+" "+"MZ"+" "+'non-executable')