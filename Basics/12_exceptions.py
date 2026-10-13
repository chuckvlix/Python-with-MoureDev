## Exceptions Handling ##

number1, number2 = 5, 2
number2 = '2'

# try - except
try:
    print(number1 + number2) # (Lanza TypeError al sumar int y str)
    print('Se ejecutó con éxito') # (No se ejecuta debido al error previo)
except: # Se ejecuta si se produce una excepción
    print('Se ha producido un error') # -> Se ha producido un error

# try - except - else
try:
    print(number1 + number2) # (Lanza TypeError)
    print('Se ejecutó con éxito') # (No se ejecuta)
except:
    print('Se ha producido un error') # -> Se ha producido un error
else: # Se ejecuta si NO se produce una excepción
    print('La ejecución continúa correctamente') # (No se ejecuta porque hubo excepción)

# try - except - else - finally
try:
    print(number1 + number2) # (Lanza TypeError)
    print('Se ejecutó con éxito') # (No se ejecuta)
except:
    print('Se ha producido un error') # -> Se ha producido un error
else:
    print('La ejecución continúa correctamente') # (No se ejecuta)
finally: # Se ejecuta siempre
    print('La ejecución continúa') # -> La ejecución continúa (finally siempre se ejecuta)

# Excepciones por tipo
try:
    print(number1 + number2) # (Lanza TypeError)
    print('Se ejecutó con éxito') # (No se ejecuta)
except ValueError:
    print('Se ha producido un ValueError') # (No se ejecuta para este tipo de error)
except TypeError:
    print('Se ha producido un TypeError') # -> Se ha producido un TypeError

# Captura de la información de la excepción
try:
    print(number1 + number2) # (Lanza TypeError)
    print('Se ejecutó con éxito') # (No se ejecuta)
except Exception as error:
    print(error) # -> unsupported operand type(s) for +: 'int' and 'str'

