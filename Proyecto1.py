#Hecho por: Paola V. Zambrano S
# CI: 31808227


#Cree una funcion donde nos lea los archivos passwords y patters
def leer_archivo_passwords(nombre_archivo):
    print("Comenzamos a leer el archivo: ", nombre_archivo)
    #Abri el archivo 
    archivo = open(nombre_archivo, "r")
    #Cree una lista llamado lineas donde nos guarde en un arreglo todas las claves
    lineas = []
    #Cree un for donde nos va a elimnar el espacio en blanco al final de cada clave y agrega la clave a la lista de lineas
    for linea in archivo:
        linea = linea[:-1]
        lineas.append(linea)
    #Imprimi a longitud de la lista lineas 
    print("La cantidad de lineas son: ", len(lineas))
    #Cerre el archivo y le pedimos que nos retorne el arreglo de lista
    archivo.close()
    return lineas


#Cree una nueva funcion que nos calcule el puntaje de seguridad de cada clave
def calcular_puntaje_seguridad(clave, patterns):
    print("----")
    print("Comenzamos a calcular el puntaje de seguridad para la clave: ", clave)
    #Asigne valores a las variables
    puntaje_final = 0
    tiene_minuscula = 0
    tiene_numero = 0
    tiene_mayuscula = 0
    puntaje_simbolos = 0
    contador_simbolos = 0 
    puntaje_patrones = 0
    #Imprimi la longitud de cada clave
    cant_caracteres = len(clave)
    print("La cantidad de caracteres son:", cant_caracteres)
    #Cree un for donde nos chequee si la clave contiene minusculas
    for caracter in clave:
        if caracter.islower():
            tiene_minuscula = 1
            print("Si tiene minuscula: ", caracter)
            break 
    #Cree un for donde nos chequee si la clave contiene numeros
    for caracter in clave:
        if caracter.isdigit():
            tiene_numero = 1
            print("Si tiene numero: ", caracter)
            break
    #Cree un for donde nos chequee si la clave contiene mayusculas
    for caracter in clave:
        if caracter.isupper():
            tiene_mayuscula = 1
            print("Si tiene mayuscula: ", caracter)
            break
    #Cree un for donde nos chequee si la clave contiene simbolos 
    for caracter in clave:
        es_simbolo = not caracter.isalnum()
        if es_simbolo:
            contador_simbolos = contador_simbolos + 1
            print("Si tiene simbolos: ", caracter)
            print("simbolo numero: ", contador_simbolos)    
            #Si la clave contiene un primer simbolo se le suman +3 puntos 
            if contador_simbolos == 1: 
                puntaje_simbolos = 3
            #Si la clave contiene mas de un simbolo; por cada simbolo adicional se le sumara +2 puntos al puntaje final 
            else: 
                puntaje_simbolos =  puntaje_simbolos + 2
    print("puntaje de simbolo total: ", puntaje_simbolos)

    #Si la clave contiene patrones obvios; por cada patron obvio se le restaran 5 puntos al puntaje final
    for p in patterns:
        if p in clave:
            puntaje_patrones = puntaje_patrones + 5
            print(f"El patron '{p}' si esta contenido")
    print("puntaje de patrones en total: ", puntaje_patrones)
    #Operacion sobre el puntaje de seguridad de cada clave
    puntaje_final = cant_caracteres + tiene_minuscula + tiene_numero + tiene_mayuscula + puntaje_simbolos - puntaje_patrones
    print("El puntaje para la contraseña es: ", puntaje_final)

    #Dependiendo del valor del puntaje final, el programa debera clasificar cada clave en una categoria
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

#Cree una funcion donde nos cree un nuevo archivo donde se guardara cada clave con su puntaje de seguridad y su categoria seleccionada
def esribir_datos_archivo(matriz_de_informacion):
    archivo_write = open("datos_archivos.txt", "w")
    for fila in matriz_de_informacion:
        for i in range(len(fila)):
            dato = fila[i]
            archivo_write.write(str(dato))
            #Inserte el simbolo " | " para que nos separe la clave, categoria y puntaje final y nos inserte un salto en linea al final
            if i == 0 or i == 1:
                archivo_write.write(" | ") 
            else: 
                archivo_write.write("\n")
    #Cerre el archivo
    archivo_write.close()


#Cree una funcion donde nos ordene las claves 
def ordenamiento(matriz_de_informacion):
    #Use el metodo ordenamiento de burbuja (mayor a menor)
    for i in range(len(matriz_de_informacion)):
        for j in range(len(matriz_de_informacion) - 1 - i):
            if matriz_de_informacion[j][2] < matriz_de_informacion[j + 1][2]:
                aux = matriz_de_informacion[j]
                matriz_de_informacion[j] = matriz_de_informacion[j + 1]
                matriz_de_informacion[j + 1] = aux
    return matriz_de_informacion


#Imprimi una bienvenida al proyecto 
print ("Bienvenidos al proyecto de Paola Zambrano")
passwords = leer_archivo_passwords("Contraseñas - Proyecto (Fundamentos de Programación SEM202415).txt")
patterns = leer_archivo_passwords("Patrones obvios de contraseña - Proyecto (Fundamentos de Programación SEM202415).txt")
#Creamos una lista que contendra la informacion de las claves
matriz_de_informacion = []
#Cree un for que recorre la lista de clave
for clave in passwords: 
    #Por cada clave calcula el puntaje de seguridad
    informacion_de_clave = calcular_puntaje_seguridad(clave, patterns)
    #Agrega la informacion de cada clave a la matriz de informacion
    matriz_de_informacion.append(informacion_de_clave)

#Hacemos llamada a la funcion de ordenamiento
matriz_de_informacion = ordenamiento(matriz_de_informacion)
#Llama a la funcion que escribe en el archivo la matriz de informacion ya ordenada
esribir_datos_archivo (matriz_de_informacion)
#Culminacion del proyecto
print("El proyecto ha llegado a su fin y ha sido ejecutado con exito")
