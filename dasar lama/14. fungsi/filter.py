alfabet = ['a', 'b', 'c', 'd', 'e', 'u', 'k','a', 'i', 'x', 'y', 'z']

def filter_huruf_vokal(alfabet):
	vokal = ['a', 'i', 'u', 'e', 'o']
	if alfabet in vokal:
		return True
	else:
		return False

vokal_terfilter = filter(filter_huruf_vokal, alfabet)
# artinya filter semua hufuf vokal dalam list alfabet

for i in vokal_terfilter:
	print(i)
