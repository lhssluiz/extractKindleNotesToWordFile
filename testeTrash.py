
import numbers
from unicodedata import numeric
import operator

lista = ["1","2","3","4","#","5","6","7","-","8","9"]
casas = 0

testeDicionario = {'Primeiro':150, 'Terceiro':99, 'Segundo': 50, 'Quarto':4, 'Sexto':6, 'Segundo2': 2, 'Quinto':5, 'Primeiro1':1}
dictPositionNotes = dict(sorted(testeDicionario.items(), key=operator.itemgetter(1)))

print(dictPositionNotes)

