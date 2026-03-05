soma= 0 # valor final
qtde_entradas = 4  # o contador de entradas

while qtde_entradas > 0:
    altura = input("Digite a altura: ")
    altura = float(altura)  
    soma += altura
    qtde_entradas -= 1

print("Soma da altura: ", soma)