#Comprhension list
digitos = [x**2 for x in range(0, 25, 2) if x < 10]
print(digitos)

if 0:
    abecedario = ("a", "b", "c", "d", "e", "f")
    abc = [c for (i, c) in enumerate(abecedario) if not i % 2]
    print(abc)

#Generadores
generador = (d for d in digitos if not d % 3)
for num in generador:
    print(num)