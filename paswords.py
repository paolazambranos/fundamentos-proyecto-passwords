def leer_archivo():
    archivo_passwords = open("passwords.txt", "r")
    for linea in archivo_passwords:
        print(linea)

print ("Bienvenidos al proyecto de Paola Zambrano")
leer_archivo()
print("El proyecto ha llegado a su fin y ha sido ejecutado con exito")
