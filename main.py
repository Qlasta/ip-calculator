import sys

hex_letters = ["a", "b", "c", "d", "e", "f"]
cmd_args = sys.argv


# Functions:


def validate_ipv4(ip_num_list):
    """ Validates ipv4 by the rules: form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros.
    IP provided as list items. Returns valid True or False."""
    if len(ip_num_list) == 4:
        correct_n = 0
        for n in ip_num_list:
            try:
                int(n) and int(n[0])
            except ValueError:
                return False
            if 0 <= int(n) <= 255:
                if len(n) > 1 and int(n[0]) == 0:
                    return False
                else:
                    correct_n += 1
        if correct_n == 4:
            return True
        else:
            return False
    else:
        return False


def validate_ipv6(ip_num_list):
    """ Validates ipv6 by the rules: form "x1:x2:x3:x4:x5:x6:x7:x8" where 1 <= xi.length <= 4 xi is a hexadecimal string
     which may contain digits, lowercase and upper-case letters ('a' to 'f'). IP provided as list items. Returns valid True or False."""
    if len(ip_num_list) == 8:
        correct_n = 0
        for n in ip_num_list:
            if len(n) in range(1, 5):
                for x in n:
                    try:
                        if x in hex_letters or int(x) in range(10):
                            correct_n += 1
                    except ValueError:
                        return False
        if correct_n == len(''.join(ip_num_list)):
            return True
        else:
            return False
    else:
        return False


def calculate_ipv4(starting_ip, ending_ip):
    """Returns IP's count in range, giving two IPv4 addresses divided to list items."""
    ip_count = 0
    # limit - decimal numbers in one ip fragment including 0.
    limit = int("11111111", 2) + 1
    for n in range(4):
        diff = int(ending_ip[n]) - int(starting_ip[n])
        ip_count *= limit
        ip_count += diff
    return ip_count

def calculate_ipv6(starting_ip, ending_ip):
    """Returns IP's count in range, giving two IPv6 addresses divided to list items."""
    ip_count = 0
    # limit - hexadecimal numbers in one ip fragment including 0.
    limit = int("ffff", 16) + 1
    for n in range(8):
        diff = int(ending_ip[n], 16) - int(starting_ip[n], 16)
        ip_count *= limit
        ip_count += diff
    return ip_count

# Inputs
if len(cmd_args) == 4:
    ip_format = cmd_args[1].lower()
    first_ip = cmd_args[2].lower()
    second_ip = cmd_args[3].lower()
else:
    ip_format = input("Wrong count of variables, try again one by one. \nEnter 'ipv4' or 'ipv6': ").lower()
    first_ip = input("Enter starting IP: ").lower()
    second_ip = input("Enter ending IP: ").lower()
count = 0


# IP format validation and calculation
if ip_format == 'ipv4':
    if validate_ipv4(first_ip.split(".")) and validate_ipv4(second_ip.split(".")):
        count = calculate_ipv4(first_ip.split("."), second_ip.split("."))
    else:
        print("Format is not valid (should be 'n1.n2.n3.n4', where 'n' between 0 and 255, without leading zeros), please try again.")
        exit()

elif ip_format == 'ipv6':
    if validate_ipv6(first_ip.split(":")) and validate_ipv6(second_ip.split(":")):
        count = calculate_ipv6(first_ip.split(":"), second_ip.split(":"))
    else:
        print("Format is not valid (should be 'n1:n2:n3:n4:n5:n6:n7:n8', where 'n' in in hexadecimal numbers, 1-4 digits), please try again.")
        exit()
else:
    print("Enter IPv4 or IPv6, please try again. ")
    exit()

# Check if ending address is greater than starting and display calculation or error message.

if count > 0:
    print(count)
else:
    print("The ending address must be greater than the starting one. Please try again.")

# Documentation.
'''A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", 
and "192.168@1.1" are invalid IPv4 addresses. 

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4 xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and 
upper-case English letters ('A' to 'F'). Leading zeros are allowed in xi. For example, 
"2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, 
while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses. 


'''
