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
NUM_BARCOS = 5

AGUA = "~"
TOCADO = "X"
FALLO = "O"


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

def recibir_disparo(tablero_jugador1: list[list[str]], coord: str, id_barco : str, barcos_hundidos : list[str]) -> str:
    # TODO: ARREGLAR LÓGICA BARCOS HUNDIDOS Y AÑADIR LÓGICA FIN DE JUEGO

    coord_parsed = [0, 0]
    coord_parsed[0] = int(coord[1])
    coordenada_columna = desparsear_letra(coord[0])
    coord_parsed[1] = coordenada_columna

    if tablero_jugador1[coord_parsed[0]][coord_parsed[1]] == AGUA:
        return "AGUA"
    elif tablero_jugador1[coord_parsed[0]][coord_parsed[1]] == FALLO or tablero_jugador1[coord_parsed[0]][coord_parsed[1]] == TOCADO:
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
            preferente = (i + j) % 2 == 0
            if preferente and tablero_jugador2[i][j] == AGUA:
                disparo = parsear_letra(j) + str(i) # Coordenada a mandar (y,x)
                resultado = # Llamar a función servidor
                match resultado:
                    case "AGUA":
                        tablero_jugador2[i][j] = "O"
                    case "YA DISPARADO":
                        pass
                    case "TOCADO":
                        tablero_jugador2[i][j] = "X"
                        target(tablero_jugador2,i,j)



def target(tablero_jugador2 : list[list[str]],fila_inicial : int,col_inicial : int):
    """
    Estrategia de 'target':
    - Empieza desde una casilla tocada (fila_inicial, col_inicial)
    - Va añadiendo a posiciones_barco_actual todas las 'X' que consiga de este barco
    - Cuando reciba 'HUNDIDO', llama a marcar_zona_muerta
    """
    hundido = False
    posiciones_barco_actual = [(fila_inicial, col_inicial)]
    while not hundido:
        fila_disparo, col_disparo = # TODO: LÓGICA DE LA ESTRATEGIA TARGET

        coord = parsear_letra(col_disparo) + str(fila_disparo)
        resultado = ...  # Llamada a servidor con coord

        match resultado:
            case "AGUA":
                tablero_jugador2[fila_disparo][col_disparo] = FALLO
            case "YA DISPARADO":
                pass
            case "TOCADO":
                tablero_jugador2[fila_disparo][col_disparo] = TOCADO
                posiciones_barco_actual.append((fila_disparo, col_disparo))
            case "HUNDIDO":
                tablero_jugador2[fila_disparo][col_disparo] = TOCADO
                posiciones_barco_actual.append((fila_disparo, col_disparo))
                marcar_zona_muerta(tablero_jugador2, posiciones_barco_actual)
                hundido = True

def marcar_zona_muerta(tablero_jugador2: list[list[str]],posiciones_barco_actual: list[tuple[int, int]]):
    """
    Marca como 'O' todas las casillas de agua (~) adyacentes
    (8 direcciones) a las posiciones del barco hundido.
    """
    for fila, columna in posiciones_barco_actual:
        for direccion_fila, direccion_columna in DIRECCIONES:
            nueva_fila = fila + direccion_fila
            nueva_columna = columna + direccion_columna
            if 0 <= nueva_fila < TAMAÑO_TABLERO and 0 <= nueva_columna < TAMAÑO_TABLERO:
                if tablero_jugador2[nueva_fila][nueva_columna] == AGUA:
                    tablero_jugador2[nueva_fila][nueva_columna] = FALLO


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
