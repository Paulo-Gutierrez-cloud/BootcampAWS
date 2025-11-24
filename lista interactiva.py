#  sistema de gestion de alumnos usando listas python
#CRUD

alumnos = []
alumno1 = input("Ingrese el nombre del alumno 1: ")
alumno2 = input("Ingrese el nombre del alumno 2: ")
alumno3 = input("Ingrese el nombre del alumno 3: ")
alumno4 = input("Ingrese el nombre del alumno 4: ")
alumno5 = input("Ingrese el nombre del alumno 5: ")

alumnos.append(alumno1)
alumnos.append(alumno2)
alumnos.append(alumno3)
alumnos.append(alumno4)
alumnos.append(alumnos)

print(alumnos)

# Actualizamos con nuevo alumno para la posicion 2 
alumnos.insert(1,input("Ingrese el nombre del nuevo alumno para la posicion 2: "))

print(alumnos)

alumnos.remove(input("Ingrese el nombre del alumno a eliminar: "))