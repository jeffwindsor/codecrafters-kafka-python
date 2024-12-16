import socket  # noqa: F401
from protocol import Response, decode_request, encode_response


def handle_request(req_str: str) -> str:
    request = decode_request(req_str)
    response = Response(0, request.correlation_id)
    return encode_response(response)


def handle_client(client):
    client.sendall(handle_request(client.recv(1024)))
    client.close()


def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)

    while True:
        client, address = server.accept()
        handle_client(client)


if __name__ == "__main__":
    main()
