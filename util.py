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

def clean_line(line):
    result = ""

    # remove the hyper links

    # remove the chars
    special = False
    for char in line.lower():
        char_value = ord(char)
        if char_value > 96 and char_value < 123:
            result += char
            special = False
        elif not special:
            result += " "
            special = True
            
    return result.strip()
    
def main():
    print(clean_line("  test(*TEST#*789243%%^62534"  ))

main()
