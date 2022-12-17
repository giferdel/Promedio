

def val_nom(nombre):
    while nombre == '':
        print('Ingrese un Nombre y Apellido')
        nombre = input('Ingrese Nombre y Apellido: ')
    print('Nombre ingresado con éxito')
    return nombre

def val_dni(dni):
    while len(dni)<7 or len(dni)>8:
        dni = input('Ingrese un D.N.I. válido: ')       
    print('D.N.I. ingresado con éxito')
    return dni
        


