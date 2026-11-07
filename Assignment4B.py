
# Program Name: Assignment4B.py
# Course: IT3883/Section W07
# Student Name: Tavion Manior
# Assignment Number: Assignment 4
# Due Date: 11/6/2026
# Purpose: This program listens for a message from Program A.
# It converts the received message to uppercase and sends it
# back to Program A using a socket connection.
# Resources: Python socket documentation
import socket

# Set the server IP address and port number.
SERVER_IP = "127.0.0.1"
SERVER_PORT = 50000

# Create the server socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow the port to be reused.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # Connect the socket to the IP address and port.
    server_socket.bind((SERVER_IP, SERVER_PORT))

    # Listen for a connection from Program A.
    server_socket.listen(1)
    print("Program B is listening for Program A...")

    # Accept the connection.
    connection, client_address = server_socket.accept()

    with connection:
        print("Connected to:", client_address)

        # Receive the message from Program A.
        received_message = connection.recv(1024).decode("utf-8")
        print("Message received:", received_message)

        # Convert the message to uppercase.
        uppercase_message = received_message.upper()

        # Send the uppercase message back to Program A.
        connection.sendall(uppercase_message.encode("utf-8"))
        print("Response sent:", uppercase_message)

except OSError as error:
    print("A socket error occurred:", error)

finally:
    # Close the server socket.
    server_socket.close()
