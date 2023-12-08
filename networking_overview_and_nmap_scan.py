import nmap
import subprocess
import re
import socket
import struct

def perform_nmap_scan():
    nm = nmap.PortScanner()
    nm.scan('10.196.200.0/23', '21-25,80,443,22', arguments='-sT -T4')

    for host in nm.all_hosts():
        print("\n--------------------------------------------------")
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        print("--------------------------------------------------")

        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto.upper()}")
            print("Port\tState\tService")

            for port in nm[host][proto]:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                print(f"{port}\t{state}\t{service}")

def get_default_gateway():
    try:
        result = subprocess.check_output("netstat -nr | grep default", shell=True).decode()
        return re.search(r"default\s+(\S+)", result).group(1)
    except Exception as e:
        return str(e)

def get_dns_servers():
    try:
        with open('/etc/resolv.conf', 'r') as file:
            content = file.readlines()
        return [line.split()[-1] for line in content if line.startswith('nameserver')]
    except Exception as e:
        return str(e)

def get_ip_and_subnet():
    try:
        result = subprocess.check_output("ifconfig", shell=True).decode()
        interfaces = re.findall(r"(\w+): flags", result)
        ips = re.findall(r"inet (\S+) netmask (\S+)", result)
        return dict(zip(interfaces, ips))
    except Exception as e:
        return str(e)

def hex_to_decimal_netmask(hex_netmask):
    hex_netmask = hex_netmask.lstrip('0x').zfill(8)
    return '.'.join(str(int(hex_netmask[i:i+2], 16)) for i in range(0, 8, 2))

def main():
    print("===============================================")
    print("NETWORK SCANNING REPORT")
    print("===============================================")
    print("This report provides information about the state of network hosts and their open ports.")
    perform_nmap_scan()

    print("\n===============================================")
    print("NETWORK CONFIGURATION REPORT")
    print("===============================================")
    print("This report shows the default gateway, DNS servers, and IP configurations of network interfaces.")
    print(f"Default Gateway: {get_default_gateway()}")
    print(f"DNS Servers: {', '.join(get_dns_servers())}")

    ip_subnet_info = get_ip_and_subnet()
    for interface, (ip, netmask) in ip_subnet_info.items():
        print(f"\nInterface: {interface}")
        print(f"IP Address: {ip}")
        print(f"Subnet Mask: {hex_to_decimal_netmask(netmask)}")

if __name__ == "__main__":
    main()
