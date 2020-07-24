# Reto #3 Ajusta las iniciales

"""Ahora, pedirás a tu usuario que ingrese su nombre, apellido y país de origen en minúsculas. Después mostrarás los datos de salida con mayúscula inicial al tratarse de nombres propios."""


def main():
    print('-'*60)
    name = str(input('Escribe tu nombre: ').capitalize())
    lastName = str(input('Escribe tu apellido: ').capitalize())
    country = str(input('Escribe tu país de origen: ').capitalize())
    print('Hola, mi nombre es %s %s y soy originario de %s' %
          (name, lastName, country))
    print('-'*60)


if __name__ == '__main__':
    main()
