import socket  # noqa: F401


def big_endian(value):
    return value.to_bytes(4, byteorder="big")


def message(id):
    id_be = big_endian(id)
    len_be = big_endian(len(id_be))
    return len_be + id_be


def handle_client(client):
    client.recv(1024)
    client.sendall(message(7))
    client.close()


def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)

    while True:
        client, address = server.accept()
        handle_client(client)


if __name__ == "__main__":
    main()
