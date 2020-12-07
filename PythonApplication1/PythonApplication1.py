
import random
import time
import math

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%Y/%m/%d | %H:%M", named_tuple)
#print(time_string)
version = input("Hide numbers game / ukryte liczby\n\nPlease choose version write \
'En'/ \nProsze wybierz wersje napisz 'Pl': ") #choose version EN/PL
version = version.capitalize() #large input string does not matter
print()
while (version != "En") and ( version != "Pl"): #for sure to right answer
    version = input("error, error, please write 'En'/ wykryto blad, prosze wpisz 'Pl': ") 
    print()
    version = version.capitalize() 

#english version
if version == "En":
    answer = "yes"
    print ("Hello,\nHow are You? Game choose randomly number, \
and your job is gussed it.\nIf You need a help \
(just 2 times avilable) write 'help'.\nHave fun ;)") #welcome
   
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
        Words = []

        print ("\nTry to guess integer from range", a, "to", b)# print the range
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
                elapsed_time = int(elapsed_time)
                print("\nGreat! You got it!\nYour time is", elapsed_time, "seconds\nYou writed:", WriteNumber, "\nYou guess after",Guessing,"guess")                
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
                    Save = ( str(Guessing) + " | " + str(elapsed_time)\
                       + " | "  + Name + " | " + time_string + " | " + str(SN)) 
                    Save = str(Save)
                    Save = Save + ("\n")
    #save in file
                    with open(filepath, "a") as f:
                        f.write(Save) #write in the end thank "a"
    #list
                    with open(filepath, "r") as f:
                        lines = f.readlines() #create list
                        Place = 0

                        for line in lines:
                            line = line[:-1]
                            SplitLine = line.split(" | ")
                            newLine = [[int(SplitLine[0])] + [int(SplitLine[1])] + SplitLine[2:]]
                            Words.extend(newLine)

                        Save = []
                        time_string = time_string.split(" | ")
                        Save = [Guessing, int(elapsed_time)]
                        Save.append (Name)
                        Save.append (time_string[0])
                        Save.append (time_string[1])
                        Save.append(str(SN))
                        Words.sort()        #sort list
                        number = 0 

                        for Result in Words: 
                            number +=1

                    Place = Words.index(Save)+ 1 #how place
                    print("\nYou have", Place , "place among", number, "results")                    
#ranking 1-10
                print("\n10 the best results is: \nplace.....Guess | Time | Name | Day | Hour |  Hide number") #ranking 1-10
                number = 0
                for result in Words[0:10]:
                    number +=1
                    print(str(number) + "....." + str(result[0]) + " | " + str(result[1]) + " | " + str(result[2]) + " | " + str(result[3]) + " | " + str(result[4]) + " | " + str(result[5]))                                       
#restart
                answer = input("\nDo You want to repeat? Write yes or no: ") 
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
    print ("Czesc ;)\nGra polega na odgadnieciu wylosowanej losowo liczby.\n\
Jesli potrzebujesz pomocy (tylko dwa razy mozliwe) napisz 'pomoc'.\nMilej zabawy ;)") 
    
    while odpowiedz == "tak":
#ustawienia wstepne
        a = random.randint(1,500)
        b = random.randint(500,1000)   
        SL = random.randint(a, b) #SekretnaLiczba
        #print (SL)
        SciezkaPliku = "wyniki.txt"
        imie = 0
        WpisaneLiczby = []
        WL = 0
        odgadywanie = 0
        LiczPomoc = 0
        ZapisWyniku = 0
        wyrazy = []

        print("\nsprobuj zgadnac liczbe calkowita z zakresu od", a, "do", b)
        PoczatekCzasu = time.time()
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
                KoniecCzasu = int(KoniecCzasu)
                print("\nsuper! Udalo Ci sie!\nzajelo Ci to", KoniecCzasu, "sekund\nwpisales nastepujace liczby:", WpisaneLiczby,"\nzgadles po",odgadywanie,"probach")   
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
                    zapis = ( str(odgadywanie) + " | " + str(KoniecCzasu) + " | "  + imie + " | " + time_string + " | " + str(SL)) 
                    zapis = str(zapis)
                    zapis = zapis + ("\n")                    
    #zapisuje w pliku
                    with open(SciezkaPliku, "a", encoding="utf-8") as S: #encoding="utf-8" - by polskie znaki czytalo
                        S.write(zapis) #dopisuje na koncu dzieki "a"
    #lista
                    with open(SciezkaPliku, "r") as S:
                        wiersze = S.readlines() #utworz liste
                        miejsce = 0

                        for wiersz in wiersze:
                            wiersz = wiersz[:-1]
                            rozdzielonyWiersz  = wiersz.split(" | ")
                            nowyWiersz = [[int(rozdzielonyWiersz[0])] + [int(rozdzielonyWiersz[1])] + rozdzielonyWiersz[2:]]
                            wyrazy.extend(nowyWiersz)

                        zapis = []
                        time_string = time_string.split(" | ")
                        zapis = [ odgadywanie, int(KoniecCzasu)]
                        zapis.append (imie)
                        zapis.append (time_string[0])
                        zapis.append (time_string[1])
                        zapis.append(str(SL))
                        wyrazy.sort()    
                        liczba = 0     

                        for wynik in wyrazy: 
                            liczba +=1
                            
                        miejsce = wyrazy.index(zapis) + 1 #jakie miejsce
                        print("\nmasz", miejsce , "miejsce sposrod", liczba, "wynikow") #wyswietla ktore miejsce z ilu wynikow
#ranking 1-10
                print("\n10 najlepszych wynikow to: \n\nmiejsce.....liczba prob | czas | imie | data | godzina |  ukryty numer") #pokazuje ranking 1-10
                liczba = 0

                for wynik in wyrazy[0:10]: 
                    liczba += 1
                    print( str(liczba) + "....." + str(wynik[0]) + " | " + str(wynik[1]) + " | " + str(wynik[2])\
                    + " | " + str(wynik[3]) + " | " + str(wynik[4]) + " | " + str(wynik[5]))                                       
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
                   
"""  
wszystkie wyniki
                        for wynik in newS: 
                            print(wynik)
"""