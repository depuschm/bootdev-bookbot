from stats import count_words, count_characters, print_report

def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        print_report(path_to_file, word_count, char_count)

main("books/frankenstein.txt")
