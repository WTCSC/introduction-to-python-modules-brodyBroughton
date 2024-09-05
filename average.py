import text_utils, math

totalWords = text_utils.count_words('sample.txt')
totalSentences = text_utils.count_sentences('sample.txt')

avg = math.floor(totalWords / totalSentences)

return f'Average words per line: {avg}'

