import functions_file

#opening file to read, please add fullpath of the file
file = open(r"/Users/josuemartinez/Downloads/ASCE.txt", "r+")

array_list = functions_file.filter_file(file)
file.close()
#counting = functions_file.tokenizer_gpt3(array_list)
array_list_modified = functions_file.tokenizer_gpt3(array_list)
#print(array_list_modified[0])

count = 0

for i in array_list_modified[3]:

    count = count + 1

print(count)
#print(array_list_modified[3])

#functions_file.query_creator(array_list)