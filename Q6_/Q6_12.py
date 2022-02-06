from scapy.all import *

domain = input("Domain: ")
dns_packet = IP(dst='8.8.8.8')/UDP(sport=24601,dport=53)/DNS(qdcount=1,rd=1)/DNSQR(qname=str(domain))
response = sr1(dns_packet)
response.show()
print(response[DNSRR].rdata)
