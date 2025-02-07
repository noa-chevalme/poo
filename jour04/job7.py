import random

# Classe Carte
class Carte:
    """Classe représentant une carte du jeu de Blackjack."""
    
    def __init__(self, valeur, couleur):
        # Valeur et couleur de la carte (ex : 'As', '10', 'Coeur')
        self.valeur = valeur
        self.couleur = couleur
    
    def get_points(self):
        """Retourne la valeur de la carte en points."""
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10  # Les figures valent 10 points
        elif self.valeur == "As":
            return 1  # Par défaut, l'As vaut 1
        else:
            return int(self.valeur)  # Les cartes de 2 à 10 ont leur valeur numérique

# Classe Jeu
class Jeu:
    """Classe représentant le jeu de Blackjack."""
    
    def __init__(self):
        """Initialise le jeu avec un paquet de 52 cartes et mélange les cartes."""
        self.paquet = self.creer_paquet()  # Créer un paquet de cartes
        random.shuffle(self.paquet)  # Mélange les cartes
        self.joueur_main = []  # Main du joueur
        self.croupier_main = []  # Main du croupier
    
    def creer_paquet(self):
        """Crée un paquet de cartes avec toutes les valeurs et couleurs possibles."""
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        paquet = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
        return paquet
    
    def distribuer_carte(self):
        """Distribue une carte du paquet et la retire du paquet."""
        return self.paquet.pop()
    
    def valeur_main(self, main):
        """Calcule la valeur totale de la main en tenant compte des As."""
        total = 0
        as_count = 0
        
        # Calcul de la valeur de chaque carte dans la main
        for carte in main:
            total += carte.get_points()
            if carte.valeur == "As":
                as_count += 1
        
        # Si le joueur a des As, on essaie de les compter comme 11 si possible
        for _ in range(as_count):
            if total + 10 <= 21:  # Si ajouter 10 ne fait pas dépasser 21, on ajoute 10 pour l'As
                total += 10
        
        return total
    
    def afficher_main(self, joueur):
        """Affiche la main d'un joueur."""
        if joueur == "joueur":
            print("Main du joueur:", [str(carte.valeur) + " de " + carte.couleur for carte in self.joueur_main])
        else:
            print("Main du croupier:", [str(carte.valeur) + " de " + carte.couleur for carte in self.croupier_main])
    
    def tour_joueur(self):
        """Le joueur peut choisir de 'prendre' ou 'passer'."""
        while True:
            self.afficher_main("joueur")
            total_joueur = self.valeur_main(self.joueur_main)
            print(f"Total du joueur : {total_joueur}")
            
            if total_joueur > 21:
                print("Dommage, vous avez dépassé 21, vous perdez !")
                return False  # Si le joueur dépasse 21, il perd
            
            action = input("Voulez-vous 'prendre' une carte ou 'passer' ? (prendre/passer): ").lower()
            
            if action == "prendre":
                self.joueur_main.append(self.distribuer_carte())
            elif action == "passer":
                return True  # Le joueur passe, fin de son tour
            else:
                print("Choix invalide, essayez encore.")
    
    def tour_croupier(self):
        """Le croupier joue selon les règles (il prend des cartes jusqu'à avoir au moins 17)."""
        while True:
            total_croupier = self.valeur_main(self.croupier_main)
            self.afficher_main("croupier")
            print(f"Total du croupier : {total_croupier}")
            
            if total_croupier >= 17:
                print("Le croupier s'arrête.")
                break  # Le croupier s'arrête de tirer des cartes si il a 17 ou plus
            self.croupier_main.append(self.distribuer_carte())
    
    def determiner_gagnant(self):
        """Détermine qui gagne entre le joueur et le croupier."""
        total_joueur = self.valeur_main(self.joueur_main)
        total_croupier = self.valeur_main(self.croupier_main)
        
        print(f"Total du joueur: {total_joueur}")
        print(f"Total du croupier: {total_croupier}")
        
        if total_joueur > 21:
            print("Le joueur a perdu en dépassant 21.")
        elif total_croupier > 21:
            print("Le croupier a perdu en dépassant 21.")
        elif total_joueur > total_croupier:
            print("Le joueur gagne !")
        elif total_joueur < total_croupier:
            print("Le croupier gagne !")
        else:
            print("C'est une égalité !")
    
    def jouer(self):
        """Lance une partie de Blackjack."""
        # Distribution des cartes de départ
        self.joueur_main = [self.distribuer_carte(), self.distribuer_carte()]
        self.croupier_main = [self.distribuer_carte(), self.distribuer_carte()]
        
        print("Début du jeu !")
        
        # Tour du joueur
        if not self.tour_joueur():
            return  # Si le joueur perd, la partie est finie
        
        # Tour du croupier
        self.tour_croupier()
        
        # Déterminer qui a gagné
        self.determiner_gagnant()

# Créer une instance du jeu et commencer une partie
jeu = Jeu()
jeu.jouer()
