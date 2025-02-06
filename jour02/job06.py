class Commande:
    def __init__(self, numero_commande):
        # Attributs privés
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats et leur prix
        self.__statut = 'en cours'  # Statut de la commande (par défaut 'en cours')

    # Accesseur pour le numéro de commande
    def get_numero_commande(self):
        return self.__numero_commande

    # Accesseur pour le statut de la commande
    def get_statut(self):
        return self.__statut

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {'prix': prix, 'statut': 'commandé'}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")

    # Méthode pour annuler une commande
    def annuler_commande(self):
        if self.__statut == 'en cours':
            self.__statut = 'annulée'
            print(f"La commande {self.__numero_commande} a été annulée.")
        else:
            print(f"La commande {self.__numero_commande} ne peut pas être annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = 0
        for plat, details in self.__plats_commandes.items():
            total += details['prix']
        return total

    # Méthode pour calculer la TVA (20% par exemple)
    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.20  # TVA à 20%
        return tva

    # Méthode pour afficher les détails de la commande
    def afficher_commande(self):
        print(f"Commande numéro : {self.__numero_commande}")
        print(f"Statut : {self.__statut}")
        print("Plats commandés :")
        for plat, details in self.__plats_commandes.items():
            print(f"- {plat} : {details['prix']} €")
        if self.__statut != 'annulée':
            total = self.__calculer_total()
            tva = self.calculer_tva()
            total_ttc = total + tva
            print(f"Total (HT) : {total} €")
            print(f"TVA (20%) : {tva} €")
            print(f"Total TTC : {total_ttc} €")
        else:
            print("La commande est annulée. Aucun paiement nécessaire.")

# Exemple d'utilisation avec des plats africains
commande = Commande(12345)

# Ajouter des plats africains à la commande
commande.ajouter_plat("Jollof Rice", 12)  # Plat populaire d'Afrique de l'Ouest
commande.ajouter_plat("Poulet Yassa", 15)  # Plat sénégalais avec du poulet et des oignons
commande.ajouter_plat("Bunny Chow", 18)   # Plat populaire en Afrique du Sud

# Afficher la commande avant annulation
commande.afficher_commande()

# Annuler la commande
commande.annuler_commande()

# Ajouter un plat après annulation (ne sera pas pris en compte)
commande.ajouter_plat("Saka Saka", 10)    # Plat à base de feuilles de manioc

# Afficher la commande après annulation
commande.afficher_commande()
