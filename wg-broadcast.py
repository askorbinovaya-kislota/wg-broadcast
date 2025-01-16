#!/usr/bin/python3
from scapy.all import *;

conf.verb = 0;

ips = [];
f = open("/etc/wireguard/wg0.conf", "r");

for line in f:
    if line.startswith("AllowedIPs"):
        ips.append(line.split("=")[1].strip().split("/")[0]);
f.close();
print("Listening for IPs: ", end="");
print(*ips, sep=", ");

def hook(pkt):
    if pkt[IP].dst == "255.255.255.255":
        print(pkt.summary());
        for ip in ips:
            if pkt[IP].src == ip: continue;
            pkt[IP].dst = ip;
            del pkt[IP].chksum;
            del pkt[UDP].chksum;
            try:
                send(pkt);
                print("+ forwarded to ", ip);
            except:
                pass;

sniff(iface="wg0", filter="udp", prn=hook);
