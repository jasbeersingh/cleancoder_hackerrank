import re

randstr = '''
This is a random str. It has some random values. what is mentioned over here is not a matter of concern.
what matters is that the required regex is able to work correctly, just as intended
set it to otter
'''

print(re.findall('is', randstr))
print(len(re.findall('is',randstr)))

print(re.findall('[i,s][i,s]', randstr))
print(re.findall('[i,t][i,t]',randstr))
