# LOOP FOR - repete uma quantidade definida de vezes
print("=== Controle de Estoque - Loop For ===")

produtos = ["Arroz", "Feijão", "Açúcar", "Café"]

for produto in produtos:
    print(f"Produto em estoque: {produto}")

print()

# LOOP FOR com range - repete um número de vezes
print("=== Contagem de 1 a 5 ===")
for numero in range(1, 6):
    print(f"Número: {numero}")

print()

# LOOP WHILE - repete enquanto uma condição for verdadeira
print("=== Loop While - Simulação de Caixa ===")
saldo = 100
saque = 0

while saldo > 0:
    saque = int(input("Digite o valor do saque (ou 0 para sair): "))
    if saque == 0:
        print("Saindo...")
        break
    if saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= saque
        print(f"Saque realizado. Saldo atual: R$ {saldo}")

print(f"\nSaldo final: R$ {saldo}")
