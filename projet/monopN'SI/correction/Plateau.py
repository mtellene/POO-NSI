from Terrain import Terrain
from Case_speciale import Case_speciale

class Plateau:

    def __init__(self):
        self.liste_terrains = [
            [
                Case_speciale("Départ"),
                Terrain("Boulevard de Belleville", "marron"),
                Terrain("Rue Lecourbe", "marron"),
                Case_speciale("GM"),
                Terrain("Rue de Vaugirard", "bleu"),
                Terrain("Rue de Courcelles", "bleu"),
                Terrain("Avenue de la République", "bleu")
            ],
            [
                Case_speciale("Prison"),
                Terrain("Boulevard de la Vilette", "rose"),
                Terrain("Avenue de Neuilly", "rose"),
                Terrain("Rue de Paradis", "rose"),
                Terrain("Avenue de Mozart", "orange"),
                Terrain("Boulevard de Saint-Michel", "orange"),
                Terrain("Place Pigalle", "orange")
            ],
            [
                Case_speciale("Parc gratuit"),
                Terrain("Avenue Matignon", "rouge"),
                Terrain("Boulevard Malesherbes", "rouge"),
                Terrain("Avenue Henri-Martin", "rouge"),
                Terrain("Faubourg Saint-Honoré", "jaune"),
                Terrain("Place de la Bourse", "jaune"),
                Terrain("Rue la Fayette", "jaune")
            ],
            [
                Case_speciale("Allez en prison"),
                Terrain("Avenue de Breteuil", "vert"),
                Terrain("Avenue Foch", "vert"),
                Terrain("Boulevard des Capucines", "vert"),
                Case_speciale("GSL"),
                Terrain("Avenue des Champs-Elysées", "violet"),
                Terrain("Rue de la Paix", "violet")
            ],
        ]

    def __str__(self):
        ch = ""
        for i in range(len(self.liste_terrains)):
            for j in range(len(self.liste_terrains[i])):
                ch += self.liste_terrains[i][j].nom + " ; "
            ch += "\n"
        return ch

    def avoir_terrain_i_j(self, i, j):
        return self.liste_terrains[i][j]