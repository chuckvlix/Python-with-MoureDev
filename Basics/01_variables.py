## Variables ##

my_str_variable = 'My string variable' # snake_case o minúsculas
print(my_str_variable) # -> My string variable

int_variable = 5
print(int_variable) # -> 5

int_to_str_variable = str(int_variable)
print(int_to_str_variable) # -> 5
print(type(int_to_str_variable)) # -> <class 'str'> (type es para mostrar el tipo de dato)

bool_variable = False
print(bool_variable) # -> False

# Funsion len()
print(len(my_str_variable)) # -> 18

# Concatenación de variables en un print
print(my_str_variable, int_to_str_variable, bool_variable) # -> My string variable 5 False
print('The value is: ', bool_variable) # -> The value is:  False

# Variables en una sola linea
name, surname, nick, age = 'Miguel', 'Colque', 'Micky', 35

# Concatenar con formato f""
print(f"My name is: {name} {surname}, I'm {age} years old and my nick is {nick}") # -> My name is: Miguel Colque, I'm 35 years old and my nick is Micky

# Input para pedir datos al usuario
# Las variables pueden ser reasignadas
name = input('What\'s your name? ') # Se usa \ para escapar caracteres reservados (\')
age = input('How old are you? ')

print(name) # -> Imprime el valor ingresado por el usuario (ej. Miguel)
print(age) # -> Imprime el valor ingresado por el usuario (ej. 35)
