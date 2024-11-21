
contador_empleado_bajo = 0 
contador_empleados_alto = 0
contador_total_sueldos = 0


n = int(input("Ingresa el número de empleados: "))

i = 1
while i <= n:
    sueldo = float(input(f"Ingrese el sueldo del empleado {i}: "))
    if sueldo>=1000000 and sueldo<=3000000:
        contador_empleado_bajo=contador_empleado_bajo+1
    elif sueldo > 3000000:
        econtador_mpleados_alto = contador_empleados_alto+1
    contador_total_sueldos= contador_total_sueldos + sueldo
    i += 1
print(f"Cantidad de empleados que cobran entre $1,000,000 y $3,000,000: {empleados_bajo}")
print(f"Cantidad de empleados que cobran más de $3,000,000: {contador_empleados_alto}")
print(f"El total de sueldos que gasta la empresa es: ${contador_total_sueldos:.2f}")
