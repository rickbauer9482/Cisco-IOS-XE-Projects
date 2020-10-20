#!/bin/python

# python module import
from random import randint
import ipaddress 

# Variables
max_mask = 27
max_ip = 254
class_max_a = 126
class_max_b = 191
class_max_c = 223

# User input for number of subnets to create
print("Basic router configuration script that creates a variable number or Loopbacks")
print("and creates the basic BGP routing process with the ASN you provide")
val = input ("How many networks to create: ")
bgp_asn = input ("AS# for your router: ")
file_name = input ("File Name for the output: ")

# set up the counter for the while loop
n = int(val)
i = 0
c = 0

# define the lists to work with
bgp_list = []
interface_list = []

# work to be done - randomly generate Internet Address and Subnet
with open(str(file_name) + '.txt', 'w') as file1:
    while i <= n:
        oct_1 = randint(1, class_max_c)
        oct_2 = randint(1, max_ip)
        oct_3 = randint(1, max_ip)
        oct_4 = randint(1, max_ip)

        if oct_1 < class_max_a and oct_1 != 127:
            mask = randint(9, max_mask)
        elif oct_1 < class_max_b and oct_1 != 127:
            mask = randint(17, max_mask)
        else:
            mask = randint(25, max_mask)

        subnet = (str(oct_1) + "." + str(oct_2) + "." + str(oct_3) + "." + str(oct_4) + "/" + str(mask))
        # bits = ("/"+ str(mask))
        net4 = ipaddress.IPv4Network(subnet, False)
        interface = ipaddress.IPv4Interface(subnet)

        # print (subnet)
        # print (bits)
        bgp_list.append(net4.with_netmask)
        interface_list.append(interface.with_netmask)
        
        # Increase the counter by 1 for each loop
        # print(i)
        i = i+1

    # Write stuff to the file
    for a in range(len(interface_list)):
        file1.write('interface loopback' + str(c+100) + '\n')
        file1.write('description Auto-created from python script\n') 
        file1.write('ip address ' + interface_list[a].replace ('/', ' ') + '\n')
        file1.write('!\n')
        c = c+1

    file1.write('router bgp ' + bgp_asn +'\n')    
    for b in range(len(bgp_list)):
        file1.write('network ' + bgp_list[b].replace ('/', ' mask ') + '\n')
        file1.write('!\n')
   
    file1.close()
