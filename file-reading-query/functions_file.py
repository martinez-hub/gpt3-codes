
#function for filter file without specific text that we do not want
def filter_file(file):

    doc_list = file.read()
    count = 0

    file_array = []
    for line in doc_list:

        #filtering the file
        l = line.replace('<|startoftext|>', '')
        l1 = l.replace('<|endoftext|>', '')
        l2 = l1.replace("\\n\\n", '')
        #print(len(l2))

        #saving the filtered file in an array
        file_array.append(l2)

        #count += 1

    #print(file_array[3])

    return file_array

#function for tokenize the array creating a new array where every element consist of 8000 characters
def tokenizer_gpt3(filtered_array):
    #array for hold the 8000 words per element
    split_characters = []

    #variable to hold 8000 words
    s = ''

    #variable for count the words
    count = 0
    #loop for iterate per every word of the array
    for i in filtered_array:
        #concatenating words on s var
        s+=i
        #updating the count
        count +=1

        #when count = 8000 then save that 8000 words in the new array
        if count == 8000:
            #saving the words on the array
            split_characters.append(s)

            #creating query
            query_creator(split_characters)

            #cleaning variables
            s = ''
            count = 0

    #n = 8000
    #split_characters = [filtered_array[i:i+n] for i in range(0, len(filtered_array),n)]
    #split_characters = filtered_array.split(None, 1500)
    #list(filtered_array[8000])
    #chars_count = len(filtered_array)

    return split_characters

def query_creator(split_characters):

        #creating query
        response = '{"prompt"' + ":" + ' "' f'{split_characters} '"\\n\\n###\\n\\n" "," + '" completion"' + ":" + '<legal document>' +"}"

        #saving query on file
        f = open("test.txt", "a")
        f.write(response+"\n\n")

        #closing file
        f.close()
