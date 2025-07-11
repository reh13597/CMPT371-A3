import socket
import time

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.178', 53333))
    print("Connected to the server at: ('192.168.1.178', 53333)")

    message = b"hello TCP\n"
    start_time = time.perf_counter()

    for i in range(1000):
        client_socket.send(message)
        print(f"Sent message #{i+1}.")

    print("1000 messages successfully sent.")

    response = client_socket.recv(256)
    end_time = time.perf_counter()
    rtt = end_time - start_time

    client_socket.close()

    print(f"SERVER: {response.decode()}\nRTT: {rtt:.10f} seconds\nDisconnected from the server.\n==========")

if __name__ == "__main__":
    tcp_client()

""" import socket
import time

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.178', 53333))
    print("Connected to the server at: ('192.168.1.178', 53333)")

    message = b"hello TCP"
    start_time = time.perf_counter()
    client_socket.sendall(message)
    print("Message successfully sent.")

    response = client_socket.recv(256)
    end_time = time.perf_counter()
    rtt = end_time - start_time

    client_socket.close()

    print(f"SERVER: {response.decode()}\nRTT: {rtt:.10f} seconds\nDisconnected from the server.\n==========")

if __name__ == "__main__":
    tcp_client() """
