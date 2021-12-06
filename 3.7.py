MAC = 'AAAA:BBBB:CCCC'

p1, p2, p3 = MAC.split(':')

p1 = ( bin(int(p1, 16)) ).replace('0b', '')
p2 = ( bin(int(p2, 16)) ).replace('0b', '')
p3 = ( bin(int(p3, 16)) ).replace('0b', '')

print("{} {} {}".format(p1, p2, p3))