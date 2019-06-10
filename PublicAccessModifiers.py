class CuentaBanco:

    def __init__(self, balance_inicial):
        self.balance = balance_inicial
        

    def get_balance(self):
        return self.balance

        

def main():

    #Crear nueva cuenta
    cuenta = CuentaBanco(500)


    #Mostrar el balance de la cuenta
    print('Estimado usuario, su balance actual es de: $', cuenta.get_balance())

    #Añadir valor al balance actual
    cuenta.balance += 1500

    #Mostrar el balance nuevo de la cuenta
    print('Estimado usuario, su nuevo balance es de: $', cuenta.get_balance())

main()

