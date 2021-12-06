while True:
    try:
        ip_address = input("[ Enter \"stop\" to stop the program ]\n"
                           "IP: ")
        
        if ip_address == "stop":
            break

        ip_address_list = ip_address.split('.')
        
        for oct in ip_address_list:
            if len(oct) > 3 or len(oct) == 0 or int(oct) > 255 or int(oct) < 0:
                error = 3/0 # istead raise smth :)

        oct1 = int(ip_address_list[0])

        if 1 <= oct1 <= 223  and oct1 != 127:
            print("Address type: unicast")
        elif 224 <= oct1 <= 239:
            print("Address type: multicast")
        elif ip_address == "255.255.255.255":
            print("Address type: local broadcast")
        elif ip_address == "0.0.0.0":
            print("Address type: unassigned")
        elif ip_address == "127.0.0.1":
            print("Address type: loopback")
        else:
            print("Address type: unused")

    except:
        print("Incorrect IPv4 address")