liste_courses = []

while True:
    print("Choisissez parmi les 5 options suivantes :")
    print("1. Ajouter un élément dans la liste")
    print("2. Retirer un élément dans la liste")
    print("3. Afficher tous les éléments de la liste")
    print("4. Vider tous les éléments de la liste")
    print("5. Quitter")

    user_choice = input("Votre choix : ")

    if user_choice == "1":
        ajout = input("Entrez le nom de l'élément à ajouter dans la liste : ")
        liste_courses.append(ajout)
        print(f"L'élémént {ajout} à été ajouté à la liste.")

    elif user_choice == "2":
        retire = input("Entrez le nom de l'élément à supprimer dans la liste : ")
        if retire in liste_courses:
            while retire in liste_courses:
                liste_courses.remove(retire)
                print(f"L'élément {retire} a été supprimé de la liste")
        else:
            print(f"L'éléement {retire} ne figure pas dans la liste")

    elif user_choice == "3":
        x = 0
        for elem in liste_courses:
            x += 1
            print(f"{x}. {elem}")

    elif user_choice == "4":
        liste_courses.clear()

    elif user_choice == "5":
        break

    else:
        print("Merci d'indiquer une option valide")
