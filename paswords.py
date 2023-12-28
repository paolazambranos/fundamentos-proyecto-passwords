def leer_archivo_passwords(nombre_archivo):
    print("Comenzamos a leer el archivo: ", nombre_archivo)
    archivo = open(nombre_archivo, "r")
    lineas = []
    
    for linea in archivo:
        lineas.append(linea)
   
    print("La cantidad de lineas son: ", len(lineas))
    return lineas


print ("Bienvenidos al proyecto de Paola Zambrano")
passwords = leer_archivo_passwords("passwords.txt")
patterns = leer_archivo_passwords("patterns.txt")
print("El proyecto ha llegado a su fin y ha sido ejecutado con exito")
