'''
6.	Escreva uma função chamada right_justify, que receba uma string chamada s
 como parâmetro e exiba a string com espaços suficientes à frente para que a
 última letra da string esteja na coluna 70 da tela:

>>> right_justify('monty')
Dica: Use concatenação de strings e repetição. Além disso, o Python oferece
uma função integrada chamada len, que apresenta o comprimento de uma string,
então o valor de len('monty') é 5.
'''
nome = str(input('Insira uma palavra: '))
def right_justify(nome):
    i=1
    j=70-len(nome)
    while i<=j:
        nome = ''+nome
        i += 1
    return print(nome)
right_justify(nome)