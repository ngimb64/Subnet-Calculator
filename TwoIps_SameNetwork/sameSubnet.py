# This program determines whether two ips are in the same subnet based on
# /32 - /24 CIDR. If you wish to see how the numbers work feel free to 
# uncomment the print statements placed in the defined procedures. #
import sys
import time
from InputMod import *

# This defined procedure takes parameters to create a range. Then a list is 
# created and the range of parameters is added to the list. Then each 
# individual range is scanned to check if the last octet from both IPs
# exist in the same range. If not the list is cleared and returns to the
# mask_(number) def. #
def ip_ran(n1, n2):
    ips = []
    for n in range(int(n1), int(n2)):
        ips.append(n)
        # print(ips)
    while IP_Fourth in ips:
        if IP2_Fourth in ips:
            print('Both IPs are on the same network.')
            sys.exit(0)
        else:
            del ips[:]
            # print(ips)
            return
    else:
        del ips[:]
        # print(ips)
        return

# The below mask_(number) procedures are used to create a range of 
# network addresses to confirm the user has not input an invalid IP.
# If this test is passed it continues to the else statement where the 
# range in between the subnets network and broadcast addresses is tested. #
def mask_30():
    sbnt_list = []
    for sbnts in range(0, 254, 4):
        sbnt_list.append(sbnts)
    # print(sbnt_list)
    print()
    if IP_Fourth in sbnt_list:
        print('Your first IP is a network address...please try again.')
        sys.exit(0)
    elif IP2_Fourth in sbnt_list:
        print('Your second IP is a network address...please try again.')
        sys.exit(0)
    else:
        ip_ran(1, 3) ; ip_ran(5, 7) ; ip_ran(9, 11) ; ip_ran(13, 15)
        ip_ran(17, 19) ; ip_ran(21, 23) ; ip_ran(25, 27) ; ip_ran(29, 31)
        ip_ran(33, 35) ; ip_ran(37, 39) ; ip_ran(41, 43) ; ip_ran(45, 47)
        ip_ran(49, 51) ; ip_ran(53, 55) ; ip_ran(57, 59) ; ip_ran(61, 63)
        ip_ran(65, 67) ; ip_ran(69, 71) ; ip_ran(73, 75) ; ip_ran(77, 79)
        ip_ran(81, 83) ; ip_ran(85, 87) ; ip_ran(89, 91) ; ip_ran(93, 95)
        ip_ran(97, 99) ; ip_ran(101, 103) ; ip_ran(105, 107) ; ip_ran(109, 111)
        ip_ran(113, 115) ; ip_ran(117, 119) ; ip_ran(121, 123) ; ip_ran(125, 127)
        ip_ran(129, 131) ; ip_ran(133, 135) ; ip_ran(137, 139) ; ip_ran(141, 143)
        ip_ran(145, 147) ; ip_ran(149, 151) ; ip_ran(153, 155) ; ip_ran(157, 159)
        ip_ran(161, 163) ; ip_ran(165, 167) ; ip_ran(169, 171) ; ip_ran(173, 175)
        ip_ran(177, 179) ; ip_ran(181, 183) ; ip_ran(185, 187) ; ip_ran(189, 191)
        ip_ran(193, 195) ; ip_ran(197, 199) ; ip_ran(201, 203) ; ip_ran(205, 207)
        ip_ran(209, 211) ; ip_ran(213, 215) ; ip_ran(217, 219) ; ip_ran(221, 223)
        ip_ran(225, 227) ; ip_ran(229, 231) ; ip_ran(233, 235) ; ip_ran(237, 239)
        ip_ran(241, 243) ; ip_ran(245, 247) ; ip_ran(249, 251) ; ip_ran(253, 255)

def mask_29():
    sbnt_list = []
    for sbnts in range(0, 254, 8):
        sbnt_list.append(sbnts)
    # print(sbnt_list)
    print()
    if IP_Fourth in sbnt_list:
        print('Your first IP is a network address...please try again.')
        sys.exit(0)
    elif IP2_Fourth in sbnt_list:
        print('Your second IP is a network address...please try again.')
        sys.exit(0)
    else:
        ip_ran(1, 7) ; ip_ran(9, 15) ; ip_ran(17, 23) ; ip_ran(25, 31)
        ip_ran(33, 39) ; ip_ran(41, 47) ; ip_ran(49, 55) ; ip_ran(57, 63)
        ip_ran(65, 71) ; ip_ran(73, 79) ; ip_ran(81, 87) ; ip_ran(89, 95)
        ip_ran(97, 103) ; ip_ran(105, 111) ; ip_ran(113, 119) ; ip_ran(121, 127)
        ip_ran(129, 135) ; ip_ran(137, 143) ; ip_ran(145, 151) ; ip_ran(153, 159)
        ip_ran(161, 167) ; ip_ran(169, 175) ; ip_ran(177, 183) ; ip_ran(185, 191)
        ip_ran(193, 199) ; ip_ran(201, 207) ; ip_ran(209, 215) ; ip_ran(217, 223)
        ip_ran(225, 231) ; ip_ran(233, 239) ; ip_ran(241, 247) ; ip_ran(249, 255)

