import re

str = 'I would like to eat hat'

regex = re.compile("[h]at")

new_str = regex.sub('food',str)

print new_str

