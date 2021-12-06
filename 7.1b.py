access_dict = {  'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150
             }

def gen_access_conf(access, psecurity=False):
    access_template = [ 'switchport mode access',
                        'switchport access vlan',
                        'switchport nonegotiate',
                        'spanning-tree portfast',
                        'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    access_conf_dict = {}
    
    for interface, vlan in access_dict.items():
        access_conf = []
        access_template_copy = access_template.copy()
        access_template_copy[1] += " {}".format(vlan)
        access_conf += access_template_copy
        if psecurity:
            access_conf += port_security
        access_conf_dict.update({interface: access_conf})
    return access_conf_dict

for key, value in gen_access_conf(access_dict, psecurity=True).items():
    print(key, value)