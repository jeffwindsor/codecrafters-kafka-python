import socket  # noqa: F401
from .protocol import decode_request, encode_response


def handle_client(client):


def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)

    while True:
        client, address = server.accept()
        request_bytes = client.recv(2048)
        response_bytes = encode_response(decode_request(request_bytes))
        client.sendall(response_bytes)


if __name__ == "__main__":
    main()
