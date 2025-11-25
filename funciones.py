def mensaje_bienvenida():
    print("¡Bienvenido!")

def saludo_personalizado(nombre):
    print(f"Hola, {nombre}!")

def edades(nombre, edad):
    print(f"{nombre} tiene {calculo_edad(edad)} días de vida.")

def calculo_edad(edad):
    dias_anio = 365
    dias_totales = edad * dias_anio
    return dias_totales

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))


saludo_personalizado(nombre)
edades(nombre, edad)