def mask_28():
    sbnt_list = []
    for sbnts in range(0, 254, 16):
        sbnt_list.append(sbnts)
    # print(sbnt_list)
    print()
    if IP_Fourth in sbnt_list:
        print('Your first IP is a network address...please try again.')
        sys.exit(0)
    elif IP2_Fourth in sbnt_list:
        print('Your second IP is a network address...please try again.')
        sys.exit(0)
    else:
        ip_ran(1, 15) ; ip_ran(17, 31) ; ip_ran(33, 47) ; ip_ran(49, 63)
        ip_ran(65, 79) ; ip_ran(81, 95) ; ip_ran(97, 111) ; ip_ran(113, 127)
        ip_ran(129, 143) ; ip_ran(145, 159) ; ip_ran(161, 175) ; ip_ran(177, 191)
        ip_ran(193, 207) ; ip_ran(209, 223) ; ip_ran(225, 239) ; ip_ran(241, 255)

def mask_27():
    sbnt_list = []
    for sbnts in range(0, 254, 32):
        sbnt_list.append(sbnts)
    # print(sbnt_list)
    print()
    if IP_Fourth in sbnt_list:
        print('Your first IP is a network address...please try again.')
        sys.exit(0)
    elif IP2_Fourth in sbnt_list:
        print('Your second IP is a network address...please try again.')
        sys.exit(0)
    else:
        ip_ran(1, 31) ; ip_ran(33, 63) ; ip_ran(65, 95) ; ip_ran(97, 127)
        ip_ran(129, 159) ; ip_ran(161, 191) ; ip_ran(193, 223) ; ip_ran(225, 255)

def mask_26():
    sbnt_list = []
    for sbnts in range(0, 254, 64):
        sbnt_list.append(sbnts)
    # print(sbnt_list)
    print()
    if IP_Fourth in sbnt_list:
        print('Your first IP is a network address...please try again.')
        sys.exit(0)
    elif IP2_Fourth in sbnt_list:
        print('Your second IP is a network address...please try again.')
        sys.exit(0)
    else:
        ip_ran(1, 63) ; ip_ran(65, 127) ; ip_ran(129, 191) ; ip_ran(193, 255)

def mask_25():
    sbnt_list = []
    for sbnts in range(0, 254, 128):
        sbnt_list.append(sbnts)
    # print(sbnt_list)
    print()
    if IP_Fourth in sbnt_list:
        print('Your first IP is a network address...please try again.')
        sys.exit(0)
    elif IP2_Fourth in sbnt_list:
        print('Your second IP is a network address...please try again.')
        sys.exit(0)
    else:
        ip_ran(1, 127) ; ip_ran(129, 255)


