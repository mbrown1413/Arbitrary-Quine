
=========================
Arbitrary Quine Generator
=========================


----------------------
What this Program Does
----------------------

What is a Quine?
````````````````
A quine is a program that outputs its own source code.  They are also called
self replicating programs.  They can be tricky, but *very* fun to write.  I
highly recommend you write your own quine before reading about how they work.

Arbitrary Quine
```````````````
Some people have written quines that go from one language to another, called
multiquines.  For example a Ruby program that outputs a C program that outputs
the original program.  People have written multiquines that go through quite a
few languages before outputting the original source.  This program is a
multiquine generator.  You give it the sequence of languages and a working
multiquine is output.

That is where the name "Arbitrary Quine Generator" came from.  It generates
multiquines that can be arbitrarily long and use an arbitrary language
sequence.  It is written to be extensible, so that adding different language
capability is easy.

More about Quines
`````````````````
There are many creatively written quines out there.  Another interesting type
of quine is the multiglot quine.  A multiglot is a program that works in more
than one programming language.

Here are some places to read more about quines:

* `C2 Wiki (Quine Program) <http://c2.com/cgi/wiki?QuineProgram>`_ - A good
  quine introduction and lots of interesting examples.
* `Wikipedia (Quine) <http://en.wikipedia.org/wiki/Quine_(computing)>`_ - Some
  good examples and references.


-------------
Program Usage
-------------
There are two scripts of interest: "run_quine.py" and "generate.py".

generate.py will generate the source code for a quine, given a list of
languages.  For example::

    $ python generate.py c python
    char* python_prog[] = {
    ...
    <More C code follows>

run_quine.py is used similarly to generate.py, except that instead of
outputting the source code, it runs the program recursively.  The result is
compared to the original source code and "Quine Succeeded" is printed if it
matched.  This program takes a list of languages just like generate.py, for
example::

    $ python run_quine.py c python c c c c c c c c c
    c...  python...  c...  c...  c...  c...  c...  c...  c...  c...  c... 
    Quine Succeeded.

I think its fun to make a really long list of languages and watch run_quine.py do its job!

Supported Languages
```````````````````
Sadly, only Python and C are supported at the moment.  Changes need to be made
to make adding languages easier (see "Further Ideas" section below).


--------------
How this Works
--------------
TODO


-------------
Further Ideas
-------------
Right now adding a new language is a O(2n+1) operation, where n is the number of
languages.  That means it's a pain to add a language, because you need to
add to every language template just to add a single language.

That makes me feel a little guilty when I brag about how "extensible" this is.
However, I've been pondering an idea to make adding a language O(1).  Each
language can have a set of string expressions which describes how to print a
list in that language.  Then every language will only need to implement a
function that takes in a list and prints the list in a language given that
language's list format expression(s).

I doubt any more languages will be added until this is implemented.  If you
want this implemented, give me a shout.


--------
Feedback
--------
Questions, comments, feedback, inquiries, insults, suggestions, etc are all
welcome.  Feel free to contact me, my name is Michael Brown and my permanent
email is mbrown1413@gmail.com.

Remember, you can fork this on `github
<https://github.com/mbrown1413/arbitrary_quine>`_ and even contribute back!

