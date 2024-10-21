from collections import namedtuple
from datetime import *
import csv

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta_fichero):
    entrenos = []
    with open(ruta_fichero,encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora,"%d/%m/%Y %H:%M")
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido2 = compartido == "S"

            entrenos.append(Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido2))
    return entrenos