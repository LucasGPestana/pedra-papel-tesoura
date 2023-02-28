import os
import random

def limpaTela():
    os.system('cls') or None

possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']
resposta = 'S'

while resposta == 'S':

  limpaTela()

  print("+" + "-----"*6 + "+")
  print("|    PEDRA, PAPEL OU TESOURA   |")
  print("+" + "-----"*6 + "+")
  print("1 - P1 VS. COMP")
  print("2 - P1 VS. P2 (PARTIDA LOCAL)")
  modo = int(input("Escolha o modo de jogo: "))

  match modo:
      case 1:
          escolhaP1 = input("Escolha entre PEDRA, PAPEL OU TESOURA: ").upper()
          escolhaCOMP = random.choice(possibilidades)

          limpaTela()

          print(f"P1 escolheu: {escolhaP1}")
          print(f"COMP escolheu: {escolhaCOMP}")
          if escolhaP1 == 'PEDRA' and escolhaCOMP == 'PAPEL':
              print("COMP venceu!")
          elif escolhaP1 == 'PAPEL' and escolhaCOMP == 'PEDRA':
              print("P1 venceu!")
          elif escolhaP1 == 'TESOURA' and escolhaCOMP == 'PEDRA':
              print("COMP venceu!")
          elif escolhaP1 == 'PEDRA' and escolhaCOMP == 'TESOURA':
              print("P1 venceu!")
          elif escolhaP1 == 'PAPEL' and escolhaCOMP == 'TESOURA':
              print("COMP venceu!")
          elif escolhaP1 == 'TESOURA' and escolhaCOMP == 'PAPEL':
              print("P1 venceu!")
          else:
              print("Empate!")
      case 2:
          print("Vez de P1")
          escolhaP1 = input("Escolha entre PEDRA, PAPEL OU TESOURA: ").upper()

          limpaTela()

          print("Vez de P2")
          escolhaP2 = input("Escolha entre PEDRA, PAPEL OU TESOURA: ").upper()

          limpaTela()

          print(f"P1 escolheu: {escolhaP1}")
          print(f"P2 escolheu: {escolhaP2}")

          if escolhaP1 == 'PEDRA' and escolhaP2 == 'PAPEL':
              print("P2 venceu!")
          elif escolhaP1 == 'PAPEL' and escolhaP2 == 'PEDRA':
              print("P1 venceu!")
          elif escolhaP1 == 'TESOURA' and escolhaP2 == 'PEDRA':
              print("P2 venceu!")
          elif escolhaP1 == 'PEDRA' and escolhaP2 == 'TESOURA':
              print("P1 venceu!")
          elif escolhaP1 == 'PAPEL' and escolhaP2 == 'TESOURA':
              print("P2 venceu!")
          elif escolhaP1 == 'TESOURA' and escolhaP2 == 'PAPEL':
              print("P1 venceu!")
          else:
              print("Empate!")

  resposta = input("Deseja jogar novamente (S/N)? ").upper()




