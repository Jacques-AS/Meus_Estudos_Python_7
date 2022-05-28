'''
5.	Escreva um programa Python para inserir um elemento
no início de um determinado DicionárioOrdenado.
DicionárioOrdenado original:
DicionárioOrdenado ([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
Insira um elemento no início do referido DicionárioOrdenado:
DicionárioOrdenado atualizado:
DicionárioOrdenado ([('color4', 'Orange'), ('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
'''
dicionario_ordenado = {('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')}
dicionario_ordenado.append({('color4', 'Orange')})
print(dicionario_ordenado)

