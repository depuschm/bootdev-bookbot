from stats import count_words, count_characters

def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        print_report(path_to_file, word_count, char_count)

def sort_on(d):
    return d[1]

def print_report(path_to_file, word_count, character_count):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")

    is_alpha = lambda x : x.isalpha()
    characters_alphabet = {
        k:v for (k,v) in sorted(character_count.items(), key=sort_on, reverse=True)
        if is_alpha(k)
    }
    for char in characters_alphabet:
        print(f"The '{char}' character was found {character_count[char]} times")

    print("--- End report ---")


main("books/frankenstein.txt")
