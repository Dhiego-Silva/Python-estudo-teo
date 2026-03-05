#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago


valor_sorvete = 0.0
nome_sorvete = "item"
artigo = "do seu"

texto = """Escolha o tipo de sorvete:
1 - Casquinha - R$ 1,00
2 - Cascão - R$ 2,50
3 - Cestinha - R$ 4,00
"""
opcao = input(texto)
if opcao == "1":
    valor_sorvete = 1.0
    nome_sorvete = "Casquinha"
    artigo = "da sua"
elif opcao == "2":
    valor_sorvete = 2.5
    nome_sorvete = "Cascão"
    artigo = "do seu"
elif opcao == "3":
    valor_sorvete = 4.0
    nome_sorvete = "Cestinha"
    artigo = "da sua"
texto2 = """Escolha o sabor do sorvete:
1 - Morango
2 - Creme
3 - Chocolate
"""
sabor = input(texto2)

if sabor == "1":
    sabor = "Morango"
    nome_sorvete += " de Morango"
elif sabor == "2":
    sabor = "Creme"
    nome_sorvete += " de Creme"
elif sabor == "3":
    sabor = "Chocolate" 
    nome_sorvete += " de Chocolate"

texto3 = """Escolha a cobertura do sorvete:
1 - Caramelo - R$ 1,50
2 - Morango - R$ 1,50
3 - Chocolate - R$ 1,50
4 - Sem cobertura - R$ 0,00
"""
cobertura = input(texto3)
valor_cobertura = 0
nome_cobertura = ""

if cobertura == "1":
    valor_cobertura = 1.5
    nome_cobertura = "Caramelo" 
elif cobertura == "2":
    valor_cobertura = 1.5
    nome_cobertura = "Morango"
elif cobertura == "3":
    valor_cobertura = 1.5
    nome_cobertura = "Chocolate"
elif cobertura == "4":
    valor_cobertura = 0.0
    nome_cobertura = "Sem cobertura"


if cobertura == "4":
    print(f"O valor total {artigo} {nome_sorvete} a ser pago é: R$ {valor_sorvete + valor_cobertura:.2f}")
else:
    print(f"O valor total {artigo} {nome_sorvete} com cobertura de {nome_cobertura} a ser pago é: R$ {valor_sorvete + valor_cobertura:.2f}")