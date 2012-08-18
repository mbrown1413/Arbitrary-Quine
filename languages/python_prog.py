
from collections import namedtuple

ListFormat = namedtuple("ListFormat", ["list_start",
                                       "item_start",
                                       "item_end",
                                       "item_seperator",
                                       "list_end",
                                       "escape_chars"])

LIST_FORMATS = {
    'python': ListFormat("%s = [\n",
                         "    \"",
                         "\",\n",
                         "",
                         "]",
                         "\\\""),
    'c': ListFormat("char* %s[] = {\n",
                    "    \"",
                    "\"",
                    ",\n",
                    "\n};",
                    "\\\"")
}

def escape(s, escape_chars):
    for char in escape_chars:
        s = s.replace(char, "\\"+char)
    return s

def format_list(name, l, language):
    list_format = LIST_FORMATS[language]
    result = ""
    result += list_format.list_start % name
    for i, item in enumerate(l):
        result += list_format.item_start
        result += escape(item, list_format.escape_chars)
        result += list_format.item_end
        if not i == len(l) - 1:
            result += list_format.item_seperator
    result += list_format.list_end
    return result

if __name__ == "__main__":

    PROGRAMS = {
        "python": python_prog,
        "c": c_prog,
    }

    next_lang = languages[0]

    # Print all program lists
    for lang, program in PROGRAMS.iteritems():
        print format_list("%s_prog" % lang, program, next_lang)

    # Rotate and print language array
    next_language_list = languages[1:] + [languages[0]]
    print format_list("languages", next_language_list, next_lang)

    # Print the actual program
    for line in PROGRAMS[next_lang]:
        print line
