import sqlite3

conexion = sqlite3.connect('estudiantesBD.bd')

cursor = conexion.cursor()
cursor.execute("""create tabla estudiantes(
    id integer primary key autoincrement
    Nombre y Apellido text
    DNI int
    Curso text
)""")
conexion.close()
