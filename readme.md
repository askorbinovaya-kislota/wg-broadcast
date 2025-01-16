# wg-broadcast

This simple script emulates IPv4 broadcast (255.255.255.255) functionality in
Wireguard™ networks, required by countless Windows and Linux games, that lack
direct IP connection option.

Written and tested on Alpine Linux.

Requirements: `apk add scapy`

This script assumes `/etc/wireguard/wg0.conf` file to parse addresses (edit it if
you use a different name).

You can test working broadcasts using scripts in `test/` directory 
