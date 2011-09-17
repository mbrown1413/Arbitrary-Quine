code = 'print "code = \'"+code.replace("\\\\","\\\\\\\\").replace("\'","\\\\\'").replace("\\n", "\\\\n")+"\'"\nprint code'
print "code = '"+code.replace("\\","\\\\").replace("'","\\'").replace("\n", "\\n")+"'"
print code
