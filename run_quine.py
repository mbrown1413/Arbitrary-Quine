
import sys
import os
import subprocess
from hashlib import md5

import generate

OKGREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

def write_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()

def run_python(code):
    if not os.path.exists("tmp/"):
        os.mkdir("tmp")
    write_file("tmp/tmp.py", code)
    return check_output(["python", "tmp/tmp.py"])

def run_c(code):
    if not os.path.exists("tmp/"):
        os.mkdir("tmp")
    write_file("tmp/tmp.c", code)
    subprocess.check_call(["gcc", "tmp/tmp.c", "-o", "tmp/tmp_executable"])
    return check_output(["./tmp/tmp_executable"])

def check_output(*popenargs, **kwargs):
    r"""Run command with arguments and return its output as a byte string.

    This function taken from python2.7 for computers without python2.7.

    If the exit code was non-zero it raises a CalledProcessError.  The
    CalledProcessError object will have the return code in the returncode
    attribute and output in the output attribute.

    The arguments are the same as for the Popen constructor.  Example:

    >>> check_output(["ls", "-l", "/dev/null"])
    'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

    The stdout argument is not allowed as it is used internally.
    To capture standard error in the result, use stderr=STDOUT.

    >>> check_output(["/bin/sh", "-c",
    ...               "ls -l non_existent_file ; exit 0"],
    ...              stderr=STDOUT)
    'ls: non_existent_file: No such file or directory\n'
    """
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(retcode, cmd)
    return output

LANGUAGE_RUN_FUNCS = {
    "python": run_python,
    "c": run_c,
}

def run_multiquine(quine, languages):

    generated_code = quine
    for language in languages:
        run_func = LANGUAGE_RUN_FUNCS[language]
        generated_code = run_func(generated_code)
    return generated_code


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
        if arg in generate.LANGUAGE_TEMPLATES.keys():
            languages.append(arg)
        else:
            usage_error(sys.argv[0])
            print 'Error: Argument "%s" must be one of the allowed languages: ' \
                '%s' % (arg, LANGUAGE_TEMPLATES.keys())
            sys.exit(1)

    quine = generate.generate_multiquine(languages)

    generated_code = quine
    for language in languages:
        if len(languages) > 1:
            print language+"... ",
        sys.stdout.flush()
        run_func = LANGUAGE_RUN_FUNCS[language]
        generated_code = run_func(generated_code)
    if len(languages) > 1:
        print

    if md5(generated_code).digest() == md5(quine).digest():
        print OKGREEN+"Quine Succeeded."+ENDC
    else:
        write_file("tmp/original", quine)
        write_file("tmp/generated", generated_code)
        print RED+"ERROR: Quine Failed:"+ENDC
        print "       First quine file in: tmp/original"
        print "       Last quine file (should be equal) in: tmp/generated"
        sys.exit(2)

if __name__ == "__main__":
    main()
