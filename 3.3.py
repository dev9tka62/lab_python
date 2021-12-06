CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"

CONFIGlist = CONFIG.split()
VLANS = CONFIGlist[-1].split(',')

print(VLANS)