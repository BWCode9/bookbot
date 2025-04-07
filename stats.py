def get_words_in_text(text):
    num_words = len(text.split())
    return f"{num_words} words found in the document"

def get_character(words):
    characters = {}
    for character in words:
        lowercase_letter = character.lower()
        if lowercase_letter in characters:
            characters[lowercase_letter] +=1
        else:
            characters[lowercase_letter] = 1
    return characters
