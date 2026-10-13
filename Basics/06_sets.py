## Sets ##

my_set = {35, 1.73, 'Micky'}
other_set = set({32, 24, 24, 53, 40})

print(my_set) # -> {1.73, 35, 'Micky'} (orden no garantizado)
print(other_set) # -> {32, 24, 40, 53} (orden no garantizado y no muestra datos repetidos)
print(type(my_set)) # -> <class 'set'>
print(type(other_set)) # -> <class 'set'>

'''
Los sets, a diferencia de las listas y tuplas, no son estructuras ordenadas
Sus elementos son únicos y no admite repetidos
'''

# Funciones
print(len(other_set)) # -> 4 (longitud del set, no cuenta elementos repetidos)
other_set.add(20) # Agrega un elemento en cualquier posición
print(other_set) # -> {32, 40, 20, 53, 24}
my_set.add('Micky') #No admite el dato repetido
print(my_set) # -> {1.73, 35, 'Micky'} (solo mantiene 'Micky' una vez)

print('Micky' in my_set) # -> True (porque 'Micky' existe en 'my_set')
print('Mickey' in my_set) # -> False (porque 'Mickey' no existe en 'my_set')

other_set.remove(24) # Elimina el elemento del set
print(other_set) # -> {32, 40, 20, 53} (* Solo existe un elemento 24 porque el set no admite repetidos)

other_set.clear() # Limpia el set y lo deja sin elementos
print(other_set) # -> set() (representación en consola de un set vacío)

# del es una operacion propia del lenguaje
del other_set # Elimina la variable del set
#print(other_set) # Error en consola indicando que other_set no está definido

# Convertir a lista
my_list = list(my_set)
print(my_list) # -> [1.73, 35, 'Micky'] (orden dependiente del set)
print(my_list[0]) # -> 1.73

# Unir sets
language_set = {'JavaScript', 'Python', 'Rust'}
new_set = my_set.union(language_set) # Combina los elementos de manera desordenada
print(new_set) # -> {1.73, 'Rust', 35, 'JavaScript', 'Python', 'Micky'}
print(new_set.union({'C#', 'Java', 'Rust'})) # -> {1.73, 'Rust', 35, 'JavaScript', 'Micky', 'C#', 'Python', 'Java'} (ignora repetidos)

print(new_set.difference(my_set)) # -> {'Rust', 'JavaScript', 'Python'} (quita los elementos de my_set)
