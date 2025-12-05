class Produto :
    produto = []
    movimentacao = []
    protocolo = 1
    def __init__(self,codigo=0,descricao="",estoque=0):
        self.codigo_produto = codigo
        self.descricao = descricao
        self.quantidade_estoque = estoque
        Produto.produto.append(self)

    def to_dict(self):
        return {

            "codigoProduto": self.codigo_produto,
            "descricaoProduto": self.descricao,
            "estoque": self.quantidade_estoque
        }

    def __str__(self):
        return f'Codigo-({self.codigo_produto}) Descriçao-({self.descricao}) Estoque-({self.quantidade_estoque})'

    def entrada(self,codigo,quantidade=0):
        for item in Produto.produto:
            if item.codigo_produto == codigo:
                item.quantidade_estoque += quantidade
                Produto.movimentacao.append(f'Protocolo-{Produto.protocolo} {item.descricao} teve uma entrada de {quantidade}')
                Produto.protocolo +=1
        return 'Produto nao encontrado na lista '

    def saida(self,codigo, quantidade=0):
        for item in Produto.produto:
            if item.codigo_produto == codigo:
                if item.quantidade_estoque >= quantidade:
                    item.quantidade_estoque -= quantidade
                    Produto.movimentacao.append(f'Protocolo-{Produto.protocolo} {item.descricao} teve uma saida de {quantidade}')
                    Produto.protocolo += 1
                else:
                    print("quantidade invalida")
        return 'Produto nao encontrado na lista '

    @classmethod
    def lista_produtos(cls):
        for item in cls.produto:
            print(f"Codigo-({item.codigo_produto}) Descricao-({item.descricao}) Estoque-({item.quantidade_estoque})")

    @classmethod
    def movimetacoes(cls):
        for item in cls.movimentacao:
            print(item)

