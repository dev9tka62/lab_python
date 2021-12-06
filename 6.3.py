input_file = open("CAM_table.txt", 'r')

input_file_data = input_file.readlines()
input_file_data_processed = []

for line in input_file_data:
    if '.' in line:
        input_file_data_processed.append(line)

for line in input_file_data_processed:
    print(line.rstrip())