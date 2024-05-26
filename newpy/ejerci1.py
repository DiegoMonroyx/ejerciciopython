
print("Programa para sacar el Promedio de  notas.")

nombre_usuario = input("para comenzar, ""¡Cual es su nombre?: ")
Num_mat = int(input(nombre_usuario + ", Cual es su nota de matematica?: "))
Num_esp = int(input(nombre_usuario + ", Cual es su nota de Español?: "))
Num_bio = int(input(nombre_usuario + ", Cual es tu nota de Biologia: "))

resultado1 = (Num_mat + Num_esp + Num_bio) / 3
if resultado1 >= 5:
    print("Probate por ensima de 5: ", resultado1)
else:
    print(nombre_usuario + " Reprobaste")