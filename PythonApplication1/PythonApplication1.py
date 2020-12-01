
import random

version = input("Please choose version write 'En'/ Prosze wybierz wersje napisz 'Pl': ") #choose version EN/PL
version = version.capitalize() #large input string does not matter
while (version != "En") and ( version != "Pl"): #for sure to right answer
    version = input("error, error, please write 'En'/ wykryto blad, prosze wpisz 'Pl': ") 
    version = version.capitalize() 

if version == "En":
    answer = "yes"
    WN = 0
    print ("Hello, \n How are You? Game choose randomly number, and your job is gussed it. Have fun ;)") #welcome
    while answer == "yes": #loop to restart game
        a = random.randint(1,500)
        b = random.randint(500,1000)    
        SN = random.randint(a, b) #SecretNumber randomly chosen
        #print (SN)

        print ("try to guess integer from range", a, "to", b)# print the range
        while WN != SN:
            WN = int(input("try to guess the number: ")) #WrittenNumber  
            if(WN == SN):   #loop repeat game and good/bad number
                print("Great! You got it!")   
                answer = input("Do You want to repeat? Write yes or no: ") 
                answer = answer.lower()
                while (answer != "yes") and (answer != "no"): #for sure to right answer
                        answer = input("error, error, please write 'yes' or 'no'") 
                        answer = answer.lower()

                if (answer == "yes"): 
                    continue
                elif (answer == "no"): 
                    break

            elif(WN < SN):
                print ("error, Secret Number is bigger, try again") 
            elif(WN > SN):
                print ("error, Secret Number is smaller, try again") 
            else:
                print ("error, try again") 

elif (version == "Pl"):
    odpowiedz = "tak"
    WL = 0
    print ("Czesc ;) \n Gra polega na odgadnieciu wylosowanej losowo liczby. Milej zabawy ;)")    
    while odpowiedz == "tak":
        a = random.randint(1,500)
        b = random.randint(500,1000)
    
        SL = random.randint(a, b) #SekretnaLiczba
        #print (SL)

        print ("sprobuj zgadnac liczbe calkowita z zakresu od", a, "do", b)#
        while WL != SL:
            WL = int(input("sprobuj zgadnac liczbe: ")) #WpisanaLiczba  #
            if(WL == SL):
                print("super! Udalo Ci sie!")   #
                odpowiedz = input("czy chcesz zagrac ponownie? Wpisz tak lub nie: ") #
                odpowiedz = odpowiedz.lower()
                while (odpowiedz != "tak") and (odpowiedz != "nie"): #for sure to right answer
                    odpowiedz = input("error, error, wykryto blad, prosze wpisz 'tak' lub 'nie'") 
                    odpowiedz = odpowiedz.lower()

                if (odpowiedz == "tak"): #
                    continue
                elif (odpowiedz == "nie"): #
                    break

            elif(WL < SL):
                print ("blad, ukryta liczba jest wieksza, sprobuj ponownie") #
            elif(WL > SL):
                print ("blad, ukryta liczba jest mniejsza, sprobuj ponownie") #
            else:
                print ("error, wykryto blad, sprobuj ponownie") #