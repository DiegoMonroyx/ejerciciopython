def main():
    calificaciones = []

    # Pedir el nombre del usuario
    nombre_usuario = input("Ingrese su nombre: ")

    calificacion_str = input(f"{nombre_usuario}, ingrese una calificación (1 al 5) o 'fin' para terminar: ")

    while calificacion_str.lower() != 'fin':
        try:
            calificacion = int(calificacion_str)
            if 1 <= calificacion <= 5:
                calificaciones.append(calificacion)
            else:
                print("Por favor, ingrese una calificación válida en el rango de 1 al 5.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

        calificacion_str = input(f"{nombre_usuario}, ingrese una calificación (1 al 5) o 'fin' para terminar: ")

    if calificaciones:
        print(f"Calificaciones ingresadas por {nombre_usuario}: {calificaciones}")
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de calificaciones es : {promedio}")
    else:
        print(f"No se ingresaron calificaciones por {nombre_usuario}.")

