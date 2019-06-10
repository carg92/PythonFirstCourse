class CuentaBanco:
    'Clase Padre'


    def __init__(self, balance_inicial):
        self.__balance = balance_inicial

    def get_balance(self):
        return self.__balance

    def depositar(self, monto):
        self.__balance += monto

    def retirar(self, monto):
        self.__balance -= monto

class Ahorros(CuentaBanco): #ChildClass de CuentaBanco

    def __init__(self, balance_inicial):
        CuentaBanco.__init__(self, balance_inicial)

def main():

    #Objeto 
    ahorrar = Ahorros(8000)

    # Mostrar balance actual
    print('Balance de Cesar Romero')
    print('Balance de cuenta de ahorros: $', ahorrar.get_balance())

    #Depositar dinero a la cuenta de ahorros
    ahorrar.depositar(2000)

    print('Deposito a cuenta')
    #Mostrar el nuevo balance actual
    print('Balance de cuenta de ahorros: $', ahorrar.get_balance())


    #Retirar dinero  de la cuenta de ahorros
    ahorrar.retirar(5000)
    #Mostrar el nuevo balance actual
    print('Retiro de cuenta')
    print('Balance de cuenta de ahorros: $', ahorrar.get_balance())

main()
