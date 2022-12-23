import os
import random

# Lista de palabras que se usarán para generar nombres de carpetas y texto aleatorio
palabras = [
    "conejo",
    "león",
    "oveja",
    "cerdo",
    "ratón",
    "zorro",
    "caballo",
    "gallina",
    "perro",
    "gato",
]

# Bucle que crea 3000 carpetas con nombres aleatorios
for i in range(3000):
    # Genera un nombre de carpeta aleatorio usando tres palabras aleatorias y un numero serial
    nombre_carpeta = "-".join([random.choice(palabras) for _ in range(3)]) + f"-{i+1}"
    # Crea la carpeta con el nombre generado
    os.makedirs(nombre_carpeta)

    # Genera dos archivos .md con texto aleatorio en la carpeta recién creada
    for j in range(2):
        # Abre el archivo en modo de escritura
        with open(os.path.join(nombre_carpeta, f"cuento{j+1}.md"), "w") as f:
            # Genera un título aleatorio usando dos palabras aleatorias
            titulo = " ".join([random.choice(palabras).capitalize() for _ in range(2)])
            # Escribe el título en el archivo
            f.write(f"# {titulo}\n\n")
            # Genera un cuerpo de texto aleatorio usando diez palabras aleatorias
            cuerpo = " ".join([random.choice(palabras) for _ in range(10)])
            # Escribe el cuerpo de texto en el archivo
            f.write(cuerpo)
