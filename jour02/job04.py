class Student:
    def __init__(self, nom, prenom, id_etudiant):
        self.__nom = nom  # Attribut privé
        self.__prenom = prenom  # Attribut privé
        self.__id_etudiant = id_etudiant  # Attribut privé
        self.__credits = 0  # Attribut privé, nombre de crédits
        self.__level = self.__student_eval()  # Attribut privé, niveau de l'étudiant basé sur les crédits

    # Méthode pour ajouter des crédits
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            # Mise à jour du niveau après ajout de crédits
            self.__level = self.__student_eval()
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    # Méthode privée pour évaluer le niveau de l'étudiant en fonction des crédits
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def student_info(self):
        print(f"Nom={self.__nom}\nPrénom={self.__prenom}\nid={self.__id_etudiant}\nNiveau={self.__level}")

# Instanciation de l'objet représentant John Doe
john_doe = Student("John", "Doe", 145)

# Ajout des crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)

# Affichage du total des crédits de John Doe
print(f"Le nombre de crédits de {john_doe._Student__nom} {john_doe._Student__prenom} est de {john_doe._Student__credits} points\n")

# Affichage des informations complètes de l'étudiant
john_doe.student_info()
