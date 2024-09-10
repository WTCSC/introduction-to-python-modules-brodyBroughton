import text_utils, math
# Imports the text utils and math to use math.floor

# Opens file
file = open('sample.txt','r')

# File turned into a string
text = ''.join(file.readlines())

# Total amount of words in the file using the count_words function
totalWords = text_utils.count_words(text.strip())

# Total amount of lines
totalLines = text_utils.count_lines(text)

# Averages and floors the amount of words by the sentences
avg = int(totalWords / totalLines)

# Close the file
file.close()

# Returns it all :)
print(f'Average words per line: {avg}')

