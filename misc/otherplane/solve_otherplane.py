#!/usr/bin/python3
from scapy.all import *
import pyshark

pcap = pyshark.FileCapture('./otherplane.data')

counter = 0
captured_file = ''
for pkt in pcap:
    if pkt['IP'].src == '10.67.8.102':
        counter += 1
        if counter >= 3:
            captured_file += str(pkt['ICMP'].data)

file_raw = bytes.fromhex(captured_file)
outfile = open("captured_file", "wb")
outfile.write(file_raw)




