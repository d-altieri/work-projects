import re

text = '''
'''

lines = text.splitlines()
pattern = r"\w{8}_\d{2}LAB"
match = re.findall(pattern, text)
result = sorted(match)

if match:
    print(*result, sep="\n")
else:
    print("No equipment found")