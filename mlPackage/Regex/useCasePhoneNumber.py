import re

#\w [a-zA-Z0-9_] will match all the values present in []
#\W [^a-zA-Z0-9_] will match everything but in []
phone = '443-689-0029'

if re.search('\w{3}-\w{3}-\w{4}',phone):
    print 'thats correct number'

# though its digit, so replacing 'w' with 'd' wont make any difference.