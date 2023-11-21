def mostrar_mapa(personagem, tesouro):
    for i in range(10):
        for j in range(10):
            if [i, j] == personagem.posicao:
                print("@", end=" ")
            elif [i, j] == tesouro.posicao:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

def fase_personagem(personagem, monstro):
    dano_personagem = personagem.atacar()
    monstro.defender(dano_personagem)
    print(f"Você causou {dano_personagem} de dano ao monstro. Vida do monstro: {monstro.vida}")

def fase_monstro(personagem, monstro):
    dano_monstro = monstro.atacar()
    personagem.defender(dano_monstro)
    print(f"O monstro causou {dano_monstro} de dano. Sua vida: {personagem.vida_atual}/{personagem.vida_maxima}")
