from scapy.all import *

def filter(packet):
    return ICMP in packet and IP in packet and packet[ICMP].type == 0


Destination = input("DST: ")
PNumber = int(input("Number OF Packets: "))
packet = IP(dst=Destination) / ICMP() / "Hii1"

send(packet,count=PNumber)
response = sniff(count=PNumber,lfilter=filter)
print(response.show())


