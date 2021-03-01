# put your code here.
# iterate through each line, split words by space, add words to a list
# create an empty dictionary
# loop through words, add count per item encountered
# print dictionary

def create_dictionary(file_name):
    text_file = open(file_name)

    words = []

    for line in text_file:
        line = line.rstrip()
        line_words = line.split(" ")
        words.extend(line_words)

    word_counts = {}

    for word in words:
        # word_counts[word] = words.count(word)  # using built in count method 
        word_counts[word] = word_counts.get(word, 0) + 1 # custom count method 

    testing_text = ""

    for word, count in word_counts.items():
        testing_text += f"{word} {count}\n"
    
    return testing_text
        

print(create_dictionary('test.txt'))
# print(create_dictionary('twain.txt'))
