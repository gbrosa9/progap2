import random

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
