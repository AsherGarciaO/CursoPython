condicion1 = True
condicion2 = True

if condicion1 and condicion2:
    print("Hola la primera y segunda condiciones son verdaderas")
elif condicion1:
    print("Solo la primer condicion es verdadera")
elif condicion2:
    print("Solo la segunda condicion es verdadera")
else:
    print("Ninguna condicion es verdadera")

i = 0
while i <= 5:
    #print("Numero actual "+str(i))
    i += 1

lista = [1, 2, 3, 4, 5, 6, 7, 8]
print("")

for u in lista:
    if u == 5:
        continue
    print(u)