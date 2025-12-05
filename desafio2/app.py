import json
from desafio2.produto import Produto
with open('estoque.json', 'r', encoding='utf-8') as json_arquivo:
    estoque = json.load(json_arquivo)

    for item in (estoque['estoque']):
        item = Produto(item["codigoProduto"],item["descricaoProduto"],item["estoque"])

item.saida(102,2)

item.entrada(101,32)

item.entrada(103,12)

lista_dict = [p.to_dict() for p in Produto.produto]

Produto.movimetacoes()

with open('estoque.json', "w" , encoding='utf-8') as f:
    json.dump({"estoque": lista_dict},f,indent=2,ensure_ascii=False)


