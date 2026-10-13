## Lists ##

my_list = [35, 1.73, 'Micky', True]
other_list = list([32, 24, 24, 62, 19, 53, 40])
print(my_list) # -> [35, 1.73, 'Micky', True]
print(other_list) # -> [32, 24, 24, 62, 19, 53, 40]
print(type(my_list)) # -> <class 'list'>
print(type(other_list)) # -> <class 'list'>

# Recorrer listas
print(my_list[0]) # -> 35
print(my_list[2]) # -> Micky
print(my_list[-1]) # -> True (Último elemento)
print(my_list[-3]) # -> 1.73 (Tercer elemento contando desde atrás)


# Funciones
print(len(other_list)) # -> 7 (Muestra la longitud de la lista)

print(other_list.count(24)) # -> 2 (Cuenta la cantidad de veces que se repite un elemento)

other_list.append('ages') # Agregar un elemento al final de la lista
print(other_list) # -> [32, 24, 24, 62, 19, 53, 40, 'ages']

other_list.insert(1, 'yellow') # Agregar un elemento en el índice señalado
print(other_list) # -> [32, 'yellow', 24, 24, 62, 19, 53, 40, 'ages']

other_list[1] = 'blue' # Cambia el valor del índice 1 de yellow a blue
print(other_list) # -> [32, 'blue', 24, 24, 62, 19, 53, 40, 'ages']

other_list.remove('blue') # Eliminar un elemento
print(other_list) # -> [32, 24, 24, 62, 19, 53, 40, 'ages']
other_list.remove(24) # Elimina el primer elemento 24 que encuentra
print(other_list) # -> [32, 24, 62, 19, 53, 40, 'ages']

print(other_list.pop()) # -> ages (Elimina el último elemento y lo devuelve/imprime)
print(other_list) # -> [32, 24, 62, 19, 53, 40]
pop_element = other_list.pop(2) # Remueve el elemento[2] y lo almacena en una variable
print(pop_element) # -> 62
print(other_list) # -> [32, 24, 19, 53, 40]

# del es una operacion propia del lenguaje
del other_list[2] # Elimina un elemento de la lista por índice
print(other_list) # -> [32, 24, 53, 40]

new_list = other_list.copy() # Copia los valores de la lista y los asigna a otra lista
print(new_list) # -> [32, 24, 53, 40]

other_list.clear() # Limpia la lista y la deja sin elementos
print(other_list) # -> []

new_list.reverse() # Invierte el orden de los elementos de la lista
print(new_list) # -> [40, 53, 24, 32]

new_list.sort() # Ordena los elementos de la lista, por defecto de menor a mayor
print(new_list) # -> [24, 32, 40, 53]

print(new_list[1:3]) # -> [32, 40] (Separa los elementos de la lista comenzando en [1] y antes de llegar a [3])

# Asignar variables a una lista
age, height, nick, single = my_list
print(height) # -> 1.73
print(nick) # -> Micky
