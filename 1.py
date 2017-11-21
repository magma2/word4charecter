import itertools

char = 'abcdefghijklmnopqrstuvwxyz'

n = 4

for xs in itertools.product(char, repeat=n):
	print xs