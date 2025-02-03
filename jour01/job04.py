class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."

personne1 = Personne("Marston", "John")
personne2 = Personne("Arthur", "Morgan")
print(personne1.SePresenter())
print(personne2.SePresenter())