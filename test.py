'''
def getQ_Domain(data):
    state = 0
    exceptLength = 0
    domainString =''
    domainParts = []
    x = 0    
    y = 0

    for byte in data:
        if state == 1:
            domainString += chr(byte)
            x +=1
            if x == exceptLength:
                domainParts.append(domainString)
                domainString = ''
                state = 0 
                x = 0
            if byte == 0:
                domainParts.append(domainString)
                break
        else:
            state = 1
            exceptLength = byte
        y +=1
    
    questionType = data [y:y+2]
    return (domainParts, questionType)
'''

def flags (flags):

    byte1 = flags[:1]

    QR = '1'

    OPCODE = ''
    for bit in range(1,5):
        OPCODE += str(ord(byte1)&(1<<bit)) # For checking the bits in the byte
    
    AA ='1'

    TC = '0'

    RD = '0'

    RA = '0'

    Z = '000'

    RC = '0000'

    return int(QR+OPCODE+AA+TC+RD,2).to_bytes(2, byteorder='big')+int(RA+Z+RC).to_bytes(2, byteorder='little')


def response(data):

    # Transaction ID
    TransactionID = data[:2]
    TID = ''
    for byte in TransactionID:
        TID += (hex(byte)[2:])
    
    # Flags
    Flags = flags(data[2:4])

    # QDCOUNT
    QDCOUNT = b'\x00\x01'

    # Answer Count
    
    ASCOUNT = b'\xc0\x0c\x01\x01\x00\x00\x01\x2c\x00\x04\x23\xba\xe0\x19'

    # Nameserver Count

    NSCOUNT = (0).to_bytes(2, byteorder='big')

    ARCOUNT = (0).to_bytes(2, byteorder='big')

    dnsheader = TransactionID+Flags+QDCOUNT+ASCOUNT+NSCOUNT+ARCOUNT
     
      



import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',53))

while True:
    data, addr = sock.recvfrom(1024)
    # print(data + '\n')
    # print(response(data))
    sock.sendto(b'', addr)
