temperatura = int(input("Digite a temperatura: "))

if temperatura <= 12:
    print("Está frio, ligue o aquecedor!")

elif temperatura >= 12 and temperatura <= 24:
    print("temperatura agradável!")

else:
    print("está calor, ligue o ar-condicionado!")
    