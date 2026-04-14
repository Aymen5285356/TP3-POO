class Personnage:
    def __init__(self, nom, niveau, pv, attaque):
        self.nom = nom
        self.niveau = niveau
        self.points_de_vie = pv
        self.points_attaque = attaque


class Guerrier(Personnage):
    def __init__(self, nom, niveau, pv, attaque, force):
        super().__init__(nom, niveau, pv, attaque)
        self.force = force

    def frappe_lourde(self):
        print("Frappe lourde !")


class Mage(Personnage):
    def __init__(self, nom, niveau, pv, attaque, magie):
        super().__init__(nom, niveau, pv, attaque)
        self.magie = magie

    def lancer_sort(self):
        print("Sort magique lancé !")


class Archer(Personnage):
    def __init__(self, nom, niveau, pv, attaque, agilite):
        super().__init__(nom, niveau, pv, attaque)
        self.agilite = agilite

    def tir_precision(self):
        print("Tir de précision !")


class Arme:
    def __init__(self, nom, degats):
        self.nom = nom
        self.degats = degats


class Inventaire:
    def __init__(self):
        self.armes = []

    def ajouter_arme(self, arme):
        self.armes.append(arme)

    def afficher_inventaire(self):
        for arme in self.armes:
            print(f"{arme.nom} - {arme.degats} dégâts")

guerrier = Guerrier("Thor", 10, 100, 20, 50)
epee = Arme("Épée", 30)

inventaire = Inventaire()
inventaire.ajouter_arme(epee)

inventaire.afficher_inventaire()
guerrier.frappe_lourde()
