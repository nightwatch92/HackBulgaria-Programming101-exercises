def count_consonants(str):
	consonants = "bcdfghjklmnpqrstvwxz"
	count = 0
	for v in consonants:
		count += str.lower().count(v)
	return count
