
def escape(s):
    return s.replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')

def print_c_list(name, l):
    print "char* %s[] = {" % name
    for line in l:
        print '    "%s",' % escape(line)
    print "};"

def print_python_list(name, l):
    print '%s = [' % name
    for line in l:
        print '    "%s",' % escape(line)
    print "]"

LANGUAGE_LIST_PRINT_FUNCS = {
    "python": print_python_list,
    "c": print_c_list,
}

def print_list(l):
    for item in l:
        print item

if __name__ == "__main__":

    # Print program lists
    next_lang_func = LANGUAGE_LIST_PRINT_FUNCS[languages[0]]
    next_lang_func("python_prog", python_prog)
    next_lang_func("c_prog", c_prog)

    # Rotate and print language array
    next_lang_func("languages", languages[1:] + [languages[0]])

    # Print the actual program
    if languages[0] == "python":
        print_list(python_prog)
    elif languages[0] == "c":
        print_list(c_prog)
    else:
        raise NameError("UNRECOGNIZED LANGUAGE")
