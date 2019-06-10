import ParentClass
import ChildClass2
import ChildClass

def main():
    cuentaAhorro = ChildClass.Ahorros(200)
    cuentaCheques = ChildClass2.CuentaCheques(500)

    print('Tu cuenta de ahorros cuenta con un monto de : $', cuentaAhorro.get_balance())
    print('Tu cuenta de cheques cuenta con un monto de : $', cuentaCheques.getBalance())

main()