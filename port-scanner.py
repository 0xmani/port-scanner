#!/usr/bin/env python3

import socket
import subprocess
import sys
from datetime import datetime
import concurrent.futures

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("{}/tcp Open".format(port))
        sock.close()
    except Exception as e:
        pass


if len(sys.argv) != 2:
    print("Usage: {} <remote host>".format(sys.argv[0]))
    sys.exit(1)

remoteServer = sys.argv[1]
remoteServerIP = socket.gethostbyname(remoteServer)


print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(scan_port, range(1, 65535))

t1 = datetime.now()
t2 = datetime.now()
total = t2 - t1


print('Scanning Completed in: ', total)
