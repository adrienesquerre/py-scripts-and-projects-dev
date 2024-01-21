import subprocess
import re
import ipaddress

def get_ip_and_subnet():
    try:
        # Run ipconfig command and capture the output
        # result = subprocess.check_output("cmd.exe /c ipconfig", shell=True).decode()
        result = subprocess.check_output(["cmd.exe", "/c", "ipconfig"], shell=True).decode()


        # Find the IPv4 Address and Subnet Mask
        ipv4_info = re.findall(r'IPv4 Address.*?: (\S+).*?Subnet Mask.*?: (\S+)', result, re.DOTALL)
        
        # Just take the first match (assuming single network interface for simplicity)
        if ipv4_info:
            ip, subnet_mask = ipv4_info[0]
            return ip, subnet_mask
        else:
            return None, None
    except Exception as e:
        return None, None

def calculate_cidr(ip, subnet_mask):
    # Combine the IP with the subnet mask to form a network address
    network = ipaddress.IPv4Network(f'{ip}/{subnet_mask}', strict=False)
    # Return the network in CIDR notation
    return str(network.with_prefixlen)

ip, subnet_mask = get_ip_and_subnet()
if ip and subnet_mask:
    cidr = calculate_cidr(ip, subnet_mask)
    print(f'Your network CIDR range is: {cidr}')
else:
    print('Unable to determine the network CIDR range.')
