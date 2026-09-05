estoque = {
    "Arroz": 10,
    "Feijão": 5,
    "Açúcar": 8
}

def mostrar_estoque(estoque):
    print("\n=== Estoque Atual ===")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")


def retirar_produto(estoque, produto):
    if produto not in estoque:
        print("Produto não encontrado.")
        return False
    
    if estoque[produto] <= 0:
        print(f"{produto} está em falta!")
        return False
    
    estoque[produto] -= 1
    print(f"Retirado 1 {produto}. Restam: {estoque[produto]}")
    return True


mostrar_estoque(estoque)

while True:
    escolha = input("\nQual produto retirar? (ou 'sair'): ").capitalize()
    
    if escolha == "Sair":
        print("Encerrando...")
        break
    
    retirar_produto(estoque, escolha)
