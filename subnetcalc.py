lowip = "172.23.4.11"
highip = "172.23.9.15"

lowlist = lowip.split('.')
highlist = highip.split('.')
iplow = 0
iphigh = 0
for count,octet in enumerate(lowlist, start=1):
    iplow = (iplow << 8) + int(octet)

for count,octet in enumerate(highlist, start=1):
    iphigh = (iphigh << 8) + int(octet)

mask = 0
previousmask = 0
for bit in range(31, 0, -1):
    previousmask = mask
    mask = mask + (1 << bit)
    netlow = iplow & mask
    nethigh = iphigh & mask
    if (nethigh != netlow):
        break

mask = previousmask
mask1 = mask >> 24
mask2 = (mask >> 16) & 255
mask3 = (mask >> 8) & 255
mask4 = mask & 255
print(f'Common Netmask = {mask1}.{mask2}.{mask3}.{mask4}')

