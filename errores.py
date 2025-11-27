while True:
    try:
        numero = int(input("Ingresa un número nuevamente: "))
        print("Número válido:", numero)
        break
    except ValueError:
        print("Error: no ingresaste un número válido. Inténtalo de nuevo.")

n = input("Ingresa un numero a dividir por 5: ")
try:
    n = int(n)
    resultado = 5 / n
    print("El resultado de la division es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debes ingresar un número entero válido.") 
except Exception as e:
    print("Ocurrió un error inesperado:", e)