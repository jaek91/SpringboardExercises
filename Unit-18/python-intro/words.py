def print_upper_words(word_list, must_start_with):
    '''this function takes in a list of words (word_list) and the letters that the words must start with 
       (must_start_with) and prints the words in caps that satisfy the criteria on a new line
    '''
    ## this is a empty list which will store all our list of words that satisfy the start letter requirement
    desired_list = [] 

    for char in must_start_with: ##first loop through all the characters in our set must_start_with
        desired_words = list(filter(lambda x: x.lower().startswith(char),word_list))
        for idx in range(len(desired_words)):
            desired_list.append(desired_words[idx])
    for word in desired_list:
        print(word.upper())

##test example
words_list = ["hello", "Elephant", "Elevate", "lie", "counting", "euler", "lazy"]
print_upper_words(words_list, {"e","l"}) 

##expected output: the words LIE, LAZY, ELEPHANT, ELEVATE, EULER