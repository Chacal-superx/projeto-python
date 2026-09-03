estoque = {
    "Arroz": 10,
    "Feijão": 5,
    "Açúcar": 8
}

# mostra o estoque com for
for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade} unidades")

# loop while pra retirar produtos
while True:
    escolha = input("\nQual produto retirar? (ou 'sair'): ").capitalize()
    
    if escolha == "Sair":
        print("Encerrando...")
        break
    
    if escolha in estoque:
        if estoque[escolha] > 0:
            estoque[escolha] = estoque[escolha] - 1
            print(f"Retirado 1 {escolha}. Restam: {estoque[escolha]}")
        else:
            print(f"{escolha} está em falta!")
    else:
        print("Produto não encontrado.")
