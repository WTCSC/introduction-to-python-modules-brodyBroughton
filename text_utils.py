def count_words(text):
    
    # Splits the string into words and returns how many
    return len(text.split())

def count_lines(text):
    
    # Counts how many sentence breakers there are and returns them
    return (text.count('\n')
