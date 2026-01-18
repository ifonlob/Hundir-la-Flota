"""TODO: Tablero 8x8. Barcos: 5 (Portaaviones), 4 (Acorazado), 3 (Submarino), 3 (Crucero), 3 (Destructor) 2 Coordenadas (letra,numero), numero: fila, letra, columna"""
from random import randint, choice

"""
TODO: 
--- Funciones mínimas ---
- colocar_barcos(tablero_jugador1 : list[list[Any]]
- disparar(tablero,fila,col) : String --> "AGUA" , "TOCADO" o "HUNDIDO"

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

def disparar(tablero: list[list], coord: str, barco_id : str):
    try:
        if len(coord) != 2:
            raise Exception("msg")
        elif coord[0] not in {"A", "B", "C", "D", "E", "F", "G", "H"}:
            raise Exception("msg")
        elif coord[1] not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
            raise Exception("msg")
    except Exception as err:
        print(f"[ERROR]: {err}")

    coord_parsed = [0, 0]

    coord_parsed[1] = int(coord[1]) - 1
    match coord[0]:
        case "A":
            coord_parsed[0] = 0
        case "B":
            coord_parsed[0] = 1
        case "C":
            coord_parsed[0] = 2
        case "D":
            coord_parsed[0] = 3
        case "E":
            coord_parsed[0] = 4
        case "F":
            coord_parsed[0] = 5
        case "G":
            coord_parsed[0] = 6
        case "H":
            coord_parsed[0] = 7



    #TODO: Implementar disparo cuando se tenga la logica de la posicion de los barcos
    # Desconocido: ~
    # Barco: X
    # Agua: O

    coord_tablero = tablero[coord_parsed[0]][coord_parsed[1]]
    if coord_tablero == "~":
        coord_tablero = "O"
        return "AGUA"
    elif coord_tablero == "0" or "x":
        return "YA DISPARADO"
    elif coord_parsed == " ":
        pass

    #TODO:
    # if coordenada == "0" or coordenada == "x"
    #     repite y da otra coordenada


    barco_id = coord_tablero
    coord_tablero = "X"
     

    return coordenadas_disparo



def actualizar_tablero_nuestro(tablero_jugador1, mensaje):
    accion, letra, numero = mensaje.split(",")


    tablero_jugador1 = [letra][numero]

    # tablero_jugador1 = [
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    # ]
    return tablero_jugador1


def actualizar_tablero_enemigo(tablero_jugador2, coordenadas_disparo, mensaje):

    letra, numero = coordenadas_disparo.split(",")

    accion, letra, numero = mensaje.split(",")

    tablero_jugador2[letra][numero] = accion

    # tablero_jugador2 = [
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    #     ["~", "~", "~", "~", "~", "~", "~", "~"],
    # ]
    return tablero_jugador2



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
        ["~","~","~","~","~","~","~","~"],
    ]

    for id_barco, tamaño_barco in barcos.items():
        colocar_un_barco(tablero_jugador1, tamaño_barco, id_barco)

if __name__ == "__main__":
    main()
