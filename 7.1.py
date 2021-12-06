access_dict = {  'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150
             }

def gen_access_conf(access):
    access_template = [ 'switchport mode access',
                        'switchport access vlan',
                        'switchport nonegotiate',
                        'spanning-tree portfast',
                        'spanning-tree bpduguard enable']
    access_conf = []
    for interface, vlan in access_dict.items():
        access_conf.append('interface {}'.format(interface))
        access_template_copy = access_template.copy()
        access_template_copy[1] += " {}".format(vlan)
        access_conf += access_template_copy
    return access_conf

for string in gen_access_conf(access_dict):
    print(string)