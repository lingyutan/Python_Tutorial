import re

s = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 ada@sdf.ac.uk"

y = re.findall('\S+@\S+', s)
print(y)
