import socket  # noqa: F401
from .protocol import Response, decode_request, encode_response


def handle_request(req_str: str) -> str:
    request = decode_request(req_str)
    response = encode_response(Response(0, request.correlation_id))
    print(response)
    return response


def handle_client(client):
    req_str = client.recv(1024)
    print(req_str)
    resp_str = handle_request(req_str)
    print(resp_str)
    client.sendall(resp_str)
    client.close()


def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)

    while True:
        client, address = server.accept()
        handle_client(client)


if __name__ == "__main__":
    main()
