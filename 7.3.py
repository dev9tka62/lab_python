def get_int_vlan_map(file):
    input_config = []
    with open(file, 'r') as f:
        input_config = [s.rstrip() for s in f.readlines()]
    print(input_config)
    access_dict = {}
    trunk_dict = {}

    key_interface = ""
    for string in input_config:

        if string.find("interface") != -1:
            key_interface = (string.split())[-1]
        if string.find("switchport trunk allowed") != -1:
            vlans = ( (string.split())[-1] ).split(',')
            trunk_dict.update({key_interface: [int(i) for i in vlans]})
        if string.find("switchport access vlan") != -1:
            vlans = (string.split())[-1]
            access_dict.update({key_interface: vlans})
    
    return access_dict, trunk_dict

 
access, trunk = get_int_vlan_map('config_sw1.txt')

print("---------- access_dict")
for key, item in access.items():
    print("{}: {}".format(key, item))

print("---------- trunk_dict")
for key, item in trunk.items():
    print("{}: {}".format(key, item))
