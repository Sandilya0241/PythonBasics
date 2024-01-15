##############################################################################
# Regular Expressions Patterns
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Character identifiers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Character |  Description     |  Example pattern  |  Example match 
#             |                  |  code             |
#-------------|------------------|-------------------|--------------------------
#       /d    | A digit          | file_\d\d         | file_25
#-------------|------------------|-------------------|--------------------------
#       /w    | Alphanumeric     | \w-\w\w\w         | A-b_1
#-------------|------------------|-------------------|--------------------------
#       /s    | White space      | a\sb\sc           | a b c
#-------------|------------------|-------------------|--------------------------
#       /D    | Non digit        | \D\D\D            | ABC
#-------------|------------------|-------------------|--------------------------
#       /W    | Non Alphanumeric | \W\W\W\W\W        | *-+=)
#-------------|------------------|-------------------|--------------------------
#       /S    | Non White space  | \S\S\S\S          | Yoyo
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quatifiers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Character |  Description     			|  Example pattern  |  Example match 
#             |                  			|  code             |
#-------------|-----------------------------|-------------------|--------------------------
#       +     | Occurs one or more times    | Version \w-\w+    | Version A-b1_1
#-------------|-----------------------------|-------------------|--------------------------
#      {3}    | Occurs exactly 3 times      | \D{3}             | abc
#-------------|-----------------------------|-------------------|--------------------------
#     {2,4}   | Occurs 2 to 4 times      	| \d{2,4}           | 123
#-------------|-----------------------------|-------------------|--------------------------
#     {3,}    | Occurs 3 or more        	| \w{3,}            | anycharacters
#-------------|-----------------------------|-------------------|--------------------------
#       *     | Occurs zero or more times   | A*B*C*            | AACCCC
#-------------|-----------------------------|-------------------|--------------------------
#       ?     | Once or none 			    | plurals?          | plural
#-------------|----------------------------------------------------------------------------
#-------------|----------------------------------------------------------------------------
#-------------|----------------------------------------------------------------------------
#       ()    | Group multiple patterns     | (\d{3})-(\d{4})   | 123-8769
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Additional operators
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Character |  Description     			|  Example pattern  |  Example match 
#             |                  			|  code             |
#-------------|-----------------------------|-------------------|--------------------------
#       |     | Or operator                 |  cat|dog          | The cat is here
#-------------|-----------------------------|-------------------|--------------------------
#       .     | Wild card operator          |  .at              | The cat sat there   
#             | (to match any charcter)     |                   | 
#-------------|-----------------------------|-------------------|--------------------------
#       ^     | Starts with (should be in   |  ^\d              | 1AJSJSJ
#  (At start) |   the beginning of pattern) |                   |                
#-------------|-----------------------------|-------------------|--------------------------
#       $     | Ends with (should be at     |  \d$              | The number is 2 
#   (At end)  |   the end of pattern)       |                   |                
#-------------|-----------------------------|-------------------|--------------------------
#   [^]       | Exculsion operator          |  [^\d]            | There are 2 apples 
# (things to  |                             |                   |   
# be excluded |                             |                   |
# should be   |                             |                   |
# between `[^`|                             |                   |  
# and `]`)    |                             |                   |                
#-------------|-----------------------------|-------------------|--------------------------
#       []    | Group multiple patterns     | []                | 123-8769
#
##############################################################################

import re

# Check for phone number
text = 'The cat is here'

pattern = r'cat|dog'

match = re.search(pattern, text)
print(f'pattern matched at {match.span()} and text found is {match.group()}')

matches = re.findall(r'at','The cat in the hat sat there')
print(matches)

matches = re.findall(r'.at','The cat in the hat sat there')
print(matches)

# IF we have more charcters before at and we are using 3 wild characters along with `at` 3 characters before at will be captured in results. If we want more control, we need to use character identifiers.

matches = re.findall(r'...at','The cat in the hat went splat')
print(matches)

# Start with (caret operator)
match_number = re.findall(r'^I','I838383923')
print(match_number)

match_number = re.findall(r'^\d','1 is a number')
print(match_number)

match_number = re.findall(r'^\d','There are 2 spoons')
print(match_number)

# Ends with ($ operator)
match_number = re.findall(r'\d$','1 is a number')
print(match_number)

match_number = re.findall(r'\d$','The number is 2')
print(match_number)

# Exclusion operators
# This can be more helpful when we are having punctuations in a phrase and we want to remove them.
match_exclusion = re.findall(r'[^\d]','There are 3 numbers 34 inside 5 this sentence')
print(match_exclusion)

match_exclusion = re.findall(r'[^\d]+','There are 3 numbers 34 inside 5 this sentence')
print(match_exclusion)

# Exclusion operators 2
match_exclusion = re.findall(r'[^!.? ]+','This is a string! But it has punctuations. How can we remove it?')
print(' '.join(match_exclusion))

# Inclusion
text = 'Only find hyphen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'
matches = re.findall(pattern,text)
print(matches)

matches = re.findall(r'\w+-\w+',text)
print(matches)