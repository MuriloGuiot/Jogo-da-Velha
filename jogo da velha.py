def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all([s == jogador for s in linha]):
            return True

    # Verifica colunas
    for col in range(3):
        if all([tabuleiro[linha][col] == jogador for linha in range(3)]):
            return True

    # Verifica diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    turno = 0

    while True:
        jogador_atual = jogadores[turno % 2]
        imprimir_tabuleiro(tabuleiro)

        # Solicita a jogada do jogador
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        turno += 1

if __name__ == "__main__":
    jogar()
