class Article:
    def __init__(self, nom, description, prix, quantite):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantite = quantite

    def __str__(self):
        return f'Nom : {self.nom}\n Description : {self.description}\n Prix : {self.prix}\n Quantite : {self.quantite}'


class Inventaire:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, nom, description, prix, quantite):
        article = Article(nom, description, prix, quantite)
        self.articles.append(article)
        print("Article ajouté avec succès!")

    def supprimer_article(self, nom):
        for i, article in enumerate(self.articles):
            if article.nom == nom:
                del self.articles[i]
                print("Article supprimé avec succès!")
                return
        print("Article non trouvé!")

    def modifier_article(self, nom, attribut, nouvelle_valeur):
        for article in self.articles:
            if article.nom == nom:
                setattr(article, attribut, nouvelle_valeur)
                print("Article modifié")
                return
        print("article non trouvé")

    def rechercher_article(self, nom):
        for article in self.articles:
            if article.nom == nom:
                print(article)
                return
        print("article non trouvé")

    def afficher_inventaire(self):
        if len(self.articles) == 0:
            print("L'inventaire est vide")
            return
        for article in self.articles:
            print(article)
            print("--" * 20)


inventaire = Inventaire()

inventaire.ajouter_article("shirt", "shirt blanc", 12, 34)
inventaire.ajouter_article("short", "short blanc", 22, 44)
inventaire.ajouter_article("blouse", "blouse noir", 42, 34)
inventaire.ajouter_article("jupe", "jupe rouge", 12, 44)
inventaire.ajouter_article("shoes", "shoes jordan", 12, 54)
inventaire.supprimer_article("jupe")
inventaire.ajouter_article("jupe", "jupe rouge", 12, 44)
inventaire.rechercher_article("gomme")
inventaire.modifier_article("jupe", "nom", "robe")
inventaire.modifier_article("jupe", "attribut", "robe")
inventaire.afficher_inventaire()
#

# while True:
#     inventaire = Inventaire()
#     choix = input("\nBienvenue dans le système de gestion d'inventaire.  \n" +
#                   "1. Ajouter un article\n" +
#                   "2. Supprimer un article\n" +
#                   "3. Modifier un article\n" +
#                   "4. Rechercher  un article\n" +
#                   "5. Afficher l'inventaire \n" +
#                   "6. Quittter\n" +
#                   "Que souhaitez vous faire?  ")
#     if choix == "1":
#         nom = input("Entrez le nom de l'article  : ")
#         description = input("Description : ")
#         prix = input("Prix : ")
#         quantite = input("Quantite en stock : ")
#         inventaire.ajouter_article(nom, description, prix, quantite)
#     elif choix == "2":
#         nom = input("Entrez l'article à supprimer : ")
#         inventaire.supprimer_article(nom)
#     elif choix == "3":
#         nom = input("Entrez l'article à modifier : ")
#         attribut = attribut
#         nouvelle_valeur = input("Entrez la nouvelle valeur de l'article ; ")
#         inventaire.modifier_article(nom, attribut, nouvelle_valeur)
#     elif choix == "4":
#         nom = input("Rechercher un article : ")
#         inventaire.rechercher_article(nom)
#     elif choix == "5":
#         inventaire.afficher_inventaire()
#     elif choix == "6":
#         print("Au revoir!")
#         break
#     else:
#         print("Choix invalide. Réessayer!")
