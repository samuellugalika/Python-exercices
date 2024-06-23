def moy(nombre):
    if not nombre:
        return None
    else:
        return sum(nombre) / len(nombre)


def med(nombre):
    if not nombre:
        return None
    else:
        nbr_sort = sorted(nombre)
        longueur = len(nombre)
        mid = longueur // 2
        if longueur % 2 == 0:
            return (nbr_sort[mid - 1] + nbr_sort[mid]) / 2
        else:
            nbr_sort[mid]


def main():
    nombres = []
    while True:
        nombre_str = input("Entrez un nombre (ou vide pour terminer) : ")
        if not nombre_str:
            break
        try:
            nombre = float(nombre_str)
            nombres.append(nombre)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
    if nombre:
        print(f"Moyenne : {moy(nombres)}")
        print(f"Médiane : {med(nombres)}")
    else:
        print("Aucune donnée entrée.")


if __name__ == "__main__":
    main()
