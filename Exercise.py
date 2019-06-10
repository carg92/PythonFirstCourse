class Employee:
    'Clase base de Employee'

    #Data attributes
    first_name = 'Cesar'
    last_name = 'Romero'
    age = '27'

def main():
    #Titulo del programa
    print('******* WELCOME TO THE EMPLOYEE DATABASE*********')
    
    #Imprime los datos 
    print('Fist name: ',Employee.first_name)
    print('Last name:', Employee.last_name)
    print('Age: ', Employee.age)

#Llamado al metódo main
main()
        