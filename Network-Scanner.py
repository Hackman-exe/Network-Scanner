import nmap
import socket

#get your own local IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

#turn it into a subnet range e.g. 192.168.0.0/24
subnet = local_ip.rsplit('.', 1)[0] + '.0/24'

print(f"Scanning your network: {subnet}")
print("-" * 55)

#set up the scanner
scanner = nmap.PortScanner()
scanner.scan(hosts=subnet, arguments='-sn')

#print all devices found
for host in scanner.all_hosts():
    state = scanner[host].state()
    
    #grab manufacturer if available
    vendor = "Unknown"
    try:
        v = scanner[host].get('vendor', {})
        if v:
            vendor = list(v.values())[0]
    except:
        pass
        
    print(f"IP: {host:<16} Manufacturer: {vendor:<25} Status: {state}")

print("-" * 55)
print(f"Total devices found: {len(scanner.all_hosts())}")