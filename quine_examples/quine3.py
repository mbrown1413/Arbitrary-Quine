# This is an interesting one that I found coded up in PHP here:
# http://c2.com/cgi/wiki?QuineProgram
from base64 import b64decode
encoded = "IyBUaGlzIGlzIGFuIGludGVyZXN0aW5nIG9uZSB0aGF0IEkgZm91bmQgY29kZWQgdXAgaW4gUEhQIGhlcmU6CiMgaHR0cDovL2MyLmNvbS9jZ2kvd2lraT9RdWluZVByb2dyYW0KZnJvbSBiYXNlNjQgaW1wb3J0IGI2NGRlY29kZQplbmNvZGVkID0gIioiCnByaW50IGI2NGRlY29kZShlbmNvZGVkKS5yZXBsYWNlKGNocig0MiksIGVuY29kZWQp"
print b64decode(encoded).replace(chr(42), encoded)
