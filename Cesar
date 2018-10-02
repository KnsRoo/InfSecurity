alp = list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ")
phrase = list('ПМЯПРАГЛЛЩЗПГИОГРЛЩЗИЙЪХМРНОЮАЖРГЙЭКМДГРЯЩРШЖПНМЙШЕМАЮЛВЙЭЦЖТОМАИЖПММЯЧГЛЖЭ')

for k in range(1,31):
  for i in range(len(phrase)):
    phrase[i] = alp[(alp.index(phrase[i])-k) % 32]
  print(str(k)+" "+"".join(phrase))
