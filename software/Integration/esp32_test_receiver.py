import socket
from data_storage import shared_data

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind(('0.0.0.0', 65000))
        server_socket.listen()
        print("Server started, waiting for connection...")

        connection, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")

        while True:
            data = connection.recv(4096)
            if not data:
                print("No more data from", client_address)
                break

            decoded_data = data.decode('utf-8').strip()
            shared_data.update_data(decoded_data)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
        print("Connection with", client_address, "closed.")


