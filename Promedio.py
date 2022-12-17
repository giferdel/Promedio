from validaciones import val_nom , val_dni
from io import open


def datos():
    nombre = val_nom(input('Nombre y Apellido: '))
    dni = val_dni(input('D.N.I.: '))
    curso = input('Curso: ')
    # alumnx = {'Nombre':nombre , 'Dni':dni , 'Curso':curso}
    alumnx = 'Nombre y Apellido: '+ nombre + '\nDNI: ' + dni + '\nCurso: ' + curso
    lista_alum = open('archivo.txt', 'w')
    lista_alum.write(alumnx)
    # lista_alum.seek(len(alumnx.read()))
    lista_alum.close()
    return nombre

def cal(nombre):
    # import pdb;pdb.set_trace()

    notas = []
    nota = int(input('Ingrese calificación: '))
    while nota != 0:
        notas.append(nota)
        nota = int(input('Ingrese calificación: '))
    print('Las calificaciones de ' + str(nombre) + ' son ')
    print(notas)
    return notas

def prom(notas):
    suma_notas = sum(lista_notas)
    promedio_parcial = suma_notas / len(lista_notas)
    print('Su promedio será ' + str(promedio_parcial))
    return promedio_parcial

alum = datos()
# import pdb;pdb.set_trace()

lista_notas = cal(alum)
prom(lista_notas)



