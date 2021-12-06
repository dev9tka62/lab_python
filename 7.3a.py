def get_int_vlan_map(file):
    input_config = []
    with open(file, 'r') as f:
        input_config = [s.strip() for s in f.readlines()]
    #print(input_config)
    access_dict = {}
    trunk_dict = {}

    key_interface = ""
    for i in range(0, len(input_config)):

        if input_config[i].find("interface") != -1:
            key_interface = (input_config[i].split())[-1]
        if input_config[i].find("switchport trunk allowed") != -1:
            vlans = ( (input_config[i].split())[-1] ).split(',')
            trunk_dict.update({key_interface: [int(i) for i in vlans]})
        if input_config[i] == "switchport mode access":
            #print(input_config[i])
            if (input_config[i+1]).find("switchport access vlan") != -1:
                vlans = ( (input_config[i+1]).split() )[-1]
                access_dict.update({key_interface: vlans})
            else:
                access_dict.update({key_interface: 1})
        ++i

    return access_dict, trunk_dict

 
access, trunk = get_int_vlan_map('config_sw1.txt')

print("---------- access_dict")
for key, item in access.items():
    print("{}: {}".format(key, item))

print("---------- trunk_dict")
for key, item in trunk.items():
    print("{}: {}".format(key, item))
