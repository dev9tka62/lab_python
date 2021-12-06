trunk_dict = {  'FastEthernet0/1':[10,20],
                'FastEthernet0/2':[11,30],
                'FastEthernet0/4':[17]
             }


def gen_trunk_conf(trunk):
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    trunk_conf = []
    for interface, vlan in trunk_dict.items():
        trunk_conf.append('interface {}'.format(interface))
        trunk_template_copy = trunk_template.copy()
        trunk_template_copy[3] += " {}".format(", ".join([str(i) for i in vlan]))
        trunk_conf += trunk_template_copy
    return trunk_conf

for string in gen_trunk_conf(trunk_dict):
    print(string)