lista = [5, 9.5, "Asher", True, 'p']
tupla = (1, 5, 0)
diccionario = {"nombreDeLaPersona":"Asher", "edad":19, "profesor":True}
tipo4 = {1, 2, 2, 3, 4, 8, 2, 3, 5, 6}

#Tipo de Dato de Lista
#Funciones para la lista


#lista2 = lista.copy()
#lista = lista+[4]
#lista.append("garcía")
#lista.extend([1, 33, 6])
#lista.insert(0, "Hola Mundo")

#lista.pop()
#lista.pop(2)
#lista.remove("Asher")
#del lista[0]
#lista.clear()

#print("Datos de la Lista: "+str(type(lista))+":")
#print(lista2)


#Tipo de Dato de Tupla
#Funciones para la tupla


print("\n\nDatos de la Tupla: "+str(type(tupla))+":")

print(any(tupla))
print(all(tupla))
print(len(tupla))
print(tupla[1:2])

print(sum(tupla))
print(tupla)


#Tipo de Dato de Diccionario
#Funciones para el diccionario
print("\n\nDatos del Diccionario: "+str(type(diccionario))+":")


print(any(diccionario))
print(all(diccionario))
print(len(diccionario))
diccionario["modulo"] = 3
print(max(diccionario))
print(min(diccionario))
print(diccionario)
#for item in diccionario: 
#print(str(item)+": "+str(diccionario[item])+": "+str(type(diccionario[item])))
#print(diccionario)


#Tipo de Dato de Set
#Funciones para el set

print("\n\nDatos del Set: "+str(type(tipo4))+":")

print(any(tipo4))
print(all(tipo4))
print(len(tipo4))
print(max(tipo4))
print(min(tipo4))

tipo5 = tipo4.union({1, 8, 9, 0})
print(tipo4)
print(tipo5)