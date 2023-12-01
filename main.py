from forex_python.converter import CurrencyRates

change = CurrencyRates()

historique = []

devise_pref = []

ajout_devise = input("Souhaitez-vous ajoutez une devise ? (oui/non) : ")

if ajout_devise == "oui":
    nom_devise = input ("Entrez le nom de la devise : ")
    valeur_devise = float(input("Entrez la valeur de la devise : "))

while True:
    while True:
        try:
            amount = float(input("Veuillez entrer une valeur à convertir : "))
            break
        except ValueError:
            print("ERREUR, la valeur saisie est invalide")
    

    while True:
        try:
            devise1 = input("Entrez la devise de départ en majuscules (USD, EUR...) : ")
            break
        except ValueError:
            print("ERREUR, la devise saisie est incorrecte")
        
    if ajout_devise == "oui":
        print (amount ,devise1 ,"converti en", nom_devise ,"vaut" ,amount / valeur_devise)
        to_continue = input("Souhaitez-vous continuer à faire des conversions ? (oui/non) : ")
        if to_continue == "non":
            break

    while True:
        try:
            devise2 = input("Entrez la devise d'arrivée en majuscules (USD, EUR...) : ")
            break
        except ValueError:
            print("ERREUR, la devise saisie est incorrecte")
  

    convertisseur = change.convert(devise1, devise2, amount)
    print(convertisseur)

    historique.append((amount, devise1, devise2, convertisseur))

    to_continue = input("Souhaitez-vous continuer à faire des conversions ? (oui/non) : ")
    
    question = input("Souhaitez-vous afficher l'historique des résultats ? (oui/non) : ")

    if question == "oui":
        print("Historique des résultats :")
        for entry in historique:
            print(f"Montant : {entry[0]}, Devise de départ : {entry[1]}, Devise d'arrivée : {entry[2]}, Résultat : {entry[3]}")

    afficher_devise_pref = input("Souhaitez vous affichez votre devise personalisée ? (oui/non) : ")

    if afficher_devise_pref == "oui":
        print (devise_pref)

    if to_continue == "non":
        break
    
  