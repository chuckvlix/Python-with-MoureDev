## Strings ##

my_string = 'Mi string' # El uso de comillas simples o dobles es indistinto
other_string = "Otro string"

print(len(my_string)) # -> 9 (Muestra la longitud del string)
print(len(other_string)) # -> 11 (Longitud del contenido de la variable)

print(my_string + ' ' + other_string) # -> Mi string Otro string (Se pueden concatenar con el signo +)

line_break_string = 'Este es un String\ncon salto de línea'
print(line_break_string) # -> Imprime en dos líneas: Este es un String / con salto de línea

tab_string = '\tEste es un string con tabulación'
print(tab_string) # -> 	Este es un string con tabulación (con sangría/tab)

# Se usa \ para escapar caracteres reservados
scape_string = '\\tEste es un string \\n escapado'
print(scape_string) # -> \tEste es un string \n escapado

# Formateo
name, age = 'Micky', 35
print('My name is {} and I´m {} years old'.format(name, age)) # -> My name is Micky and I´m 35 years old
print('My name is %s and I´m %d years old' %(name, age)) # -> My name is Micky and I´m 35 years old (%s para strings y %d para integers)
print(f'My name is {name} and I´m {age} years old') # -> My name is Micky and I´m 35 years old (Más práctico y más utilizado)

# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(a) # -> P
print(b) # -> y
print(e) # -> o

# División
language_slice = language[1:3]
print(language_slice) # -> yt
language_slice = language[2:]
print(language_slice) # -> thon
language_slice = language[-3]
print(language_slice) # -> h

# Reverse
reversed_language = language[::-1] # Invierte el orden del string
print(reversed_language) # -> nohtyP

# Funciones
print(language.capitalize()) # -> Python (Convierte la primera letra en mayúscula)
print(language.upper()) # -> PYTHON (Convierte todas las letras en mayúsculas)
print(language.lower()) # -> python (Convierte todas las letras en minúsculas)
print(language.count('t')) # -> 1 (Cuenta cuántas 't' tiene el string)
print(language.isnumeric()) # -> False (Para saber si es un número)
print(language.isupper()) # -> False (Para saber si las letras son mayúsculas)
print(language.startswith('py')) # -> False (Para saber si el string comienza con 'Py'. Importan las mayúsculas)