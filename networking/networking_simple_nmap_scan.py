import nmap
import subprocess
import re

def perform_nmap_scan():
    nm = nmap.PortScanner()
    # SIMPLE COMMAND: nmap -sT -T4 -p 21-25,80,443 192.168.0.0/24
    # nm.scan('192.168.0.0/24', '21-25,80,443', arguments='-sT -T4')
    nm.scan('192.168.0.0/24', '21-25,80,443', arguments='-sT -T4')


    for host in nm.all_hosts():
        print("\n--------------------------------------------------", flush=True)
        print(f"Host: {host} ({nm[host].hostname()})", flush=True)
        print(f"State: {nm[host].state()}", flush=True)
        print("--------------------------------------------------", flush=True)

        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto.upper()}", flush=True)
            print("Port\tState\tService", flush=True)

            for port in nm[host][proto]:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                print(f"{port}\t{state}\t{service}", flush=True)
                
# WINDOWS using SUBPROCESS
# def perform_nmap_scan():
#     try:
#         # Define the nmap command
#         nmap_cmd = ['nmap', '-sT', '-T4', '-p', '21-25,80,443', '192.168.0.1']

#         # Run the nmap command and capture the output
#         nmap_output = subprocess.check_output(nmap_cmd).decode()

#         # Print the output
#         print(nmap_output)

#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred while running nmap: {e}")

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
                
def main():
    print("===============================================", flush=True)
    print("NETWORK SCANNING REPORT", flush=True)
    print("===============================================", flush=True)
    print("This report provides information about the state of network hosts and their open ports.", flush=True)
    perform_nmap_scan()


if __name__ == "__main__":
    main()