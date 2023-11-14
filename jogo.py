import random

class Item:
    def __init__(self, nome, tipo, intensidade):
        self.nome = nome
        self.tipo = tipo
        self.intensidade = intensidade

class Aventureiro:
    def __init__(self, nome):
        self.nome = nome
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida_maxima = random.randint(100, 120)
        self.vida_atual = self.vida_maxima
        self.mochila = []
        self.posicao = [0, 0]

    def atacar(self):
        return self.forca + random.randint(1, 6)

    def defender(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida_atual -= dano_final

    def mover(self, direcao):
        if direcao == "A" and self.posicao[1] > 0:
            self.posicao[1] -= 1
        elif direcao == "W" and self.posicao[0] > 0:
            self.posicao[0] -= 1
        elif direcao == "D" and self.posicao[1] < 9:
            self.posicao[1] += 1
        elif direcao == "S" and self.posicao[0] < 9:
            self.posicao[0] += 1

    def coletar_item(self, item):
        self.mochila.append(item)

    def usar_item(self, item):
        if item.tipo == "Vida":
            self.vida_atual += 20 * item.intensidade
            if self.vida_atual > self.vida_maxima:
                self.vida_atual = self.vida_maxima
        elif item.tipo == "Forca":
            self.forca += item.intensidade
        elif item.tipo == "Defesa":
            self.defesa += item.intensidade
        self.mochila.remove(item)

    def ver_mochila(self):
        for item in self.mochila:
            print(f"{item.nome} ({item.tipo}) - Intensidade: {item.intensidade}")

    def esta_vivo(self):
        return self.vida_atual > 0

class Monstro:
    def __init__(self):
        self.forca = random.randint(5, 25)
        self.defesa = random.randint(5, 10)
        self.vida = random.randint(10, 100)

    def atacar(self):
        return self.forca

    def defender(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final

    def esta_vivo(self):
        return self.vida > 0

class Tesouro:
    def __init__(self):
        self.posicao = [random.randint(1, 9), random.randint(1, 9)]

def mostrar_mapa(aventureiro, tesouro):
    for i in range(10):
        for j in range(10):
            if [i, j] == aventureiro.posicao:
                print("@", end=" ")
            elif [i, j] == tesouro.posicao:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

def fase_aventureiro(aventureiro, monstro):
    dano_aventureiro = aventureiro.atacar()
    monstro.defender(dano_aventureiro)
    print(f"Você causou {dano_aventureiro} de dano ao monstro. Vida do monstro: {monstro.vida}")

def fase_monstro(aventureiro, monstro):
    dano_monstro = monstro.atacar()
    aventureiro.defender(dano_monstro)
    print(f"O monstro causou {dano_monstro} de dano. Sua vida: {aventureiro.vida_atual}/{aventureiro.vida_maxima}")

def main():
    nome_aventureiro = input("Digite o nome do aventureiro: ")
    aventureiro = Aventureiro(nome_aventureiro)
    tesouro = Tesouro()
    turno = 1

    print("Bem-vindo ao Jogo Caça ao Tesouro!")
    print("Use as teclas W, A, S, D para se mover.")
    print("Pressione I para ver a mochila, T para ver os atributos e Q para sair do jogo.")

    while True:
        print(f"\nTurno {turno}")
        mostrar_mapa(aventureiro, tesouro)

        acao = input("Escolha sua ação (W, A, S, D, I, T, Q): ").upper()

        if acao in ["W", "A", "S", "D"]:
            aventureiro.mover(acao)
            efeito = random.choice(["Nada", "Item", "Monstro"])
            if efeito == "Item":
                item = Item("Pocao", random.choice(["Vida", "Forca", "Defesa"]), random.randint(1, 2))
                aventureiro.coletar_item(item)
                print(f"Você encontrou uma {item.tipo} de intensidade {item.intensidade}!")
            elif efeito == "Monstro":
                monstro = Monstro()
                print(f"Você encontrou um monstro! Prepare-se para a batalha.")
                while aventureiro.esta_vivo() and monstro.esta_vivo():
                    fase_aventureiro(aventureiro, monstro)
                    fase_monstro(aventureiro, monstro)
                if not monstro.esta_vivo():
                    print("Você derrotou o monstro!")
                    item = Item("Pocao", random.choice(["Vida", "Forca", "Defesa"]), random.randint(1, 2))
                    aventureiro.coletar_item(item)
                    print(f"Você encontrou uma {item.tipo} de intensidade {item.intensidade}!")
            turno += 1
        elif acao == "I":
            aventureiro.ver_mochila()
        elif acao == "T":
            print(f"\nAtributos do Aventureiro {aventureiro.nome}:")
            print(f"Força: {aventureiro.forca}")
            print(f"Defesa: {aventureiro.defesa}")
            print(f"Vida Atual: {aventureiro.vida_atual}/{aventureiro.vida_maxima}")
        elif acao == "Q":
            print("Você desistiu da busca pelo tesouro. O jogo acabou.")
            break
        else:
            print("Comando inválido. Tente novamente.")

        if aventureiro.posicao == tesouro.posicao:
            print("Parabéns! Você encontrou o tesouro e venceu o jogo!")
            break

        if not aventureiro.esta_vivo():
            print("Você foi derrotado. O jogo acabou.")
            break

if __name__ == "__main__":
    main()
