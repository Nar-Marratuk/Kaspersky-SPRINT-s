alph = 'qwertyuiopasdfghjklzxcvbnm_{}1234567890'
text = list('yourflagis{fhke37_kdrjknbmpr_04374j}')
gamma = 'thekey'
for count, i in enumerate(text, start=0):
    text[count] = alph[(alph.index(i) + alph.index(gamma[count % len(gamma)]) + 2) % len(alph)]
print(*text, sep='')

'''Отличный код, в целом даже не прикопаться. Однако все таки можно было это организовать как функцию с вызовом из main.
(но это вообще не обязательно). 
Итог:
    Совет на будущее - всегда писать всё в функциях или классах. В целом, часто в этом вооооооообще нету смысла, 
    однако это просто полезная привычка, которые показывает что ты более опытный программист.
    
Награда за труды и неплохой код:  https://clck.ru/3vyXS. '''