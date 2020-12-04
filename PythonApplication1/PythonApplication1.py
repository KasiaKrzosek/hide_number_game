
import random
import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%Y/%m/%d | %H:%M", named_tuple)
#print(time_string)
version = input("Hide numbers game / ukryte liczby\n\nPlease choose version write 'En'/ \nProsze wybierz wersje napisz 'Pl': ") #choose version EN/PL
version = version.capitalize() #large input string does not matter
print()
while (version != "En") and ( version != "Pl"): #for sure to right answer
    version = input("error, error, please write 'En'/ wykryto blad, prosze wpisz 'Pl': ") 
    version = version.capitalize() 


if version == "En":
    answer = "yes"
   
    print ("Hello,\nHow are You? Game choose randomly number, and your job is gussed it.\nIf You need a help (just 2 times avilable) write 'help'.\nHave fun ;)") #welcome
   
    while answer == "yes": #loop to restart game
#start setup         
        a = random.randint(1,500)
        b = random.randint(500,1000)    
        SN = random.randint(a, b) #SecretNumber randomly chosen
        #print (SN)
        CountHelp = 0
        filepath = "Results.txt"
        Guessing = 0
        Help = 0
        Name = 0
        WN = 0
        WriteNumber = []       
        SaveResults = 0
        print ()
        print ("Try to guess integer from range", a, "to", b)# print the range
        start_time = time.time()
#check number WN        
        while WN != SN:
            WN = input("Try to guess the number: ") #WrittenNumber  
            WriteNumber.append(WN)
            print("You writed:", WriteNumber, "range is from", a, "to", b)
            while WN.isdigit() == False: #if input is not integer   
#help
                WN = WN.lower()
                while (WN == "help") and (CountHelp == 1):
                    CountHelp += 1
                    Help = SN % 3
                    if Help == 0:
                        print("Number is divisible by 3")
                    else:
                        print ("Number is not divisible by 3")
    
                while (WN == "help") and (CountHelp < 1):
                    CountHelp += 1
                    Help = SN % 2
                    if Help == 0:
                        print("Number is not divisible by 2")
                    else:
                        print ("Number is divisible by 2")
#wrong number
                else:
                    Guessing +=1

                WN = input("Please, write a number: ")  
                WriteNumber.append(WN)
                print("You writed:", WriteNumber, "range is from", a, "to", b)                
    #change to integer            
            WN = int(WN)           
            Guessing +=1
#Congratulation
            if(WN == SN):   #loop repeat game and good/bad number
                elapsed_time = time.time() - start_time
                print()
                print("Great! You got it!\nYour time is", int(elapsed_time), "seconds\nYou writed:", WriteNumber, "\nYou guess after",Guessing,"guess")                
#save results
                SaveResults = input("Do You want to save your results? Please, write yes / no ") #ask
                SaveResults = SaveResults.lower()

                while (SaveResults != "yes") and (SaveResults != "no"): #error
                    SaveResults = input("error, error, please, write yes / no ")
                    SaveResults = SaveResults.lower()

                if SaveResults == "no":
                    print("results unsaved")
                else:
    #name, data
                    Name = input("Please, write your name: ")
                    Save = ( str(Guessing) + " | " + str(elapsed_time) + " | "  + Name + " | " + time_string + " | " + str(SN)) 
                    Save = str(Save)
                    Save = Save + ("\n")
    #save in txt
                    f = open(filepath, "a")
                    f.write(Save) #write in the end thank "a"
                    f.close()
    #list
                    f = open(filepath, "r")
                    lines = f.readlines() #create list
                    Place = 0
                    lines.sort() #sort list
                    #is some problem with sort
                    Place = lines.index(Save)+ 1 #jakie miejsce
                    print()
                    print("You have", Place , "place among", len(lines), "results") #wyswietla ktore miejsce z ilu wynikow
                    f.close()
#ranking 1-10
                print()
                print("10 the best results is: \n") #ranking 1-10
                print("Guess | Time | Name | Day | Hour |  Hide number")
                for Result in lines[0:10]: 
                    print(Result, end="")
#restart
                print()
                answer = input("Do You want to repeat? Write yes or no: ") 
                answer = answer.lower()

                while (answer != "yes") and (answer != "no"): #for sure to right answer
                        answer = input("error, error, please write 'yes' or 'no'") 
                        answer = answer.lower()

                if (answer == "yes"): 
                    continue
                elif (answer == "no"): 
                    break
#wrong number
            elif(WN < SN):
                print ("error, Secret Number is bigger, try again") 
            elif(WN > SN):
                print ("error, Secret Number is smaller, try again") 
            else:
                print ("error, try again") 

#wersja polska
elif (version == "Pl"):
    odpowiedz = "tak" #gra dziala, na koniec pytanie czy uruchomic ponownie

    print ("Czesc ;)\nGra polega na odgadnieciu wylosowanej losowo liczby.\nJesli potrzebujesz pomocy (tylko dwa razy mozliwe) napisz 'pomoc'.\nMilej zabawy ;)") 
    
    while odpowiedz == "tak":
