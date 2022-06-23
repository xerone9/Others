import os

sons = []
daughters = []
wifes = []
brothers = []
sisters = []
alpha_count = ['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th']
grandmother = []
grandfather = []
separation = []
count = 0
index = 0



print("""

Calculate Family Inheritenche
______________________________

""")

input("Press Enter to continue...")
print("""

    """)

inheritence_amount = float(input("Enter Inheritence Amount: "))
inheritence_of_person = input("Enter the name of whom inheritence is: ").lower()
gender_of_person = input("Enter Gender of Person (Male or female): ").lower()

father_alive = input("is " + inheritence_of_person + "'s father alive (Yes or No): ").lower()
if father_alive == "yes":
    father_name = input("Enter " + inheritence_of_person + "'s father name: ").lower()
    father_count = 1
elif father_alive == "no":
    father_count = 0
else:
    print("I don't understand you")

mother_alive = input("is " + inheritence_of_person + "'s mother alive (Yes or No): ").lower()
if mother_alive == "yes":
    mother_name = input("Enter "+ inheritence_of_person + "'s mother name: ").lower()
    mother_count = 1
elif mother_alive == "no":
    mother_count = 0
else:
    print("I don't understand you")

grandfather_alive = input("is " + inheritence_of_person + "'s grandfather alive (Yes or No): ").lower()
if grandfather_alive == "yes":
    grandfather_name = input("Enter " + inheritence_of_person + "'s grandfather name: ").lower()
    grandfather_count = 1
elif grandfather_alive == "no":
    grandfather_count = 0
else:
    print("I don't understand you")

grandmother_alive = input("is " + inheritence_of_person + "'s grandmother alive (Yes or No): ").lower()
if grandmother_alive == "yes":
    grandmother_name = input("Enter "+ inheritence_of_person + "'s grandmother name: ").lower()
    grandmother_count = 1
elif grandmother_alive == "no":
    grandmother_count = 0
else:
    print("I don't understand you")





if gender_of_person == "male":
    wifes_count = float(input("How many of " + inheritence_of_person + "'s wifes are alive: "))
    counts = 1
    if wifes_count > count:
       for count, items in enumerate(alpha_count):
            wives = input("Enter " + str(counts) + items + " Wife Name: ").lower()
            wifes.append(wives)
            counts += 1
            count += 1
            if count == wifes_count:
                break
    count = 0

if gender_of_person == "female":
    husband_alive = input("is " + inheritence_of_person + "'s husband alive (Yes or No): ").lower()
    if husband_alive == "yes":
        husband_name = input("Enter " + inheritence_of_person + "'s husband name: ").lower()
    elif husband_alive == "no":
        count = 0
    else:
        print("I don't understand you")

sons_count = float(input("How many sons " + inheritence_of_person + " have: "))
if sons_count > count:
    counts = 1
    for count, items in enumerate(alpha_count):
        boys = input("Enter " + str(counts) + items + " Son name: ").lower()
        sons.append(boys)
        count += 1
        counts += 1
        if count == sons_count:
            break
    count = 0

daughters_count = float(input("How many daughters " + inheritence_of_person + " have: "))
if daughters_count > count:
    counts = 1
    for count, items in enumerate(alpha_count):
        girls = input("Enter " + str(counts) + items + " daughter Names : ").lower()
        daughters.append(girls)
        count += 1
        counts += 1
        if count == daughters_count:
            break
    count = 0

if father_alive == "no" and mother_alive == "no" and wifes_count == 0 and sons_count == 0 and daughters_count == 0:
    print("it seems none of " + inheritence_of_person + " close family meember is alive. In that case the inheritence amount will be given to " + inheritence_of_person + " brothers and sisters")
    brothers_count = float(input("How many brohthers " + inheritence_of_person + " have alive: "))
    if brothers_count > count:
        counts = 1
        for count, items in enumerate(alpha_count):
            male = input("Enter " + str(counts) + items + " Brother Name: ")
            brothers.append(male)
            count += 1
            counts += 1
            if count == brothers_count:
                break
        count = 0

    sisters_count = float(input("How many sisters " + inheritence_of_person + " have alive: "))
    if sisters_count > count:
        counts = 1
        for count, items in enumerate(alpha_count):
            female = input("Enter " + str(counts) + items + " sister Name: ")
            sisters.append(female)
            count += 1
            counts += 1
            if count == sisters_count:
                break
        count = 0

sons_calcua = 1
daughters_calcula = 1/2
daughters_calcula2 = 2/3
mother_calcula = 1/6
father_calcula = 1/6
grandmother_calcula = 1/6
grandfather_calcula = 1/6
wifes_calcula = 1/8

if daughters_count < 3:
    grand_calcula = (sons_count * sons_calcua) + (daughters_count * daughters_calcula) + (wifes_count * wifes_calcula) + (father_count * father_calcula) + (mother_count * mother_calcula) + (grandfather_count * grandfather_calcula) + (grandmother_count * grandmother_calcula)

else:
    grand_calcula = (sons_count * sons_calcua) + (daughters_count * daughters_calcula2) + (wifes_count * wifes_calcula) + (father_count * father_calcula) + (mother_count * mother_calcula) + (grandfather_count * grandfather_calcula) + (grandmother_count * grandmother_calcula)

if mother_count == 1:
    work = str((inheritence_amount * mother_calcula) / grand_calcula)
    separation.append(float(work))
    print("")
    print ("=============Parnets==========================")
    print (mother_name + " Share is " + work)

if father_count == 1:
    work = str((inheritence_amount * father_calcula) / grand_calcula)
    separation.append(float(work))
    print (father_name + " Share is " + work)

if grandmother_count == 1:
    work = str((inheritence_amount * grandmother_calcula) / grand_calcula)
    separation.append(float(work))
    print("")
    print("=============Grand Parnets==========================")
    print (grandmother_name + " Share is " + work)

if grandfather_count == 1:
    work = str((inheritence_amount * grandfather_calcula) / grand_calcula)
    separation.append(float(work))
    print (grandfather_name + " Share is " + work)

print("")
print("=============Childrens==========================")
for items in sons:
    work = str((inheritence_amount * sons_calcua) / grand_calcula)
    separation.append(float(work))
    print (items + " Share is " + work)

if daughters_count < 3:
    for items in daughters:
        work = str((inheritence_amount * daughters_calcula) / grand_calcula)
        separation.append(float(work))
        print (items + " Share is " + work)
else:
    for items in daughters:
        work = str((inheritence_amount * daughters_calcula2) / grand_calcula)
        separation.append(float(work))
        print (items + " Share is " + work)

print("")
print("=============Wife / Wifes==========================")
for items in wifes:
    work = str((inheritence_amount * wifes_calcula) / grand_calcula)
    separation.append(float(work))
    print (items + " Share is " + work)

total = 0
for items in separation:
    total += items

print("")
print("=============Grand Total==========================")
print ("total: " + str(total))

