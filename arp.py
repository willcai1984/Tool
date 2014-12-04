#!/usr/bin/python
# Filename: arp.py
# Function: Send large number of arp pkts in a short time
# coding:utf-8
# Author: Will
# argv0:dst_ip
# argv1:loop
# Example: send inc arp pkts 8k to 10.155.3.222
# python arp.py  10.155.3.222 8000


from scapy.all import *
import sys

def main():
    input_list = sys.argv
    dst_ip = input_list[1]
    loop = input_list[2]

    for i in range(int(loop)):
        mac_ip1 = (i + 1) / 200
        mac_ip2 = (i + 1) % 200
        src_ip = "192.168.%s.%s" % (mac_ip1, mac_ip2)
        mac = "000c%04d%04d" % (mac_ip1, mac_ip2)
        src_mac = mac[:2] + ':' + mac[2:4] + ':' + mac[4:6] + ':' + mac[6:8] + ':' + mac[8:10] + ':' + mac[10:]
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src=src_mac) / ARP(pdst=dst_ip, hwdst="00:00:00:00:00:00", psrc=src_ip, hwsrc=src_mac)
        sendp(pkt)
        print "SrcIP %s, SrcMac %s done" % (src_ip, src_mac)

    return True
            
if __name__ == '__main__':
    exec_result = main()
    if exec_result:
        sys.exit(0)
    else:
        sys.exit(1)
