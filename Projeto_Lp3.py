import pickle 
import os
import sys
import time
from datetime import datetime 

reservas = []
nome_arquivo = "reservas.pkl"
quartos_disponíveis = {"standard": 10, "premium": 5, "luxo": 3}


def mostrar_menu():
    print("\nO que você deseja fazer? ")
    print('''
          1 - Cadastrar nova reserva:
          2 - Carregar reservas já existentes
          3 - Consultar disponibilidade
          4 - Cancelar reserva
          5 - Listar reservas
          6 - Exibir estatísticas gerais
          7 - Sair''')
    print()
    opçao = int(input(": "))
    return opçao


def carregar_reservas():
    try:
        with open (nome_arquivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def salvar_reservas():
    global reservas
    with open (nome_arquivo, "wb") as f:
        pickle.dump(reservas, f)        


def exibir_estatisticas():
    print("\n Carregando para exibir as estatísticas gerais, aguarde alguns instantes...")
    time.sleep(3)
    print(f"\n RESERVAS: {len(reservas)} \n")  
    quantidade_standard = 0
    quantidade_premium = 0
    quantidade_luxo = 0   
    reserva_mais_cara = 0
    responsavel_reserva_mais_cara = ""
    valor_total_reservas = 0
    maior_quantidade_dias = 0
    responsavel_mais_dias = ""

    for r in (reservas):
        if r["tipo_de_quarto"] == "standard":
            valor_quarto = 100
        elif r["tipo_de_quarto"] == "premium":
            valor_quarto = 180
        else:
            valor_quarto = 250      
        valor_reserva = r["quantidade_quartos"] * r["tipo_de_quarto"] * valor_quarto      
        if r["tipo_de_quarto"] == "standard":
            quantidade_standard += r["quantidade_quartos"]
        elif r["tipo_de_quarto"] == "premium":
            quantidade_premium += r["quantidade_quartos"]
        else:
            quantidade_luxo += r["quantidade_quartos"]   
        valor_total_reservas += valor_reserva
        if valor_reserva > reserva_mais_cara:
            reserva_mais_cara = valor_reserva
            responsavel_reserva_mais_cara = r["responsável"]
        if r["quantidade_dias"] > maior_quantidade_dias:    
            maior_quantidade_dias = r["quantidade_dias"]
            responsavel_mais_dias = r["responsável"]

    print(f"\n Valor total das reservas: {valor_total_reservas}")    
    print(f"\n Reserva mais cara: {reserva_mais_cara} \n Responsável pela reserva mais cara: {responsavel_reserva_mais_cara}")    
    print(f"\n Quantidade de dias da reserva mais longa: {maior_quantidade_dias} \n Responsável pela reserva mais longa: {responsavel_mais_dias}")
    print(f"\n Quantidade de quartos Standard: {quantidade_standard} \n Quantidade de quartos Premium: {quantidade_premium} \n Quantidade de quartos Luxo: {quantidade_luxo}")
     
    sair = int(input("\n  Digite [1] para sair: "))
    if sair == 1:
        return   
    


def cancelar_reservas():
    buscar_nome = input("\n Digite o nome do responsável pela reserva que desejas cancelar: ").lower()
    cont = 0
    for r in (reservas):
        if r ["responsável"] == [buscar_nome]:
            cont += 1
            print(f"\n Nome: {r["responsável"]} \n Check-in: {r["checkin"]} \n Check-out: {r["checkout"]} \n Tipo de quarto: {r["tipo_de_quarto"]} \n Quantidade de quartos: {r["quantidade_quartos"]} \n Dias de reserva: {r["quantidade_dias"]} ")
            cancelar = int(input("\n Deseja continuar e cancelar a reserva? \n [1] - Sim \n [2] - Não"))
            if cancelar == 2:
                return
            else:    
                data_atual = datetime.today()
                if r["checkin"] > data_atual:
                    reservas.remove(r)
                    print("\n A reserva foi cancelada com êxito!")
                else:
                    print("\n Não foi possível cancelar esta reserva, a data de Check-in já passou.")    
    if cont == 0:
        print("\nNão existem reservas com este nome.")
    sair = int(input("\n  Digite [1] para sair: "))
    if sair == 1:
        return   


def listar_reservas(a):
    reservas = carregar_reservas()
    print("\nTodas as reservas já cadastradas: ")
    for r in (reservas):
            print(f"\n Nome: {r["responsável"]} \n Check-in: {r["checkin"]} \n Check-out: {r["checkout"]} \n Tipo de quarto: {r["tipo_de_quarto"]} \n Quantidade de quartos: {r["quantidade_quartos"]} \n Dias de reserva: {r["quantidade_dias"]} ")
    sair = int(input("\n  Digite [1] para sair: "))
    if sair == 1:
        return   

def consultar_disponibilidade(checkin, checkout, tipo_quarto, quantidade_quartos):  
    quartos_reservados = 0
    print("Iremos consultar a disponibilidade...")
    for r in (reservas):
        if r["tipo_de_quarto"] == tipo_quarto:
            if checkin < r["checkout"] and checkout > r["checkin"]:
                quartos_reservados += r["quantidade_quartos"]  
    global disponibilidade
    disponibilidade = quartos_disponíveis[tipo_quarto] - quartos_reservados
    if quantidade_quartos > disponibilidade:
        return False
    else:
        return True     
        

def consultar_reservas():
    buscar_nome = input("\nDigite o nome do responsável pela reserva que desejas consultar: ").lower()
    nome_encontrado = 0
    for r in (reservas):
        if r ["responsável"] == [buscar_nome]:
            print("\nReserva: ")
            print(f"\n Nome: {r["responsável"]} \n Check-in: {r["checkin"]} \n Check-out: {r["checkout"]} \n Tipo de quarto: {r["tipo_de_quarto"]} \n Quantidade de quartos: {r["quantidade_quartos"]} \n Quantidade de dias de reserva: {r["quantidade_dias"]} ")
            nome_encontrado += 1
    if nome_encontrado == 0:
        print("\n  Não existem reservas com este nome, tente outro! ")       
        time.sleep(3) 
    sair = int(input("\n  Digite [1] para sair: "))
    if sair == 1:
        return   


def cadastrar_reserva(): 
    reservas = []
    nome = input("\nDigite o nome do responsável pela reserva: ").lower().split()
    if nome == "":
        print("Nome inválido!")
        time.sleep(3)
    formato = "%d/%m/%Y"
    quantidade_dias_reserva = 0
    while True:
        while True:
            checkin = input("\nDigite a data de Check-in (No modelo dd/mm/aaaa): ")
            try:
                check_in = datetime.strptime(checkin, formato).date()
                break
            except ValueError:
                print("\n  Data inválida! Tente novamente! ")
        check_in = check_in    

        while True:
            checkout = input("Digite a data de Check-out (No modelo dd/mm/aaaa): ") 
            try:
                check_out = datetime.strptime(checkout, formato).date()
                break
            except ValueError:
                print("\n  Data inválida! tente novamente!")
        check_out = check_out

        quantidade_dias_reserva = (check_out - check_in).days

        if quantidade_dias_reserva < 0:
            print("\n  Data inválida! A data de Check-in é maior que a de Check-out. Tente novamente!")
        else:
            break         
    
    print(f"\nQuartos disponíveis: {quartos_disponíveis}")
    print("\n  Digite qual dos quartos listados abaixo você deseja: ")    
    print('''
          [1] - Standard - R$100
          [2] - Premium - R$180
          [3] - Luxo - R$ 250
          ''')
    while True:      
        tipo_quarto = int(input(": "))
        if tipo_quarto == 1 or tipo_quarto == 2 or tipo_quarto == 3:
            if tipo_quarto == 1:
                tipo_quarto = "standard"
            if tipo_quarto == 2:
                tipo_quarto = "premium"
            if tipo_quarto == 3:
                tipo_quarto = "luxo"
            break    
        else:
            print("\n  Esse tipo de quarto não existe! Escolha um dos tipos mencionados.")

    while True:
        quantidade_quartos = int(input("\nDigite a quantidade de quartos desejados: "))  
        disponibilidade1 = consultar_disponibilidade(checkin, checkout, tipo_quarto, quantidade_quartos)
        if disponibilidade1 == True:
            nova_reserva = {"responsável": nome, "checkin": checkin, "checkout": checkout, "tipo_de_quarto": tipo_quarto, "quantidade_quartos": quantidade_quartos, 'quantidade_dias': quantidade_dias_reserva}
            reservas.append(nova_reserva)
            salvar_reservas()
            break
        else:
            print(f"\n  Nesse perídodo de tempo, temos apenas {quartos_disponíveis}. ")

    
def sair():   
    print("\n Agradecemos pela preferẽncia, volte sempre!") 
    salvar_reservas()


def main():
    global reservas
    reservas = carregar_reservas()
    while True:
        opçao = int(mostrar_menu())
        if opçao == 1:
            cadastrar_reserva()
        elif opçao == 2:
            consultar_reservas()  
        elif opçao == 3:
            consultar_disponibilidade()
        elif opçao == 4:
            cancelar_reserva()     
        elif opçao == 5:
            listar_reservas(reservas)
        elif opçao == 6:
            exibir_estatisticas()            
        elif opçao == 7:
            sair()
            break
        else:
            print("Essa opçao não existe! Tente novamente.")
            time.sleep(2)
        time.sleep(3)
        #os.system("clear")


main()  
