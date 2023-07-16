import random
import os

os.system("cls")
print("-" *30)
print("BEM-VINDO AO JOGO DO VIRCS")
print("-" *30)
perguntinha = str(input("Você deseja começar o jogo ? (sim/nao): ")) 
if perguntinha == "sim":       
    pergunta = str(input("Par ou impar(p/i): "))
    escolha = int(input("Escolha um número: "))
    computador = random.randint(0, 11)
    n = escolha + computador

    if n %2 == 0:
        if pergunta == "p":
            print(f"Você: {escolha} computador: {computador} o resultado foi {n}")
            print("Você ganhou")
        else:
            print(f"Você: {escolha} computador: {computador} o resultado foi {n}")
            print("Você perdeu")

    if n %2 == 1:
        if pergunta == "i":
            print(f"Você: {escolha} computador: {computador} o resultado foi {n}")
            print("Você ganhou")
        else:
            print(f"Você: {escolha} computador: {computador} o resultado foi {n}")
            print("Você perdeu") 
if perguntinha == "nao":
    print("CAGAOOOOOOOO...")  