import ChildClass
import ChildClass2


def main():
    cuentaAhorro = ChildClass.Ahorros(100)
    cuentaCheques = ChildClass2.CuentaCheques(500)

    print('El monto en tu cuenta de ahorros es: $', cuentaAhorro.get_balance())
    print('El monto en tu cuenta de cheques es: $', cuentaCheques.getBalance())

    cuentaCheques.depositar(75)
    print('Haciendo deposito en la cuenta de cheques por $75...')
    print('El nuevo monto en tu cuenta de cheques es: $', cuentaCheques.getBalance())

    cuentaAhorro.depositar(300)
    print('Haciendo deposito en la cuenta de ahorros por $300...')
    print('El nuevo monto en tu cuenta de ahorros es: $', cuentaAhorro.get_balance())


main()