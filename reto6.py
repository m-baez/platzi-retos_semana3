# Reto #6 Nombres cortos y largos

"""Ya sabemos trabajar con nombres ¿pero qué pasa si cumple ciertas cualidades?
Tu usuario ingresará su nombre, si tiene una longitud mayor a 5 caracteres mostrarás un saludo con su nombre en pantalla. Si tiene menos de 5 caracteres, pedirás su apellido, mostrarás el saludo con nombre y apellido. En ambos casos deberás mostrarlos con mayúscula inicial."""


def main():
    print('-'*60)
    name = str(input('Ingresa tu nombre: ').capitalize())
    nameLen = name.__len__()
    if nameLen > 5:
        print('\nHola %s, un gusto tenerte de vuelta!' % name)
    else:
        lastName = str(input('Ingresa tu apellido: ').capitalize())
        print('\nHola %s %s, un gusto tenerte de vuelta!' % (name, lastName))
    print('-'*60)


if __name__ == '__main__':
    main()
