#!/usr/bin/python3
import socket;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("0.0.0.0", 0));
sock.sendto(input("message to send: ").encode(), ("255.255.255.255", 50000));

print("message sent!");
