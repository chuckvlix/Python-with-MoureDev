## Loops ##


## While
my_condition = 0

while my_condition < 10:
    print(my_condition) # -> Imprime sucesivamente: 0, 2, 4, 6, 8 (uno por línea)
    my_condition += 2
    # Se puede anidar condicionales (if, elif, else)
else: # Ejecutar un else junto a while es propio de Python
    print('Mi condición es mayor o igual que 10') # -> Mi condición es mayor o igual que 10
# No se puede ejecutar 'if' ni 'elif' junto a while porque estas llevan condicional

print('La ejecución continúa') # -> La ejecución continúa

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print('Mi condición es 16') # -> Mi condición es 16
        break # Detiene la ejecución del ciclo
    print(my_condition) # -> Imprime: 12, 14 (uno por línea)

## For
my_list = [32, 24, 24, 62, 19, 53, 40]
# Recorre los elementos de variables iterables (listas, tuplas, sets y diccionarios)
for element in my_list:
    print(element) # -> Imprime cada elemento: 32, 24, 24, 62, 19, 53, 40 (uno por línea)

my_dict = {'name': 'Miguel', 'nick': 'Micky', 'age': 35}
# En diccionarios imprime solamente las claves o llaves
for element in my_dict:
    print(element) # -> Imprime cada clave: name, nick, age (uno por línea)

# Para imprimir valores se usa .values()
for element in my_dict.values():
    print(element) # -> Imprime: Miguel, luego Micky (y corta con break)
    if element == 'Micky':
        break # Detiene la ejecución en este punto
        #continue # Regresa al ciclo sin ejecutar lo que está debajo
    print('Se ejecuta') # -> Se ejecuta (solo se ejecuta en la 1ª iteración con 'Miguel') # No se muestra si se usa continue
else:
    print('El bucle for para el diccionario finalizó') # (No se ejecuta porque se interrumpió con break)

print('Ejecución terminada') # -> Ejecución terminada