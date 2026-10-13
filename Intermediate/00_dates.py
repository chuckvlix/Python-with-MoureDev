## Dates ##

# Importa los módulos 'datetime', 'time', 'date' y 'timedelta'
from datetime import datetime, time, date, timedelta

# Función para imprimir año, mes, día, hora, minuto y segundo
def print_date(date):
    print(date.year) # -> Imprime el año (ej. 2026 o 2025)
    print(date.month) # -> Imprime el mes (1-12)
    print(date.day) # -> Imprime el día (1-31)
    print(date.hour) # -> Imprime la hora (0-23)
    print(date.minute) # -> Imprime los minutos (0-59)
    print(date.second) # -> Imprime los segundos (0-59)
    print(date.timestamp()) # -> Imprime timestamp en segundos desde el Epoch
# Nota: 'timestamp' es el tiempo en segundos que han transcurrido desde las 0 hrs del 01-enero-1970

# 'datetime' permite obtener: fecha y hora actual, manipular fechas, calcular diferencias de tiempo, formatear fechas, etc.
now = datetime.now()
print_date(now) # -> Muestra componentes de la fecha y hora actuales

year_2025 = datetime(2025, 7, 24)
print_date(year_2025) # -> 2025, 7, 24, 0, 0, 0, 1753329600.0

# 'time' maneja el tiempo en segundos desde el Epoch (1970) y proporciona funciones para pausar la ejecución o medir el tiempo transcurrido.
current_time = time(13, 50, 35)
print(current_time.hour) # -> 13
print(current_time.minute) # -> 50
print(current_time.second) # -> 35

# 'date' solo maneja fechas sin información de la hora.
current_date = date.today()
print(current_date.year) # -> Año actual (ej. 2026)
print(current_date.month) # -> Mes actual
print(current_date.day) # -> Día actual

current_date = date(2021, 7, 24)
print(current_date.year) # -> 2021
print(current_date.month) # -> 7
print(current_date.day) # -> 24

# Se pueden hacer operaciones con los parámetros de date
current_date = date(current_date.year + 3, current_date.month, current_date.day)
print(current_date.year) # -> 2024

# Se pueden hacer operaciones entre objetos del mismo tipo
diff = year_2025 - now
print(diff) # -> Diferencia en días y horas respecto a now (ej. -447 days, 13:27:05...)
diff = year_2025.date() - current_date
print(diff) # -> 365 days, 0:00:00 (2025-07-24 menos 2024-07-24)

# 'timedelta' se utiliza para realizar sumas, restas y cálculos con fechas y tiempos.
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta) # -> 121 days, 0:00:00
print(end_timedelta + start_timedelta) # -> 661 days, 0:03:20.000200
