input_file = open('config_sw1.txt', 'r')
output_file = open('config_sw1_cleared.txt', 'w+')
ignore = ['duplex', 'alias', 'Current configuration']

for line in input_file.readlines():
    if not line.startswith('!'):
        
        in_ignore = False
        
        for item in ignore:
            if line.find(item) != -1:
                in_ignore = True

        if not in_ignore:
            output_file.write(line)

output_file.seek(0)
for line in output_file.readlines():
    print(line.rstrip())

input_file.close()
output_file.close()