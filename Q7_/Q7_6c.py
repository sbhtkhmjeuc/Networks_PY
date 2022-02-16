from scapy.all import *

Destination = input("DST: ")

packet = IP(dst=Destination) / ICMP() / "Hii1"
packet2 = IP(dst=Destination) / ICMP() / "Hii2"

response = sr1([packet,packet2],timeout=5)
