#!/bin/sh
install -m755 -d /etc/kislota-cloud
install -m755 wg-broadcast.py /etc/kislota-cloud/wg-broadcast.py
install -m755 init.d/wg-broadcast /etc/init.d/wg-broadcast
