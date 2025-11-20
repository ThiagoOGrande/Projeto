import pickle
import sys
from datetime import datetime
import os
import time

Todas_reservas = []
quartos_disponiveis = {"standard": 10, "premium": 5, "luxo": 3}
espaçamento = '=' * 40
nome_arquivo = "reservas.pkl"
def carregar_reserva():
    try:
        with open (nome_arquivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def salvar_reservas():
    global Todas_reservas
    with open(nome_arquivo, "wb") as f:
        pickle.dump(Todas_reservas, f)

def exibir_estatisticas_gerais():
    print(espaçamento)
    print(f'QUANTIDADE TOTAL DE RESERVAS: {len(Todas_reservas)}')
    print(espaçamento)
    valor_totalreservas = 0
    reserva_maiscara = 0
    responsavel_maiscara = ''
    maior_quantidade_dias = 0
    responsavel_maisdias = ''
    quantidade_standard = 0
    quantidade_premium = 0
    quantidade_luxo = 0

    for r in Todas_reservas:
        if r['tipo_de_quarto'] == 'standard':
            valor_do_quarto = 100
        elif  r['tipo_de_quarto'] == 'premium':
            valor_do_quarto = 180
        else:
            valor_do_quarto = 250
        valor_re = r['quantidade_quarto'] * r['quantidade_dias'] * valor_do_quarto
        if r ['tipo_de_quarto'] == 'standard':
            quantidade_standard += r['quantidade_quarto']
        elif r ['tipo_de_quarto'] == 'premium':
            quantidade_premium += r['quantidade_quarto']
        else:
            quantidade_luxo += r['quantidade_quarto']
        valor_totalreservas += valor_re
        if valor_re > reserva_maiscara:
            reserva_maiscara = valor_re
            responsavel_maiscara = r['responsável']
        if r['quantidade_dias'] > maior_quantidade_dias:
            maior_quantidade_dias = r['quantidade_dias']
            responsavel_maisdias = r['responsável']
        
    print('VALOR TOTAL DE RESERVAS:', valor_totalreservas)
    print('RESERVA MAIS CARA: ', reserva_maiscara)
    print(espaçamento)
    print('RESPONSAVEL POR RESERVA MAIS CARA:',responsavel_maiscara)
    print(espaçamento)

    print('RESERVA MAIS LONGA:', maior_quantidade_dias)
    print('RESPONSÁVEL POR MAIOR QUANTIDADE DE DIAS:', responsavel_maisdias)
    print(espaçamento)
    print('QUANTIDADE QUARTOS STANDARD:', quantidade_standard )
    print('QUANTIDADE QUARTOS PREMIUM:', quantidade_premium )
    print('QUANTIDADE QUARTOS LUXO:', quantidade_luxo )
    print(espaçamento)
    terminar = input('Quer sair \n[1] Sim ')
    if terminar == 1:
        return


        

def cancelar_reservas():
    nome_procurado = input('Digite o nome do responsável pela reserva:  ').lower()
    soma = 0
    for r in (Todas_reservas):
        if r ['responsável'] == [nome_procurado]:
            soma += 1
            print(espaçamento)
            print(f"Nome: {r['responsável']} \ncheck-in: {r['checkin']} \ncheck-out'{r['checkout']} \ntipo de quarto: {r['tipo_de_quarto']} \nquantidade de quartos: {r['quantidade_quarto']} \ndias de estadia: {r['quantidade_dias']} ")
            print(espaçamento)
            print('VOCÊ QUER MESMO ELIMINAR ESSE QUARTO \n[1] SIM \n[2] NÃO')
            cancelamento = input(': ')
            if cancelamento == 2:
                return
            else:
                data_hoje = datetime.today()
                if r['checkin'] > data_hoje:
                    Todas_reservas.remove(r)
                    print('QUARTO EXCLUIDO COM SUCESSO')
                else:
                    print(espaçamento)
                    print('Não é possível eliminar')
                    print('A data de check-in já passou')
                    print(espaçamento)
    if soma == 0:
        print('Não há reservas com esse nome')


    terminar = input('Quer sair \n[1] Sim ')
    if terminar == 1:
        return


   
def consultar_reservas():
    nome_procurado = input('Digite o nome do responsável pela reserva:  ').lower()
    teve_resultado = 0
    print(espaçamento)
    print('QUARTOS RESERVADOS')
    for r in (Todas_reservas):
        if r ['responsável'] == [nome_procurado]:
            print('INFORMAÇÕES DE SUA RESERVA')
            print(f"Nome: {r['responsável']} \ncheck-in: {r['checkin']} \ncheck-out'{r['checkout']} \ntipo de querto: {r['tipo_de_quarto']} \nquantidade de quartos: {r['quantidade_quarto']} \ndias de estadia: {r['quantidade_dias']} ")
            teve_resultado += 1
    if teve_resultado == 0:
        print('Não houve reserva com esse nome.')
    print(espaçamento)
    terminar = input('Quer sair \n[1] Sim ')
    if terminar == 1:
        return


def listar_todas_reservas(a):
    Todas_reservas = carregar_reserva()
    print('Todas as reservas feitas')
#nova_reserva = {'responsável': nome, 'checkin': data_checkin, 'checkout': data_checkout, 'tipo_de_quarto': tipo_quarto, 'quantidade_quarto': quantidade_quarto, 'quantidade_dias': dias_reservados}

    for r in Todas_reservas:
        print(espaçamento)
        print(f"Nome: {r['responsável']} \ncheck-in: {r['checkin']} \ncheck-out'{r['checkout']} \ntipo de quarto: {r['tipo_de_quarto']} \nquantidade de quartos: {r['quantidade_quarto']} \ndias de estadia: {r['quantidade_dias']} ")
        print(espaçamento)
    terminar = input('Quer sair \n[1] Sim ')
    if terminar == 1:
        return

def consultar_disponibilidade(data_checkin, data_checkout, tipo_quarto, quantidade_quarto):
    quartos_consumidos = 0
    for r in Todas_reservas:
        if r['tipo_de_quarto'] == tipo_quarto:
            if data_checkin < r["checkout"] and data_checkout > r["checkin"]:
                quartos_consumidos += r["quantidade_quarto"]
    global quantos_disponiveis
    quantos_disponiveis = quartos_disponiveis[tipo_quarto] - quartos_consumidos
    if quantidade_quarto > quantos_disponiveis:
        return False
    else:
        return True

def cadastrar_nova_reserva():
    nome = input("Digite o nome do responsável da reserva:").lower().split()
    dias_reservados = 0
    while True:
        while True:
            check_in = input('Qual o dia da reserva: (aa/mm/aaaa) ')
            try:
                data_checkin = datetime.strptime(check_in, "%d/%m/%Y")
                break
            except ValueError:
                print('Data inválida em check_in!')
                print('Tente novamente')
    
        data_checkin = data_checkin
        
        while True:    
            check_out = input('Qual o dia de saída: (aa/mm/aaaa) ')
            try:
                data_checkout = datetime.strptime(check_out, "%d/%m/%Y")
                break
            except ValueError:
                print('Data de check-out inválida!')
                print('Tente novamente')
        data_checkout = data_checkout
        
        dias_reservados  = (data_checkout - data_checkin).days
        
        if dias_reservados < 0:
            print(espaçamento)
            print('A data de check-in é maior que a de check-out')
            print('Digite novamente')
            print(espaçamento)
        else:
            break


    print(espaçamento)
    print('Quartos Disponíveis')
    print(quartos_disponiveis)
    print(espaçamento)
    print('Digite [1] para standard: R$ 100.00\nDigite [2] para premium: R$ 180.00 \nDigite [3] para luxo: R$ 250.00')
    
    while True:
        tipo_quarto = int(input("Digite o tipo de quarto:"))
        if tipo_quarto == 1 or tipo_quarto == 2 or tipo_quarto == 3:
            if tipo_quarto == 1:
                tipo_quarto = 'standard'
            if tipo_quarto == 2:
                tipo_quarto = 'premium'
            if tipo_quarto == 3:
                tipo_quarto = 'luxo'
            break
        else:
            print('Digite um tipo de quarto existente')


    while True:
        quantidade_quarto = int(input('Digite a quantidade de quarto desejado: '))
        possibilidade = consultar_disponibilidade(data_checkin, data_checkout, tipo_quarto, quantidade_quarto)
        if possibilidade == True:       
            nova_reserva = {'responsável': nome, 'checkin': data_checkin, 'checkout': data_checkout, 'tipo_de_quarto': tipo_quarto, 'quantidade_quarto': quantidade_quarto, 'quantidade_dias': dias_reservados}
            Todas_reservas.append(nova_reserva)
            salvar_reservas()
            break
        else:
            print(espaçamento)
            print("Não tem disponibilidade!")
            print(f'Você tentou pegar {quantidade_quarto} quartos, porém nesse periodo só temos {quantos_disponiveis} quartos disponiveis')
            print('Digite " 0 " para sair.')
            print(espaçamento)
def mostrar_menu():
    print("[1] Cadastrar nova reserva \n[2] Listar todas as reservas  \n[3] Consultar reserva \n[4] Cancelar reserva \n[5] Exibir estatísticas gerais \n[6] Sair do programa")
    escolha = int(input(': '))
    return escolha



def main():
    global Todas_reservas
    Todas_reservas = carregar_reserva()
    while True:
        escolha = int(mostrar_menu())
        if escolha == 1:
            cadastrar_nova_reserva()
        if escolha == 2:
            listar_todas_reservas(Todas_reservas)       
        if escolha == 3:
            consultar_reservas()
        if escolha == 4:
            cancelar_reservas()
        if escolha == 5:
            exibir_estatisticas_gerais()
        if escolha == 6:
            print('Obrigado por visitar o nosso site')
            salvar_reservas()
            break
        
        time.sleep(1)
        os.system("clear")

main()
