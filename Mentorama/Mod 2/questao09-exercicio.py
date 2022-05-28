'''
9.	Dada uma lista encadeada de caracteres formada por uma sequência alternada
de letras e dígitos, construa um método que retorne uma lista na qual as letras
são mantidas na sequência original e os dígitos são colocados na ordem inversa.
Exemplos:
A 1 E 5 T 7 W 8 G → A E T W G 8 7 5 1
'''

from collections import deque
letras=[]
numeros=[]
digitos=[0,1,2,3,4,5,6,7,8,9]
lista=input("Digite a sequência: ")

for e in lista:
    if e in digitos:
        numeros.append(e)
    else:
        letras.append(e)
numeros.sort(key=int, reverse=True)
letras.sort()
total = numeros + letras
print(total)