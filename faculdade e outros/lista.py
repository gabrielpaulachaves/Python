def filtrar(lista, minimo, maximo):
    resposta = []
    for produto in lista:
        for keys in produto.keys():
            if produto.get(keys)>=minimo and produto.get(keys)<=maximo:
                resposta.append(produto)
    return resposta

products = [{'frango':30},{'peixe':177},{'cacho de banana':12},{'danone':9}]

print(filtrar(products, 8, 177))




