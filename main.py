def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        print(character_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    result = {}
    for character in text:
        character_lower = character.lower()
        if character_lower not in result:
            result[character_lower] = 1
        else:
            result[character_lower] = result[character_lower] + 1
    return result

main("books/frankenstein.txt")
