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
    - numeros identificativos barcos : posición que ocupa cada barco
    - X : tocado --> cuando todas las coordenadas de un barco sean igual a "X" se retornará "HUNDIDO"
    - O : disparo al agua
"""

def colocar_barcos(tablero: list[list], barcos:dict[int,dict[str,int]]):
    rango = 5
    barcos_disponibles = [key for key in barcos.keys()]
    orientaciones = ["Horizontal, Vertical"]
    orientacion = orientaciones[randint(0,1)]
    numero_barco_generado = choice(barcos_disponibles)
    max_inicio_barco = 8 - barcos[numero_barco_generado][]
    inicio_barco = randint(0,max_inicio_barco)
    if orientacion == "Horizontal":
        fila = randint(0,7)
        for j in range(inicio_barco,7):

    if orientacion == "Vertical":

def disparar():


def main():
    barcos = {
        1: {"Portaviones": 5},
        2: {"Acorazado": 4},
        3: {"Submarino": 3},
        4: {"Crucero": 3},
        5: {"Destructor": 2},
    }
    tablero_jugador1 = [
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],

    ]
    tablero_jugador2 = [
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
        ["~"],["~"],["~"],["~"],["~"],["~"],["~"],["~"],
    ]
    colocar_barcos(tablero_jugador1,barcos)

if __name__ == "__main__":
    main()
