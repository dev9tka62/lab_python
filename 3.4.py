command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"

command1VLANS = (command1.split())[-1].split(',')
command2VLANS = (command2.split())[-1].split(',')

commonVLANS = list(set(command1VLANS) & set(command2VLANS))

print(commonVLANS)