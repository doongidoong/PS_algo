import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)


l1 = ['A', 'B']
l2 = ['1', '2']
l3 = ['s', 'k']

l4 = ['11', '22']
for i in itertools.product(l1,l2,l3,l4): #l1과 l2의 모든 쌍을 지어 리턴한다
	print(i)
