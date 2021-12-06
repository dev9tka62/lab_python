IP = "192.168.3.1"

oct1, oct2, oct3, oct4 = IP.split('.')

print("{:10}{:10}{:10}{:10}\n".format(oct1, oct2, oct3, oct4) +
      "{:08b}  {:08b}  {:08b}  {:08b}".format(int(oct1), int(oct2), int(oct3), int(oct4)))