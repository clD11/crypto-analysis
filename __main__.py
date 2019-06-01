from utils.util import clean_line
from utils.util import remove_non_words


def use_file():
    ts = open("resources/training_set.txt", "r", encoding="utf8")
    c = open("resources/sample_set_cleaned.txt", "w+", encoding="utf8")

    words = [line.rstrip('\n') for line in open("resources/words.txt")]

    for line in ts:
        symbols = clean_line(line)
        clean = remove_non_words(words, symbols)
        print(clean)
        c.write(clean + "\n")


def main():
    use_file()
    print("ENDED")


main()
