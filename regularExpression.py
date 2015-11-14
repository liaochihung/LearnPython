import re

# print(re.split(r'\s*', 'here are some words'))
# print(re.split(r'(\s*)', 'here are some words'))
# print(re.split(r'(s*)', 'here are some words'))

# [a-z] find a range of characters
# print(re.split(r'[a-hA-F0-9]', 'saldkfjeilksjdLKJSAEIAL;SDF', re.I | re.M))

'''

\d = digits
\D = non-digits
\s = Space
\S = non-Space
\w = alphanumeric
\. = regular period (.)

. = Any character but newline(\n)

* = 0 or more
+ = 1 or more
? = 0 or 1 of ...
{5} = exact number of ...
{1,60} = range on number of ...
'''
# print(re.split(r'\d', 'ocinwe324 main st.asdvce'))
print(re.findall(r'\d{1,5}\s\w+\s\w+\.', 'ocinwe324 main st.asdvce'))
