class CuentaBanco:


    def __init__(self, balance_inicial):
        self.__balance = balance_inicial

    def get_balance(self):
        return self.__balance

    def depositar(self, monto_deposito):
        self.__balance += monto_deposito

def main():
    #Crear nueva cuenta

    cuenta = CuentaBanco(420)

    #Mostrar balance de la cuenta
    print('Estimado usuario, tu balance actual es: $', cuenta.get_balance())

    #Añadir nuevos valores a balance
    cuenta.depositar(100)
    
    #Mostrar balance de la cuenta
    print('Estimado usuario, tu balance actual es: $', cuenta.get_balance())


main()    