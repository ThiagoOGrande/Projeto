
#Entrada 1 - Cadastro de Uma Única Reserva

nome = input("Digite o nome do responsável pela reserva:")
 
if nome == "":
    print("Nome inválido! Nome vazio!")
    quit()

check_in_dia = int(input("Digite o dia de check-in:"))
if check_in_dia > 31:
    print("Erro! Dia inválido!")
    quit()

check_in_mês = int(input("Digite o mês de check-in:"))    
if check_in_mês > 12:
    print("Erro! Mês inválido")
    quit()

check_in_ano = int(input("Digite o ano de check-in:"))

check_out_dia = int(input("Digite o dia de ckeck-out:"))
if check_out_dia > 31:
    print("Erro! Dia inválido")
    quit()

check_out_mês = int(input("Digite o mês de check-out:"))
if check_out_mês > 12:
    print("Erro! Mês inválido")
    quit()
    
check_out_ano = int(input("Digite o ano de check-out:"))

