input_file = open("CAM_table.txt", 'r')

input_file_data = input_file.readlines()
input_file_data_processed = []

# It is choosing time
chosen_VLAN = int(input("Enter VLAN number: "))

# Lines with MAC only
for line in input_file_data:
    if '.' in line and int((line.split())[0]) == chosen_VLAN:
        input_file_data_processed.append(line)

# It is output time
for line in input_file_data_processed:
    print(line.rstrip())