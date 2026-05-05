valor = float(input("digite o valor do pedido: "))



if valor <= 100:
    desconto = 0.95


elif valor > 100 and valor < 299.99:
    desconto = 0.90


else:
    desconto = 0.85


total = valor * desconto

descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual,0)

# print("valor total foi de: ", total, ". E o desconto foi de: ", descontoPercentual")


#print(f"Sua compra deu R$ {valor}. Você ganhou {descontoPercentual}%"  f"de desconto. O total agora é R${total}.")

textoResultado = f"""
Sua compra deu R$ {valor}.
Você ganhou {descontoPercentual}% de desconto.
O valor final ficou R${total}.
"""

print(textoResultado)

