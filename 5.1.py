ip_address = input("IP: ")
ip_address_list = ip_address.split('.')

oct1 = int(ip_address_list[0])

if 1 <= oct1 <= 223:
    print("unicast")
elif 224 <= oct1 <= 239:
    print("multicast")
elif ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
else:
    print("unused")