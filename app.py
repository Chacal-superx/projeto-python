# app.py - versão interativa

nome = input("Qual é o seu nome? ")
ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print(f"Olá, {nome}! Você tem aproximadamente {idade} anos.")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
