from datetime import datetime

def calcular_edad_exacta(fecha_nacimiento):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Calcular la diferencia entre la fecha actual y la fecha de nacimiento
    diferencia = fecha_actual - fecha_nacimiento

    # Extraer años, días y horas de la diferencia
    anios = diferencia.days // 365
    dias_restantes = diferencia.days % 365
    horas, _ = divmod(diferencia.seconds, 3600)

    return anios, dias_restantes, horas

# Ingresar la fecha de nacimiento como objeto datetime
fecha_nacimiento = datetime(1990, 1, 1)  # Reemplaza con tu fecha de nacimiento

# Calcular la edad exacta
anios, dias, horas = calcular_edad_exacta(fecha_nacimiento)

# Mostrar los resultados
print(f"Tienes {anios} años, {dias} días y {horas} horas de edad.")
