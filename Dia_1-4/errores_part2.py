def validar_mail(mail):
    if "@" in mail and "." in mail:
        return True
    else:
        raise ValueError("Correo electrónico inválido.")

try:
    email = input("Ingresa tu correo electrónico: ")
    validar_mail(email)
    print(f"Correo electrónico válido: {email}")

except ValueError as error_detectado:
    print(f"Error: {error_detectado}")