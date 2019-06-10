class Employee:
    'Clase base de Employee'

    #Class Attributes
    first_name = 'Cesar'
    last_name = 'Romero'
    age = '27'
    id = '999'

def main():
    print('First name: ', Employee.first_name)
    print('Last name: ', Employee.last_name)
    print('Age: ', Employee.age)
    print('User ID: ', Employee.id)

main()
