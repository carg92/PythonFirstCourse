class CuentaBanco:
    'Clase padre'


    def __init__(self, balance_inicial):
        self.__balance = balance_inicial

    def depositar(self, monto):
        self.__balance += monto

    def retirar(self, monto):
        self.__balance -= monto

    def getBalance(self):
        return self.__balance

class CuentaCheques(CuentaBanco): #Child Class

    def __init__(self, balance_inicial):
        CuentaBanco.__init__(self,balance_inicial)

    


def main():

    #Crear cuenta de cheques
    cuenta_cheques = CuentaCheques(300)
    print('Balance inicial: $', cuenta_cheques.getBalance())
    #Deposito
    cuenta_cheques.depositar(2000)
    print('Nuevo Balance con deposito: $', cuenta_cheques.getBalance())
    #Retiro
    cuenta_cheques.retirar(1000)
    print('Nuevo Balance con el retiro: $', cuenta_cheques.getBalance())

main()