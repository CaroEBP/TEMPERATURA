#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

ciudades = ["Machala", "Ponce Enríquez", "El Guabo"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 3D: temperaturas[ciudad][semana][día]
temperaturas = [
    [   # Machala
        [28, 29, 30, 29, 31, 32, 30],
        [27, 28, 29, 28, 30, 31, 29],
        [26, 27, 28, 27, 29, 30, 28],
        [25, 26, 27, 26, 28, 29, 27]
    ],
    [   # Ponce Enríquez
        [24, 25, 26, 25, 27, 28, 26],
        [23, 24, 25, 24, 26, 27, 25],
        [22, 23, 24, 23, 25, 26, 24],
        [21, 22, 23, 22, 24, 25, 23]
    ],
    [   # El Guabo
        [26, 27, 28, 27, 29, 30, 28],
        [25, 26, 27, 26, 28, 29, 27],
        [24, 25, 26, 25, 27, 28, 26],
        [23, 24, 25, 24, 26, 27, 25]
    ]
]

# Recorrer la matriz correctamente
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\n Ciudad: {ciudades[ciudad_idx]}")
    for semana_idx, semana in enumerate(ciudad):
        print(f" Semana {semana_idx + 1}")
        suma = 0
        for dia_idx, temp in enumerate(semana):
            print(f"   {dias[dia_idx]}: {temp}°C")
            suma += temp
        promedio = suma / len(semana)
        print(f" Promedio semana {semana_idx + 1}: {promedio:.2f}°C")
