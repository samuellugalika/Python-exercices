class Personne:
    def __init__(self, nom: str, age: int, ville: str, poste: str, email: str):
        self.nom = nom
        self.age = age
        self.ville = ville
        self.poste = poste
        self.email = email

    def __str__(self):
        return f'---- Info sur le personnel ----\nNom : {self.nom}\nAge : {self.age}\nVille : {self.ville}\nPoste : {self.poste}\nEmail : {self.email}\n'


class Afficher:
    def __init__(self):
        self.liste = []

    def ajout_personne(self, humain):
        self.liste.append(humain)

    def show_person(self, humain):

        if not self.liste:
            print('Aucun personnel n\'est enregistré')
        else:
            print("Liste du personnel \n")
            for humain in self.liste:
                print(f'{humain}')

    def del_person(self, nom_humain):
        person_found = False

        for humain in self.liste:
            if humain.nom == nom_humain:
                self.liste.remove(humain)
                print(f'{nom_humain} a été supprimé de la liste du personnel')
                person_found = True
                break
        if not person_found:
            print(f'{nom_humain} n\'est pas reconnu!')

    def modify_person(self, nom_humain):
        person_found = False

        for humain in self.liste:
            if humain.nom == nom_humain:
                while True:
                    print('-----------------------------------')
                    print('MODIFIER LES INFORMATIONS DU PERSONNEL')
                    print('-----------------------------------')
                    print('     1. Modifier le nom du personnel')
                    print('     2. Modifier l\'age du personnel')
                    print('     3. Modifier la ville de residence du personnel')
                    print('     4. Modifier le poste du personnel')
                    print('     5. Modifier l\'adresse mail du personnel')
                    print('     6. Retour au menu principal')
                    choice_mod = input("Choisissez entre un 1-6 : ")
                    if choice_mod == '1':
                        new_name = input("Entrez le nouveau nom du personnel : ")
                        humain.nom = new_name
                        print(f'{new_name} est le nouveau nom du personnel')
                    elif choice_mod == '2':
                        try:
                            new_age = int(input('Entrez le nouvel age du personnel : '))
                            humain.age = new_age
                            print(f'{new_age} est le nouvel age du personnel')
                        except:
                            print("L'age du personnel doit etre un nombre entier!")
                    elif choice_mod == '3':
                        new_town = input("Entrez la nouvelle ville du personnel : ")
                        humain.ville = new_town
                        print(f'{new_town} est la nouvelle ville du personnel')
                    elif choice_mod == '4':
                        new_poste = input("Entrez le nouveau poste du personnel : ")
                        humain.poste = new_poste
                        print(f'{new_poste} est le nouveau poste du personnel')
                    elif choice_mod == '5':
                        new_mail = input("Entrez le nouvel adresse mail du personnel : ")
                        humain.email = new_mail
                        print(f'{new_mail} est nouvel adresse mail du personnel')
                    elif choice_mod == '6':
                        break
                person_found = True
                break
        if not person_found:
            print(f'{nom_humain} n\'est pas reconnu!')

    def search_person(self, nom_humain):
        for humain in self.liste:
            if humain.nom == nom_humain:
                print(f'{nom_humain} trouvé')
            else:
                print(f'{nom_humain} n\'est pas trouvé ')


def main():
    show = Afficher()
    while True:
        print('\n--------------------------------------')
        print("|                  GESTIONNAIRE DU PERSONNEL            |")
        print('--------------------------------------')
        print('Opérations sur le système de gestion du personnel:\n')
        print('     1. Ajouter un personnel')
        print('     2. Supprimer un personnel')
        print('     3. Modifier les infos du personnel')
        print('     4. Rechercher un personnel')
        print('     5. Afficher la liste du personnel')
        print('     6. Quitter')
        choice = input("Choisissez entre un 1-6 : ")
        if choice == '1':
            nom = input("Nom du personnel : ")
            try:
                age = int(input("Age du personnel : "))
            except:
                print("L'age du personnel doit etre un nombre entier!")
            ville = input("Ville de résidence du personnel : ")
            poste = input("Poste du personnel dans la structure : ")
            email = input("Adresse mail du personnel : ")
            new_person = Personne(nom, age, ville, poste, email)
            show.ajout_personne(new_person)
            print(f'Personnel {nom} ajouté à la liste du personnel')
        elif choice == '2':
            nom_humain = input("Entrez le nom du personnel à supprimer : ")
            show.del_person(nom_humain)
        elif choice == '3':
            nom_humain = input("Entrez le nom du personnel à modifier : ")
            show.modify_person(nom_humain)
        elif choice == '4':
            nom_humain = input("Entrez le nom du personnel à rechercher : ")
            show.search_person(nom_humain)
        elif choice == '5':
            show.show_person(Personne)
        elif choice == '6':
            print('Merci d\'avoir utilisé le gestionnaire du personnel')
            break
        else:
            print("Choix invalide! Ressayer!")


if __name__ == '__main__':
    main()
