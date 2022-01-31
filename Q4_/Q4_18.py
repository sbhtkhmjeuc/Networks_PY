from asyncio import DatagramProtocol
import socket
DNS_SERVER_IP = '0.0.0.0'
DNS_SERVER_PORT = 53
DEFAULT_BUFFER_SIZE = 1024

def dns_handler(data, addr):
    data_array = data
    print(data_array)
    


def dns_udp_server(ip,port):
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((ip,port))
    print ("Server started Seccssfully! Waiting for Data...")
    while True:
        try:
            data,addr = server_socket.recvfrom(DEFAULT_BUFFER_SIZE)
            dns_handler(data, addr)
        except Exception:
            print("Client Expection! %s" % (str(Exception)))

def main():
    print("Starting UDP Server...")
    dns_udp_server(DNS_SERVER_IP, DNS_SERVER_PORT)

if __name__ == '__main__':
    main()