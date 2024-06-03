choice = input() 

if choice == 'vertebrado':
    choice = input()

    if choice == 'ave':
        choice = input()

        if choice == 'carnivoro':
            print("aguia")

        if choice == 'onivoro':
            print("pomba")

    if choice == 'mamifero':
        choice = input()

        if choice == 'onivoro':
            print("homem")

        if choice == 'herbivoro':
            print("vaca")



elif choice == 'invertebrado':
    choice = input()

    if choice == 'inseto':
        choice = input()

        if choice == 'hematofago':
            print("pulga")

        if choice == 'herbivoro':
            print("lagarta")

    if choice == 'anelideo':
        choice = input()

        if choice == 'hematofago':
            print("sanguessuga")

        if choice == 'onivoro':
            print("minhoca")
