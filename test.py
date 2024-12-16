import collections

c = collections.Counter()

with open('/usr/share/dict/words', 'rt') as file:
  for line in file:
    c.update(line.rstrip().lower())
print('Most common:')
for letter, count in c.most_common(3):
  print(f'{letter}: {count:>7}')