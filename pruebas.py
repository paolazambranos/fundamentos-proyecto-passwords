print("------------ inicio ")

clave = "12adminPaola"
patterns = ["admin" , "123", "Paola", "22"]
print(patterns)
puntaje_patrones = 0 
for i in range(len(patterns)):
    p = patterns[i]
    print(p)
    if p in clave:
        puntaje_patrones = puntaje_patrones + 5
        print("Esta contenido")
    else:
        print("No esta contenido")
print("Puntaje de patrones es: ", puntaje_patrones)
    

print("--")

for p in patterns:
    print(p)

print("------------ fin ")