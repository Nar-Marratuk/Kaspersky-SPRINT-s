import time
'''В принципе, задумка с классом неплохая, однако можно было продумать структуру лучше,
например, добавить поля родителя и массива из n детей, тогда можно было бы просто проходится
по всему древу не создавая массивов.'''
class virys():
    def __init__(self):
        self.status = False
        self.timer = 0

n = int(input())
k = int(input())
files = [virys()]

for hours in range(n):
    for v in files:
        if v.status:
            '''Если мы не создаем массив, а просто проходимся выполняем дейсвия k раз, то такая запись не очень подойдет.
            Лучше будет 2 строчки, но логическая структура кода будет явснее.'''
            [files.append(virys()) for i in range(k)]
        elif not v.status and v.timer == 1:
            v.status = True
        v.timer += 1
print(len(files))

'''В целом алгоритм понятный и рабочий, однако, достаточно тяжелый. Эту задачу можно было решить горадо проще, 
одним циклом for, а данным метод хоть и работает, но тратится большое количество времени на создание объектов, следовательно,
быстродействие страдает.
За использование класса (пусть и элементарного) лайк. Алгоритм можно было продумать лучше.
Явных косяков не наблюдаю.'''
