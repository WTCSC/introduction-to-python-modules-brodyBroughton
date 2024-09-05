def count_chars(text):

    # Returns the length of the text which is the amount of characters
    return len(text)

def count_words(text):
    
    # Splits the string into words and returns how many
    return len(text.split())

def count_sentences(text):
    
    # Counts how many sentence breakers there are and returns them
    return (text.count('.') + text.count('!') + text.count('?'))
