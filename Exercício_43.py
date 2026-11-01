print("1 - Vendas")
print("2 - Recursos Humanos")
print("3 - Financeiro")
print("")
opcao = int(input("Qual setor? "))

match opcao:
    case 1:
        print("")
        print("Carregando dados do setor de vendas...")
    case 2:
        print("")
        print("Carregando dados do setor de recuros humanos...")
    case 3:
        print("")
        print("Carregando dados do setor de financeiro...")
    case _:
        print("")
        print("Opção inválida")