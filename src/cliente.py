
import socket

def start_client():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("[Cliente] Conectado al servidor.")

        while True:
            mensaje = input("[Cliente] Ingresa un mensaje: ")
            s.sendall(mensaje.encode('utf-8'))

            if mensaje.strip().upper() == "DESCONEXION":
                print("[Cliente] Desconectando...")
                break

            data = s.recv(1024).decode('utf-8')
            print(f"[Cliente] Servidor responde: {data}  CLIENTE")

if __name__ == "__main__":
    start_client()
    input("Presiona Enter para cerrar el servidor...")