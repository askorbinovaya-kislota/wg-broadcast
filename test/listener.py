#!/usr/bin/python3
import socket;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
sock.bind(("0.0.0.0", 50000));

print("Listening for broadcast packets on port 50000...");

while True:
    data, addr = sock.recvfrom(1500);
    print(f"Received message: {data.decode()} from {addr}");