if __name__ == '__main__':
    try:
        # Starts program  description and displays loading time for 3 seconds #
        print('This program will determine if two assigned IPs' \
            ' are in the same subnet based on the CIDR mask.')

        for x in range(0, 4):
            b = 'Loading ' + '.' * x
            print(b, end='\r')
            time.sleep(1)

        # The next few sections prompt the user for individual octets of
        # 2 IP addresses and their subnet mask #    
        print('Enter the first IP address')
        IP_First = main_input('First octet: ')
        IP_Second = main_input('Second octet: ')
        IP_Third = main_input('Third octet: ')
        IP_Fourth = alt_input('Fourth octet: ')

        First_IpAddr = 'First IP address: {}.{}.{}.{}'.format(IP_First, \
                        IP_Second, IP_Third, IP_Fourth)
        print(First_IpAddr)
        print()

        print('Enter the second IP address')
        IP2_First = main_input('First octet: ')
        IP2_Second = main_input('Second octet: ')
        IP2_Third = main_input('Third octet: ')
        IP2_Fourth = alt_input('Fourth octet: ')

        Second_IpAddr = 'Second IP address: {}.{}.{}.{}'.format(IP2_First, \
                        IP2_Second, IP2_Third, IP2_Fourth)
        print(Second_IpAddr)
        print()

        print('Enter the subnet mask')
        print('Please enter 255 for first three octets')
        Sub1 = sub_input('First octet: ')
        Sub2 = sub_input('Second octet: ')
        Sub3 = sub_input('Third octet: ')
        print('Your options are: 128,192,224,240,248,252,255')
        Sub4 = cidr_input('Fourth octet: ')

        Subnet_Mask = 'Subnet mask: {}.{}.{}.{}'.format(Sub1, Sub2, Sub3, Sub4)
        print(Subnet_Mask)
        print()

        # This section creates preset CIDRs so the users input can
        # be assigned to a variable #
        CIDR_32 = 'Subnet mask: 255.255.255.255'
        CIDR_31 = 'Subnet mask: 255.255.255.254'
        CIDR_30 = 'Subnet mask: 255.255.255.252'
        CIDR_29 = 'Subnet mask: 255.255.255.248'
        CIDR_28 = 'Subnet mask: 255.255.255.240'
        CIDR_27 = 'Subnet mask: 255.255.255.224'
        CIDR_26 = 'Subnet mask: 255.255.255.192'
        CIDR_25 = 'Subnet mask: 255.255.255.128'
        CIDR_24 = 'Subnet mask: 255.255.255.0'

        # Since this program only covers /32 - /24 CIDRs, the first
        # three octets should be identical if not the program
        # refers back to the start defined procedure #
        if IP_First != IP2_First:
            print('First octets not on same network.')
            sys.exit(0)

        if IP_Second != IP2_Second:
            print('Second octets not on same network.')
            sys.exit(0)

        if IP_Third != IP2_Third:
            print('Third octets not on same network.')
            sys.exit(0)

        # For the next section if the input of the subnet mask matches
        # one of the assigned CIDR variables then the program will end
        # due to the lack of assignable IPs in those CIDR values #
        if Subnet_Mask == CIDR_32:
            print('There is no possible way these two IPs are on same subnet.')
            sys.exit(0)

        if Subnet_Mask == CIDR_31:
            print('There is no possible way these two IPs are on same subnet.')
            sys.exit(0)

        # For CIDR 30 - 25 if the subnet mask matches the assigned CIDR
        # variable then it will access the mask_(CIDR number) defined procedure #
        if Subnet_Mask == CIDR_30:
            try:
                mask_30()

            except Exception:
                print('There was an unknown error.')
            else:
                print('The IPs are on separate subnets or if assigned ' \
                        'sequentially one was assigned a broadcast address.')
                sys.exit(0)

        if Subnet_Mask == CIDR_29:
            try:
                mask_29()

            except Exception:
                print('There was an unknown error.')
            else:
                print('The IPs are on separate subnets or if assigned ' \
                        'sequentially one was assigned a broadcast address.')
                sys.exit(0)

        if Subnet_Mask == CIDR_28:
            try:
                mask_28()

            except Exception:
                print('There was an unknown error.')
            else:
                print('The IPs are on separate subnets or if assigned ' \
                        'sequentially one was assigned a broadcast address.')
                sys.exit(0)

        if Subnet_Mask == CIDR_27:
            try:
                mask_27()

            except Exception:
                print('There was an unknown error.')
            else:
                print('The IPs are on separate subnets or if assigned ' \
                        'sequentially one was assigned a broadcast address.')
                sys.exit(0)

        if Subnet_Mask == CIDR_26:
            try:
                mask_26()

            except Exception:
                print('There was an unknown error.')
            else:
                print('The IPs are on separate subnets or if assigned ' \
                        'sequentially one was assigned a broadcast address.')
                sys.exit(0)

        if Subnet_Mask == CIDR_25:
            try:
                mask_25()

            except Exception:
                print('There was an unknown error.')
            else:
                print('The IPs are on separate subnets or if assigned ' \
                        'sequentially one was assigned a broadcast address.')
                sys.exit(0)

        # If subnet mask matches below CIDR the two IPs
        # logically have to be in the same network #
        if Subnet_Mask == CIDR_24:
            print('These two IPs are absolutely on the same network!')
            sys.exit(0)

    # This is a error handling exception to control output when
    # user hits ctrl C to exit program #
    except KeyboardInterrupt:
        print('Ctrl + C detected....program exiting.')