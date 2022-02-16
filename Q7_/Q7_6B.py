from scapy.all import *

id = 0x01

packet1 = IP(dst = "www.facebook.com")/ICMP(id = id)/"Hi Facebook"
id = id + 1
packet2 = IP(dst = "www.facebook.com")/ICMP(id = id)/"Hi Facebook 2"

send(packet1)
send(packet2)
response_packets1 = sr1(packet1)
response_packets2 = sr1(packet2)
print(response_packets1.show() , response_packets2.show())
