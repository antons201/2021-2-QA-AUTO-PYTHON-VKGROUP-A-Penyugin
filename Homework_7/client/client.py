import settings
import socket


class Client:

    def __init__(self):
        self.target_host = settings.MOCK_HOST
        self.target_port = int(settings.MOCK_PORT)
        self.client = None
        self.logger = None

    def create_client(self, client_logger):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(100)
        self.client.connect((self.target_host, self.target_port))
        self.logger = client_logger

    def send_request(self, request_type, params):
        self.logger.info("Request:\n")
        request = f'{request_type} {params} HTTP/1.1\r\nHost:{self.target_host}\r\nConnection: close\r\n\r\n'
        self.logger.info(request)

        self.client.send(request.encode())

    def get_response(self):
        total_data = []

        self.logger.info("Response:")

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        self.logger.info(data)
        return data
