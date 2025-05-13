
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

if check_out_mês > 12 or check_out_mês:
    print("Erro! Mês inválido")
    sys.exit
    
check_out_ano = int(input("Digite o ano de check-out:"))

if check_in_ano == check_out_ano:
    check_in_mês < check_out_mês
    print("Erro! Não há como o mês de check-out ser menor que o de check-in")
    

if check_in_ano > check_out_ano:
    print("Erro! Não há como a data de check-in ser maior que a de check-out")
    sys.exit()


 
quarto = input("Digite o tipo de quarto que deseja (Standard, Premium, Luxo):")

if quarto != "Standard" and quarto != "Premium" and quarto != "Luxo":
    print("Erro! O tipo de quarto deve ser Standard, Premium ou Luxo")    

out_mês_dias = check_out_mês * 30
total_meses = check_out_mês - check_in_mês    
