# VOTAÇÃO
while True:
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é elegível para votar.")
        
        # Candidatos
        print("\nOpções de candidatos:")
        print("1. Ricardo Nunes (15)")
        print("2. Marçal (28)")
        print("3. Boulos (50)")
        print("4. Drankao (171)")

        candidato = input("\nDigite o nome ou número do candidato em quem você irá votar: ").lower()

        # Escolha o seu prefeito
        if candidato == "ricardo nunes" or candidato == "15":
            print("Parabéns, você votou em Ricardo Nunes! Vamos seguir com a administração da cidade!")
        elif candidato == "marçal" or candidato == "28":
            print("Parabéns, você votou em Marçal! Vou acabar com a cambada de vagabundo.")
        elif candidato == "boulos" or candidato == "50":
            print("Parabéns, você votou em Boulos! A luta por moradia continua!")
        elif candidato == "drankao" or candidato == "171":
            print("Parabéns, você votou em Drankao! Vou abrir uma rua do Grau pra geral que não quer nada com nada e vou dar 200 reais pra quem votar em mim.")
        else:
            print(f"Você escolheu votar em {candidato.capitalize()}, que não está na lista.")
        break
    else:
        print("Você não pode votar ainda. Tente novamente.\n")