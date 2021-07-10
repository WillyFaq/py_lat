#!/usr/bin/env python3

# Import Python library
import networkscan

# Main function
if __name__ == '__main__':

    # Define the network to scan
    my_network = "192.168.1.0/24"

    # Create the object
    my_scan = networkscan.Networkscan(my_network)

    # Run the scan of hosts using pings
    my_scan.run()

    # Display the IP address of all the hosts found
    for i in my_scan.list_of_hosts_found:
        print(i)