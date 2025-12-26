"""Python program to demonstrate
extended slicing syntax.
"""

# s = 'CODEISFUN'
# 	   012345678	(+ve) positive indexing
# 	   987654321	(-ve) negative indexing

s = "CODEISFUN"
# default value of start = -1 and stop = -len(s)-1 if step is (-ve).
s1 = s[::-1]
# default value of start = 0 and stop = len(s) if step is (+ve), also default step is +1.
s2 = s[::]
print(s1, s2, sep="\n")

# There are many possibilities, 2 of which are mentioned above.
s3 = s[3::-1]
s4 = s[:4:]
print(s3, s4, sep="\n")

s5 = s[-3::]
s6 = s[8:5:-1]
print(s5, s6, sep="\n")

s7 = s[5:3:-1]
s8 = s[-5:-3:]
print(s7, s8, sep="\n")
