dicionario = {"Alo":1, "AloAlo":1, "aaaaa":2, "arroz":4, "arroz batata":4, "nao e para sair":7, "também fica":10, "Alo":1, "Aconteceu de ficar":50, "arroz ba":4 }

## SOLUÇÃO 1
'''
for chaves, valores in dicionario.items():
    for keys, values in copia1.items():
        if valores in values:
            if chaves != keys:
                dicionario[chaves] = "apagar"

print(dicionario)
'''
"""
## SOLUÇÃO FUNCIONAL
for chaves, valores in dicionario.items():
    print("Primeiro For: Chaves ", chaves)
    print("Primeiro For: Valores ", str(valores))
    print("_____________________")

    for keys, values in dicionario.items():
        print("Segundo for: Chaves", chaves)
        print("Segundo for: Valores", valores)
        print("_____________________")

        if chaves != keys:
            print("Se Chaves: " + chaves + " em Keys: " + keys )
            if valores == values:
                print("Se Valores: " + str(valores) + " em values: " + str(values))
                dicionario[chaves] = "apagar"
                print(dicionario[chaves])
                print("_____________________")

copia1 = {}
for chaves, valores in dicionario.items():
    if valores != "apagar":
        copia1[chaves] = valores

print(dicionario)
print("__________________")
print(copia1)

"""


"""
for chaves, valores in copia3.items():
    print("Chaves primeiro for:  ", str(chaves))
    print("Valores primeiro for: ", valores)
    print("__________")
    for keys, values in copia1.items():
        print("Key segundo for: ", str(keys))
        print("Values segundo for: ", values)
        print("__________")

        if valores in values:
            print("entrei no elif")
            copia1[chaves] = "apagar"
            print("__________")
            break

print(copia3)
print(copia1)
"""


"""
for valores in copia1.values():
    print("Valores primeiro for: ", valores)
    if valores == copia3.values():
        print("Valor pesquisado ===  ")
        print(copia3)

print(copia3)
"""

"""
for chaves, valores in dicionario.items():
    print("Primeiro For: Chaves ", chaves)
    print("Primeiro For: Valores ", str(valores))
    print("_____________________")

    for keys, values in dicionario.items():
        print("Segundo for: Chaves", chaves)
        print("Segundo for: Valores", valores)
        print("_____________________")

        if chaves != keys:
            print("Se Chaves: " + chaves + " em Keys: " + keys )
            if valores == values:
                if chaves < keys:
                    print("Se Valores: " + str(valores) + " em values: " + str(values))
                    dicionario[chaves] = "apagar"
                    print(dicionario[chaves])
                    print("_____________________")
                else:
                    print("Se Valores: " + str(valores) + " em values: " + str(values))
                    dicionario[keys] = "apagar"
                    print(dicionario[chaves])
                    print("_____________________")                   

copia1 = {}
for chaves, valores in dicionario.items():
    if valores != "apagar":
        copia1[chaves] = valores

print(dicionario)
print("__________________")
print(copia1)
"""

for chaves, valores in dicionario.items():
    for keys, values in dicionario.items():
        if chaves != keys and valores == values:
            if chaves < keys:
                dicionario[chaves] = "apagar"
            else:
                dicionario[keys] = "apagar"

copia1 = {}
for chaves, valores in dicionario.items():
    if valores != "apagar":
        copia1[chaves] = valores

print(dicionario)
print("__________________")
print(copia1)