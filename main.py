def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        print_report(path_to_file, word_count, char_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    result = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in result:
            result[char_lower] = 1
        else:
            result[char_lower] += 1
    return result

def sort_on(dict):
    return dict["num"]

def print_report(path_to_file, word_count, character_count):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")

    is_alpha = lambda x : x.isalpha()
    characters_alphabet = filter(is_alpha, character_count)
    for char in characters_alphabet:
        print(f"The '{char}' character was found {character_count[char]} times")

    print("--- End report ---")


main("books/frankenstein.txt")
