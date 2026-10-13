## List Comprehension ##

# Sintaxis: elemento 'for' para iterar el elemento 'in' lugar donde iterará
my_list = [i for i in range(7)]
print(my_list) # -> [0, 1, 2, 3, 4, 5, 6]
# Nota: puede ser rango, lista, tupla

# El elemento puede ser modificado dentro de la list comprehension
my_list = [i * i for  i in range(7)]
print(my_list) # -> [0, 1, 4, 9, 16, 25, 36]

def sum_five(number):
    return number + 5
# El elemento está siendo modificado por la función 'sum_five'
my_list = [sum_five(i) for  i in range(7)]
print(my_list) # -> [5, 6, 7, 8, 9, 10, 11]

# También puede incluirse una condicional dentro de la list comprehension
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers) # -> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]