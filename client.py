# Client-sided aplication using TCP protocol
# @author 333-333-333 (David Millar Sanhueza)
# [ICC337-1]

# Importing libraries
import socket
import threading
import sys
import os
import time

# Inicializating TCP socket on port 30303
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 30303))

# The function asks the user for both the string and the character
def ask_user():
    # Asks the user for the string
    string = input("String: ")
    # Asks the user for the character
    character = input("Character: ")

    # Returns the string and the character
    return string, character

# Takes both string and character, and returns an only string with the format
# "string;character"
def format_request(string, character):
    return string + ';' + character



# Sends the request to the server
def send_request(client, request):
    # Sends the request
    client.send(request.encode('utf-8'))


# Recieves the response from the server
def recieve_response(client):
    # Recieves the response
    response = client.recv(1024).decode('utf-8')
    # Returns the response
    return response

# Prints the response with the format "[Server hh:mm:ss] response"
def print_response(response):
    # Prints the response
    print("[Server " + time.strftime("%H:%M:%S") + "] " + response)

# Ask the user for the string and the character
string, character = ask_user()

# Formats the request
request = format_request(string, character)

# Sends the request
send_request(client, request)

# Recieves the response
response = recieve_response(client)

# Prints the response
print_response(response)

# Closes the connection
client.close()