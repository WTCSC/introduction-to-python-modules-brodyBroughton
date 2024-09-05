import text_utils, math
# Imports the text utils and math to use math.floor

# Total amount of words in the file using the count_words function
totalWords = text_utils.count_words('sample.txt')

# Total amount of sentences
totalSentences = text_utils.count_sentences('sample.txt')

# Averages and floors the amount of words by the sentences
avg = math.floor(totalWords / totalSentences)

# Returns it all :)
return f'Average words per line: {avg}'

