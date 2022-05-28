'''
1.	Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a)	Quantas pessoas foram cadastradas
b)	A média de idade
c)	Uma lista com as mulheres
d)	Uma lista de pessoas com idade acima da média
'''
print()
print('***** SISTEMA DE CADASTRO *****')
lista = []
lista_mulher = []
soma_idade = 0

while True:
    nome = input('Digite o seu nome: ').capitalize()
    sexo = input('Digite seu sexo [M/F]?: ').upper()
    idade = int(input('Digite sua idade: '))
    dic = {'nome': nome, 'sexo': sexo, 'idade': idade}
    lista.append(dic)
    soma_idade+= idade

    if sexo == 'F':
        lista_mulher.append(sexo)
        lista_mulher.append(nome)
    pergunta = input('Quer continuar com os cadastros [S/N]?: ').upper()

    if not pergunta == 'S':
        break
print()
print('***** ANÁLISE DO SISTEMA DE CADASTRO *****')
print('<<<>>>'*10)
print(f'AO TODO FORAM REGISTRADAS {len(lista)} PESSOA/S')
print('<<<>>>'*10)
print(f'A MÉDIA DAS IDADE/S É DE {soma_idade/len(lista)} ANO/S DE IDADE')
print('<<<>>>'*10)
print('LISTA DE MULHERES')
for lista_mulher in lista:
    if lista_mulher['sexo'] == 'F':
        print('Nome:', lista_mulher['nome'], 'Idade:', lista_mulher['idade'])

print('<<<>>>'*10)
print('LISTA DE PESSOAS COM IDADE ACIMA DA MÉDIA')
for lista_mulher in lista:
    if(lista_mulher['idade'] > (soma_idade/len(lista))):
        print('Nome:',lista_mulher['nome'],  'Sexo:',lista_mulher['sexo'],  'Idade:',lista_mulher['idade'])

