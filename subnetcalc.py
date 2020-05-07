#!/usr/bin/env python3
import sys

lowip = "172.23.4.11"
highip = "172.23.9.15"

if (len(sys.argv) == 3):
    lowip = sys.argv[1]
    highip = sys.argv[2]
lowlist = lowip.split('.')
highlist = highip.split('.')
iplow = 0
iphigh = 0

# This block will take a list of octets in string format
# and convert to int (8 bits at a time) and shift left until
# a 32 bit integer is created from the four octets.
# This gives us a 32 bit address we can bit-wise manipulate
for count,octet in enumerate(lowlist, start=1):
    iplow = (iplow << 8) + int(octet)

for count,octet in enumerate(highlist, start=1):
    iphigh = (iphigh << 8) + int(octet)

# Start with mask 00000000 00000000 00000000 00000000
# We will AND the mask with each IP to derive the IP Network for each IP.
mask = 0
# We will use previousmask since we find out netmask
# as a post-condition to the loop.
previousmask = 0
for bit in range(31, -1, -1):
    # After first iteration, our mask is
    # 10000000 00000000 00000000 00000000
    # After the second, our mask is
    # 11000000 00000000 00000000 00000000
    # And so on until we find a mask that when AND'ed
    # with each IP, no longer results in the same network number for both IPs
    previousmask = mask
    mask = mask + (1 << bit)
    netlow = iplow & mask
    nethigh = iphigh & mask
    if (nethigh != netlow):
        break

mask = previousmask
# Now we want to print the mask, so we shift right and AND out anything left of bit 8.
mask1 = mask >> 24
mask2 = (mask >> 16) & 255
mask3 = (mask >> 8) & 255
mask4 = mask & 255
print('IP 1 - %s' % (lowip))
print('IP 2 - %s' % (highip))
# Commenting this out because it don't work in Python 3.5 :(
# print(f'Common Netmask = {mask1}.{mask2}.{mask3}.{mask4}')
print('Common Netmask = %s.%s.%s.%s' % (mask1, mask2, mask3, mask4))
