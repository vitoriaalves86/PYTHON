# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
#total do seu salário no referido mês.
print("********BEM VINDO********")
nome = input("Olá, qual o seu nome? ")
print(f"Muito bem {nome}, vamos calcular quanto você ganha no mês, com base nas horas trabalhadas.")
horas = float(input("Quantas horas por mês você trabalha? "))
valor = float(input("Quanto você ganha por hora? "))
salario_mensal = horas * valor
print(f'{nome}, seu sálario mensal é R$: {salario_mensal}')
