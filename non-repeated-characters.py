# counting-non-repeating-letter
import collections
str1 = 'alphxxdida'
e=[]
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] == 1:
      e.append(c)
print(len(e))
