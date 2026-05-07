frutas = ["laranja", "caju", "abacaxi", "goiaba", "limao"]

frutaFavorita = input("qual a sua fruta favorita?: ")

# Para cada posição (índice) e fruta na lista numerada
for posicao, fruta in enumerate(frutas):
    
    #Faça isso:
    #Se a fruta dessa interação é igual a fruta favorita
    if fruta == fruta_favorita:
        
        # Salva numa nova variável a posição dessa interação
        posicao_fruta_favorita = posição
       
        #Quebra o for (faz ele parar)
        break

# Saída algoritmo: