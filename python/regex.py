import re

nameAge = '''
Ram is 22 and Sita is 20
Ajay is 38 and Jay is 19
'''

names = re.findall(r'[A-Z][a-z]*', nameAge)
ages = re.findall(r'\d{1,3}', nameAge)

ageDict = {}

for x,y in zip(names,ages):
    ageDict[x] = y

print(ageDict)

