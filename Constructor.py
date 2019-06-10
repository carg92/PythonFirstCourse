class Employee:
    'Cuarta fase, Constructor y Destructor'

    def __init__(self, Nombre, Apellido, Id):
        self.nombre = Nombre
        self.apellido = Apellido
        self.id = Id

    def detalles(self):
        print('\t')
        print('Nombre:', self.nombre)
        print('Apellido:', self.apellido)
        print('Id:', self.id)


def main():
    #Crear nuevo objeto empleado
    empleado = Employee('Cesar','Romero','qwerty00')
    
    empleado2 = Employee('Alonso','Garcia','12312das')

    #Mostrar detalles de empleado
    empleado.detalles()
    empleado2.detalles()



main()