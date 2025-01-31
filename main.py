def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

if __name__ == "__main__":
    main("books/frankenstein.txt")
