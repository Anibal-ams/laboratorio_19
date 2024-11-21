cant1 = 0
cant2 = 0
cant3 = 0
cant4 = 0
n = int(input("Cantidad de puntos: "))
for f in range(n):
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        cant1 += 1
    elif x < 0 and y > 0:
        cant2 += 1
    elif x < 0 and y < 0:
        cant3 += 1
    elif x > 0 and y < 0:
        cant4 += 1
    else:
        print(f"El punto ({x},{y}) no está en ningún cuadrante 'X=0 y=0'.")

print(f"Cantidad de puntos en el primer cuadrante: {cant1}")
print(f"Cantidad de puntos en el segundo cuadrante: {cant2}")
print(f"Cantidad de puntos en el tercer cuadrante: {cant3}")
print(f"Cantidad de puntos en el cuarto cuadrante: {cant4}")