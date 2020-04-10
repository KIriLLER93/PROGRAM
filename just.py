def JUST(G):
	"""Проверяет является ли аргумент функции простым числом """
	if G < 2: R = False
	elif G < 4: R = True
	elif not G % G**0.5: R = False
	else:
		for j in range(2, int(G**0.5)+1):
			if not G % j:
				R = False
				break
		else:
			R = True
	return R

# print(JUST(11))

def JUSTRANGE_by_Erastophen(G, S = 2):
	"""Возвращает последовательность всех простых чисел от S до G"""

	A = [x for x in range (2, G)]
	d = 0
	L = A[-1]**0.5
	while A[d] < L:
		for y in range(d + 1, len(A)):
			if not A[y] % A[d]:
				A[y] = 1
		d +=1
		while A[d] == 1:
			d +=1
	A = list(filter(lambda x: x > 1, A))
	if S == 2:
		return A
	elif S >= A[-1]:
		# print("В данном диапазоне нет простых чисел!!!")
		return []
	else:
		i = len(A) - 1 
		while A[i] >= S:
			i -= 1
		A = A[i + 1:]
		return A

__version__ = "1.1"