#ustawienia wstepne
        a = random.randint(1,500)
        b = random.randint(500,1000)   
        SL = random.randint(a, b) #SekretnaLiczba
        print (SL)
        SciezkaPliku = "wyniki.txt"
        imie = 0
        WpisaneLiczby = []
        PoczatekCzasu = time.time()
        WL = 0
        odgadywanie = 0
        LiczPomoc = 0
        ZapisWyniku = 0
        print("\nsprobuj zgadnac liczbe calkowita z zakresu od", a, "do", b)

# sprawdzLiczbe(WL)          
        while WL != SL:  
            WL = input("sprobuj zgadnac liczbe: ") #WpisanaLiczba  
            WpisaneLiczby.append(WL)
            print("wpisales nastepujace liczby:", WpisaneLiczby, "zakres to od", a, "do", b)
            while WL.isdigit() == False: #jesli wpisana jest liczba   
    #pomoc           
                WL = WL.lower()     
                while (WL == "pomoc") and (LiczPomoc == 1):
                    LiczPomoc += 1
                    pomoc = SL % 3

                    if pomoc == 0:
                        print("liczba jest podzielna przez 3")
                    else:
                        print ("liczba jest niepodzielna przez 3")
    
                while (WL == "pomoc") and (LiczPomoc < 1):
                    LiczPomoc += 1
                    pomoc = SL % 2

                    if pomoc == 0:
                        print("liczba jest podzielna przez 2")
                    else:
                        print ("liczba jest niepodzielna przez 2")
    #nie liczba
                else:
                    odgadywanie +=1

                WL = input("prosze wpisz liczbe: ")  
                WpisaneLiczby.append(WL)
                print("wpisales nastepujace liczby:", WpisaneLiczby, "zakres to od", a, "do", b)                
    #wpis na liczbe            
            WL = int(WL)           
            odgadywanie +=1
#gratulacje
            if(WL == SL):
                KoniecCzasu = time.time() - PoczatekCzasu
                print()
                print("super! Udalo Ci sie!\nzajelo Ci to", KoniecCzasu, "sekund\nwpisales nastepujace liczby:", WpisaneLiczby,"\nzgadles po",odgadywanie,"probach")   
#zapis wyniku
                ZapisWyniku = input("czy chcesz zapisac swoj wynik? napisz tak / nie ") #pytanie
                ZapisWyniku = ZapisWyniku.lower()

                while (ZapisWyniku != "tak") and (ZapisWyniku != "nie"): #blad
                    ZapisWyniku = input("error, error, napisz tak / nie ")
                    ZapisWyniku = ZapisWyniku.lower()

                if ZapisWyniku == "nie":
                    print("nie zapisano wyniku")
                else:
    #imie, dane
                    imie = input("wpisz swoje imie: ")
                    KoniecCzasu = int(KoniecCzasu)
                    zapis = ( str(odgadywanie) + " | " + str(KoniecCzasu) + " | "  + imie + " | " + time_string + " | " + str(SL)) 
                    zapis = str(zapis)
                    zapis = zapis + ("\n")
                     
                    #imie1 = imie + "\n" #przechodzi do kolejnej linijki
    #zapisuje w pliku
                    S = open(SciezkaPliku, "a", encoding="utf-8") #encoding="utf-8" - by polskie znaki czytalo
                    S.write(zapis) #dopisuje na koncu dzieki "a"
                    S.close()
    #lista
                    S = open(SciezkaPliku, "r")
                    wiersze = S.readlines() #utworz liste
                    miejsce = 00
                    wiersze.sort() #sortuje liste
                    #sortowanie ma problem nie bierze liczby jako liczby 100 jest mniejsze niz 2
                    miejsce = wiersze.index(zapis)+ 1 #jakie miejsce
                    print()
                    print("masz", miejsce , "miejsce sposrod", len(wiersze), "wynikow") #wyswietla ktore miejsce z ilu wynikow
                    S.close()
#ranking 1-10
                print()
                print("10 najlepszych wynikow to: \n") #pokazuje ranking 1-10
                print("liczba prob | czas | imie | data | godzina |  ukryty numer")
                for wynik in wiersze[0:10]: 
                    print(wynik, end="")                      
#ponowna gra
                print()
                odpowiedz = input("czy chcesz zagrac ponownie? Wpisz tak lub nie: ") 
                odpowiedz = odpowiedz.lower()
    
                while (odpowiedz != "tak") and (odpowiedz != "nie"): #blad
                    odpowiedz = input("error, error, wykryto blad, prosze wpisz 'tak' lub 'nie'") 
                    odpowiedz = odpowiedz.lower()

                if (odpowiedz == "tak"):  
                    continue
                elif (odpowiedz == "nie"): 
                    break
#inna liczba                
            elif(WL < SL):
                print ("blad, ukryta liczba jest wieksza, sprobuj ponownie") 
            elif(WL > SL):
                print ("blad, ukryta liczba jest mniejsza, sprobuj ponownie")  
                   
                
               
               