import ipaddress
import socket
import time
import uuid


def obtener_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        mi_ip = s.getsockname()[0]
    finally:
        s.close()
    return mi_ip

def calcular_broadcast():
    ip = obtener_ip()
    red = ipaddress.IPv4Network(ip + "/24", strict=False)
    return str(red.broadcast_address)



def buscar_oponente():
    puerto = 4000
    nombre = "Cris"
    mi_id = str(uuid.uuid4())
    mi_ip = obtener_ip()
    dir_broadcast = calcular_broadcast()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", puerto))
    sock.settimeout(1.0)

    estado = "ESPERANDO"
    oponente = None

    print(f"Buscando en red... Mi IP: {mi_ip}")


    while estado == "ESPERANDO":
        msg = f"DESCUBRIR;{mi_id};{nombre}"
        sock.sendto(msg.encode(), (dir_broadcast, puerto))

        try:
            data, addr = sock.recvfrom(1024)
            msg = data.decode()
            ip, _ = addr
            partes = msg.split(";")

            if partes[0] == "DESCUBRIR":
                otro_id, otro_nombre = partes[1], partes[2]

                if otro_id != mi_id and mi_id < otro_id:
                    print(f"Aceptando a {otro_nombre}...")
                    reply = f"ACEPTADO;{mi_id};{nombre}"
                    sock.sendto(reply.encode(), addr)
                    oponente = (otro_nombre, ip)
                    estado = "JUGANDO"

            elif partes[0] == "ACEPTADO":
                _, otro_id, otro_nombre = partes
                print(f"{otro_nombre} me ha aceptado")
                oponente = (otro_nombre, ip)
                estado = "JUGANDO"

        except socket.timeout:
            pass

        if estado == "ESPERANDO":
            time.sleep(1)

    sock.close()
    return oponente



def servidor():
    ip = obtener_ip()

    host = ip
    puerto = 4000

    #aqui hay que añadir una forma de que no empieze uno siempre, o no dado k el host es aleatorio de momento
    mi_turno = True
    partida_activa = True

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, puerto))
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

                    mi_turno = False
                else:
                    data = conn.recv(1024).decode().strip()
                    accion, letra, numero = data.split(",")

                    print(f"Disparo recibido: {letra},{numero}")

                    # lógica del jeugo
                    resultado = "agua"
                    conn.sendall(f"respuesta,{resultado}\n".encode())

                    mi_turno = True






def cliente(rival):

    ip_rival = rival[1]

    HOST = ip_rival
    PORT = 4000

    mi_turno = False

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado al servidor")

        while True:
            if mi_turno:
                disparo = input("Tu disparo (ej A,1): ")
                s.sendall(f"disparo,{disparo}\n".encode())

                respuesta = s.recv(1024).decode().strip()
                accion, resultado = respuesta.split(",")
                #esto hay que mirarlo para mirar la accion
                print("Resultado:", resultado)

                mi_turno = False
            else:
                datos_mensaje = s.recv(1024).decode().strip()
                accion, letra, numero = datos_mensaje.split(",")

                print(f"Disparo recibido: {letra},{numero}")

                #logica del juego
                resultado = "agua"
                s.sendall(f"respuesta,{resultado}\n".encode())

                mi_turno = True


def main():
    rival = buscar_oponente()
    print(f"Conexión establecida con: {rival}")

    print("\n")


    #TODO mirar esto para que sea aleatorio
    servidor()
    # cliente(rival)





if __name__ == "__main__":
    main()
