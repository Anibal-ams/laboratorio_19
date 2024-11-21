estudiantes = {
    "Juan": 5.0,
    "Ana": 4.2,
    "Luis": 4.5
}
nombre = input("Ingresa el nombre del estudiante: ")
calificacion = float(input("Ingresa la calificación del estudiante: "))

if nombre in estudiantes:
    estudiantes[nombre] = calificacion
    print(f"La calificación de {nombre} ha sido actualizada a {calificacion}.")
else:
    estudiantes[nombre] = calificacion
    print(f"El estudiante {nombre} ha sido agregado con la calificación {calificacion}.")

print("\nLista de estudiantes y sus calificaciones:")
for estudiante, calif in estudiantes.items():
    print(f"{estudiante}: {calif}")
