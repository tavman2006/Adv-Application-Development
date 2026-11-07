# Program Name: Assignment4A.py
# Course: IT3883/Section W07
# Student Name: Tavion Manior
# Assignment Number: Assignment 4
# Due Date: 11/6/2026
# Purpose: This client program asks the user to enter a message and sends it
# to Program B through a socket. It then receives and prints the uppercase
# response sent back by the server.
# Resources: Python socket module documentation

import socket

# Set the server address and port.
SERVER_IP = "127.0.0.1"
SERVER_PORT = 50000

# Ask the user for a message to send to Program B.
message = input("Enter a message to send to Program B: ")

try:
    # Create a TCP socket and connect to Program B.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Send the message as bytes.
    client_socket.sendall(message.encode("utf-8"))

    # Receive the response and convert it back to a string.
    response = client_socket.recv(1024).decode("utf-8")
    print("Response from Program B:", response)

except ConnectionRefusedError:
    print("Could not connect. Make sure Program B is running first.")

except OSError as error:
    print("A socket error occurred:", error)

finally:
    # Close the socket when communication is finished.
    if "client_socket" in locals():
        client_socket.close()
