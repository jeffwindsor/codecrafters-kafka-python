import socket  # noqa: F401
import threading
from .protocol import decode_request, encode_response


def handle_client(client):
    while True:
        request_bytes = client.recv(2048)
        response_bytes = encode_response(decode_request(request_bytes))
        client.send(response_bytes)


def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)

    while True:
        client, _ = server.accept()
        t = threading.Thread(target=handle_client, args=(client,))
        t.start()


if __name__ == "__main__":
    main()
