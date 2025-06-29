nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if(edad < 18):
    print(nombre+" le faltan "+str(18-edad)+" años para cumplir su mayoría de edad")
else:
    print(nombre+" YA es mayor de edad")