soma= 0 # valor final
qtde_entradas = 4  # o contador de entradas

for i in range(qtde_entradas):
    altura = input("Digite a altura: ")
    altura = float(altura)  
    soma += altura

print("Soma da altura: ", soma)