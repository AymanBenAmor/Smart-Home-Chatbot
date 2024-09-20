import socket


def send_command(data_to_send):
    # IP address and port of the ESP32
    ESP32_IP = "192.168.179.141"  # Change this to your ESP32's IP address
    ESP32_PORT = 12345  # Change this to the port you chose in the ESP32 code

    # Create a TCP/IP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the ESP32 server
    client_socket.connect((ESP32_IP, ESP32_PORT))

    # Send data to the ESP32


    client_socket.sendall(data_to_send.encode())

    # Close the socket
    client_socket.close()
