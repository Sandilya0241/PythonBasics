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
#       |     | Or operator                 | cat|dog           | The cat is here
#-------------|-----------------------------|-------------------|--------------------------
#
#-------------|----------------------------------------------------------------------------
#-------------|----------------------------------------------------------------------------
#-------------|----------------------------------------------------------------------------
##############################################################################

import re

# Check for phone number
text = 'My phone number is 408-555-1234'

pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

match = re.search(pattern, text)

print(f'pattern matched at {match.span()} and text found is {match.group()}')

text = 'My phone number is 408-555-7777'

match = re.search(pattern, text)

print(f'pattern matched at {match.span()} and text found is {match.group()}')

pattern = r'\d{3}-\d{3}-\d{4}'

match = re.search(pattern, text)

print(f'pattern matched at {match.span()} and text found is {match.group()}')

# To group patterns together we use compile. Paranthesis indicates it's a group of pattern
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(phone_pattern, text)

print(f'pattern matched at {result.span()} and text found is {result.group()}')
print(result.group(0))
print(result.group(1))
try:
    print(result.group(4))
except IndexError as ie:
    print(ie)
