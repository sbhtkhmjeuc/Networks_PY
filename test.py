import socket

IP = '0.0.0.0'
PORT = 80
SOCKET_TIMEOUT = 0.1

def validate_http_request(request):

    valid_http = True
    request_array = request.rsplit()
    if request_array[0].decode() != "GET":
        valid_http = False
    if request_array[2].decode() == "HTTP/1.1":
        valid_http = False

    resource = request_array[1].decode()
    resource = resource.replace('/','\\')
    return valid_http, resource

def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    client_socket.send(FIXED_RESPONSE.encode())

    while True:
        client_request = client_socket.recv(2048)
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')
            break

    print('Closing connection')
    client_socket.close()


def main():
    # Open a socket and loop forever while waiting for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()