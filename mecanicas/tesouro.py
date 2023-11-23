import random
from mecanicas.item import Item

class Tesouro:
    def __init__(self):
        self.posicao = [random.randint(1, 9), random.randint(1, 9)]

class Baú:
    def __init__(self):
        self.itens = [
            Item('Pocao', 'Vida', random.randint(1, 2)),
            Item('Espada', 'Forca', random.randint(1, 2)),
            Item('Escudo', 'Defesa', random.randint(1, 2))
        ]

    def abrir_baú(self, personagem):
        print('Você encontrou um baú! Escolha um item:')
        poções_coletadas = {'Vida': 0, 'Forca': 0, 'Defesa': 0}

        for i, item in enumerate(self.itens, start=1):
            print(f'{i}. {item.nome} ({item.tipo}) - Intensidade: {item.intensidade}')

        escolha = int(input('Digite o número do item desejado (ou 0 para sair): ')) - 1
        if escolha == -1:
            return poções_coletadas

        if 0 <= escolha < len(self.itens):
            item_escolhido = self.itens[escolha]
            print(f'Você pegou {item_escolhido.nome}!')
            personagem.coletar_item(item_escolhido)
            self.itens.pop(escolha)

            if item_escolhido.tipo in poções_coletadas:
                poções_coletadas[item_escolhido.tipo] += 1
        else:
            print('Escolha inválida. Nenhum item foi adicionado à sua mochila.')

        return poções_coletadas
