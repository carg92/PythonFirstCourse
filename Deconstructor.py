class Clase:

    def __init__(self):
        print('Creando nuevo objeto...')

    def __del__(self):
        print('Destruyendo el objeto...')

def main():
    object1 = Clase()
    object2 = Clase()
    object3 = Clase()

    print("\n\n")

    del(object1)
    del(object2)
    del(object3)


main()