alp = list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ")
phrase = list('ПМЯПРАГЛЛЩЗПГИОГРЛЩЗИЙЪХМРНОЮАЖРГЙЭКМДГРЯЩРШЖПНМЙШЕМАЮЛВЙЭЦЖТОМАИЖПММЯЧГЛЖЭ')
crypt = list('СОБСТВЕННЫЙСЕКРЕТНЫЙКЛЮЧОТПРАВИТЕЛЯМОЖЕТБЫТЬИСПОЛЬЗОВАНДЛЯШИФРОВКИСООБЩЕНИЯ')
filter = ["ГЪ","КЩ","ЩФ","ЩЗ","ЭЩ","ЩК","ГЩ","ЩП","ЩТ","ЩШ","ЩГ","ЩМ","ФЩ","ЩЛ","ЩД","ДЩ","ЧЦ","ВЙ","ЙА","ШЯ","ШЫ","ГЮ","ХЯ","ЙЫ","ЦЯ","ГЬ","СЙ","ХЮ","ЪЖ","ЪД","УЬ","ЩЧ","ЧЙ","ШЙ","ШЗ","ЫФ","ЖЩ","ЖШ","ЖЦ","ЫЪ","ЫЭ","ЫЮ","ЫЬ","ЖЙ","ЫЫ","ЖЪ","ЖЫ","ЪШ","ПЙ","ЪЩ","ЗЩ","ЪЧ","ЪЦ","ЪУ","ЪФ","ЪХ","ЪЪ","ЪЫ","ЫО","ЖЯ","ЗЙ","ЪЬ","ЪЭ","ЫА","НЙ","ЕЬ","ЦЙ","ЬЙ","ЬЛ","ЬР","ПЪ","ЕЫ","ЕЪ","ЬА","ШЪ","ЪТ","ЩС","ОЬ","КЪ","ОЫ","ЩХ","ЩЩ","ЩЪ","ЩЦ","КЙ","ОЪ","ЦЩ","ЛЪ","МЙ","ШЩ","ЦЬ","ЦЪ","ЩЙ","ЙЬ","ЪГ","ИЪ","ЪБ","ЪВ","ЪИ","ЪЙ","ЪП","ЪР","ЪС","ЪО","ЪН","ЪК","ЪЛ","ЪМ","ИЫ","ИЬ","ЙУ","ЩЭ","ЙЫ","ЙЪ","ЩЫ","ЩЮ","ЩЯ","ЪА","МЪ","ЙЙ","ЙЖ","ЬУ","ГЙ","ЭЪ","УЪ","АЬ","ЧЪ","ХЙ","ТЙ","ЧЩ","РЪ","ЮЪ","ФЪ","УЫ","АЪ","ЮЬ","АЫ","ЮЫ","ЭЬ","ЭЫ","БЙ","ЯЬ","ЬЫ","ЬЬ","ЬЪ","ЯЪ","ЯЫ","ХЩ","ДЙ","ФЙ"]

#-----------------------Шифрование-----------------------
k = 30 # Сдвиг

for i in range(len(crypt)):
    crypt[i] = alp[(alp.index(phrase[i])+k+2) % 32]
print("".join(crypt))

#-----------------------Дешифрование-----------------------

def stroka(tmp, ret = True):
    for j in range(len(filter)):
        if tmp.count(filter[j]) != 0:
            ret = False  
    return ret

for k in range(1,31):
    for i in range(len(phrase)):
        phrase[i] = alp[(alp.index(phrase[i])-k+2) % 32]
    tmp = "".join(phrase)
    if stroka(tmp):
        print(tmp)
