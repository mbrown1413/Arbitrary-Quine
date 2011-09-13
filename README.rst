
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
few languages before outputing the original source.  This program is a
multiquine generator.  You give it the sequence of languages for a multiquine
and a working multiquine is output.

That is where the name "Arbitrary Quine Generator" came from.  It generates
multiquines that can be arbitrarily long and use an arbitrary language
sequence.  It is written to be extensible, so that adding different language
capability is easy.

More about Quines
`````````````````
There are many creatively written quines out there.  Another interesting type
of quine is the multiglot quine.  A multiglot is a program that works in more
than one programming language.  It requires writing one source file which is
valid and working in more than one language.


-------------
Program Usage
-------------
There are two main programs: "run_quine.py" and "generate.py".

generate.py will generate the source code for a quine, given a list of
languages.  For example::

    $ python generate.py c python
    char* python_prog[] = {
    <More C code follows>

run_quine.py is used similarly to generate.py, except that instead of outputing
the source code, it runs the source code recursively.  The result is compared
to the original source code and "Quine Succeeded" is printed if it matched.
This program takes a list of languages just like generate.py, for example::

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
TODO

