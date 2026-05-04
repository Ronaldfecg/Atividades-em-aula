Nota = float(input("Digite a nota: "))

if Nota < 6:
    print("O aluno está lascado!")

elif Nota >= 6 and Nota <= 8:
    print("Dá pro gasto.")

elif Nota > 8 and Nota <= 10:
    print("O aluno está tirando onda!")

else:
    print("Nota fora de contexto.")