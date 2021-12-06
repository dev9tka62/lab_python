trunk_dict = {  'FastEthernet0/1':[10,20],
                'FastEthernet0/2':[11,30],
                'FastEthernet0/4':[17]
             }


def gen_trunk_conf(trunk):
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    trunk_conf_dict = {}

    for interface, vlan in trunk_dict.items():
        trunk_conf = []
        trunk_template_copy = trunk_template.copy()
        trunk_template_copy[3] += " {}".format(", ".join([str(i) for i in vlan]))
        trunk_conf += trunk_template_copy
        trunk_conf_dict.update({interface: trunk_conf})
    return trunk_conf_dict

for key, value in gen_trunk_conf(trunk_dict).items():
    print(key, value)