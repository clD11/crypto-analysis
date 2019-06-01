## lowercase
## remove punctuation
## remove numbers
## remove hyper links
## remove RT
## remove HashTags
## remove non ascii characters and symbols

## read in file
## file = open("training_set.txt", r)
##
##for line in file:
##    print(line)

def remove_punctuation(line):
    result = ""
    special = False
    for char in line:
        char_value = ord(char)
        if (char_value > 64 and char_value < 91) or (char_value > 96 and char_value < 123):
            result += char
            special = False
        elif not special:
            result += " "
            special = True
    return result.strip()
    
def main():
    print(remove_punctuation("  test(*test#*789y243%%^62534"  ))

main()
