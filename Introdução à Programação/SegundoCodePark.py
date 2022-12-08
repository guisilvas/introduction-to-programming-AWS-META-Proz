"""
Linguagem e lógica de programação
Professora: Juliana Sinnott 
Autor: Guilherme Soares Silva 
Atualizado em: 31/10/2022

Instruções do projeto
Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
"""

print(
  "Seja bem vindo(a)! Para selecionar o tipo do seu veículo faça o questionário a seguir."
)

quantidadeRodas = int(input("Quantas rodas possui seu veículo? "))
pesoBruto = float(input("Qual é o peso bruto do seu veículo em Kg? "))
numeroPessoas = int(input("Quantas pessoas seu veículo suporta? "))

if quantidadeRodas <= 3 and numeroPessoas <= 3 and pesoBruto < 3500:
  print("A categoria indicada é a CNH A")
elif quantidadeRodas == 4 and numeroPessoas <= 8 and pesoBruto <= 3500:
  print("A categoria indicada é a CNH B")
elif quantidadeRodas >= 4 and numeroPessoas <= 8 and pesoBruto >= 3500 <= 6000:
  print("A categoria indicada é a CNH C")
elif quantidadeRodas >= 4 and numeroPessoas >= 8 and pesoBruto >= 3600 <= 6000:
  print("A categoria indicada é a CNH D")
elif quantidadeRodas >= 4 and numeroPessoas >= 8 and pesoBruto > 6000:
  print("A categoria indicada é a CNH E")
else:
  print("Você inseriu algum dado incorretamente. Tente novamente.")
