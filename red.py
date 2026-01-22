import ipaddress
import socket
import time
import uuid

#esto es para prueba
import random
tocado_agua = ("tocado", "agua")
#---

def obtener_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        mi_ip = s.getsockname()[0]
    finally:
        s.close()

    return mi_ip


def calcular_broadcast():
    # RED
    return str(ipaddress.IPv4Network(obtener_ip() + "/24", strict=False).broadcast_address)


def buscar_oponente(nombre: str, puerto: int = 4000):
    mi_id = str(uuid.uuid4())
    dir_broadcast = calcular_broadcast()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", puerto))
    sock.settimeout(1.0)

    estado = "ESPERANDO"
    soy_host = False

    print(f"Buscando en red... Mi IP: {obtener_ip()}")


    # TODO [GONZALO]: Posible mejora:
    while estado == "ESPERANDO":
        msg = f"DESCUBRIR;{mi_id};{nombre}"
        sock.sendto(msg.encode(), (dir_broadcast, puerto))

        try:
            data, addr = sock.recvfrom(1024)
            ip, _ = addr
            modo, otro_id, otro_nombre = data.decode().split(";")

            if modo == "DESCUBRIR":
                if otro_id != mi_id and mi_id < otro_id:
                    print(f"ACEPTADO: {otro_nombre}")

                    sock.sendto(f"ACEPTADO;{mi_id};{nombre}".encode(), addr)
                    oponente = otro_nombre
                    ip_oponente = ip
                    estado = "JUGANDO"
                    soy_host = True

                    print(f"Aceptando a {otro_nombre}...")
                else:
                    print(f"Esperando respuesta {nombre}")

            elif modo == "ACEPTADO":
                print(f"{otro_nombre} me ha aceptado")

                oponente = otro_nombre
                ip_oponente = ip
                estado = "JUGANDO"
                soy_host = False

        except socket.timeout:
            pass

        if estado == "ESPERANDO":
            time.sleep(1)

    sock.close()
    return oponente, ip_oponente, soy_host


def servidor(puerto: int = 4000):
    #TODO: Mirar que sea aleatorio
    #TODO: Aqui hay que añadir una forma de que no empieze uno siempre, o no dado k el host es aleatorio de momento
    #TODO: [GONZALO] Esto habria que discutirlo con el otro grupo

    mi_turno = True
    partida_activa = True

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((obtener_ip(), puerto))
        s.listen(1)
        print("Esperando jugador...")

        conn, addr = s.accept()
        print("Conectado:", addr)

        with conn:
            while partida_activa:
                if mi_turno:
                    disparo = input("Tu disparo (ej A,1): ")
                    mensaje = f"disparo,{disparo}"
                    conn.sendall((mensaje + "\n").encode())

                    respuesta = conn.recv(1024).decode().strip()
                    accion, resultado = respuesta.split(",")
                    # esto hay que mirarlo para mirar la accion
                    print("Resultado:", resultado)

                    if resultado == "tocado":
                        mi_turno = True
                    else:
                        mi_turno = False
                else:
                    data = conn.recv(1024).decode().strip()
                    accion, letra, numero = data.split(",")

                    print(f"Disparo recibido: {letra},{numero}")

                    # lógica del jeugo
                    resultado = random.choice(tocado_agua)
                    conn.sendall(f"respuesta,{resultado}\n".encode())

                    if resultado == "tocado":
                        mi_turno = False
                    else:
                        mi_turno = True


def cliente(rival: tuple[str, int], puerto: int = 4000):
    mi_turno = False

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((rival[1], puerto)) # rival[1] seria el host
        print("Conectado al servidor")

        while True:
            if mi_turno:
                disparo = input("Tu disparo (ej A,1): ")
                s.sendall(f"disparo,{disparo}\n".encode())

                respuesta = s.recv(1024).decode().strip()
                accion, resultado = respuesta.split(",")

                #TODO: Esto hay que mirarlo para mirar la accion
                print("Resultado:", resultado)

                if resultado == "tocado":
                    mi_turno = True
                else:
                    mi_turno = False
            else:
                datos_mensaje = s.recv(1024).decode().strip()
                accion, letra, numero = datos_mensaje.split(",")

                print(f"Disparo recibido: {letra},{numero}")

                resultado = random.choice(tocado_agua)
                # Mirar
                s.sendall(f"respuesta,{resultado}\n".encode())

                if resultado == "tocado":
                    mi_turno = False
                else:
                    mi_turno = True

        # TODO: [GONZALO] No faltaria romper el bucle en funcion de una variable?


# =====================================================================
# TODO [GONZALO]: Como gran parte del codigo de Cliente y Servidor se repite, propongo una funcion comun:
def bucle_cliente_servidor(conn, mi_turno: bool):
    partida = True
    try:
        while partida:
            if mi_turno:
                disparo = input("Tu disparo (ej A,1): ")
                mensaje = f"disparo,{disparo}"
                conn.sendall((mensaje + "\n").encode())

                respuesta = conn.recv(1024).decode().strip()
                accion, resultado = respuesta.split(",")
                # esto hay que mirarlo para mirar la accion
                print("Resultado:", resultado)

                mi_turno = False
            else:
                data = conn.recv(1024).decode().strip()
                accion, letra, numero = data.split(",")

                print(f"Disparo recibido: {letra},{numero}")

                # lógica del jeugo
                resultado = "agua"
                conn.sendall(f"respuesta,{resultado}\n".encode())

                mi_turno = True
    except ConnectionResetError:  # Supuestamente esta es la excepcion de desconexion que he encontrado
        print("\n[ERROR]: Desconexion")
    finally:
        print("\nFin de la conexion")


def iServidor(puerto: int = 4000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((obtener_ip(), puerto))
        s.listen(1)
        print("Esperando jugador...")

        conn, addr = s.accept()
        print("Conectado:", addr)

        with conn:
            print(f"CONECTADO: {addr}")
            bucle_cliente_servidor(conn, True)


def iCliente(rival: tuple[str, int], puerto: int = 4000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_conn:
        print(f"CONECTADO SERVIDOR: {rival[0]} {rival[1]}")

        time.sleep(1)
        s_conn.connect((rival[1], puerto))  # rival[1] seria el host
        bucle_cliente_servidor(s_conn, False)
# =====================================================================


def main():
    puerto = 4000
    nombre = "Cris"

    # cliente(rival, puerto)

    nombre_rival, ip_rival, soy_el_host = buscar_oponente(nombre, puerto)

    print(f"PARTIDA ENCONTRADA: {nombre} VS {nombre_rival}\n")

    if soy_el_host:
        print(f"[HOST]: {nombre} {obtener_ip()} (YO)")
        print(f"[CLIENTE]: {nombre_rival} {ip_rival}")
        servidor(puerto)
        # iServidor(puerto)
    else:
        print(f"[HOST]: {nombre_rival} {ip_rival}")
        print(f"[CLIENTE]: {nombre} {obtener_ip()} (YO)")
        time.sleep(1)
        cliente((nombre_rival, ip_rival), 4000)
        # iCliente((nombre_rival, ip_rival), 4000)

    # TODO: [GONZALO]
    # Hay que hacer una estructura de ejecucion correcta, posiblemente reste nota. Ademas he simplificado diversas funciones
    # porque habia variables que solo se usaban 1 vez o se asignaban a si mismas, eso a Jose no le gusta.


if __name__ == "__main__":
    main()
