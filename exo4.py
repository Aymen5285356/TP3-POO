class Paiement:
    def __init__(self, montant, date):
        self.montant = montant
        self.date = date


class CarteDeCredit(Paiement):
    def __init__(self, montant, date, numero_de_carte):
        super().__init__(montant, date)
        self.numero_de_carte = numero_de_carte

    def effectuer_paiement(self):
        print("Paiement par carte effectué")


class PayPal(Paiement):
    def __init__(self, montant, date, email):
        super().__init__(montant, date)
        self.email = email

    def connexion_paypal(self):
        print("Connexion à PayPal")

    def effectuer_paiement(self):
        print("Paiement via PayPal effectué")


class VirementBancaire(Paiement):
    def __init__(self, montant, date, compte):
        super().__init__(montant, date)
        self.compte = compte

    def initier_virement(self):
        print("Virement bancaire initié")

    def effectuer_paiement(self):
        print("Paiement par virement effectué")


class ClientPaiement:
    def __init__(self, nom, adresse, moyen_de_paiement):
        self.nom = nom
        self.adresse = adresse
        self.moyen_de_paiement = moyen_de_paiement

    def effectuer_paiement(self):
        self.moyen_de_paiement.effectuer_paiement()

carte = CarteDeCredit(100, "2026-04-13", "1234-5678")
client = ClientPaiement("Sara", "Rabat", carte)

client.effectuer_paiement()
