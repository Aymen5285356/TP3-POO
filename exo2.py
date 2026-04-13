class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Livre(Produit):
    def __init__(self, nom, prix, auteur):
        super().__init__(nom, prix)
        self.auteur = auteur

    def afficher_auteur(self):
        print(f"Auteur: {self.auteur}")


class Vetement(Produit):
    def __init__(self, nom, prix, taille):
        super().__init__(nom, prix)
        self.taille = taille

    def afficher_taille(self):
        print(f"Taille: {self.taille}")


class Electronique(Produit):
    def __init__(self, nom, prix, marque):
        super().__init__(nom, prix)
        self.marque = marque

    def afficher_marque(self):
        print(f"Marque: {self.marque}")


class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.panier = []

    def ajouter_au_panier(self, produit):
        self.panier.append(produit)

    def afficher_panier(self):
        for p in self.panier:
            print(f"{p.nom} - {p.prix}€")
            if isinstance(p, Livre):
                p.afficher_auteur()
            elif isinstance(p, Vetement):
                p.afficher_taille()
            elif isinstance(p, Electronique):
                p.afficher_marque()


# Test
client = Client("Ali", "Casablanca")

livre = Livre("Python", 20, "Dupont")
vetement = Vetement("T-shirt", 15, "M")

client.ajouter_au_panier(livre)
client.ajouter_au_panier(vetement)

client.afficher_panier()