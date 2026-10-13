## Challenges ##

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 20 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for num in range(1, 21):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz") # -> fizzbuzz (si es múltiplo de 3 y 5, ej. 15)
        elif num % 3 == 0:
            print("fizz") # -> fizz (si es múltiplo de 3, ej. 3, 6, 9, 12, 18)
        elif num % 5 == 0:
            print("buzz") # -> buzz (si es múltiplo de 5, ej. 5, 10, 20)
        else:
            print(num) # -> Imprime el número (1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19)

fizzbuzz()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Roma", "Mora")) # -> True


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 10 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números enla que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0
    next = 1
    for _ in range(0, 11):
        print(prev) # -> Imprime sucesivamente: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

        fib = prev + next
        prev = next
        next = fib

fibonacci()


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 20.
"""

def is_prime():
    for number in range(1, 21):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number) # -> Imprime sucesivamente: 2, 3, 5, 7, 11, 13, 17, 19

is_prime()


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text

print(reverse("Hola mundo")) # -> odnum aloH