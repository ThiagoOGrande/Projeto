import pickle 
import os
import sys
import time
from datetime import datetime 

reservas = []
nome_arquivo = "reservas.pkl"

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
    
valor_quartos = {'Standard': 100,
                 'Premium': 180,
                 'Luxo': 250}    

total_quartos = {'Standard': 10,
                 'Premium': 5,
                 'Luxo': 3}


def carregar_reservas():
    try:
        with open (nome_arquivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def salvar_reservas():
    with open (nome_arquivo, "wb") as f:
        pickle.dump(reservas, f)        

def exibir_estatisticas():
    print("\n Carregando para exibir as estatísticas gerais das reservas, aguarde alguns instantes...")
    todas_reservas = len(reservas)        

def cancelar_reservas():
    buscar_nome = input("\n Digite o nome do responsável pela reserva que desejas cancelar: ").lower()
    for r in (reservas):
        if r ["responsável"] == [buscar_nome]:
            print (r)
            data_hoje = datetime.today()
            if r["check_in"] == [data_hoje]:
                reservas.remove(r)
            else:
                print("\n Não foi possível cancelar esta reserva, tente novamente em alguns instantes...")
                time.sleep(3)    

def listar_reservas():




def mostrar_menu():
    print("O que você deseja fazer? ")
    print('''
          1 - Cadastrar nova reserva:
          2 - Carregar reservas já existentes
          3 - Consultar disponibilidade
          4 - Cancelar reserva
          5 - Listar reservas
          6 - Exibir estatísticas gerais
          7 - Sair''')
    print()




def data():
    formato = "%d/%m/%Y"
    check_in = input("Digite a data de Check-In (No modelo dd/mm/aaaa): ")
    #try:
     #   check_in = datetime.strptime(check_in, formato).date()
    #except ValueError:  
     #   print("Data de Check-In inválida!")  
      #  quit()
    check_in = datetime.strptime(check_in, formato).date()
    check_out = input("Digite a data de Check-Out (No modelo dd/mm/aaaa): ")
    #try: 
      #  check_out = datetime.strptime(check_out, formato).date()
    #except ValueError:
     #   print("Data de Check-Out inválida!")
      #  quit()    
    check_out = datetime.strptime(check_out, formato).date()
    
def quartos():
    print("Digite qual dos quartos listados abaixo você gostaria: ")    
    print('''
          1 - Standard
          2 - Premium
          3 - Luxo
          ''')
    quarto = input(": ")
    if quarto == 1:
        print("Standard")
    

def consultar_disponibilidade(checkin, checkout, tipo_quarto, quantidade_quartos):  
    print("Iremos consultar a disponibilidade...")
    for r in reservas:check_out = datetime.strptime(check_out, formato).date()
        if r['tipo_quarto'] == tipo_quarto:
            if checkin < r['checkout'] and checkout > r['checkin']:
                quartos_consumidos += r['quantidade_quartos'] 


def cadastrar_reserva():
    while True: 
       print()
       print("Cadastre uma nocheck_out = datetime.strptime(check_out, formato).date()va reserva: ")
       nome = input("Digite o nome do responsável pela reserva: ").strip() 
       if nome == "":
          print("Nome inválido!")
          time.sleep(3)
          continue
       data()
       break
    mostrar_menu()
    quartos()
    

    

def sair():   
    print()
    print("Muito obrigado pela preferẽncia, vole sempre!")  

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
