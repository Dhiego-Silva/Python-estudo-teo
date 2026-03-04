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