
import sys
import os

# We will use the list formatting functions straight from the python program
sys.path.append(os.path.abspath("languages"))
import python_prog

LANGUAGE_TEMPLATES = {
    "python": "languages/python_prog.py",
    "c": "languages/c_prog.c",
}

def generate_multiquine(languages):

    for language in languages:
        if language not in LANGUAGE_TEMPLATES.keys():
            raise ValueError('Language "%s" not one of the available languages: %s' % (language, LANGUAGE_TEMPLATES.keys()))

    quine = ''
    first_lang = languages[0]

    # Print program lists
    for lang in LANGUAGE_TEMPLATES.keys():
        lang_file = open(LANGUAGE_TEMPLATES[lang], 'r')
        lines = [line.rstrip("\n") for line in lang_file.readlines()]
        quine += python_prog.format_list("%s_prog" % lang, lines, first_lang)
        quine += "\n"
        lang_file.close()

    # Print language sequence list
    quine += python_prog.format_list("languages", languages[1:] + [languages[0]], first_lang)
    quine += "\n"

    # Print the actual program
    first_lang_file = open(LANGUAGE_TEMPLATES[first_lang], 'r')
    for line in first_lang_file.readlines():
        quine += line
    first_lang_file.close()

    return quine


def usage_error(prog):
    print "Usage: %s language [language...]" % prog

def main():

    # Parse args
    # TODO: Convert to optparse/argparse
    languages = []
    if len(sys.argv) <= 1:
        usage_error(sys.argv[0])
        print "Error: At least one argument expected"
        sys.exit(1)
    for arg in sys.argv[1:]:
        if arg in LANGUAGE_TEMPLATES.keys():
            languages.append(arg)
        else:
            usage_error(sys.argv[0])
            print 'Error: Argument "%s" must be one of the allowed languages: ' \
                '%s' % (arg, LANGUAGE_TEMPLATES.keys())
            sys.exit(1)

    print generate_multiquine(languages),

if __name__ == "__main__":
    main()
