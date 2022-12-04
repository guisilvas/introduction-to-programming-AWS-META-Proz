"""
Linguagem e lógica de programação
Professora: Juliana Sinnott 
Autor: Guilherme Soares Silva 
Atualizado em: 04/11/2022

Instruções do projeto
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
operacao = int(input('''Insira o número da operação:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
'''))

if operacao == 1:
  result = n1 + n2
elif operacao == 2:
  result = n1 - n2
elif operacao == 3:
  result = n1 * n2
elif operacao == 4:
  result = n1 / n2
else:
 result = '0'
print(f'O resultado é: {result}')
