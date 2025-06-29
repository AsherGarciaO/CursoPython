if False:
    print("Hola")
    print("Mundo")

variable = 6

#Operadores relacionales == (igual), != (diferente), < (menor que), > (mayor que), <= (menor O igual que), >= (mayor O igual que)
if variable <= 6:
    print("Condición SI se cumplió")
else:
    print("Condición NO cumplida")

#Operadores lógicos and (y), or (o) y not (no)
boleano = False

if not boleano:
    print("Condición2 SI se cumplió")
else:
    print("Condición2 NO cumplida")

#Operadores aritméticos + (suma), - (resta), * (multiplicacion), / (division), // (división entera), % (modulo, resto), ** (potencia)
#print(str( 2 ** 4 ))

#Operadores de asignación += (mas igual), -= (menos igual), *= (por igual), /= (entre igual), // (entre entero igual | entre igual entero), %= (modulo igual, resto igual), **= (portencia igual), ++ (más más), -- (menos menos)
prueba = 5
#prueba = prueba + 10 === prueba += 10
#el operador de asignacion ++ aumenta en UNA unidad el valor de la variable en cuestion (NO disponible para python)
#el operador de asignacion -- disminuye en UNA unidad el valor de la variable en cuestion (NO disponible para python)
prueba += 1
print(prueba)