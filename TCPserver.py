import socket

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 53333))
    server_socket.listen(1)
    print("Server is listening on port 53333...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client has connected from: {addr}")

        file = client_socket.makefile('r')

        counter = 1
        while counter <= 1000:
            line = file.readline()

            if not line:
                break
            if line.strip() == "hello TCP":
                print(f"{counter}. CLIENT: {line.strip()}")
                counter += 1

        client_socket.sendall(b"back at you TCP")
        client_socket.close()
        print("Message successfully sent & client disconnected.\n==========")

if __name__ == "__main__":
    tcp_server()

""" import socket

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 53333))
    server_socket.listen(1)
    print("Server is listening on port 53333...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client has connected from: {addr}")

        response = client_socket.recv(256)

        if response.decode() == "hello TCP":
            print(f"CLIENT: {response.decode()}")
            client_socket.sendall(b"back at you TCP")

        client_socket.close()

        print("Message successfully sent & client disconnected.\n==========")

if __name__ == "__main__":
    tcp_server() """