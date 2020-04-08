import re

a = 'qwe'
b = 'qwe thjvs;b lkjffbq; qwe;sdjfqwevsdhbllgbqwekdfj;gqenrfqwee'

a = len(re.findall(a,b))

print(a)
