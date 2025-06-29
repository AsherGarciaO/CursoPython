tipo = input("¿Qué tipo de dato vas a ingresar? (binario o decimal): ").strip().lower()

if tipo == "decimal":
    decimal = input("Ingresa un número decimal: ").strip()
    
    if not decimal.isdigit():
        print("No es un número decimal válido")
    else:
        decimal = int(decimal)
        if decimal == 0:
            print("Binario: 0")
        else:
            binario = ""
            while decimal > 0:
                residuo = decimal % 2
                binario += str(residuo)
                decimal //= 2
            print(f"Binario: {binario}")

elif tipo == "binario":
    binario = input("Ingresa un número binario: ").strip()

    bandera = True
    for character in binario:
        if character != '0' or character != '1':
            bandera = False
            break

    if bandera:
        print("No es un número binario válido")
    else:
        decimal = 0
        potencia = 0
        for digito in reversed(binario):
            decimal += int(digito) * (2 ** potencia)
            potencia += 1
        print(f"Decimal: {decimal}")

else:
    print("Tipo no reconocido. Escribe 'binario' o 'decimal'")