"""
Linguagem e lógica de programação
Professora: Juliana Sinnott 
Autor: Guilherme Soares Silva 
Atualizado em: 05/11/2022

Instruções
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
"""

name = str(input("Qual é o seu nome? "))
continuar = True
while continuar == True:
  try:
    anoNasc = int(input("Em que ano que você nasceu? (Entre 1922 e 2021): "))
    if anoNasc >= 1922 and anoNasc <= 2021:
      age = 2022 - anoNasc
      print(f"{name}, você terá {age} anos em 2022")
      continuar = False
    else:
      print("O ano inserido está fora do limite permitido.")   
  except:
    print("Insira um valor de entrada válido!")
