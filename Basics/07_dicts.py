## Dictionaries ##

my_dict = {'name': 'Miguel', 'nick': 'Micky', 'age': 35}
other_dict = dict({1: 'id', 2: 1.77, 3: 'text'})
print(type(my_dict)) # -> <class 'dict'>
print(type(other_dict)) # -> <class 'dict'>

# Se puede separar por saltos de línea para legibilidad
my_dict = {
    'name': 'Miguel',
    'nick': 'Mike',
    'age': 35,
    'languages': {'Python', 'JavaScript', 'C#'} # set dentro del diccionario
}
print(my_dict) # -> {'name': 'Miguel', 'nick': 'Mike', 'age': 35, 'languages': {'JavaScript', 'C#', 'Python'}}

# Acceder a elentos
print(my_dict['name']) # -> Miguel (Muestra el valor de la clave 'name')
#print(my_dict[35]) # Error en consola porque solo se puede pasar la clave
my_dict['nick'] = 'Micky' # Actualiza el valor de una clave
print(my_dict['nick']) # -> Micky
my_dict['address'] = 'Micky Street' # Agrega una nueva llave con su respectivo valor
print(my_dict) # -> {'name': 'Miguel', 'nick': 'Micky', 'age': 35, 'languages': {'JavaScript', 'C#', 'Python'}, 'address': 'Micky Street'}


# Funciones
print(len(my_dict)) # -> 5 (Muestra la cantidad de claves del diccionario)
print(other_dict.clear()) # -> None (limpia el diccionario y retorna None)

# del es una operacion propia del lenguaje
del my_dict['address'] # Elimina un elemento del diccionario accediendo a la clave
print(my_dict) # -> {'name': 'Miguel', 'nick': 'Micky', 'age': 35, 'languages': {'JavaScript', 'C#', 'Python'}}

print('Micky' in my_dict) # -> False (No realiza la búsqueda por el valor)
print('nick' in my_dict) # -> True (Solo busca por la clave)

print(my_dict.items()) # -> dict_items([('name', 'Miguel'), ('nick', 'Micky'), ('age', 35), ('languages', {'JavaScript', 'C#', 'Python'})])
print(my_dict.keys()) # -> dict_keys(['name', 'nick', 'age', 'languages'])
print(my_dict.values()) # -> dict_values(['Miguel', 'Micky', 35, {'JavaScript', 'C#', 'Python'}])

new_dict = dict.fromkeys(my_dict) # Copia el diccionario conservando solamente las llaves
print(new_dict) # -> {'name': None, 'nick': None, 'age': None, 'languages': None}
# Puede tener sentido para transformar esta copia en una lista, una tupla o un set
print(list(new_dict)) # -> ['name', 'nick', 'age', 'languages'] (Las claves pasan a ser elementos de una lista)