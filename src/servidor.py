
import socket

def start_server():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"[Servidor] Escuchando en {host}:{port}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[Servidor] Conectado por {addr}")
                while True:
                    data = conn.recv(1024).decode('utf-8')
                    if not data:
                        break
                    print(f"[Servidor] Mensaje recibido: {data}")
                    if data.strip().upper() == "DESCONEXION":
                        print("[Servidor] Cliente desconectado.")
                        break
                    conn.sendall(data.upper().encode('utf-8'))

if __name__ == "__main__":
    start_server()
    input("Presiona Enter para cerrar el servidor...")