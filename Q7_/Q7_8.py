from types import NoneType
from scapy.all import *
import time

domain = input("Domain: ")
scapy_domain = Net(domain)
global ttl
ttl = 0
run_time = time.time()

packet = IP(dst = scapy_domain)/ICMP()
response = IP(src = "0.0.0.0")/ICMP()

while(response[IP].src != scapy_domain):
    ttl = ttl + 1
    packet[IP].ttl = ttl
    response = sr1(packet,timeout=5)
    if (type(response) != NoneType):
        print (response[IP].src)
    else:
        response = IP(src = "0.0.0.0")/ICMP()
        print("Not Enough Information: IP Did not ditected")
    time.sleep(1)

print("Run Time " + str(run_time))