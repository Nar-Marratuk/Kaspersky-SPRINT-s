with open('code.txt', encoding = 'utf-8') as f:
    text = f.readline()
    sp = []
    '''Названия переменных - мрак. Ничего не понятно.'''
    '''Не стоит эту переменную создавать отдельно. 
    Её значения используются только один раз, а всё оставшиеся время работы программы просто висят в памяти 
    и нечего не делают.'''
    raz = [text.find('('), text.find(')')]
    text = text[raz[0]+1:raz[1]]
    sl = text.split(',')
    #a =text[:text.find('=')].lstrip()
    for text in f.readlines():
        if '+=' in text or '==' in text or '-=' in text or '*=' in text or '/=' in text or '**=' in text:
            continue
        elif '=[' in text:
            '''Не учитываются пробелы, а это критично, потому что хоть в примере их нет, но обычно их всегда ставят.'''
            sp.append(text[:text.find('=')].lstrip())
        elif '=' in text:
            sl.append(text[:text.find('=')].lstrip())

'''Файл открывается 2 раза. Очень плохо...'''
with open('code.txt', encoding = 'utf-8') as f:
    text = f.read()
sp = list(set(sp))
sl = list(set(sl))
'''Также как и выше, не стоит создавать такие переменные, легче просто подставить их значения в range.'''
lsp = len(sp)
lsl = len(sl)
#gg = 'R'+str(i+1)
#bg = 'a'+str(i+1)
for i in range(lsp):
    text = text.replace(sp[i], 'R'+str(i+1))
for i in range(lsl):
    text = text.replace(sl[i], 'a'+str(i+1))
print(text)

'''Итог:
    Код не универсальный - будет работать только с конкретным примером.
    Быстродействие и память страдают. Код можно сильно ускорить и облегчить.
    Читабельность из-за названий переменных и общего алгоритма (много лишних действий) тоже на низком уровне.
    Стоит лучше подходить к планированию кода.'''