
import sys
import os

# We will use the list printing functions straight from the python program
sys.path.append(os.path.abspath("languages"))
from python_prog import LANGUAGE_LIST_PRINT_FUNCS

LANGUAGE_FILES = {
    "python": "languages/python_prog.py",
    "c": "languages/c_prog.c",
}

language_order = ["python", "python", "c", "c"]

def remove_ending_newlines(str):
    if str.endswith("\n"):
        return str[:-1]
    else:
        return str

first_lang = language_order[0]
list_print_func = LANGUAGE_LIST_PRINT_FUNCS[first_lang]

# Print program lists
for lang in LANGUAGE_FILES.keys():
    lang_file = open(LANGUAGE_FILES[lang], 'r')
    lines = [remove_ending_newlines(line) for line in lang_file.readlines()]
    list_print_func("%s_prog" % lang, lines)
    lang_file.close()

# Print language array
list_print_func("languages", language_order[1:] + [language_order[0]])

# Print the actual program
first_lang_file = open(LANGUAGE_FILES[first_lang], 'r')
for line in first_lang_file.readlines():
    print remove_ending_newlines(line)
first_lang_file.close()
