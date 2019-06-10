class CuentaBanco:
    'Clase Padre'

    def __init__(self, balance_inicial):
        self.__balance = balance_inicial 

    def getBalance(self):
        print('Llamando este método getBalance de la clase padre "CuentaBanco"')


class CuentaCheques(CuentaBanco):

    def __init__(self, balance_inicial):

        CuentaBanco.__init__(self,balance_inicial)

    def getBalance(self):
        CuentaBanco.getBalance(self)
        #print('Llamando este método getBalance de la clase hijo "CuentaCheques"')

def main():

    cuenta = CuentaCheques(50)
    cuenta.getBalance()

main()
