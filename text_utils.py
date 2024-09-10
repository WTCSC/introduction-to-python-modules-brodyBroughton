def count_chars(text):

    # Returns all the characters
    return len(text)

def count_words(text):

    # Splits the string into words and returns how many
    return len(text.split())

def count_sentences(text):
    
    # Counts how many sentence breakers there are and returns them
    return (text.count('.') + text.count('!') + text.count('?'))

def count_lines(text):

    # Counts how many newline characters
    return (text.count('\n') + 1)
