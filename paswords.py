def leer_archivo_passwords():
    print("Comenzamos a leer el archivo de contraseñas")
    archivo_passwords = open("passwords.txt", "r")
    passwords = []
    
    for linea in archivo_passwords:
        passwords.append(linea)

    print("arreglo de contraseñas: ", passwords)


print ("Bienvenidos al proyecto de Paola Zambrano")
leer_archivo_passwords()
print("El proyecto ha llegado a su fin y ha sido ejecutado con exito")
