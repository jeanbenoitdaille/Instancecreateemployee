class Entreprise:
        employes = []
     
class Employe:
        def __init__(self, prenom, nom, position, salaire):
            self.prenom = prenom
            self.nom = nom
            self.position = position
            self.salaire = salaire
     
employes = [
                ("Pierre", "Smith", "Responsable RH", 35000),
                ("Julie", "Martin", "Développeur Python", 42000),
                ("Éric", "Dupont", "Chef de projet", 50000),
                ]
     
for employe_data in employes:
        employe = Employe(*employe_data)
        Entreprise.employes.append(employe)