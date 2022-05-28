#1.	Faça um programa que imprima seu nome completo na tela
nome = 'Jacques Araujo dos Santos'
print(nome)

#2.	Escreva um programa que exiba o resultado de
# 5a x 3b onde a = 2 e b = 5
a = 2
b = 5
resultado = ((5*a)*(3*b))
print(resultado)

#3.	Modifique o primeiro programa, inserindo uma terceira
# variável c = 5 e imprime a soma das três variáveis
a = 2
b = 5
c = 5
resultado = (a + b + c )
print(resultado)

#4.	Escreva um programa que leia dois números e que pergunte
# qual operação você deseja realizar. Você deve poder calcular
# a soma (+), subtração(-), multiplicação(*) e divisão(/).
# Exiba o resultado da operação.

nu1 = int(input('Digite Um Número: '))
nu2 = int(input('Digite Outro Número: '))
operacao = str(input('Escolha Uma Operação Aritmética ( +  -  *  / ): '))

if operacao == '+':
    adicao = nu1 + nu2
    print('A Adição entre {} e {} o resultado é: {}'.format(nu1, nu2, adicao))

elif operacao == '-':
    subtracao = nu1 - nu2
    print('A Subtração entre {} e {} o resultado é: {}'.format(nu1, nu2, subtracao))

elif operacao == '*':
    multiplicacao = nu1 * nu2
    print('A Multiplicação entre {} e {} o resultado é: {}' .format(nu1,nu2, multiplicacao))

elif operacao == '/':
    divisao = nu1 / nu2
    print('A Divisão entre {} e {} o resultado é: {}' .format(nu1, nu2, divisao))

else:
    print('Operação inválida, por favor escolha uma das opções informadas')

#5.	Escreva um programa em Python para contar de 1 até 10.
#a)	usando a instrução while
n = 1
while n < 11:
    print(n)
    n += 1

#b)	usando a instrução for e a função range
n = 1
for elemento in range (1,11):
    print(elemento)

#6.	Escreva um programa para contar quantos números pares e ímpares existentes entre 1 e 10 bem como a soma deles.
#a)	usando a instrução while
x = par = impar = 0
while x <=10:
    if x % 2 == 0:
        print(f'O número {x} é PAR')
        par += 1


    else:
        print(f'O número {x} é IMPAR')
        impar += 1

    x+=1

#b) usando a instrução for e as funções range e sum
lista = [1,2,3,4,5,6,7,8,9,10]
sum(lista)
for num in intervalo (1,11):
for num in lista:
    if num % 2 == 0:
        print(f'O número {num} é PAR')
    else:
        print(f'O número {num} é IMPAR')

#7.Escreva um programa para resolver equações do segundo grau
# representadas por ax2 + bx + c usando a Fórmula de Bhaskara.

#a) sem usar o módulo math
a = float(input('Digite um número para a:  '))
b = float(input('Digite um número para b:  '))
c = float(input('Digite um número para c:  '))
print('TEMOS: ')
print(f'a= {a:.0f} b= {b:.0f} c= {c:.0f}')

delta = (b ** 2 - 4 * a * c)
print(f'delta= {b:.0f}² - 4*{a:.0f}*{c:.0f}\nValor de delta= {delta:.0f}')

if delta < 0 or a == 0:
    print('Impossível de calcular a equação x1 e x2, o valor de (a) deve ser diferente de 0.')

else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

print(f'Resolução da equação x1= {x1:.0f}, x2= {x2:.0f}')

#b) usando o módulo math
import math
a = float(input('Digite um número para a:  '))
b = float(input('Digite um número para b:  '))
c = float(input('Digite um número para c:  '))
print('TEMOS: ')
print(f'a= {a:.0f} b= {b:.0f} c= {c:.0f}')

delta = (b ** 2 - 4 * a * c)
print(f'delta= {b:.0f}² - 4*{a:.0f}*{c:.0f}\nValor de delta= {delta:.0f}')

if delta < 0 or a == 0:
    print('Impossível de calcular a equação x1 e x2, o valor de (a) deve ser diferente de 0.')

