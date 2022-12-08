"""
Linguagem e lógica de programação
Professora: Juliana Sinnott 
Autor: Guilherme Soares Silva 
Atualizado em: 31/10/2022

Instruções
Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir. Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”.
Não é necessário, mas, caso deseje tornar o sistema mais realista para que o tempo realmente passe em segundos, você pode usar a função time.sleep() que existe na Python (acesse o link em anexo). No entanto, é preciso adicionar uma biblioteca antes de executá-la.

Codepark 1 - Aula 4
Algoritmo para representar o andar de 1 até 20 na ordem decressente, com excessão do andar 13.
Utilizando os três laços de repetição
"""

#Utilizando as duas formas com o laço de repetição for

for andar in range(20, 13, -1):
  print("Andar n°", andar)
for andar in range(12, 0, -1):
  print("Andar n°", andar)
  
for andar in range(20, 0, -1):
  if andar != 13:
    print("Andar n°", andar)
    
#Utilizando o laço de repetição while

andar2 = 20
while andar2 > 0:
  print(f'{andar2}° andar')
  andar2 -= 1
  if andar2 != 13:
    continue
