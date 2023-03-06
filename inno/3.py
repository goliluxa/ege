import re

l = "aaa"
l2 = "aa"
print(len(re.findall(l2, l, flags=1)))

def go(s, t):
    pattern = re.compile('(?=(' + re.escape(s) + '))')

    result = pattern.findall(t)
    print(len(result))
