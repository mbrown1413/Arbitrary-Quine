
def escape(s):
    return s.replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')

def format_c_list(name, l):
    output = "char* %s[] = {\n" % name
    for line in l:
        output += '    "%s",\n' % escape(line)
    output += "};\n"
    return output

def format_python_list(name, l):
    output = '%s = [\n' % name
    for line in l:
        output += '    "%s",\n' % escape(line)
    output += "]\n"
    return output

LANGUAGE_LIST_FORMAT_FUNCS = {
    "python": format_python_list,
    "c": format_c_list,
}

def print_list(l):
    for item in l:
        print item

if __name__ == "__main__":

    # Print program lists
    next_lang_format_func = LANGUAGE_LIST_FORMAT_FUNCS[languages[0]]
    print next_lang_format_func("python_prog", python_prog),
    print next_lang_format_func("c_prog", c_prog),

    # Rotate and print language array
    print next_lang_format_func("languages", languages[1:] + [languages[0]]),

    # Print the actual program
    if languages[0] == "python":
        print_list(python_prog)
    elif languages[0] == "c":
        print_list(c_prog)
    else:
        raise NameError("UNRECOGNIZED LANGUAGE")
