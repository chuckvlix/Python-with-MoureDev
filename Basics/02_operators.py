## Operadores aritmeticas ##
print(3 + 4) # -> 7
print(3 - 4) # -> -1
print(3 * 4) # -> 12
print(9 / 4) # -> 2.25
print(9 % 4) # -> 1
print(9 // 4) # -> 2
print(5 ** 3) # -> 125

print('hola ' + str(5)) # -> hola 5
print('hola ' * 3) # -> hola hola hola 


## Operadores comparativos ##
print(3 > 4) # -> False
print(3 < 4) # -> True
print(3 >= 4) # -> False
print(3 <= 4) # -> True
print(3 == 4) # -> False
print(3 != 4) # -> True
print(4 > 3 == 3) # -> True (evalúa 4 > 3 and 3 == 3)

print('Hola' > 'Python') # -> False
print('aaa' >= 'aba') # -> False (Orden alfabético por ASCII: 'a' < 'b')
print('aaa' >= 'AAA') # -> True (Orden alfabético por ASCII: minúsculas tienen mayor valor que mayúsculas)
print(len('aaa') >= len('bbb')) # -> True (Cuenta los caracteres: 3 >= 3)


## Operadores lógicos ##
print(5 == 5 and 4 > 5) # -> False
print(5 == 5 or 4 > 5) # -> True
print(5 == 5 or 4 > 5 and 2 < 3) # -> True
print(not(3 == 3)) # -> False
print(3 > 4 and 'hola' > 'Python') # -> False
print(3 > 4 or 'hola' > 'Python') # -> True ('h' > 'P' es True)
