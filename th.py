
import os
import sys
from datetime import datetime

quant_standard = 10
quant_premium = 5
quant_luxo = 3
quant_reservas = 0
reservas_totais = 0
maior_quant_reservas = 0
nome_reserva_cara = ""
maior_tempo_reserva = 0
nome_maior_tempo_reserva = ""

print("1 - Nova Reserva:")
print("2 - Sair")
opção = int(input("Digite a sua opção: "))


while (opção == 1):
    nome = input("Digite o nome do responsável pela reserva: ").strip()
    if nome == "":
        print("Nome inválido! Nome vazio!")
        sys.exit()
    os.system("clear")

    formato = "%d/%m/%Y"
    data = input("Digite a data de Check-In (No modelo dd/mm/aaaa): ")
    data = datetime.strptime(data, formato).date()
    data2 = input("Digite a data de Check-Out (No modelo dd/mm/aaaa): ")
    data2 = datetime.strptime(data2, formato).date()   
    if data2 < data:
        print("Erro! Não há como a data de Check-in ser maior que a de Check-out")
        sys.exit()
    diferença_dia = data - data2
    os.system("clear")

    diárias = int(input("Digite a quantidade de diárias: "))
    os.system("clear")

    print("Quantidades de quartos disponíveis;")
    print()
    print("Quartos Standard:", quant_standard)
    print("quartos Premium:", quant_premium)
    print("Quartos Luxo:", quant_luxo)
    
    quarto = int(input("""Digite o tipo de quarto que deseja:
(1) para Standard
(2) para Premium
(3) para Luxo"""""))
    os.system("clear")

    if quarto == 1:









# TIPO DE QUARTO:
'''
quarto = input("Digite o tipo de quarto desejado (Standard, Premium ou Luxo): ")

if quarto == "Standard":
    diaria = int(100)
elif quarto == "Premium":
    diaria = int(180)
elif quarto == "Luxo":
    diaria = int(250)
else:
    print("Este quarto não existe!")
    sys.exit()    
'''
