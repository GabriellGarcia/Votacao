# VOTAÇÃO
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é elegível para votar.")
    candidato = input("Em quem você irá votar? ").lower()  

    if candidato == "marçal":
        print("Vou acabar com a cambada de vagabundo.")
    elif candidato == "boulos":
        print("A luta por moradia continua!")
    elif candidato == "ricardo nunes":
        print("Vamos seguir com a administração da cidade!")
    else:
        print(f"Você escolheu votar em {candidato.capitalize()}.")
else:
    print("Você não pode votar ainda.")
