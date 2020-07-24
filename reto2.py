# Reto #2 ‘Suma’ de strings

"""Crea un programa en el que le pidas en 3 variables distintas: nombre, apellido y comida favorita. Como salida mostrarás el mensaje Hola, mi nombres es {nombre} {apellido} y mi comida favorita es {comida} en un solo string."""


def main():
    print('-'*60)
    name = str(input('Escribe tu nombre: '))
    lastName = str(input('Escribe tu apellido: '))
    fFood = str(input('Escribe tu comida favorita: '))
    print('Hola, mi nombre es %s %s y mi comida favorira es %s' %
          (name, lastName, fFood))
    print('-'*60)


if __name__ == '__main__':
    main()
