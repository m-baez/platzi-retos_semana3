# Reto #1 Longitud del string

"""Pide a tu usuario que ingrese el nombre de su curso favorito, obtén la longitud de ese string y muéstralo en pantalla."""


def main():
    print('-'*60)
    curse = str(input('Ingresa el nombre de tu curso favorito: ').__len__())
    print('\nEsta es la longitud de caracteres: %s' % curse)
    print('-'*60)


if __name__ == '__main__':
    main()
