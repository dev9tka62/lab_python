num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

element = 'ruby'
forList = word_list

print(forList)
print( (len(forList) - 1) - forList[-1::-1].index(element) )