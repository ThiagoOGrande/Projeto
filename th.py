
#Entrada 1 - Cadastro de Uma Única Reserva

import sys

nome = input("Digite o nome do responsável pela reserva:")
 
if nome == "":
    print("Nome inválido! Nome vazio!")
    sys.exit()

check_in_dia = int(input("Digite o dia de check-in:"))

if check_in_dia > 31 or check_in_dia < 1:
    print("Erro! Dia inválido!")
    sys.exit()

check_in_mês = int(input("Digite o mês de check-in:"))    

if check_in_mês > 12 or check_in_mês < 0:
    print("Erro! Mês inválido")
    sys.exit()

check_in_ano = int(input("Digite o ano de check-in:"))

check_out_dia = int(input("Digite o dia de ckeck-out:"))

if check_out_dia > 31 or check_out_dia < 1:
    print("Erro! Dia inválido")
    sys.exit()

check_out_mês = int(input("Digite o mês de check-out:"))

if check_out_mês > 12 or check_out_mês <= 0:
    print("Erro! Mês inválido")
    sys.exit()
    
check_out_ano = int(input("Digite o ano de check-out:"))

if check_in_ano == check_out_ano and check_in_mês > check_out_mês:
    print("Erro! Não há como o mês de check-in ser menor que o de check-out")
    sys.exit()
    
if check_in_ano > check_out_ano:
    print("Erro! Não há como a data de check-in ser maior que a de check-out")
    sys.exit()
 
quarto = input("Digite o tipo de quarto que deseja: Standard,Premium ou Luxo:")

if quarto != "Standard" or "standard" and quarto != "Premium" or "premium" and quarto != "Luxo" or "luxo":
    print("Esse quarto não existe.")
    sys.exit()



