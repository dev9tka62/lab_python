file = open('config_sw1.txt', 'r')

for line in file.readlines():
    if not line.startswith('!'):
        print(line.rstrip())

file.close()