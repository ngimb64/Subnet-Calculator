import sys
import time
import logging
from InputMod import *

# Takes supplied cidr range and determines if the #
# fourth octets of both IP addresses are in same  #
# subnet range #
def subnet_divider(x, y, z, IP_Fourth, IP2_Fourth):
    sbnt_list = []
    for sbnts in range(x, y, z):
        sbnt_list.append(sbnts)
    print(sbnt_list)
    
    if IP_Fourth in sbnt_list:
        print('Your first IP is a network address... Please try again\n')
        wait_time(0, 4)
        main()
    elif IP2_Fourth in sbnt_list:
        print('Your second IP is a network address... Please try again\n')
        wait_time(0, 4)
        main()
    else:
        for sbnt in sbnt_list:
            a = sbnt + 1
            b = sbnt + z - 1

            ips = []
            for ip in range(a, b):
                ips.append(ip)
            print(ips)

            while IP_Fourth in ips:
                if IP2_Fourth in ips:
                    print('* Both IPs are on the same network *.')
                    del ips[:]
                    sys.exit(0)
                else:
                    del ips[:]
                    pass
            else:
                del ips[:]
                pass

# Loading Message Function #
def wait_time(x, y):
    for sec in range(x, y):
        b = 'Loading ' + '.' * sec
        print(b, end='\r')
        time.sleep(1)

def main():
##### Input Two IP Addresses ####################################################################################################
    print('Enter the first IP address')
    IP_First = main_input('First octet: ')
    IP_Second = main_input('Second octet: ')
    IP_Third = main_input('Third octet: ')
    IP_Fourth = alt_input('Fourth octet: ')

    print('First IP address: {}.{}.{}.{}'.format(IP_First, IP_Second, \
                                                    IP_Third, IP_Fourth))
    print()

    print('Enter the second IP address')
    IP2_First = main_input('First octet: ')
    IP2_Second = main_input('Second octet: ')
    IP2_Third = main_input('Third octet: ')
    IP2_Fourth = alt_input('Fourth octet: ')

    print('Second IP address: {}.{}.{}.{}'.format(IP2_First, IP2_Second, \
                                                    IP2_Third, IP2_Fourth))
    print()

    print('Enter the subnet mask')
    print('Please enter 255 for first three octets')
    Sub1 = sub_input('First octet: ')
    Sub2 = sub_input('Second octet: ')
    Sub3 = sub_input('Third octet: ')
    print('Your options are: 128, 192, 224, 240, 248, 252, 254, 255')
    Sub4 = cidr_input('Fourth octet: ')

##### Input Subnet Mask #########################################################################################################
    Subnet_Mask = ('Subnet mask: {}.{}.{}.{}'.format(Sub1, Sub2, Sub3, Sub4))
    print(Subnet_Mask)
    print()

    CIDR_32 = 'Subnet mask: 255.255.255.255'
    CIDR_31 = 'Subnet mask: 255.255.255.254'
    CIDR_30 = 'Subnet mask: 255.255.255.252'
    CIDR_29 = 'Subnet mask: 255.255.255.248'
    CIDR_28 = 'Subnet mask: 255.255.255.240'
    CIDR_27 = 'Subnet mask: 255.255.255.224'
    CIDR_26 = 'Subnet mask: 255.255.255.192'
    CIDR_25 = 'Subnet mask: 255.255.255.128'
    CIDR_24 = 'Subnet mask: 255.255.255.0'

##### Verify That First 3 Octets Are Identical ################################################################################# 
    if IP_First != IP2_First:
        print('* First set of octets are not on same network *\n')
        wait_time(0, 4)
        main()

    elif IP_Second != IP2_Second:
        print('* Second set of octets are not on same network *\n')
        wait_time(0, 4)
        main()

    elif IP_Third != IP2_Third:
        print('* Third set of octects are not on same network *\n')
        wait_time(0, 4)
        main()

    elif Subnet_Mask == CIDR_32:
        print('* There is no possible way these two IP\'s are on the same subnet *\n')
        wait_time(0, 4)
        main()

    elif Subnet_Mask == CIDR_31:
        print('* There is no possible way these two IP\'s are on the same subnet *\n')
        wait_time(0, 4)
        main()

##### Determine What Subnet Mask The User Entered ###############################################################################
    elif Subnet_Mask == CIDR_30:
        subnet_divider(0, 254, 4, IP_Fourth, IP2_Fourth)

    elif Subnet_Mask == CIDR_29:
        subnet_divider(0, 254, 8, IP_Fourth, IP2_Fourth)

    elif Subnet_Mask == CIDR_28:
        subnet_divider(0, 254, 16, IP_Fourth, IP2_Fourth)

    elif Subnet_Mask == CIDR_27:
        subnet_divider(0, 254, 32, IP_Fourth, IP2_Fourth)

    elif Subnet_Mask == CIDR_26:
        subnet_divider(0, 254, 64, IP_Fourth, IP2_Fourth)

    elif Subnet_Mask == CIDR_25:
        subnet_divider(0, 254, 128, IP_Fourth, IP2_Fourth)

    elif Subnet_Mask == CIDR_24:
        print('* The IP\'s are absolutely on the same subnet *.')
        sys.exit(0)

    print('* The IP\'s are on separate subnets or if assigned ' \
            'sequentially one was assigned a broadcast address *\n' )
    wait_time(0, 4)
    main()


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('* Ctrl-C detected...program exiting *')

    except Exception as ex:
        logging.exception('* Error Occured: {} *'.format(ex))