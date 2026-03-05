#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50



#%%

texto = """Escolha a sua garrafa de água:
1 - Garrafa de água natural
2 - Garrafa de água com gás
"""
opcao = input(texto)

if opcao == "1":
    print("Sua conta deu: R$ 1,50")

elif opcao == "2":
    print("Sua conta deu: R$ 2,50")

else:
    print("Opção inválida, escolha 1 ou 2")