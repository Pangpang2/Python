import re


line = 'I think I understand regular expressions'
reg = re.compile(r'think')
match_resutl = reg.match(line, re.M|re.I)
if match_resutl:
    print 'Match found:' + match_resutl.group()
else:
    print 'No match was found'


search_resutl = re.search(r'think', line, re.M|re.I)
if search_resutl:
    print 'Search found:' + search_resutl.group()
else:
    print 'Nothing found in search'

