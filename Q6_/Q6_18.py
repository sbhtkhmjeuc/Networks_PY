from scapy.all import *

syn_segment = TCP(dport=80, seq=123, flags='S')
syn_packet = IP(dst='www.google.com')/syn_segment
syn_ack_packet = sr1(syn_packet)
ack_segment = 1
ack_packet = IP(dst='www.google.com')/ack_segment
send(ack_packet)