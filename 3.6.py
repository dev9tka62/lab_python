ospf_route = "O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = ospf_route.replace(',', '')
ospf_route = ospf_route.replace('[', '')
ospf_route = ospf_route.replace(']', '')
ospf_route = ospf_route.replace('via ', '')
ospf_route = ospf_route.replace('O', 'OSPF')

ospf_route = ospf_route.split()

print("Protocol:              {}\n".format(ospf_route[0]) +
      "Prefix:                {}\n".format(ospf_route[1]) +
      "AD/Metric:             {}\n".format(ospf_route[2]) +
      "Next-Hop:              {}\n".format(ospf_route[3]) +
      "Last update:           {}\n".format(ospf_route[4]) +
      "Outbound Interface:    {}".format(ospf_route[5]))