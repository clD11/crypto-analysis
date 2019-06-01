import re


def clean_line(line):
    # remove the hyper links
    hyper = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|
        (\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", line)

    # remove RT
    rt_remove = re.sub(r'^RT\s', "", hyper)

    # remove the chars
    result = ""
    special = False
    for char in rt_remove.lower():
        char_value = ord(char)
        if 96 < char_value < 123:
            result += char
            special = False
        elif not special:
            result += " "
            special = True
            
    return result.strip()


def remove_non_words(words, line):
    result = ""
    for word in line.split():
        if word in words:
            result += word
            result += " "
    return result
