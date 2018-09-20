import random

def imprimir_tabuleiro(tabuleiro):
    print(f' {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ')
    print(f'-----------')
    print(f' {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ')
    print(f'-----------')
    print(f' {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ')

def verificar_vitoria(tabuleiro):
    for possibilidade in possibilidades_vitoria:
        campo1, campo2, campo3 = possibilidade[0], possibilidade[1], possibilidade[2]
        if ((tabuleiro[campo1] == 'X' and tabuleiro[campo2] == 'X' and tabuleiro[campo3] == 'X') or (tabuleiro[campo1] == 'O' and tabuleiro[campo2] == 'O' and tabuleiro[campo3] == 'O')):
            return True

tabuleiro = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8' }
possibilidades_vitoria = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

print('--------- Tic-Tac-Py ---------')

# nome dos jogadores
jogadores = {}
jogadores[1] = input('Digite o nome do jogador 1: ')
jogadores[2] = input('Digite o nome do jogador 2: ')

primeiro_a_jogar = (input('Quem joga primeiro(1, 2 ou A)? ')).upper()

if primeiro_a_jogar not in ('1', '2', 'A'):
    print('Escolha inválida')
    
jogador_atual = random.randint(1, 2) if primeiro_a_jogar == 'A' else int(primeiro_a_jogar)

simbolo_jogador_1 = (input(f'{jogadores[1]}, qual símbolo(X ou O) você quer utilizar? ')).upper()

if simbolo_jogador_1 not in ('X', 'O'):
    print('Símbolo inválido')

simbolos_jogadores = { }
simbolos_jogadores[1] = simbolo_jogador_1
simbolos_jogadores[2] = 'X' if simbolo_jogador_1 == 'O' else 'O'

imprimir_tabuleiro(tabuleiro)

turno_atual = 1

fim_jogo = False
while not fim_jogo:
    
    posicao = int(input(f'{jogadores[jogador_atual]}. Digite uma posição para preencher: '))

    if posicao not in tabuleiro.keys():
        print('Jogada inválida!')
        continue

    if tabuleiro[posicao] != str(posicao):
        print('Posição já preenchida! Tente novamente...')
        continue

    tabuleiro[posicao] = simbolos_jogadores[jogador_atual]
    
    imprimir_tabuleiro(tabuleiro)

    houve_vitoria = False
    # somente a partir da quinta jogada pode ocorrer vitória
    if turno_atual >= 5:
        houve_vitoria = verificar_vitoria(tabuleiro)
        if houve_vitoria:
            print(f'{jogadores[jogador_atual]} venceu!!')
    elif turno_atual == 9:
        print(f'Não houve vencedores')

    jogador_atual = 1 if jogador_atual == 2 else 2

    fim_jogo = True if turno_atual == 9 or houve_vitoria else False
    
    turno_atual += 1
