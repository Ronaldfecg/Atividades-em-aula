hardware = ["notebook", "celular", "tablet", "mouse", "teclado"]
precos = [5000, 4500, 2500, 150, 250]

#atividade 02

print("O seu", hardware[0]), print("Ficou no total de R$", precos[0]);

hardware.remove("teclado")
precos.remove(250)
print("lista de produtos:", hardware)
print("lista de preços:", precos)


print(sum(precos));

produto = (input("Digite o produto: "))
desconto = 0.95 

if produto in hardware:
    indice = hardware.index(produto)
    preco = precos[indice]

    if preco > 1000:
        preco = preco * 0.95
    print(f"O preço do {produto} é R$ {preco:.2f}")

else: print("Produto não encontrado")


