saldo_total = 0 
while True:
    saldo = input("Digite o valor do saldo: ")
    
    if saldo == "":
        break
    
    saldo_total += float(saldo)

print("Saldo total: ", saldo_total)
