
import os
import sys
import time
from datetime import datetime 


def mostrar_menu():
    print("Digite o número respectivo ao que você deseja fazer a seguir: ")
    print('''
          1 - Cadastrar nova reserva:
          2 - Carregar reservas já existentes
          3 - Consultar disponibilidade
          4 - Cancelar reserva
          5- Listar reservas
          6- Exibir estatísticas gerais
          7- Sair''')
    print()
 
'''
nome = input("Digite o seu nome: ")
checkin = print("1")
checkout = print("1")
tipo_quarto = print("1")
quantidade_quartos = print("1")

reservas = [
        {
            "Responsável: ": nome,
            "Check-in: ": checkin,
            "Check-out: ": checkout,
            "Tipo de quarto: ": tipo_quarto,
            "Quantidade de quartos": 5
        },
    ]
'''
def validar_datas():
    while True:
       tempo_dias = (checkout - checkin).days
       quant_dias = tempo_dias
       if quant_dias > maior_tempo:
          maior_tempo = quant_dias
          nome_maior_tempo = nome
       if quant_dias < 0:
          print("Data de check-in maior que de check-out")
          time.sleep(3)
          continue
       os.system("clear")
       if checkout < checkin:
          print("O Check-out não pode ser maior que o Check-in! Faça novamente")
          time.sleep(3)
          continue


def cadastrar_reserva():
    while True: 
       print()
       print("Cadastre uma nova reserva: ")
       nome = input("Digite o nome do responsável pela reserva: ").strip() 
       if nome == "":
          print("Nome inválido!")
          time.sleep(3)
          continue
       time.sleep(2)
    
       checkin = int(input("Digite a data de Check-In, no formato (dd/mm/aa): "))
       checkin = datetime.strptime(check_in, formato).date()
       checkout = int(input("Digite a data de Check-Outn, no formato (dd/mm/aa): "))
       checkout = datetime.strptime(check_out, formato).date()
       os.system('clear')
       validar_datas()
       quarto = input("Digite o tipo de quarto que deseja:")




def carregar_reservas():
    print()
    print("Carregar reservas já existentes: ")
def consultar_reservas():
    print()
    print("Consultar disponibilidade: ")


def cancelar_reserva():
    print()
    print("Cancelar reservas: ")
def exibir_estatisticas():
    print()
    print("Calcular estatísticas: ")    
def listar_reservas():
    print()
    print("Listar as reservas já existentes: ")    
def sair():   
    print()
    print("Valeu pela preferência vei, vole sempre!")  


def main():
    while True:
        os.system("clear")
        mostrar_menu()
        opçao = int(input(": "))
        if opçao == 1:
            cadastrar_reserva()
        elif opçao == 2:
            carregar_reservas()  
        elif opçao == 3:
            consultar_reservas()     
        elif opçao == 4:
            cancelar_reserva()     
        elif opçao == 5:
            listar_reservas()
        elif opçao == 6:
            exibir_estatisticas()            
        elif opçao == 7:
            sair()
            break
        else:
            print("Essa opçao não existe! Tente novamente.")
            time.sleep(2)
            continue
        time.sleep(3)
    
        
main()  
