import re

digits = '123 1234 12345 123456 1234567'

print (len(re.findall('\d{5,7}',digits)))


cities = {"Paris", "Lyon", "London","Berlin","Paris","Birmingham"}
print cities