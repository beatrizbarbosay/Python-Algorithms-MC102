###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
###################################################
estoque = {}
venda = {}
compra = {}
while True:
  entrada = input()
  if entrada == str('FIM'):
    break
  (produto,quantidade)= entrada.split(" : ")
  quantidade=int(quantidade)
  if produto not in (estoque.keys()):
    estoque[produto] = venda[produto] = compra[produto] = 0
  if quantidade > 0:
    estoque[produto] += quantidade
    compra[produto] += 1
  elif quantidade < 0:
    if -quantidade > estoque[produto]:
      print(f"Quantidade indisponivel para a venda de {-quantidade} unidade(s) do produto {produto}.")
    elif -quantidade <= estoque[produto]:
      estoque[produto] += quantidade
      venda[produto] += 1
for produto in sorted(estoque.keys()):
  if compra[produto]!=0:
    print(f"Produto: {produto}")
    print(f"Quantidade em Estoque: {estoque[produto]}")
    print(f"Pedidos de Compra: {compra[produto]}")
    print(f"Pedidos de Venda: {venda[produto]}")

