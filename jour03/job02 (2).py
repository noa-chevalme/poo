class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte {self.__numero} - {self.__prenom} {self.__nom} - Solde : {self.__solde}€ - Découvert autorisé : {self.__decouvert}")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde : {self.__solde}€")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.__solde}€")
        else:
            print("Erreur : Solde insuffisant.")

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05
            print(f"Agios appliqués. Nouveau solde : {self.__solde}€")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ vers le compte {compte_destinataire.__numero} effectué.")
        else:
            print("Erreur : Solde insuffisant pour effectuer le virement.")

# Création des comptes
compte1 = CompteBancaire(12345, "Lefevre", "Alexandre", 1000)
compte2 = CompteBancaire(67890, "Bernard", "Camille", -200, True)

# Vérifications des comptes
compte1.afficher()
compte2.afficher()

# Virement du compte 1 vers le compte 2
compte1.virement(compte2, 200)

# Affichage des soldes après virement
compte1.afficherSolde()
compte2.afficherSolde()
