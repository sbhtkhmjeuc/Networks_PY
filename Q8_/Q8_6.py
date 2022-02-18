from scapy.all import *



def checking_mac(mac):

    chars = "123456789abcdefABCDEF"
    flag = 0

    if (len(mac) != 6): 
        return "Invalid"
    else:
        for couple in mac:
            if (len(couple) != 2):
                return "Invalid"
            else:
                for letter in couple:
                    for char in chars:
                        if (letter != char):
                            flag = 1
                        else:
                            flag = 0
                            break 

        if (flag == 0): return "Valid"
        else: return "Invalid"

client_mac = input('Enter Your MAC Address: ')
client_mac = client_mac.split(':')

print(checking_mac(client_mac))
