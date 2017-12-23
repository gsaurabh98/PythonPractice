import re

# \s [\f\n\t\v\r]
# \S [^\f\n\t\v\r]

if re.search(r'\w{2,20}\s\w{2,20}', 'Saurabh Sharma'):
    print 'Valid full name'