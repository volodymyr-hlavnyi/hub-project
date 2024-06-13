import ipaddress

network = ipaddress.IPv4Network('192.168.0.0/16')
for ip in network:
    print(ip)


