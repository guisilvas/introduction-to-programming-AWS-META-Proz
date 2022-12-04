"""
Linguagem e lógica de programação
Professora: Juliana Sinnott 
Autor: Guilherme Soares Silva 
Atualizado em: 07/11/2022

Instruções do projeto
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.
"""

def calc_opera (n1, n2, op):
  res: float

  if (op == 1):
    res = n1 + n2
  elif (op == 2):
    res = n1 - n2
  elif (op == 3):
    res = n1 * n2
  elif (op == 4):
    res = n1 / n2
  else:
    res = 0
    
  return res

print('-' * 20)
print('FERRAMENTA DE CALCULO')
print('-' * 20)
print('\n' * 2)
operador = 100

while (operador != 0):
  operador = int(input('\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n\nDigite a opção desejada: '))
  
  if (operador > 4):
    print('Essa opção não existe\n\n')
    continue
  elif (operador == 0):
    continue

  num1 = float(input('Digite o 1º numero: '))
  num2 = float(input('Digite o 2º numero: '))
  print('\n' * 2)
  print('O resultado da operação é {:.2f}\n\n'.format(calc_opera(num1, num2, operador)))
