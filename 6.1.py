file = open('ospf.txt', 'r')
ospf_routes = file.readlines()

file.close()
# print('---=[ ' + data + ' ]=---')
# print('---=[ ' + ospf_route + ' ]=---')

for ospf_route in ospf_routes:
      print("---=| ROUTE {} |".format( str(ospf_routes.index(ospf_route)+1)) )
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