class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "Terminée"

    def __str__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


# Création de la liste de tâches
liste = ListeDeTaches()

# Ajout des tâches
tache1 = Tache("Faire les courses", "Acheter du pain et du lait")
tache2 = Tache("Sport", "Aller courir 30 min")
tache3 = Tache("Lecture", "Lire 20 pages d'un livre")

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

# Marquer une tâche comme terminée
tache1.marquerCommeFinie()

# Suppression d'une tâche
liste.supprimerTache("Sport")

# Affichage de toutes les tâches
print("Toutes les tâches :")
liste.afficherListe()

# Affichage des tâches à faire
print("\nTâches à faire :")
taches_a_faire = liste.filterListe("À faire")
for tache in taches_a_faire:
    print(tache)
