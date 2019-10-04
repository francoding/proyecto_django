def mostrar(lista):
    for e in lista:
        print(e)


def cargar(lista):
    for i in range(len(lista)):
        lista[i] = int(input('Ingrese un nuevo elemento: '))


def main():
    lista = ['Fede', 1]
    cargar(lista)
    mostrar(lista)


if __name__ == '__main__':
    main()