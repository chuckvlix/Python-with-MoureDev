## Modules ##

#import Basics.my_module as my_module # importa el módulo completo

#my_module.sum_values(3, 6, 4)
#my_module.print_value('Hola Python')

from my_module import sum_values, print_value #importa las funciones elegidas
sum_values(4, 3, 2) # -> 9
print_value('Hola mundo') # -> Hola mundo

import math # math es un módulo integrado de Python

print(math.pi) # -> 3.141592653589793
print(math.pow(2, 8)) # -> 256.0
