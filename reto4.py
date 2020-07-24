# Reto #4 String fragmentado

"""Pongámonos más exigentes 💥
Solicita a tu usuario que indique una oración de 10 o más caracteres, la línea de un poema o canción funcioona excelente. Calcula la longitud del string, pide un número de rango inicial y final que esté entre la longitud del string para al final mostrar el fragmento que incluya los caracteres en ese intervalo."""


def main():
    print('-'*60)
    text = str(input('Escribe la parte de una canción que te guste: '))
    textLen = text.__len__()
    print('\nEl fragmento de tu canción tiene una longitud de: %s caracteres\n' % textLen)
    n1 = int(input('Escribe un número que servirá como rango incial: '))
    n2 = int(input('Escribe otro número que servirá como rango final: '))
    print('\nEl fragmento entre los dos rangos que escogiste es: "%s"' %
          text[n1:n2])
    print('-'*60)


if __name__ == '__main__':
    main()
