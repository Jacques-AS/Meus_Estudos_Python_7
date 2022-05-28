'''
4.	Crie 3 conjuntos conforme estrutura a seguir:
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])


Faça as seguintes operações sobre conjuntos:
a)	Faça a união dos três conjuntos e imprima o resultado
b)	Verifique quais os elementos comuns do conjunto setx e sety e imprima o resultado
c)	Verifique se o conjunto setx é subconjunto do conjunto sety e setz utilizando issubset()
d)	Verifique quais elementos do conjunto setx não existem em sety
'''

print('*****   a)     *****')
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
unidos = setx.union(sety, setz)
print(f'A união dos três conjunto:\n{unidos}')
print()

print('*****   b)     *****')
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
setb = set(setx).intersection(sety)
print(f'Os elementos comuns do conjunto setx e sety:\n{setb}')
print()

print('*****   c)     *****')
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print(f'O conjunto setx é subconjunto sety: {setx.issubset(sety)}')
print(f'O conjunto setx é subconjunto setz: {setx.issubset(setz)}')
print()

print('*****   d)     *****')
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print(f'Quais elementos do conjunto setx não existem em sety:\n{setx.difference(sety)}')
print()
