import os
import sys
import time
from datetime import datetime 


def mostrar_menu():
    print("Digite o número respectivo ao que você deseja fazer a seguir: ")
    print('''
          1 - Cadastrar nova reserva:
          2 - Listar resevas existentes
          3 - Cancelar reserva
          4 - Calcular estatísticas
          5 - Sair''')
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

def cadastrar_reserva():
    print()
    print("Cadastre uma nova reserva: ")
def listar_reservas():
    print()
    print("Listar as reservas já existentes: ")
def cancelar_reserva():
    print()
    print("Cancelar reservas: ")
def calcular_estatisticas():
    print()
    print("Calcular estatísticas: ")    
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
            listar_reservas()
        elif opçao == 3:
            cancelar_reserva()
        elif opçao == 4:
            calcular_estatisticas()            
        elif opçao == 5:
            sair()
            break
        else:
            print("Essa opçao não existe! Tente novamente.")
            time.sleep(2)
            continue
        time.sleep(3)
    
        
main()  
