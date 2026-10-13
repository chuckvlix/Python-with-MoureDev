## Classes ##

class EmptyPerson:
    pass # Indica que se requiere código, pero no se requiere ninguna acción

class Person:
    # __init__ es un constructor de clase
    def __init__(self, name, surname, nick='Sin nick'): # En nick define un valor por defecto
        self.name = name
        self.surname = surname
        self.nick =nick
        self.fullname = f'{name} {surname} ({nick})' # Se puede agrupar atributos
    def walk(self): # Define el método walk de la clase Person
        print(f'{self.nick} está caminando') # -> Imprime mensaje con el nick del objeto

my_person = Person('Miguel', 'Colque', 'Micky')
print(f'{my_person.name} {my_person.surname}') # -> Miguel Colque
print(my_person.fullname) # -> Miguel Colque (Micky)
my_person.walk() # -> Micky está caminando

other_person = Person('George', 'Patton')
print(other_person.fullname) # -> George Patton (Sin nick)
