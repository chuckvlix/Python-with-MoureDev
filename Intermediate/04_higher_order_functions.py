## Higher Order Functions ##

# Es una función que recibe otra función como argumento o devuelve otra función
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_plus_value(ft_value, sd_value, f_sum):
    return f_sum(ft_value + sd_value)

print(sum_two_values_plus_value(5,2, sum_one)) # -> 8
print(sum_two_values_plus_value(5,2, sum_five)) # -> 12


## Closures ##
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(2)
print(add_closure(5)) # -> 17 (Llamada a la función closure)

print(sum_ten(5)(2)) # -> 17 (Otra forma de llamar a la función closure)


## Build-in Higher Order Functions ##

numbers = [2, 5, 10, 21, 3, 16]

# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers))) # -> [4, 10, 20, 42, 6, 32]
# Se puede simplificar la llamada a otra función utilizando una lambda function
print(list(map(lambda number: number * 2, numbers))) # -> [4, 10, 20, 42, 6, 32]

# Filter
def filter_even_numbers(number):
    if number % 2 == 0:
        return True
    return False

print(list(filter(filter_even_numbers, numbers))) # -> [2, 10, 16]
# Simplificando con lambda function:
print(list(filter(lambda number: number % 2 == 0, numbers))) # -> [2, 10, 16]

# Reduce
from functools import reduce # Importa la función de un módulo nativo de Python

def sum_two_values(ft_value, sd_value):
    print(ft_value) # -> Imprime el acumulador parcial (2, 7, 17, 38, 41)
    print(sd_value) # -> Imprime el elemento actual (5, 10, 21, 3, 16)
    return ft_value + sd_value

print(reduce(sum_two_values, numbers)) # -> 57 (resultado acumulado final)