"""
Some generic patterns
[] ==> set of chars to be included
{} ==> range of characters i.e number of character in a group to satify the pattern 
^ ~ to exclude the specific pattern
\w ~ [A-Za-z0-9_]
\W ~ ^\w
\d ~ all digit i.e [0-9]
\s ~ [\f\n\r\t\v]
\S ~ ^\s
\f ~ formfeed
\n ~ new line
\r ~ carriage return
\t ~ tab
\v ~ vertical tab
"""
import re

def find_chars_including_pattern():
    a = "this is a randon string this is not per"
    b = "[his]{2,3}"

    print(re.findall(b,a))

def find_chars_excluding_pattern():
    a = "this is a randon string this is not per"
    b = "[^his]{2,3}"

    print(re.findall(b,a))

def replace_string():
    a = "This is a string"

    # by default atleast one occurance of pattern in [] must exist 
    regex = re.compile("[a-z]is")
    b = regex.sub('are', a)
    print(b)
    
    # In regex2 the pattern * indicates the 0 or more occurances of the pattern should exist.
    regex2 = re.compile("[a-z]*is")
    a = regex2.sub('are', a)
    print(a)

def random_string():
    randstr = "123 12323 12345 123234 11111"
    print(re.findall("\d{5}", randstr))


if __name__ == "__main__":
    #find_chars_excluding_pattern()
    #replace_string()
    random_string()
