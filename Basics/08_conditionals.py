## Conditionals ##

my_condition = False

if my_condition:
    print('Se ejecuta la condición del if si es true') # (No se ejecuta porque my_condition es False)

my_condition = 5 * 2

if my_condition == 10: # Si se cumple la condición es igual a True
    print('Se ejecuta la condición del segundo if') # -> Se ejecuta la condición del segundo if

# Empieza una nueva ejecución de decisión
if my_condition > 20:
    print('Es mayor que 20') # (No se ejecuta)
# Se pueden conectar varias condiciones con operadores lógicos
elif my_condition >= 10 and my_condition <= 20:
    print('Es mayor o igual a 10 y menor o igual a 20') # -> Es mayor o igual a 10 y menor o igual a 20
else:
    print('Es menor que 10') # (No se ejecuta)

print('La ejecución continúa') # -> La ejecución continúa


# Un string vacío es interpretado como False
my_string = ''
if my_string:
    print('La cadena de texto está vacía') # (No se ejecuta porque string vacío evalúa a False)

my_string = 'Cadena de texto'
if my_string:
    print('La cadena de texto no está vacía') # -> La cadena de texto no está vacía (string con contenido evalúa a True)