frutas = ["manzana","platano","uva"]
primer_elemento = frutas[0]
print(primer_elemento)
#ACTUALIZAR
frutas[1] = "pera"
#AGREGAR VALORES
frutas.append("sandia")
frutas.insert(2,"mango")
frutas.extend(["melon","fresa","kiwi"])

#ELIMINAR
retirado=frutas.pop(2)
#Elimina el ultimo elemento
ultimo=frutas.pop()
#elimina elemento en su primera aparicion
frutas.remove("uva")
#borrar casilla directamente
del frutas[0]

#BUSQUEDA
if "sandia" in frutas:
    pos = frutas.index("sandia")
    print(f"La sandia está en la casilla {pos}")
    print(frutas)

