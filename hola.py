def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0  # Si no hay calificaciones, el promedio es 0

    total_calificaciones = sum(calificaciones)
    promedio = total_calificaciones / len(calificaciones)
    return promedio

def main():
    calificaciones = []

    calificacion_str = input("Ingrese una calificación (1 al 5) o 'fin' para terminar: ")

    while calificacion_str.lower() != 'fin':
        try:
            calificacion = int(calificacion_str)
            if 1 <= calificacion <= 5:
                calificaciones.append(calificacion)
            else:
                print("Por favor, ingrese una calificación válida en el rango de 1 al 5.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

        calificacion_str = input("Ingrese una calificación (1 al 5) o 'fin' para terminar: ")

    if calificaciones:
        print("Calificaciones ingresadas:", calificaciones)
        promedio = calcular_promedio(calificaciones)
        print(f"El promedio de calificaciones es: {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones.")

if __name__ == "__main__":
    main()
