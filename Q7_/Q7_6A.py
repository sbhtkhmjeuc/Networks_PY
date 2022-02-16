from scapy.all import *

packet = IP(dst = "www.facebook.com")/ICMP(id = 0x01)/"Hi Facebook"
response_packet = sr1(packet)
print(response_packet.show())



