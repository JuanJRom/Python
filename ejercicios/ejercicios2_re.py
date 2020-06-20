import re

tex = '423'

# No letters
nl = '[^a-zA-Z]+$'
print('No letters: ', True if re.match(nl, tex) else False)

# Numbers only
no = '\d+$'
print('Numbers only: ', True if re.match(no, tex) else False)

# Capital letters only
cl = '[A-Z]+$'
print('Capital letters only: ', True if re.match(cl, tex) else False)

# No numbers
nn = '[^0-9]'
print('No Numbers: ', True if re.match(nn, tex) else False)