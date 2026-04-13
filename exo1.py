class Vehicule:
    def __init__(self, immatriculation, capacite, vitesse_max):
        self.immatriculation = immatriculation
        self.capacite = capacite
        self.vitesse_max = vitesse_max


class Camion(Vehicule):
    def __init__(self, immatriculation, capacite, vitesse_max, charge_max):
        super().__init__(immatriculation, capacite, vitesse_max)
        self.charge_max = charge_max

    def charger_marchandises(self):
        print("Chargement de marchandises dans le camion")


class Fourgon(Vehicule):
    def __init__(self, immatriculation, capacite, vitesse_max, volume_max):
        super().__init__(immatriculation, capacite, vitesse_max)
        self.volume_max = volume_max

    def charger_colis(self):
        print("Chargement de colis dans le fourgon")


class Moto(Vehicule):
    def __init__(self, immatriculation, capacite, vitesse_max, cylindree):
        super().__init__(immatriculation, capacite, vitesse_max)
        self.cylindree = cylindree

    def livrer_rapidement(self):
        print("Livraison rapide en moto")


class MissionTransport:
    def __init__(self, depart, arrivee, date):
        self.depart = depart
        self.arrivee = arrivee
        self.date = date
        self.vehicule = None

    def assigner_vehicule(self, vehicule):
        self.vehicule = vehicule


# Test
camion = Camion("123-A", 1000, 120, 5000)
moto = Moto("456-B", 100, 180, 600)

mission = MissionTransport("Casablanca", "Rabat", "2026-04-13")
mission.assigner_vehicule(camion)

camion.charger_marchandises()
moto.livrer_rapidement()