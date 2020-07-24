# Reto #5 Mayúsculas y minúsculas

"""Solicita a tu usuario que indique 2 palabras, donde al mostrarlas en pantalla una estará totalmente en mayúsculas y otra en minúsculas ¿fácil, no?"""


def main():
    print('-'*60)
    textLower = str(
        input('Escribe cualquier cosa y se mostrará en minusculas: '))
    textUpper = str(
        input('Escribe cualquier cosa y se mostrará en mayusculas: '))
    print(textLower.lower())
    print(textUpper.upper())
    print('-'*60)


if __name__ == '__main__':
    main()
