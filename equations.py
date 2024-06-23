import math  #importation de la bibliotheque pour l'utilisation de la racine carre


#equation du premier degre : ax + b = c

def equa1():
    print("---EQUATION DU PREMIER DEGRE---")
    a = int(input("Entrez la valeur de a : "))
    b = int(input("Entrez la valeur de b : "))
    c = int(input("Entrez la valeur de c : "))
    if a == 0:
        print("Impossible")
    else:
        x = float((b - c) / a)
        print(f"La valeur de x est : {x}")


equa1()


#equation du second degre : ax^2 + bx + c = 0
# a savoir : delta = (b^2) - 4ac
# si delta < 0 : y'a pas d'ensemble solution
# si delta = 0 : x1,x2 = -b/2a
# si delta > 0 : x1 = (-b + sqr(delta))/2a et x2 = (-b - sqr(delta))/2a

def equa2():
    print("\n---EQUATION DU SECOND DEGRE--")
    a = int(input("Entrez la valeur de a : "))
    b = int(input("Entrez la valeur de b : "))
    c = int(input("Entrez la valeur de c : "))
    delta = math.pow(b,2) - 4 * a * c
    if delta < 0:
        print("Il n'ya pas d'ensemble solution")
    elif delta == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)
        print(f"Les valeur de x1 et x2 sont : {x1} et {x2}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Les valeur de x1 et x2 sont : {x1} et {x2}")
        result_x1 = a*(x1*x1)+(b*x1)+c
        print(f'Preuve de x1 :  {result_x1}')
        result_x2 = a * (x1 * x1) + (b * x1) + c
        print(f'Preuve de x2 :  {result_x2}')


equa2()
