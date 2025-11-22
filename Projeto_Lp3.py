import pickle 
import os
import sys
import time
from datetime import datetime 


reservas = []
nome_arquivo = "reservas.pkl"
DISPONIBILIDADE_QUARTOS = {"standard": 10, "premium": 5, "luxo": 3}
VALORES_QUARTOS = {"standard": 100, "premium": 180, "luxo": 250}



#Funções carregar e salvar reservas:

def carregar_reservas():
    global reservas
    if os.path.exists(nome_arquivo):
        try:
            with open (nome_arquivo, "rb") as f:
                reservas = pickle.load(f)
                if not isinstance(reservas, list):
                    reservas = []
        except FileNotFoundError:
            reservas = []            
    else:
        reservas = []
    

def salvar_reservas():
    global reservas
    with open (nome_arquivo, "wb") as f:
        pickle.dump(reservas, f)        



#Funções auxiliares (ajudar na construção das principais):

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")



def ler_data(msg):
    while True:
        try:
            return datetime.strptime(input(msg).strip(), "%d/%m/%Y").date()
        except:
            print("Data inválida! Utilize o formato dd/mm/aaaa.")       


def sobreposiçao_datas(checkin1, chekcout1, checkin2, checkout2):
    return checkin1 < checkout2 and checkin2 < chekcout1



def disponibilidade(checkin, checkout, tipo_quarto, quantidade_quartos):
    quartos_ocupados = 0
    for r in (reservas):
        if r["tipo_quarto"] == tipo_quarto:
            if sobreposiçao_datas(checkin, checkout, r["checkin"], r["checkout"]):
                quartos_ocupados += r["quantidade_quartos"]  
    
    disponiveis = DISPONIBILIDADE_QUARTOS[tipo_quarto] - quartos_ocupados
    return disponiveis >= quantidade_quartos, disponiveis 



def exibir_reserva(r):
    dias_reservados = (r["checkout"] - r["checkin"]).days
    print(f"""
    Responsável: {r['responsavel']}
    Check-in: {r['checkin'].strftime("%d/%m/%Y")}
    Check-out: {r['checkout'].strftime("%d/%m/%Y")}
    Dias reservados: {dias_reservados}
    Tipo de quarto: {r['tipo_quarto']}
    Quantidade de quartos: {r['quantidade_quartos']}
    Valor total: R$ {r['valor_total']}
    ------------------------------------------------
    """)

 

#Funções principais:

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



def cadastrar_reserva(): 
    responsavel = input("\nDigite o nome do responsável pela reserva: ").lower().strip()
    if responsavel == "":
        print("\n  Nome inválido!")
        time.sleep(3)
        return

    checkin = ler_data("\nDigite a data de Check-in (No modelo [dd/mm/aaaa]): ")
    checkout = ler_data("Digite a data de Check-out (No modelo [dd/mm/aaaa]): ")    
    if checkout < checkin:
        print("\n  A data de Check-in não pode ser menor que a de Check-out!")
        return

    print("\n Digite qual dos quartos listados abaixo você deseja: ")    
    print('''
          Standard
          Premium
          Luxo
          ''')
    tipo_quarto = input("\n: ").strip().lower()
    if tipo_quarto not in DISPONIBILIDADE_QUARTOS:
        print("\n  Esse tipo de quarto não existe! Escolha um dos tipos listados.")
        return    
    
    try:
        quantidade_quartos = int(input("\nQuantidade de quartos: "))
    except:
        print("\n  Quantidade inválida!")
        return    

    disponivel, livres = disponibilidade(checkin, checkout, tipo_quarto, quantidade_quartos)

    if not disponivel:
        print(f"\n  Não há disponibilidade suficiente!\n  Quartos livres: {livres}")
        return

    dias_reservados = (checkout - checkin).days
    valor_total = dias_reservados * quantidade_quartos * VALORES_QUARTOS[tipo_quarto]

    nova_reserva = {
        "responsavel": responsavel,
        "checkin": checkin,
        "checkout": checkout,
        "tipo_quarto": tipo_quarto,
        "quantidade_quartos": quantidade_quartos,
        "valor_total": valor_total
    }

    reservas.append(nova_reserva)
    salvar_reservas()
    print("\nA Reserva foi cadastrada com sucesso!")    



