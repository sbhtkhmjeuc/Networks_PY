from scapy.all import *

def MAC_Filter(packet):
    return Ether in packet and packet[Ether].dst == "dc:fb:48:1d:56:b9"

def print_mac(packet):
    print(packet[Ether].src)



###################################################################################

packets_MAC = sniff(count=4,lfilter=MAC_Filter,prn=print_mac,store=False)