'''
João está trabalhando em uma mina, tentando retirar o máximo que consegue de diamantes "<>". Ele deve excluir todas as particulas de areia "." do processo e a cada retirada de diamante, novos diamantes poderão se formar. Se ele tem como uma entrada .<...<<..>>....>....>>>., três diamantes são formados. O primeiro é retirado de <..>, resultando  .<...<>....>....>>>. Em seguida o segundo diamante é retirado, restando .<.......>....>>>. O terceiro diamante é então retirado, restando no final .....>>>., sem possibilidade de extração de novo diamante.

Entrada

Deve ser lido um valor inteiro N que representa a quantidade de casos de teste. Cada linha a seguir é um caso de teste que contém até 1000 caracteres, incluindo "<,>, ."

Saída

Você deve imprimir a quantidade de diamantes possíveis de serem extraídos em cada caso de entrada.
'''
# -*- coding: utf-8 -*-

def extrair_diamantes(caso_teste):
  diamantes = 0
  pilha = []

  for caractere in caso_teste:
    if caractere == "<":
      pilha.append(caractere)
    elif caractere == ">" and pilha:
      pilha.pop()
      diamantes += 1

  return diamantes


def main():
  n = int(input("Digite o número de casos de teste: "))
  resultados = []

  for _ in range(n):
    caso_teste = input("Digite o caso de teste: ")
    resultados.append(extrair_diamantes(caso_teste))

  print("\nQuantidade de diamantes extraídos em cada caso:")
  for i, resultado in enumerate(resultados):
    print(f"Caso {i + 1}: {resultado} diamantes")


if __name__ == "__main__":
  main()