def consultar_reservas():
    buscar_nome = input("\nDigite o nome do responsável pela reserva que desejas consultar: ").lower()
    nome_encontrado = [r for r in reservas if buscar_nome in r["responsavel"]]

    if not nome_encontrado:
        print("\nNão existem reservas com este nome, tente outro! ")
        return

    for r in nome_encontrado:
        exibir_reserva(r)     



def consultar_disponibilidade():  
    print("\nIremos consultar a disponibilidade...")
    time.sleep(3)
    
    checkin = ler_data("\nDigite a data de check-in: ")
    checkout = ler_data("Digite a data de check-out: ")

    tipo_quarto = input("\nDigite o tipo de quarto: ").lower()
    if tipo not in DISPONIBILIDADE_QUARTOS:
        print("Tipo de quarto inválido. Escolha um dos tipos existentes.")
        return

    try:
        quantidade_quartos = int(input("Digite a quantidade de quartos: "))
    except:
        print("Inválido.")
        return

    ok, livres = disponibilidade(checkin, checkout, tipo_quarto, quantidade_quartos)

    if ok:
        print("Há quartos suficientes.")
    else:
        print(f"Não há quartos suficientes. A maior quantidade possível de quartos disponíveis é: {livres}")
      
 

def cancelar_reservas():
    buscar_nome = input("\n Digite o nome do responsável pela reserva que desejas cancelar: ").lower()
    nome_encontrado = [r for r in reservas if buscar_nome in r["responsavel"] and r["checkin"] > date.today()]

    if not nome_encontrado:
        print("Não existem reservas com este nome, tente outro!.")
        return

    print("\nReservas:")
    for i, r in enumerate(nome_encontrado, 1):
        print(f"\nReserva {i}:")
        exibir_reserva(r)

    try:
        cancelar_reserva = int(input("Digite a reserva a ser cancelada: "))
        cancelar = nome_encontrado[cancelar_reserva - 1]
    except:
        print("Opção inválida.")
        return

    reservas.remove(cancelar)
    salvar_reservas()
    print("\nA Reserva foi cancelada com sucesso!")



def listar_reservas():
    if not reservas:
        print("\n Nenhuma reserva foi cadastrada. ")
        return

    ordenadas = sorted(reservas, key=lambda r: (r["checkin"], r["responsavel"]))

    for r in ordenadas:
        exibir_reserva(r)

    sair = int(input("\n  Digite [1] para sair: "))
    if sair == 1:
        return      



def exibir_estatisticas():
    carregar_reservas()
    print("\nCarregando para exibir as estatísticas gerais, aguarde alguns instantes...")
    time.sleep(3)

    if not reservas:
        print("\n Nenhuma reserva foi cadastrada. ")
        return
    
    reservas_totais = len(reservas)
    soma = sum(r["valor_total"] for r in reservas)
    reserva_mais_cara = max(reservas, key=lambda r: r["valor_total"])
    reserva_mais_longa = max(reservas, key=lambda r: (r["checkout"] - r["checkin"]).days)

    quantidade_quartos = {"standard": 0, "premium": 0, "luxo": 0}
    for r in reservas:
        quantidade_quartos[r["tipo_quarto"]] += r["quantidade_quartos"]

    print(f"""
    Total de reservas: {reservas_totais}
    
    Soma total: R$ {soma}

    Reserva mais cara:
        - Responsável: {reserva_mais_cara['responsavel']}
        - Valor: R$ {reserva_mais_cara['valor_total']}

    Reserva mais longa:
        - Responsável: {reserva_mais_longa['responsavel']}
        - Noites: {(reserva_mais_longa['checkout'] - reserva_mais_longa['checkin']).days}

    Quartos reservados por tipo:
        Standard: {quantidade_quartos["standard"]}
        Premium:  {quantidade_quartos["premium"]}
        Luxo:     {quantidade_quartos["luxo"]}
    """)



def sair():   
    salvar_reservas()
    print("\n Agradecemos pela preferência, volte sempre!") 



def main():
    global reservas
    carregar_reservas()
    while True:
        opçao = int(mostrar_menu())
        if opçao == 1:
            cadastrar_reserva()
        elif opçao == 2:
            consultar_reservas()  
        elif opçao == 3:
            consultar_disponibilidade()
        elif opçao == 4:
            cancelar_reservas()     
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
        time.sleep(3)
        limpar_tela()


main()  
