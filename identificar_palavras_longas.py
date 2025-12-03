import random


def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)
    escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower()

    if escolha_usuario not in opcoes:
        print('Escolha Valida')
        return
    print(f'O computador escolheu {escolha_computador}')

    if escolha_usuario == escolha_computador:
        print('empate')
    elif (
        (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or
        (escolha_usuario == 'tesoura' and escolha_computador == 'papel') or
        (escolha_usuario == 'papel' and escolha_computador == 'pedra')
    ):
        print('Voce Ganhou!!')
    else:
        print('Voce perdeu')

pedra_papel_tesoura()