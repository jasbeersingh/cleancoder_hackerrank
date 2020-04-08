import re
import requests

def find_pattern_in_text(text, pattern):
    all_matches = re.findall(pattern, text)
    esc_char = re.compile("([\r\t]|<body>|</body>|<script>[/s/S]*?</script>)*")
    
    text = esc_char.sub("", all_matches[0])
    return text
    #all_matches_set = set(all_matches)
    print(all_matches)
    #print(len(all_matches))
    #print(all_matches_set)
    #print(len(all_matches_set))

url = "http://localhost:8000/"
a = requests.get(url)
pattern = "<body>[\s\S]*?</body>"
#print(a.text)
text = find_pattern_in_text(a.text, pattern)
print(text)
