input_file_name = 'config_sw1.txt'
output_file_name = 'config_sw1_cleared.txt'
ignore = ['duplex', 'alias', 'Current configuration']

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w+')

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