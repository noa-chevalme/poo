class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes = 0
        self.jaunes = 0
        self.rouges = 0

    def marquer(self):
        self.buts += 1
        print(f"{self.nom} a marqué !")

    def passer(self):
        self.passes += 1
        print(f"{self.nom} a fait une passe décisive !")

    def carton_jaune(self):
        self.jaunes += 1
        print(f"{self.nom} a reçu un jaune !")

    def carton_rouge(self):
        self.rouges += 1
        print(f"{self.nom} a reçu un rouge !")

    def afficher_stats(self):
        print(f"{self.nom} - #{self.numero} ({self.position})")
        print(f"Buts: {self.buts}, Passes: {self.passes}, Jaunes: {self.jaunes}, Rouges: {self.rouges}\n")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter(self, joueur):
        self.joueurs.append(joueur)
        print(f"{joueur.nom} rejoint {self.nom}.")

    def afficher_stats(self):
        print(f"Stats de {self.nom} :")
        for joueur in self.joueurs:
            joueur.afficher_stats()

# Création de joueurs et équipes
messi = Joueur("Messi", 10, "Attaquant")
ronaldo = Joueur("Ronaldo", 7, "Attaquant")
ramos = Joueur("Ramos", 4, "Défenseur")

barca = Equipe("Barcelone")
real = Equipe("Real Madrid")

barca.ajouter(messi)
real.ajouter(ronaldo)
real.ajouter(ramos)

# Simulation
messi.marquer()
ronaldo.passer()
ramos.carton_jaune()
ramos.carton_rouge()

# Affichage des stats
barca.afficher_stats()
real.afficher_stats()
