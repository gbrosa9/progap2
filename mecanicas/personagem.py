import random

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
        if direcao == 'A' and self.posicao[1] > 0:
            self.posicao[1] -= 1
        elif direcao == 'W' and self.posicao[0] > 0:
            self.posicao[0] -= 1
        elif direcao == 'D' and self.posicao[1] < 9:
            self.posicao[1] += 1
        elif direcao == 'S' and self.posicao[0] < 9:
            self.posicao[0] += 1

    def coletar_item(self, item):
        self.mochila.append(item)

    def usar_item_da_mochila(self, escolha):
        if 1 <= escolha <= len(self.mochila):
            item_escolhido = self.mochila[escolha - 1]
            print(f'Você utilizou {item_escolhido.nome}!')
            self.aplicar_efeito_do_item(item_escolhido.tipo, item_escolhido.intensidade)
            self.mochila.remove(item_escolhido)
        else:
            print('Escolha inválida.')

    def aplicar_efeito_do_item(self, tipo_item, intensidade):
        if tipo_item == 'Vida':
            self.vida_atual += 20 * intensidade
            if self.vida_atual > self.vida_maxima:
                self.vida_atual = self.vida_maxima
        elif tipo_item == 'Forca':
            self.forca += intensidade
        elif tipo_item == 'Defesa':
            self.defesa += intensidade

    def ver_mochila(self, baú_itens=None):
        print(f'\nMochila de {self.nome}:')
        for i, item in enumerate(self.mochila, start=1):
            print(f'{i}. {item.nome} ({item.tipo}) - Intensidade: {item.intensidade}')

        if baú_itens:
            print('\nItens no Baú:')
            for i, (tipo, quantidade) in enumerate(baú_itens.items(), start=len(self.mochila) + 1):
                print(f'{i}. Poção de {tipo} - Quantidade: {quantidade}')

        if not self.mochila and not baú_itens:
            print('A mochila está vazia.')

    def esta_vivo(self):
        return self.vida_atual > 0
