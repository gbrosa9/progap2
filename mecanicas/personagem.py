import random
# from item import Item

class Personagem:
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

    
