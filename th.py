
import sys
from datetime import datetime

# NOME:

nome = input("Digite o nome do responsável pela reserva: ").strip()
 
if nome == "":
    print("Nome inválido! Nome vazio!")
    sys.exit()

# DATA:

formato = "%d/%m/%Y"

data = input("Digite a data de Check-In (No modelo dd/mm/aaaa): ")
data = datetime.strptime(data, formato).date()

data2 = input("Digite a data de Check-Out (No modelo dd/mm/aaaa): ")
data2 = datetime.strptime(data2, formato).date()

if data2 < data:
    print("Erro! Não há como a data de Check-in ser maior que a de Check-out")
    sys.exit()

diferença = data - data2

# TIPO DE QUARTO:

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

print(f"Olá, {nome}, sua data de Check-in está marcada para o dia {data}, e sua data de Check-out para o dia {data2}. Ao total, você ficará {diferença.days} dias conosco, e estará hospedado no quarto {quarto}")
