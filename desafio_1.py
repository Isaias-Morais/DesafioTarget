import json

#organiza vendas por vendendor
with open('vendas.json','r', encoding='utf-8') as vendas:
    json_vendas = json.load(vendas)
    vendedores = {}


    for item in json_vendas['vendas']:
        nome_vendedor = item['vendedor']
        vendas_vendedor = item['valor']

        if nome_vendedor not in vendedores:
            vendedores[nome_vendedor] = []
        vendedores[nome_vendedor].append(vendas_vendedor)

#caucula comissao
for vendedor,lista_vendas in vendedores.items():
    comissao = 0
    for item in lista_vendas:
        if item < 100:
            comissao +=0
        elif item < 500:
            comissao += item*0.01
        else:
            comissao += item*0.05
    print(f' O {vendedor}, teve uma comissao de {comissao:.2f}')
