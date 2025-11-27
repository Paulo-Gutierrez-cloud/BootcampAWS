frutas = []

def ingresar_fruta():
 
    while True:
        nombre = input("ingrese el nombre de la fruta: ")

        if nombre == "salir":
            break
        precio = float(input("ingrese el precio de la fruta: "))
        cantidad = float(input("ingrese la cantidad de la fruta: "))

        fruta={
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
        }
        print(f"ingresaste la fruta: {nombre} con el precio de: {precio} y cantidad de: {cantidad} ")

        frutas.append(fruta)

def imprimir_ticket():

    total_venta = 0.0
    subtotal = 0.0

    for fruta in frutas:
        subtotal = fruta["precio"] * fruta["cantidad"]
        total_venta += subtotal
 
    print(f"Total de venta es: {total_venta}")



# for para imprimir un ticket de compra 
    print("--------------------------------------Ticket de compra-----------------------------------:")
    for fruta in frutas:
        print(f"-----------{fruta['nombre']} - Precio: {fruta['precio']} - Cantidad: {fruta['cantidad']} - Subtotal: {fruta["precio"] * fruta["cantidad"]}-------------------------")

    print (f" -----------------------------------Total venta: {total_venta}-----------------------------------")


if __name__ == "__main__":
    ingresar_fruta()
    imprimir_ticket()