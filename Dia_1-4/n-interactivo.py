print("¿que opreración deseas realizar?")
print("1. Suma")
print("2. resta")
opcion = input("Elige una opción (1/2): ")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if opcion == "1":
    print(f"la suma de {numero1} y {numero2} es {numero1 + numero2:.2f}")
elif opcion == "2":
    print(f"El resultado de la resta es:", (numero1 - numero2))