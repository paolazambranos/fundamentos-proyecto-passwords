def leer_archivo_passwords(nombre_archivo):
    print("Comenzamos a leer el archivo: ", nombre_archivo)
    archivo = open(nombre_archivo, "r")
    lineas = []
    
    for linea in archivo:
        linea = linea[:-1]
        lineas.append(linea)
   
    print("La cantidad de lineas son: ", len(lineas))
    archivo.close()
    return lineas

def calcular_puntaje_seguridad(clave, patterns):
    print("----")
    print("Comenzamos a calcular el puntaje de seguridad para la clave: ", clave)
    puntaje_final = 0
    tiene_minuscula = 0
    tiene_numero = 0
    tiene_mayuscula = 0
    puntaje_simbolos = 0
    contador_simbolos = 0 
    puntaje_patrones = 0
    cant_caracteres = len(clave)
    print("La cantidad de caracteres son:", cant_caracteres)

    for caracter in clave:
        if caracter.islower():
            tiene_minuscula = 1
            print("Si tiene minuscula: ", caracter)
            break 

    for caracter in clave:
        if caracter.isdigit():
            tiene_numero = 1
            print("Si tiene numero: ", caracter)
            break

    for caracter in clave:
        if caracter.isupper():
            tiene_mayuscula = 1
            print("Si tiene mayuscula: ", caracter)
            break

    for caracter in clave:
        es_simbolo = not caracter.isalnum()
        if es_simbolo:
            contador_simbolos = contador_simbolos + 1
            print("Si tiene simbolos: ", caracter)
            print("simbolo numero: ", contador_simbolos)
            if contador_simbolos == 1: 
                puntaje_simbolos = 3
            else: 
                puntaje_simbolos =  puntaje_simbolos + 2
    print("puntaje de simbolo total: ", puntaje_simbolos)
    
    for p in patterns:
        if p in clave:
            puntaje_patrones = puntaje_patrones + 5
            print(f"El patron '{p}' si esta contenido")
    print("puntaje de patrones en total: ", puntaje_patrones)

    puntaje_final = cant_caracteres + tiene_minuscula + tiene_numero + tiene_mayuscula + puntaje_simbolos - puntaje_patrones
    print("El puntaje para la contraseña es: ", puntaje_final)
    
    
    if puntaje_final <= 15:
            print("Pertenece a la categoria: debil")
            categoria = "debil"
    elif puntaje_final <= 20:
            print("Pertenece a la categoria: moderada")
            categoria = "moderada"
    elif puntaje_final <= 35:
        print("Pertenece a la categoria: buena")
        categoria = "buena"
    elif puntaje_final <= 100:
        print("Pertenece a la categoria: excelente") 
        categoria = "excelente"
    else: 
        print("Pertenece a la categoria: impenetrable")
        categoria = "impenetrable"

    print("----")
    print("")
    return [clave, categoria, puntaje_final]

    
def esribir_datos_archivo(matriz_de_informacion):
    archivo_write = open("datos_archivos.txt", "w")
    for fila in matriz_de_informacion:
        for i in range(len(fila)):
            dato = fila[i]
            archivo_write.write(str(dato))
            if i == 0 or i == 1:
                archivo_write.write(" | ") 
            else: 
                archivo_write.write("\n")
    archivo_write.close()

print ("Bienvenidos al proyecto de Paola Zambrano")
passwords = leer_archivo_passwords("passwords.txt")
patterns = leer_archivo_passwords("patterns.txt")

matriz_de_informacion = []
for clave in passwords: 
    informacion_de_clave = calcular_puntaje_seguridad(clave, patterns)
    matriz_de_informacion.append(informacion_de_clave)

# falta ordenar la matriz_de_informacion por: ???

esribir_datos_archivo (matriz_de_informacion)
print("El proyecto ha llegado a su fin y ha sido ejecutado con exito")
