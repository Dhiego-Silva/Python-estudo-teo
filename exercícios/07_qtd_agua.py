#Altere o programa anterior para considerar a quantidade de garrafas de água



texto = """Escolha a sua garrafa de água:
1 - Garrafa de água natural - R$ 1,50
2 - Garrafa de água com gás - R$ 2,50
Digite o número da opção desejada:   
"""
opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5


if valor_item == 0:
    print("Opção inválida, escolha 1 ou 2")
else:
    qtde = input("Quantas garrafas de água você deseja comprar? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("O valor total da compra é: R$", valor_total)
