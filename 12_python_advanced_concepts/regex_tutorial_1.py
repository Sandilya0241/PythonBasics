# Let us say if we want to search `dog` inside string `My dog is great`. We use in operator. This has severe limitations, we need to know the exact string, and need to perform additional operations to account for capitalization and punctuation.
#
# What if we only want to search for a pattern structure of the string. Like we are looking for an Email or a phone number.
#
# This is where Regular Expressions (regex) allow us to search for general patterns in text data.
# 
# Ex: Email format will be like user@email.com which is like "some text" + "@" + "some text" + "." + "some text"
#
# Python comes up with built-in regular expressions library `re`. This allows us to create specialized pattern strings and then search for matches within text.
# 
# The primary skill set for this is understanding the special syntax for these pattern strings.
# 
# Example:
#   Phone Number - (555)-555-5555
# 
# Regex pattern : r"(\d\d\d)-\d\d\d-\d\d\d\d"
#
# When we give r"(\d\d\d)-\d\d\d-\d\d\d\d", this tells Python that don't treat this as a normal string. This is a regex pattern with identifiers. These identifiers are just place holders are waiting for a match based of a particular data type. In above example, `\d` denotes digits. We will have general identifiers and exact strings with in a regular expression pattern.
#------------------------------------------------------------------------------------
# For above example, we can implement another versionof regex using quantifiers.
# Regex pattern : r"(\d{3})-\d{3}-\d{4}"

text = "The agent's phone number is 408-555-1234. Call soon"

import re

# Let us see a pattern that matches
pattern = 'phone'
print(re.search(pattern=pattern, string=text))

# Let us see a pattern that deosn't matches
pattern = 'NOT_IN_TEXT'
print(re.search(pattern=pattern, string=text))

# Let us see match object
pattern = 'phone'
match = re.search(pattern=pattern, string=text)

print(f'span is {match.span()}')
print(f'start is {match.start()}')
print(f'end is {match.end()}')

# Search method returns first match only
text = 'my phone first, my phone second'
print(re.search(pattern,text))

# To find all matches, we need to use findall method
print(re.findall(pattern,text))

# To find all matches using iterator object
for mcth in re.finditer(pattern, text):
    print(mcth.span())
    print(mcth.group())