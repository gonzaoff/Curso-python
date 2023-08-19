import re
text = "The quick brown fox jumps over the lazy dog"


if x := re.search("^The.*dog$", text):
    print("SI")
else:
    print ("NO")