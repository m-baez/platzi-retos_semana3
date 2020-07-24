# Reto #7 ¡Hablemos Pig Latin! (Puerco Latino) 🐷

"""Solo una cosa, pide a tu usuario que ingrese una palabra y tradúcela a Pig Latin.

Espera ¡¿qué?!
PuercoLatino es como el idioma de la “efe”, donde cambiamos las palabras bajo ciertas condiciones. En este caso será así:

La primer consonante de una palabra se pasa al final y se agrega la sílaba “ay”.
Si una palabra inicia con vocal, se agrega “way” al final.
Ejemplos:

Platzi 👉 Latzipay
Abeja 👉 Abejaway"""


def main():
    print('-'*60)
    wordPig = str(input('Ingresa una palabra y se traducirá en Pig Latin: '))
    vocals = ['a', 'e', 'i', 'o', 'u']
    if wordPig[0].lower() in vocals:
        print('\nEsta es tu palabra traducida: %s 🐷' %
              wordPig.__add__('way').title())
    else:
        newWordPig = wordPig[1:].__add__(wordPig[0]).__add__('ay')
        print('\nEsta es tu palabra traducida: %s 🐷' % newWordPig.title())
    print('-'*60)


if __name__ == '__main__':
    main()
