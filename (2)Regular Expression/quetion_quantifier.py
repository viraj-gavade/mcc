import re
pattern = re.compile("sh[abc]?")
result = pattern.match("shasaurs")
if result ==    None:
    print("No match found")
else:   
    print("No match found")