valor = float(input("digite o valor do pedido: "))

"""
Regra de negócio:
* Se a venda for até 100 reais, não tem desconto.
* Se a venda for entre 100,01 e 299,99, dê 10% de desconto.
* Se a venda for acima de 300 reais, dê 15% de desconto.
""" 

if valor <= 100:
   print(f"O valor da compra de R${valor}.")
   exit()


elif valor > 100 and valor < 299.99:
    desconto = 0.90


else:
    desconto = 0.85


total = valor * desconto

descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual,0)

# print("valor total foi de: ", total, ". E o desconto foi de: ", descontoPercentual")"

# print(f"Sua compra deu R$ {valor}. Você ganhou {descontoPercentual}%"  f"de desconto. O total agora é R${total}.")

textoResultado = f"""
Sua compra deu R$ {valor}.
Você ganhou {descontoPercentual}% de desconto.
O valor final ficou R${total}.
"""

print(textoResultado)

