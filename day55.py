import re
emailAddress = input()
pattern = "(\w+)@(\w+)\.(com)"
compare = re.match(pattern,emailAddress)
print(compare.group(2))