1. Considerando que o json abaixo tem registros de vendas de um time comercial, faça
um programa que leia os dados e calcule a comissão de cada vendedor, seguindo a
seguinte regra para cada venda:
 Vendas abaixo de R$100,00 não gera comissão
 Vendas abaixo de R$500,00 gera 1% de comissão
 A partir de R$500,00 gera 5% de comissão
{
&quot;vendas&quot;: [
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 1200.50 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 950.75 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 1800.00 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 1400.30 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 1100.90 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 1550.00 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 1700.80 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 250.30 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 480.75 },
{ &quot;vendedor&quot;: &quot;João Silva&quot;, &quot;valor&quot;: 320.40 },

{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 2100.40 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 1350.60 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 950.20 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 1600.75 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 1750.00 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 1450.90 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 400.50 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 180.20 },
{ &quot;vendedor&quot;: &quot;Maria Souza&quot;, &quot;valor&quot;: 90.75 },

{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 800.50 },
{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 1200.00 },

{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 1950.30 },
{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 1750.80 },
{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 1300.60 },
{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 300.40 },
{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 500.00 },
{ &quot;vendedor&quot;: &quot;Carlos Oliveira&quot;, &quot;valor&quot;: 125.75 },

{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 1000.00 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 1100.50 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 1250.75 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 1400.20 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 1550.90 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 1650.00 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 75.30 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 420.90 },
{ &quot;vendedor&quot;: &quot;Ana Lima&quot;, &quot;valor&quot;: 315.40 }
]
}

2. Faça um programa onde eu possa lançar movimentações de estoque dos produtos
que estão no json abaixo, dando entrada ou saída da mercadoria no meu depósito,
onde cada movimentação deve ter:
 Um número identificador único.
 Uma descrição para identificar o tipo da movimentação realizada
E que ao final da movimentação me retorne a qtde final do estoque do produto
movimentado.

{
&quot;estoque&quot;:
[
{
&quot;codigoProduto&quot;: 101,
&quot;descricaoProduto&quot;: &quot;Caneta Azul&quot;,
&quot;estoque&quot;: 150

},
{
&quot;codigoProduto&quot;: 102,
&quot;descricaoProduto&quot;: &quot;Caderno Universitário&quot;,
&quot;estoque&quot;: 75
},
{
&quot;codigoProduto&quot;: 103,
&quot;descricaoProduto&quot;: &quot;Borracha Branca&quot;,
&quot;estoque&quot;: 200
},
{
&quot;codigoProduto&quot;: 104,
&quot;descricaoProduto&quot;: &quot;Lápis Preto HB&quot;,
&quot;estoque&quot;: 320
},
{
&quot;codigoProduto&quot;: 105,
&quot;descricaoProduto&quot;: &quot;Marcador de Texto Amarelo&quot;,
&quot;estoque&quot;: 90
}
]
}

3. Faça um programa que a partir de um valor e de uma data de vencimento, calcule o
valor dos juros na data de hoje considerando que a multa seja de 2,5% ao dia.
