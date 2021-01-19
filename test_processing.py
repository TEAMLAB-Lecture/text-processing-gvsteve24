#######################
# Test Processing I   #
#######################

def normalize(input_string):
    normalized_string = None
    normalized_string = input_string.strip().lower()
    words = normalized_string.split()
    separator = ' '
    normalized_string = separator.join(words)
    return normalized_string

def no_vowels(input_string):
    no_vowel_string = ''
    i = 0
    prevI = 0
    while i < len(input_string):
        if input_string[i] == 'a' or input_string[i] == 'e' or input_string[i] == 'i' or input_string[i] == 'o' or input_string[i] == 'u' or input_string[i] == 'A' or input_string[i] == 'E' or input_string[i] == 'I' or input_string[i] == 'O' or input_string[i] == 'U': 
            if prevI == 0:
                no_vowel_string += input_string[prevI:i]
            else:
                no_vowel_string += input_string[prevI+1:i]
            prevI = i
        elif i == len(input_string)-1:
            no_vowel_string += input_string[prevI+1:]
        i += 1
    return no_vowel_string