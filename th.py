import sys

nome = input("Digite o nome do responsável pela reserva: ").strip()
 
if nome == "":
    print("Nome inválido! Nome vazio!")
    sys.exit()

check_in_dia = int(input("Digite o dia de check-in: "))

if check_in_dia > 31 or check_in_dia < 1:
    print("Erro! Dia inválido!")
    sys.exit()

check_in_mês = int(input("Digite o mês de check-in: "))    

if check_in_mês > 12 or check_in_mês < 0:
    print("Erro! Mês inválido")
    sys.exit()

check_in_ano = int(input("Digite o ano de check-in: "))

check_out_dia = int(input("Digite o dia de ckeck-out: "))

if check_out_dia > 31 or check_out_dia < 1:
    print("Erro! Dia inválido")
    sys.exit()

check_out_mês = int(input("Digite o mês de check-out: "))

if check_out_mês > 12 or check_out_mês < 1:
    print("Erro! Mês inválido")
    sys.exit
    
check_out_ano = int(input("Digite o ano de check-out: "))

if check_in_ano == check_out_ano and check_in_mês > check_out_mês:
    print("Erro! Não há como o mês de check-in ser menor que o de check-out")
    sys.exit()

if check_in_ano == check_out_ano and check_in_mês == check_out_mês and check_in_dia > check_out_dia:
    print("Erro! Não há como o dia de check-in ser menor que o de check-out")
    sys.exit()

if check_in_ano > check_out_ano:
    print("Erro! Não há como a data de check-in ser maior que a de check-out")
    sys.exit()

data_out = (check_out_ano * 365) + check_out_dia + (check_out_mês * 30)
data_in = (check_in_ano * 365) + (check_in_mês * 30) + check_in_dia
dif = data_out - data_in

quarto = input("Digite o tipo de quarto desejado (Standard, Premium ou Luxo): ")

if quarto == "Standard":
    diaria = int(100)
elif quarto == "Premium":
    diaria = int(180)
elif quarto == "Luxo":
    diaria = int(250)

valor = diaria * dif

print(f"Olá {nome}! Tudo bem? Seu dia de Check-In é {check_in_dia}/{check_in_mês}/{check_in_ano} e seu dia de Check Out é {check_out_dia}/{check_out_mês}/{check_out_ano} e seu quarto será o {quarto}. Ao todo você ficará {dif} dias em nosso hotel. Você pagará ao todo R${valor}!")
