import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 53444))
    print("Server is open on port 53444...")

    counter = 1
    while counter <= 1000:
        response, addr = server_socket.recvfrom(256)

        if response.decode() == "Hello UDP":
            print(f"{counter}. CLIENT: {response.decode()}")
            counter += 1

    message = b"back at you UDP"
    server_socket.sendto(message, addr)
    print(f"Client sent from: {addr}\nMessage successfully sent.\n==========")

if __name__ == "__main__":
    udp_server()

""" import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 53444))
    print("Server is open on port 53444...")

    while True:
        response, addr = server_socket.recvfrom(256)

        if response.decode() == "Hello UDP":
            print(f"CLIENT: {response.decode()}\nClient sent from: {addr}")
            message = b"back at you UDP"
            server_socket.sendto(message, addr)
            print("Message successfully sent.\n==========")

if __name__ == "__main__":
    udp_server() """