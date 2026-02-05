import random

print("🎲 Bem-vindo ao jogo da adivinhação 🎲")
print("Estou pensando em um número entre 1 e 20... 💭")

numero_secreto = random.randint(1, 20)
tentativas = 0

while True:
    chute = int(input("Digite seu palpite 🤔: "))
    tentativas += 1

    if chute < numero_secreto:
        print("O número é maior ⬆️")
    elif chute > numero_secreto:
        print("O número é menor ⬇️")
    else:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
        break
