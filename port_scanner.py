import socket
from datetime import datetime

# ================================================
# Python Port Scanner
# Author: Narasimha Mallegari
# Description: Scans ports 1-1024 on any target
#              IP address or domain name.
# Usage: python3 port_scanner.py
# Legal note: Only scan systems you own or have
#             explicit permission to test.
# ================================================

print("=" * 50)
print("  Python Port Scanner")
print("  github.com/narasimhamallegari")
print("=" * 50)

target = input("\nEnter IP address or domain to scan: ")

print("\nTarget:     " + target)
print("Scan range: Ports 1 to 1024")
print("Started:    " + str(datetime.now()))
print("-" * 50)

open_ports = []

for port in range(1, 1025):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("[OPEN]   Port " + str(port))
            open_ports.append(port)
        sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        break
    except socket.gaierror:
        print("Could not resolve hostname: " + target)
        break
    except socket.error:
        print("Could not connect to target.")
        break

print("-" * 50)
print("Scan complete.")
print("Total open ports: " + str(len(open_ports)))
if open_ports:
    print("Open ports found: " + str(open_ports))
else:
    print("No open ports found in range 1-1024.")
print("Finished:   " + str(datetime.now()))
