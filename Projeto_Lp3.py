import pickle 
import os
import sys
import time
from datetime import datetime 

def mostrar_menu():
    print("O que você deseja fazer? ")
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
    
total_quartos = {'Standard': 10,
                 'Premium': 5,
                 'Luxo': 3}
reservas = []
total_reservas = 0
maior_reservas = 0
nome_reserva_cara = ""
nome_tempo_maior = ""
maior_tempo = 0
nome_arquivo = "reservas.pkl"
agenda_telefonica = {"joao": 2345678, "Maria": 345678}

def data():
    formato = "%d/%m/%Y"
    check_in = input("Digite a data de Check-In (No modelo dd/mm/aaaa): ")
    check_in = datetime.strptime(check_in, formato).date()
    check_out = input("Digite a data de Check-Out (No modelo dd/mm/aaaa): ")
    check_out = datetime.strptime(check_out, formato).date()
    

def consultar_disponibilidade(checkin, checkout, tipo_quarto, quantidade_quartos):  
    print("Iremos consultar a disponibilidade...")
    for r in reservas:
        if r['tipo_quarto'] == tipo_quarto:
            if checkin < r['checkout'] and checkout > r['checkin']:
                quartos_consumidos += r['quantidade_quartos']    

def cadastrar_reserva():
    while True: 
       print()
       print("Cadastre uma nova reserva: ")
       nome = input("Digite o nome do responsável pela reserva: ").strip() 
       if nome == "":
          print("Nome inválido!")
          time.sleep(3)
          continue
       data()
       break
    mostrar_menu()
    
       



def carregar_reservas():
    with open(nome_arquivo, "r") as f:
        dados_carregados = pickle.load(f)
        return dados_carregados

def cancelar_reserva():
    print()
    print("Cancelar reservas: ")

def salvar_dados():
    with open(nome_arquivo, "wb") as f:
        pickle.dump(agenda_telefonica, f)

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
        mostrar_menu()
        opçao = int(input(": "))
        if opçao == 1:
            cadastrar_reserva()
        elif opçao == 2:
            carregar_reservas()  
        elif opçao == 3:
            consultar_disponibilidade()     
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





