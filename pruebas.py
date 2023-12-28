print("------------ inicio ")

cantidad = 0
tiene_minuscula = 0
puntaje_final = 0

clave = "12345678ab"
cantidad = len(clave)

for caracter in clave:
    if caracter.islower():
        tiene_minuscula = 1
        print(caracter)
        break


puntaje_final = cantidad + tiene_minuscula

print(puntaje_final)




print("------------ fin ")