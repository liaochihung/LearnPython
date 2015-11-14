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

import re
import urllib

try:
    import urllib.request
except:
    pass

sites = 'google yahoo cnn msn'.split()
pattern = re.compile(r'<title>+.*</title>+', re.I | re.M)

for s in sites:
    print('Searching: ' + s)
    try:
        u = urllib.urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')
    text = u.read()
    title = re.findall(pattern, str(text))
    print(title[0])
