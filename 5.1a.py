try:
    ip_address = input("IP: ")
    ip_address_list = ip_address.split('.')
    
    for oct in ip_address_list:
        if len(oct) > 3 or len(oct) == 0 or int(oct) > 255 or int(oct) < 0:
            error = 3/0 # istead raise smth :)

    oct1 = int(ip_address_list[0])

    if 1 <= oct1 <= 223:
        print("Address type: unicast")
    elif 224 <= oct1 <= 239:
        print("Address type: multicast")
    elif ip_address == "255.255.255.255":
        print("Address type: local broadcast")
    elif ip_address == "0.0.0.0":
        print("Address type: unassigned")
    else:
        print("Address type: unused")

except:
    print("\nIncorrect IPv4 address")