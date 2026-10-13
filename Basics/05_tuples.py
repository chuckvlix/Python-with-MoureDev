## Tuplas ##

my_tuple = (35, 1.73, 'Micky', True)
other_tuple = tuple((32, 24, 24, 19, 53, 40))
print(my_tuple) # -> (35, 1.73, 'Micky', True)
print(other_tuple) # -> (32, 24, 24, 19, 53, 40)
print(type(my_tuple)) # -> <class 'tuple'>
print(type(other_tuple)) # -> <class 'tuple'>

# Recorrer tuplas
print(my_tuple[0]) # -> 35
print(my_tuple[2]) # -> Micky
print(my_tuple[-1]) # -> True (Último elemento)
print(my_tuple[-3]) # -> 1.73 (Tercer elemento contando desde atrás)

# Funciones
print(len(other_tuple)) # -> 6 (Muestra la longitud de la tupla)
print(other_tuple.count(24)) # -> 2 (Cuenta la cantidad de veces que se repite un elemento)
print(other_tuple.index(19)) # -> 3 (Muestra el índice donde se encuentra el elemento)
print(other_tuple[2:5]) # -> (24, 19, 53) (Separa los elementos de la tupla comenzando en [2] y antes de llegar a [5])

# Concatenar tuplas
print(my_tuple + other_tuple) # -> (35, 1.73, 'Micky', True, 32, 24, 24, 19, 53, 40)

# del es una operacion propia del lenguaje
del other_tuple # Elimina la tupla
#print(other_tuple) # Error en consola indicando que other_tuple no está definido (NameError)
#del other_tuple[2] # Error en consola porque no pueden eliminarse los elementos de la tupla (TypeError)

'''
Las tuplas, a diferencia de las listas, son inmutables
Una vez definida una tupla, no se pueden agregar, modificar o remover elementos
Ej:
my_tuple[2] = 1.80 # Cambiando 1.73 por 1.80
print(my_tuple) # En consola se mostrará error
'''
