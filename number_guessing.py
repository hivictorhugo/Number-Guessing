import random

print("Advinhe o número correto!")
top_range = input("Escolha a quantidade de numeros: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Por favor digite um número maior que zero da próxima vez!")
        quit()

else:
    print("Por favor digite um número da próxima vez!")
    quit()


random_number = random.randint(0, top_range)
guesses = 0

while True:

    guesses +=1

    user_guess = input("Faça uma tentativa: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Por favor digite um número da próxima vez!")
        continue

    if user_guess == random_number:
        print(f"Você acertou! O número era {random_number}!")
        break

    else:
        print("Você errou!")

print(f"Você fez {guesses} tentativas! ")




    




