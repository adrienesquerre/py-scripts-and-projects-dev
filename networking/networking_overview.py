import subprocess
import re
import socket
import struct
             
# WINDOWS commands used in this script:
# To find the Default Gateway: route print 
# Displays full configuration information for all network interfaces: ipconfig /all
# Displays the IP configuration for all network interfaces: ipconfig
# Nmap port scanner (not used in script): nmap -sT -T4 -p 21-25,80,443 192.168.0.0/24
             

# MACBOOK/LINUX
# def get_default_gateway():
#     try:
#         result = subprocess.check_output("netstat -nr | grep default", shell=True).decode()
#         return re.search(r"default\s+(\S+)", result).group(1)
#     except Exception as e:
#         return str(e)

# WINDOWS
def get_default_gateway():
    try:
        result = subprocess.check_output("route print", shell=True).decode()
        lines = result.split('\n')
        default_gateway = None
        for line in lines:
            if '0.0.0.0' in line and not default_gateway:
                default_gateway = line.split()[-3]  # Adjusted logic to get the first occurrence
                break
        return default_gateway
    except Exception as e:
        return str(e)

# MACBOOK/LINUX
# def get_dns_servers():
#     try:
#         with open('/etc/resolv.conf', 'r') as file:
#             content = file.readlines()
#         return [line.split()[-1] for line in content if line.startswith('nameserver')]
#     except Exception as e:
#         return str(e)

# WINDOWS    
def get_dns_servers():
    try:
        result = subprocess.check_output("ipconfig /all", shell=True).decode()
        
        # Print the raw output for debugging
        print("Raw ipconfig /all output for DNS section:")
        print(result)
        
        # Find all occurrences of DNS server listings
        dns_servers = re.findall(r"DNS Servers[\s\S]*?:\s*([\d\.]+)", result)

        # Return a list of unique DNS server IPs
        return list(set(dns_servers))
    except Exception as e:
        return str(e)

# MACBOOK/LINUX
# def get_ip_and_subnet():
#     try:
#         result = subprocess.check_output("ifconfig", shell=True).decode()
#         interfaces = re.findall(r"(\w+): flags", result)
#         ips = re.findall(r"inet (\S+) netmask (\S+)", result)
#         return dict(zip(interfaces, ips))
#     except Exception as e:
#         return str(e)

# WINDOWS
def get_ip_and_subnet():
    try:
        result = subprocess.check_output("ipconfig", shell=True).decode()
        interfaces = re.findall(r"(\w+ \w+ Adapter [\w\s]+):", result)
        ips = re.findall(r"IPv4 Address.*?: (\S+)", result)
        subnets = re.findall(r"Subnet Mask.*?: (\S+)", result)
        return dict(zip(interfaces, zip(ips, subnets)))
    except Exception as e:
        return str(e)

def hex_to_decimal_netmask(hex_netmask):
    hex_netmask = hex_netmask.lstrip('0x').zfill(8)
    return '.'.join(str(int(hex_netmask[i:i+2], 16)) for i in range(0, 8, 2))

def main():
    print("\n===============================================")
    print("NETWORK CONFIGURATION REPORT")
    print("===============================================")
    print("This report shows the default gateway, DNS servers, and IP configurations of network interfaces.")
    print(f"DNS Servers: {', '.join(get_dns_servers())}")
    print(f"Default Gateway: {get_default_gateway()}")

    ip_subnet_info = get_ip_and_subnet()
    for interface, (ip, netmask) in ip_subnet_info.items():
        print(f"\nInterface: {interface}")
        print(f"IP Address: {ip}")
        print(f"Subnet Mask: {hex_to_decimal_netmask(netmask)}")

if __name__ == "__main__":
    main()
