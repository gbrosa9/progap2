import random
from mecanicas.personagem import Personagem
from mecanicas.monstro import Monstro
from mecanicas.item import Item
from mecanicas.tesouro import Tesouro
from mecanicas.utilidades import mostrar_mapa, fase_personagem, fase_monstro

def main():
    nome_personagem = input("Digite o nome do personagem: ")
    personagem = Personagem(nome_personagem)
    tesouro = Tesouro()
    turno = 1

    print("Bem-vindo ao Jogo Caça ao Tesouro!")
    print("Use as teclas W, A, S, D para se mover.")
    print("Pressione I para ver a mochila, T para ver os atributos e Q para sair do jogo.")

    while True:
        print(f"\nTurno {turno}")
        mostrar_mapa(personagem, tesouro)

        acao = input("Escolha sua ação (W, A, S, D, I, T, Q): ").upper()

        if acao in ["W", "A", "S", "D"]:
            personagem.mover(acao)
            efeito = random.choice(["Nada", "Item", "Monstro"])
            if efeito == "Item":
                item = Item("Pocao", random.choice(["Vida", "Forca", "Defesa"]), random.randint(1, 2))
                personagem.coletar_item(item)
                print(f"Você encontrou uma {item.tipo} de intensidade {item.intensidade}!")
            elif efeito == "Monstro":
                monstro = Monstro()
                print(f"Você encontrou um monstro! Prepare-se para a batalha.")
                while personagem.esta_vivo() and monstro.esta_vivo():
                    fase_personagem(personagem, monstro)
                    fase_monstro(personagem, monstro)
                if not monstro.esta_vivo():
                    print("Você derrotou o monstro!")
                    item = Item("Pocao", random.choice(["Vida", "Forca", "Defesa"]), random.randint(1, 2))
                    personagem.coletar_item(item)
                    print(f"Você encontrou uma {item.tipo} de intensidade {item.intensidade}!")
            turno += 1
        elif acao == "I":
            personagem.ver_mochila()
        elif acao == "T":
            print(f"\nAtributos do Personagem {personagem.nome}:")
            print(f"Força: {personagem.forca}")
            print(f"Defesa: {personagem.defesa}")
            print(f"Vida Atual: {personagem.vida_atual}/{personagem.vida_maxima}")
        elif acao == "Q":
            print("Você desistiu da busca pelo tesouro. O jogo acabou.")
            break
        else:
            print("Comando inválido. Tente novamente.")

        if personagem.posicao == tesouro.posicao:
            print("Parabéns! Você encontrou o tesouro e venceu o jogo!")
            break

        if not personagem.esta_vivo():
            print("Você foi derrotado. O jogo acabou.")
            break

if __name__ == "__main__":
    main()
