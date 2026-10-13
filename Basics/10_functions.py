## Funtions ##

def my_function(): # Definición de la función
    print('Esto es una función') # -> Esto es una función

my_function() # LLamada de la función

def sum_values(number_1, number_2): # Parámetros: Variables que se esperan recibir
    print(number_1 + number_2) # -> Imprime el resultado de la operación

sum_values(4, 3) # -> 7 (Argumentos: Valores que se envían a los parámetros)
sum_values(7.83, 5) # -> 12.83
sum_values('5', '4') # -> 54 (Concatena strings)
#sum_values('6', 7) # No concatena enteros con stings

def sum_values_with_return(value_1, value_2):
    return value_1 + value_2

result = sum_values_with_return(3.45, 8.25)
print(result) # -> 11.7

def print_name(name, surname):
    print(f'{name}, {surname}')

print_name('Miguel', 'Colque') # -> Miguel, Colque

def print_name_default(name, surname, nick='Sin apodo'):
    print(f'Nombre completo: {name} {surname}, Apodo: {nick}')

print_name_default('Brais', 'Moure', 'MoureDev') # -> Nombre completo: Brais Moure, Apodo: MoureDev
print_name_default('Winston', 'Churchill') # -> Nombre completo: Winston Churchill, Apodo: Sin apodo

# Con asterisco en el parámetro se puede pasar cualquier cantidad de argumentos
def print_texts(*texts):
    print(type(texts)) # -> <class 'tuple'> (Python interpreta la variable como una tupla)
    print(texts) # -> Tupla con los argumentos recibidos

print_texts('Hola', 'Python') # -> Imprime tipo y tupla: ('Hola', 'Python')
print_texts('Django', 'FastAPI', 'Flask') # -> Imprime tipo y tupla: ('Django', 'FastAPI', 'Flask')
