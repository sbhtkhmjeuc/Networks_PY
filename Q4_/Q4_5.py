# TO DO: import modules
import socket

# TO DO: set constants
IP = '127.0.0.1'
PORT = 8020
SOCKET_TIMEOUT = 0.1


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client """
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    data = "HTTP/1.1 200 OK\r\n"
    data += "Content-Type: text/html; charset=utf-8\r\n"
    data += "\r\n"
    if resource == "\calculate-next":
        data += "5"
    else:
        data += "Hello"
    client_socket.send(data.encode())
    return None


def validate_http_request(request):
    valid_http = True
    request_array = request.decode().rsplit()
    print(request_array)
    if request_array[0] != "GET":
        valid_http = False
    if request_array[2] != "HTTP/1.1":
        valid_http = False

    resource = request_array[1]
    resource = resource.replace('/', '\\')
    return valid_http, resource


def handle_client(client_socket):
    print('Client connected')
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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()