file = open('config_sw1.txt', 'r')
ignore = ['duplex', 'alias', 'Current configuration']

for line in file.readlines():
    if not line.startswith('!'):
        
        in_ignore = False
        
        for item in ignore:
            if line.find(item) != -1:
                in_ignore = True

        if not in_ignore:
            print(line.rstrip())

file.close()