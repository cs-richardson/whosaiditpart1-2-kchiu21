"""
Kolton Chiu
This program counts how many words are in two different text and prints them.
https://www.w3schools.com/python/python_file_handling.asp
https://www.w3schools.com/jsref/jsref_split.asp
https://www.w3schools.com/python/ref_file_close.asp
https://www.tutorialspoint.com/python/file_read.htm
"""
# normalize
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    total = 0
    result_dict = {}
    text = open(filename, "r")
    for key in text.read().split():
        next_key = normalize(key)
        if next_key:
            result_dict[next_key] = result_dict.get(next_key, 0) + 1
            total = total + 1
    text.close()
    result_dict.update( {'_total' : total} )
    return result_dict

shakespeare_counts = get_counts("hamlet-short.txt")
for key in shakespeare_counts:
    print ((key) + ": " + str(shakespeare_counts[key]))

print ("-----")

austen_counts = get_counts("pride-and-prejudice-short.txt")
for key in austen_counts:
    print ((key) + ": " + str(austen_counts[key]))
