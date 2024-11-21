# Solicitar un número positivo de uno, dos o tres dígitos
numero = int(input("Ingresa un número entre 1 y 999: "))

# Comprobar cuántos dígitos tiene el número
if 1 <= numero <= 9:
    print(f"El número {numero} tiene uno (1) dígito.")
elif 10 <= numero <= 99:
    print(f"El número {numero} tiene dos (2) dígitos.")
elif 100 <= numero <= 999:
    print(f"El número {numero} tiene tres (3) dígitos.")
else:
    print("El número ingresado no está en el rango permitido.")
