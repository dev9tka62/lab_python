input_file = open("CAM_table.txt", 'r')

input_file_data = input_file.readlines()
input_file_data_processed = []

# Lines with MAC only
for line in input_file_data:
    if '.' in line:
        input_file_data_processed.append(line.split())

#  It is sorting time
buffer = []
for i in range(0, len(input_file_data_processed)):
    for j in range(i+1, len(input_file_data_processed)):
        if input_file_data_processed[i][0] > input_file_data_processed[j][0]:
            buffer = input_file_data_processed[i]
            input_file_data_processed[i] = input_file_data_processed[j]
            input_file_data_processed[j] = buffer

# It is gluing time
for i in range(0, len(input_file_data_processed)):
    input_file_data_processed[i] = '    '.join(input_file_data_processed[i])

# Output time
for line in input_file_data_processed:
    print(line)