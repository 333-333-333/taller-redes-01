# Server-sided aplication using TCP protocol
# @author 333-333-333 (David Millar Sanhueza)
# [ICC337-1]

# Importing libraries
import socket
import threading
import sys
import os
import time

# Inicializating TCP socket on port 30303R
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 30303))

# The reason why server.listen() has 1 as an argue is because the server
# will only accept 1 client at a time. If the server has 1 as an argue,
# the server will accept 1 client, and the other clients will be in a queue
server.listen(1)

# Takes an string an a character: removes all the existences of the
# given character from the string
def remove_char(string, char):
    return string.replace(char, "")

# Recieves the client's request
def recieve_request(client):
    # Recieves the request
    request = client.recv(1024).decode('utf-8')
    # Returns the request
    return request

# Sends the response to the client
def send_response(client, response):
    # Sends the response
    client.send(response.encode('utf-8'))

# The recieved string from the client should have the format 
# "string;character".
# Validates the request: if the string has the format, returns True, else,
# returns False.
def validate_request(request):
    # Splits the string by the semicolon
    parsed = request.split(';')
    
    # If the array hasn't 2 elements, returns False
    if len(parsed) != 2:
        return False
    # If the second element of the array is not a character, returns False
    
    if len(parsed[1]) != 1:
        return False
    
    # Finally, returns True
    return True

# The function returns an array with the string and the character, both as 
# strings, and with the respective index 0 and 1 in the array
def parse_request(request):
    # Splits the string by the semicolon
    parsed = request.split(';')
    # Returns the array
    return parsed

# Starts a while loop that is always waiting for a client. If a client 
# connects, recieves the request, validates it, and sends the response
def start_server():
    # While loop
    while True:
        # Accepts the client
        client, address = server.accept()
        
        # Recieves the request
        request = recieve_request(client)
        # Validates the request
        valid = validate_request(request)
        
        # If the request is valid, sends the response
        if valid:
            # Parses the request
            parsed = parse_request(request)
            # Removes the character from the string
            response = remove_char(parsed[0], parsed[1])
            # Sends the response
            send_response(client, response)
        
        # If the request is not valid, sends an error message
        else:
            # Sends the error message
            send_response(client, "Error: invalid request")
        
        # Closes the connection
        client.close()

# Starts the server
start_server()