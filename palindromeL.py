from collections import Counter
s = 'aba'

for v in Counter(s).itervalues():
	print(v)

