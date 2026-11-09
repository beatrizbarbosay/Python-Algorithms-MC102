n= 1
estoque = venda = 0
while n != 0:
    n = int(input())
    if n>0:
        estoque += n
    elif n<0:
        if -n>estoque:
            print(f'Quantidade indisponível para a venda de {-n} unidades.')
        elif -n<=estoque:
            estoque += n
            venda += 1
print(f'Quantidade de vendas realizadas: {venda}')
print(f'Quantidade em estoque: {estoque}')



