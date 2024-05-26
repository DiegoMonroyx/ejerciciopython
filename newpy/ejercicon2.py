print("Programa que muestra el promedio de tres notas")

nombre = input("Porfavor Dijite su nombre: ")
matematicas = float(input( nombre + ", Porfavor su nota de matematicas: "))
ciencias = float(input(nombre + ", Porfavor ingrese su nota de ciencias: "))
biologia  = float(input(nombre + ", Porfavor ingrese su nota de ciencias: "))

resultado = (matematicas + ciencias + biologia) / 3
if resultado >= 6 :
    print( nombre + ", felicitaciones aprobaste tu promedio es de: ", resultado)
    print( nombre + ", felicitaciones aprobaste tu promedio es de: ", round(resultado, 2))
else:
    print( nombre + ", Lo sentimos resprobaste tu promedio es de : ", resultado)
    print( nombre + ", Lo sentimos resprobaste tu promedio es de : ", round(resultado))

print ("fin ")