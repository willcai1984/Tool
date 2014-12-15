#!/usr/bin/python
# Filename: arp.py
# Function: Look up the logs in big data file(more than 10G), classify them to city files 
# coding:utf-8
# Author: Will
import re
'''
Classify the big data log file to city1 or city2 file
For example
city1=1.0.0.0-100.255.255.255
city2=101.0.0.0-200.255.255.255
'''
def ip2city(log_file):
    c1_file = '/tmp/city1.log'
    c2_file = '/tmp/city2.log'
    c1_re = re.compile('^(\d|\d\d|100)\.\d+\.\d+\.\d+')
    c2_re = re.compile('^(10[1-9]|1[1-9]\d|200)\.\d+\.\d+\.\d+')
    c1_o = open(c1_file, 'wb')
    c2_o = open(c2_file, 'wb')
    with open(log_file, 'rb') as f_o:
        for i in f_o:
            if c1_re.search(i):
                c1_o.write(i)
            elif c2_re.search(i):
                c2_o.write(i)
            else:
                continue
    c1_o.close()
    c2_o.close()

'''
Transfer ip to int32
For example:
0.0.0.1 = 1
0.0.1.0 = 256
0.1.0.0 = 65536
...
>>> ip2str('192.168.1.1')
3232235777

int range
>>> import sys
>>> sys.maxint
9223372036854775807
'''
def ip2int(ip):
    ip_list = re.findall('\d+', ip)
    if ip_list:
        ip4 = ip_list[0]
        ip3 = ip_list[1]
        ip2 = ip_list[2]
        ip1 = ip_list[3]
        return int(ip1) + int(ip2) * 256 + int(ip3) * 256 * 256 + int(ip4) * 256 * 256 * 256

'''
Transfer int32 to ip
For example:
1      = 0.0.0.1
256    = 0.0.1.0
65536  = 0.1.0.0
...
>>> int2ip(a)
'192.168.1.1'
>>> ip2int('192.168.1.1')
3232235777
>>> int2ip(3232235777)
'192.168.1.1'
>>> 
'''
def int2ip(int32):
    int32 = int(int32)
    ip1 = int32 % 256
    ip2 = (int32 / 256) % 256
    ip3 = (int32 / (256 * 256)) % 256
    ip4 = (int32 / (256 * 256 * 256)) % 256
    return '%s.%s.%s.%s' % (ip4, ip3, ip2, ip1)

'''
Long list, such as 10w parameters, some of parameters appear multiple times
Find these parameters
'''
def more_para(o_list):
    pass
    

