"""Python program to demonstrate
use of  slice() constructor.
"""

# s = 'CODEISFUN'
# 	   012345678	(+ve) positive indexing
# 	   987654321	(-ve) negative indexing

s = "CODEISFUN"
# default value of start = -1 and stop = -len(s)-1 if step is (-ve).
s1 = slice(None, None, -1)
# default value of start = 0 and stop = len(s) if step is (+ve).
s2 = slice(None, None, +1)
print(s[s1], s[s2], sep="\n")

# There are many possibilities, 2 of which are mentioned above.
s3 = slice(3, None, -1)
s4 = slice(4)
print(s[s3], s[s4], sep="\n")

s5 = slice(-3, None, +1)
s6 = slice(8, 5, -1)
print(s[s5], s[s6], sep="\n")

s7 = slice(5, 3, -1)
s8 = slice(-5, -3, +1)
print(s[s7], s[s8], sep="\n")
