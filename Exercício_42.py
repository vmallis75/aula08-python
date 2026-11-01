comissao = 0
vendas = 0

for comissao in range(1, 5):
    vendas = float(input("Qual foi o valor da sua venda? R$"))
    if vendas >= 2000:
        comissao = vendas * 0.08
        print(f"Comissão no valor de R${comissao} adicionada!")
        print("")
    else:
        print("Valor minímo não atingido!")
        print("")