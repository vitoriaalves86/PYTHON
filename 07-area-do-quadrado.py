#Faça um Programa que calcule a área de um quadrado, em seguida
# mostre o dobro desta área para o usuário.

print("VAMOS CALCUAR A ÁREA DE UM QUADRADO")
lados = float(input("Digite o valor do lado do quadrado.(LEMBRE- SE QUE UM QUADRADO POSSUI LADOS IGUAIS):"))
area = lados ** 2
print(f"A área do quadrado é: {area} ")
multi = float(input("Para multiplicar esse valor, digite um fator: "))
conta = area * multi
print(f"O valor da área: {area} * o fator que foi digitado: {multi}. Gera o produto: {conta}")