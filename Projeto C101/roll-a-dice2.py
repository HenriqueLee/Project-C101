import random

def print_dice(number):
    dice_art = [
        " ------- ",
        "|       |",
        "|   *   |",
        "|       |",
        " ------- "
    ]
    
    if number == 1:
        dice_art[2] = "|       |"
    elif number == 2:
        dice_art[1] = "|     * |"
        dice_art[3] = "| *     |"
    elif number == 3:
        dice_art[1] = "|     * |"
        dice_art[2] = "|   *   |"
        dice_art[3] = "| *     |"
    elif number == 4:
        dice_art[1] = "| *   * |"
        dice_art[3] = "| *   * |"
    elif number == 5:
        dice_art[1] = "| *   * |"
        dice_art[2] = "|   *   |"
        dice_art[3] = "| *   * |"
    elif number == 6:
        dice_art[1] = "| * * * |"
        dice_art[3] = "| * * * |"

    for line in dice_art:
        print(line)

# Função para obter a resposta do usuário (y ou n)
def get_user_response():
    while True:
        response = input("Deseja continuar jogando? (y/n): ").lower()
        if response in ["y", "n"]:
            return response
        else:
            print("Resposta inválida. Digite 'y' para continuar ou 'n' para sair.")

# Loop para lançar o dado e exibir visualmente o resultado
while True:
    no = random.randint(1, 6)
    print(f"Lançamento do dado: {no}")
    print_dice(no)
    
    response = get_user_response()
    
    if response == "n":
        print("Saindo do jogo...")
        break

    print()  # Linha em branco para separar os lançamentos