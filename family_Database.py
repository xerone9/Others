population = []
females = []
males = []
family = []

while True:

    print("""
    
    1- Add Family
    2- Total Family Registered
    3- Total Members of a specific family (First search available families in the list)
    4- Total Males
    5- Total Females
    6- Total Population of the City
    
    """)

    choice = int(input("Make Choice (enter Serial No of the selected choice): "))

    if choice == 1:
        your_Name = input("What is your name: ").lower()
        family.append(your_Name)
        globals()[your_Name] = []
        population.append(your_Name)
        globals()[your_Name].append(your_Name)
        father_Name = input("What is your Father Name (Type 'deceased' if dead): ").lower()
        males.append(father_Name)
        population.append(father_Name)
        globals()[your_Name].append(father_Name)
        mother_Name = input("What is your Mother Name (Type 'deceased' if dead): ").lower()
        females.append(mother_Name)
        population.append(mother_Name)
        globals()[your_Name].append(mother_Name)
        brothers_Count = int(input("How Many Brothers you have (Enter '0' if you have no brother):"))
        count = 0


        while brothers_Count > count:
            brother_Names = input("Enter Brother Names (Enter One Name and Press Enter: ").lower()
            globals()[your_Name].append(brother_Names)
            population.append(brother_Names)
            males.append(brother_Names)
            count += 1
        count = 0


        sisters_Count = int(input("How Many Sisters you have (Enter '0' if you have no sister):"))


        while sisters_Count > count:
            sister_Names = input("Enter Sister Names (Enter One Name and Press Enter: ").lower()
            globals()[your_Name].append(sister_Names)
            population.append(sister_Names)
            females.append(sister_Names)
            count += 1
        count = 0

    elif choice == 2:
        print(family)

    elif choice == 3:
        searched_Name= input("Enter Family Name To know the see the total members: ").lower()
        if searched_Name in family:
            print(globals()[searched_Name])
        else:
            print("Family name not found in database")

    elif choice == 4:
        print(males)

    elif choice == 5:
        print(females)

    elif choice == 6:
        print(population)

    else:
        print("incorrect choice made.")
