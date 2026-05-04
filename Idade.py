idade = int(input("Qual a sua idade? "))

if idade >= 0 and idade <= 12:
    print("Tá fedendo a leite ainda.")

elif idade > 12 and idade <= 22:
    print("Idade boa, aproveite bastante!")

elif idade > 22 and idade <= 60:
    print("Chegou a tua hora, vamos acordar e construir algo!")

else:
    print("Combateu o bom combate? Agora descanse!")