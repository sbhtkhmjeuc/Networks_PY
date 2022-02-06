from scapy.all import *

mes = input("Message: ")
for letter in mes:
    mes_packet = IP(dst='127.0.0.1')/UDP(dport=ord(letter))
    send(mes_packet)
    print (mes_packet[UDP].dport)

