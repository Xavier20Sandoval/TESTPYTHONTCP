
import unittest
import socket
import threading

def start_test_server():
    from servidor import start_server
    threading.Thread(target=start_server, daemon=True).start()

class TestTCPCommunication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        start_test_server()

    def test_normal_message(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 5000))
            s.sendall(b'hello server')
            data = s.recv(1024)
            self.assertEqual(data.decode('utf-8'), 'HELLO SERVER')

    def test_disconnect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 5000))
            s.sendall(b'DESCONEXION')
            data = s.recv(1024)
            self.assertEqual(data, b'')

if __name__ == '__main__':
    unittest.main()
