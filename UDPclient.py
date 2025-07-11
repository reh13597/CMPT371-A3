import socket
import time

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = b"Hello UDP"
    start_time = time.perf_counter()

    for i in range(1000):
        client_socket.sendto(message, ('192.168.1.178', 53444))
        print(f"Sent message #{i+1}.")

    print("1000 messages successfully sent.")

    response, addr = client_socket.recvfrom(256)
    end_time = time.perf_counter()
    rtt = end_time - start_time

    print(f"SERVER: {response.decode()}\nServer sent from: {addr}\nRTT: {rtt:.10f} seconds\n==========")

if __name__ == "__main__":
    udp_client()

