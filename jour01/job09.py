class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Produit : {self.nom}, Prix HT : {self.prixHT}€, TVA : {self.TVA}%, Prix TTC : {self.calculerPrixTTC():.2f}€"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA


produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 500, 20)


print(produit1.afficher())
print(produit2.afficher())


produit1.modifierNom("PC Portable")
produit1.modifierPrixHT(850)

produit2.modifierNom("Smartphone")
produit2.modifierPrixHT(550)

print("\nAprès modification :")
print(produit1.afficher())
print(produit2.afficher())
