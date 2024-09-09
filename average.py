import text_utils, math
# Imports the text utils and math to use math.floor
text = open('sameple.txt','r')
# Total amount of words in the file using the count_words function
totalWords = text_utils.count_words(text)

# Total amount of lines
totalLines = text_utils.count_lines(text)

# Averages and floors the amount of words by the sentences
avg = math.floor(totalWords / totalLines)

# Close the file
text.close()

# Returns it all :)
print(f'Average words per line: {avg}')