else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f'Resolução da Fórmula de Bhaskara x1= {x1:.0f}, x2= {x2:.0f}')

#c)Teste seu programa com os coeficientes:
#a = 1, b = -5, c = 6
#Resposta abaixo
#Digite um número para a: 1
#Digite um número para b: -5
#Digite um número para c: 6
#TEMOS:
#a = 1
#b = -5
#c = 6
#delta = -5² - 4 * 1 * 6
#Valor de delta = 1
#Resolução da Fórmula de Bhaskara x1 = 3, x2 = 2


#a = 1, b = 0, c = -9
#Resposta abaixo
#Digite um número para a: 1
#Digite um número para b: 0
#Digite um número para c: -9
#TEMOS:
#a = 1
#b = 0
#c = -9
#delta = 0² - 4 * 1 * -9
#Valor de delta = 36
# Resolução da Fórmula de Bhaskara x1 = 3, x2 = -3

#a = 5, b = -45, c = 0
#Resposta abaixo
#Digite um número para a: 5
#Digite um número para b: -45
#Digite um número para c: 0
#TEMOS:
#a = 5
#b = -45
#c = 0
#delta = -45² - 4 * 5 * 0
#Valor de delta = 2025
#Resolução da Fórmula de Bhaskara x1 = 9, x2 = 0

#a = 1, b = -1, c = -12
#Resposta abaixo
#Digite um número para a: 1
#Digite um número para b: -1
#Digite um número para c: -12
#TEMOS:
#a = 1
#b = -1
#c = -12
#delta = -1² - 4 * 1 * -12
#Valor de delta = 49
#Resolução da Fórmula de Bhaskara x1 = 4, x2 = -3

#a = 1, b = -6, c = 10
#Resposta abaixo
#Digite um número para a: 1
#Digite um número para b: -6
#Digite um número para c: 10
#TEMOS:
#a = 1
#b = -6
#c = 10
#delta = -6² - 4 * 1 * 10
#Valor de delta = -4
#Impossível de calcular a equação x1 e x2, o valor de(a) deve ser diferente de 0.

#8.	Reescreva o programa acima criando uma função bhaskara que recebe
# como parâmetros os coeficientes a, b e c e retorna as raízes da equação.
print('Digite abaixo os coeficientes a, b, c. ')
import math

a = int(input("Digite um número para a:  "))
b = int(input("Digite um número para b:  "))
c = int(input("Digite um número para c:  "))

delta = b**2 - 4*a*c

def bhaskara(a, b, c):
    raizes = []
    if delta < 0:
        return None

    else:
        r1 = (-b + math.sqrt(delta)) / (2*a)
        raizes.append(r1)
        r2 = (-b - math.sqrt(delta)) / (2*a)
        raizes.append(r2)
        return raizes

resultado=bhaskara(a, b, c)

print(resultado)

#9. Considerando a string s = 'Mentorama' escreva um programa que:
#a) converta a string para maiúsculo, em seguida
#b) imprima-a de trás para frente
#c) imprima somente as vogais
s = "Mentorama"
maiuscula = s.upper()
invertida = maiuscula[::-1]

def vogais(string):
    v = []
    for letra in string:
        if letra in 'AEIOU':
            v.append(letra)
    return v

print("a)", maiuscula)
print("b)", invertida)
print("c)", vogais(invertida))

#10.	Escreva um programa que receba como entrada do usuário
# o nome “João” sobrenome “da Silva”, idade “25”, Cidade “São Paulo”,
# ddd “11”, telefone “3333-3333” e faça as seguintes instruções:

#a)	imprima na tela o nome completo em uma única linha Nome: João da Silva
nome = 'João da Silva'
print('Nome: ', nome)

#b)	imprima na tela o telefone com ddd em uma única linha Telefone: (11)3333-3333
telefone = '(11)3333-3333'
print('Telefone: ', telefone)

#c)	Imprima na tela a idade Idade: 25
idade = '25'
print('Idade: ', idade)

#d)	Imprima na tela a cidade Cidade: São Paulo
cidade = 'São Paulo'
print('Cidade: ', cidade)


