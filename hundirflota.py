"""TODO: Tablero 8x8. Barcos: 5 (Portaaviones), 4 (Acorazado), 3 (Submarino), 3 (Crucero), 3 (Destructor) 2 Coordenadas (letra,numero), numero: fila, letra, columna"""
from random import randint, choice
from pprint import pprint
"""
TODO: 
--- Funciones mínimas ---
- colocar_barcos(tablero_jugador1 : list[list[Any]]
- recibir_disparo(tablero,fila,col) : String --> "AGUA" , "TOCADO" o "HUNDIDO"

*** A implementar ***
- El juego se acaba cuando el contador de barcos hundidos sea igual al número de barcos a hundir.
- Símbolos:
    - "~" : agua
    - numeros identificativos barcos
    - X : tocado --> cuando todas las coordenadas de un barco sean igual a "X" se retornará "HUNDIDO"
    - O : disparo al agua
"""

DIRECCIONES = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]

TAMAÑO_TABLERO = 8

AGUA = "~"
TOCADO = "X"
FALLO = "O"

barcos_hundidos = []
# diseño irene
# AGUA = "~"
# TOCADO = "X"
# FALLO = "O"

# diseño juego normal
# AGUA = "O"
# TOCADO = "X"
# TOCADO y HUNDIDO = "XX"  este se puede cambiar



def zona_adyacente_libre(tablero_jugador1 : list[list],fila : int, columna : int) -> bool:
    if tablero_jugador1[fila][columna] != "~":
        return False
    for direccion_fila,direccion_columna in DIRECCIONES:
        nueva_fila = fila + direccion_fila
        nueva_columna = columna + direccion_columna
        if 0 <= nueva_fila < TAMAÑO_TABLERO and 0 <= nueva_columna < TAMAÑO_TABLERO:
            if tablero_jugador1[nueva_fila][nueva_columna] != "~":
                return False
    return True
def colocar_un_barco(tablero_jugador1: list[list], tamaño_barco : int, id_barco : str):
    orientaciones = ["Horizontal", "Vertical"]
    colocado = False

    while not colocado:
        orientacion = choice(orientaciones)
        max_inicio_barco = TAMAÑO_TABLERO - tamaño_barco
        inicio_barco = randint(0,max_inicio_barco)
        if orientacion == "Horizontal":
            fila = randint(0,TAMAÑO_TABLERO - 1)
            tramo_libre = True
            for columna in range(inicio_barco,inicio_barco + tamaño_barco):
                if not zona_adyacente_libre(tablero_jugador1,fila,columna):
                    tramo_libre = False
            if tramo_libre:
                for columna in range(inicio_barco,inicio_barco + tamaño_barco):
                    tablero_jugador1[fila][columna] = id_barco
                colocado = True
        else:
            columna = randint(0, TAMAÑO_TABLERO - 1)
            tramo_libre = True
            for fila in range(inicio_barco, inicio_barco + tamaño_barco):
                if not zona_adyacente_libre(tablero_jugador1, fila, columna):
                    tramo_libre = False
            if tramo_libre:
                for fila in range(inicio_barco, inicio_barco + tamaño_barco):
                    tablero_jugador1[fila][columna] = id_barco
                colocado = True

def desparsear_letra(letra : str) -> int:
    match letra:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6
        case "H":
            return 7

def parsear_letra(coordenada_y: int) -> str:
    match coordenada_y:
        case 0:
            return "A"
        case 1:
            return "B"
        case 2:
            return "C"
        case 3:
            return "D"
        case 4:
            return "E"
        case 5:
            return "F"
        case 6:
            return "G"
        case 7:
            return "H"

def recibir_disparo(tablero_jugador1: list[list], coord: str, id_barco : str, barcos_hundidos : list[str]) -> str:

    coord_parsed = [0, 0]

    tocado = True

    coord_parsed[0] = int(coord[1]) - 1
    coordenada_columna = desparsear_letra(coord[0])
    coord_parsed[1] = coordenada_columna

    if tablero_jugador1[coord_parsed[0]][coord_parsed[1]] == AGUA:
        return "DISPARO AL AGUA"
    elif tablero_jugador1[coord_parsed[0]][coord_parsed[1]] == FALLO or tablero_jugador1[coord_parsed[1]][coord_parsed[1]] == TOCADO:
            return "YA DISPARADO"

    elif tablero_jugador1[coord_parsed[0]][coord_parsed[1]] == id_barco:
        tablero_jugador1[coord_parsed[0]][coord_parsed[1]] = TOCADO
        if id_barco not in tablero_jugador1:
            barcos_hundidos.append(id_barco)
            return "HUNDIDO"
        return "TOCADO"

def paridad(tablero_jugador2 : list[list[str]]):
    for i in range(len(tablero_jugador2)):
        for j in range(0,len(tablero_jugador2[i])):
            preferente = (tablero_jugador2[i] + tablero_jugador2[j]) % 2 == 0


def target():






def main():
    barcos = {
        "1": 5,
        "2": 4,
        "3": 3,
        "4": 3,
        "5": 2
    }


    tablero_jugador1 = [
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],

    ]

    tablero_jugador2 = [
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
    ]

    for id_barco, tamaño_barco in barcos.items():
        colocar_un_barco(tablero_jugador1, tamaño_barco, id_barco)
    pprint(tablero_jugador1)


if __name__ == "__main__":
    main()
