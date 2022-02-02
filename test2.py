from scapy.all import *
import socket

def dns_filter(packet):
    return (scapy.DNS in packet and packet[scapy.DNS].opcode == 0 and packet[scapy.DNSQR].qtype == 1)

print('Starting to Sniff !!')
scapy.sniff(count = 1, lfilter = dns_filter)        