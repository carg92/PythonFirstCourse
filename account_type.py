class CuentaBanco:
    'Clase Padre'

    def __init__(self, balance_inicial):
        self.__balance = balance_inicial


    def getBalance(self):
        return self.__balance


    def depositar(self, monto):
        self.__balance += monto


    def retiro(self, monto):
        if monto >= self.__balance:
            print('No hay suficientes fondos para hacer el retiro, solo puedes retirar hasta: $', self.__balance)
        else:
            self.__balance -= monto

class cuentaAhorros(CuentaBanco):

    def __init__(self, balance_inicial):
        CuentaBanco.__init__(self, balance_inicial)

    def transferencia(self, cuenta, monto):
        if monto <= cuenta.getBalance():
            cuenta.retiro(monto)
            self.depositar(monto)
            print('Has transferido: $', monto, "a la cuenta de ahorros. \n")
        else:
            print('Fondos insuficientes. \n')

class cuentaCheques(CuentaBanco):

    def __init__(self, balance_inicial):
        CuentaBanco.__init__(self,balance_inicial)
    



            

