regex_integer_in_range = r"^[1-9]\d{5}$"	
# Condition 1:
# ^ asserts the position at the start of the string.
# [1-9] matches the first digit which must be from 1 to 9.
# \d{5} matches exactly five more digits (0-9).
# $ asserts the position at the end of the string.

regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	
# (?=(\d)\d\1) is a positive lookahead that ensures the pattern inside it is found, without consuming characters (so overlapping matches can be found).
# (\d) captures any digit.
# \d matches any single digit.
# \1 refers back to the first captured digit, ensuring it matches the same digit as the one captured by (\d).


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
