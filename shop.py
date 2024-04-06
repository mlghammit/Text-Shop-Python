

def priceList():
    #Inputing all price values for items
    SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]] 
    HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
    CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]] 
    MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]] 
    RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
    GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
    PSU = [['1', 'Corsair RM750', 164.99]]
    CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
    PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]

    return SSD, HDD, CPU, MOTHERBOARD, RAM, GRAPHICS_CARD, PSU, CASE, PREBUILTS


#Quick welcome message
print("Welcome to my PC shop!\n")


def pickItems():
    #Importing the list of items from def pricelist()
    SSD, HDD, CPU, MOTHERBOARD, RAM, GRAPHICS_CARD, PSU, CASE, PREBUILTS = priceList()

    #Making variables global 
    customTotalPrice = 0
    preBuiltTotalPrice = 0

    #This makes a set for itemPrice, this will store all totals made
    itemPrice = []

    while (True):

        #Main menu asking what the customer would like to purchase
        mainpage = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
        #This line ensures that it only accepts valid inputs, if not it asks again
        while mainpage not in ['1', '2', '3']: 
            mainpage = input ("\nWould you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")

        #Now we are askin1g for input from mainpage, if 1 goes custom, if 2 prebuilt, if 3 checkout
        if mainpage == '1':
            
            #Defining price for custom built PC
            customTotalPrice = 0
        
            print("\nGreat! Let's start building your PC!")

        
            print("\nFirst, let's pick a CPU.")
            #This now pulls from the CPU area in priceList
            #Prints out variable in 0, 1, and 2 slot. 
            for cpu in CPU:
                print(cpu[0], ":", cpu[1] + ",", "$" + str(cpu[2])) 

            #Again asking for a valid input 
            cpuPurchase = input("Choose the number that corresponds with the part you want: ")
            while cpuPurchase not in ['1', '2']:
                cpuPurchase = input("Choose the number that corresponds with the part you want: ")

            #Now if 1 adds to total and then leads to asking for a compatiable motherboard
            if cpuPurchase == "1":
                customTotalPrice += 499.99
                #Now we ensure that CPU can be paired wiht a compatiable motherboard
                #As cpu 1 is ONLY compatiable with motherboard 2 that is the only option
                print("\nNext, let's pick a compatiable motherboard.")

                for motherboard in MOTHERBOARD:
                    if motherboard[0] == '2':
                        print(motherboard[0], ":", motherboard[1] + ",", "$" + str(motherboard[2]))

                motherboardPurchase = input("Choose the number that corresponds with the part you want: ")

                while motherboardPurchase not in ['2']:
                    motherboardPurchase = input("Choose the number that corresponds with the part you want: ")

                if motherboardPurchase == "2":

                    customTotalPrice += 262.30
                    
            else: # Now we go to if cpuPurchase == 2 which only shows motherboard option 1
                customTotalPrice += 312.99
                
                print("\nNext, let's pick a compatiable motherboard.")

                for motherboard in MOTHERBOARD:
                    if motherboard[0] == '1':
                        print(motherboard[0], ":", motherboard[1] + ",", "$" + str(motherboard[2]))

                motherboardPurchase = input("Choose the number that corresponds with the part you want: ")

                while motherboardPurchase not in ['1']:
                    motherboardPurchase = input("Choose the number that corresponds with the part you want: ")

                if motherboardPurchase == "1":

                    customTotalPrice += 197.46

            #At this point for the rest of customBuild repeats, 
            print("\nNext, let's pick your RAM.")
            for ram in RAM:
                print(ram[0], ":", ram[1] + ",", "$" + str(ram[2]))                
            ramPurchase = input("Choose the number that corresponds with the part you want: ")
            while ramPurchase not in ["1", "2",]:
                ramPurchase = input("Choose the number that corresponds with the part you want: ")
            if ramPurchase == "1":
                customTotalPrice += 82.99
            else:
                customTotalPrice += 174.99

            print("\nNext, let's pick your PSU.")
            for psu in PSU:
                print(psu[0], ":", psu[1] + ",", "$" + str(psu[2]))
            psuPurchase = input("Choose the number that corresponds with the part you want: ")
            while psuPurchase not in ["1"]:
                psuPurchase = input("Choose the number that corresponds with the part you want: ")
            if psuPurchase == "1":
                customTotalPrice += 164.99

            print("\nNext, let's pick your case.")
            for case in CASE:
                print(case[0], ":", case[1] + ",", "$" + str(case[2]))
            casePurchase = input("Choose the number that corresponds with the part you want: ")
            while casePurchase not in ["1", "2"]:
                casePurchase = input("Choose the number that corresponds with the part you want: ")
            if casePurchase == "1":
                customTotalPrice += 149.99
            else:
                customTotalPrice += 149.99

            #Now we have the option to NOT seleect SSD
            #Simply allow X/x and do not increase price
            #We are gonna make it None so we are able to check for it! 
            print("\nNext, let's pick your SSD (optional, but you must have at least one SDD or HDD). ")
            for ssd in SSD:
                print(ssd[0], ":", ssd[1] + ",", "$" + str(ssd[2]))
            ssdPurchase = input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
            while ssdPurchase not in ["1", "2", "3", "X", "x"]:
                ssdPurchase = input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
            if ssdPurchase == "1":
                customTotalPrice += 69.99
  
            elif ssdPurchase == "2":
                customTotalPrice += 93.99
  
            elif ssdPurchase == "3":
                customTotalPrice += 219.99

            else:
                ssdPurchase = None
 

            print("\nNext let's pick an HDD (optional, but you must have at least one SSD or HDD).")            
            for hdd in HDD:
                print(hdd[0], ":", hdd[1] + ",", "$" + str(hdd[2]))
            hddPurchase = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
            
            if ssdPurchase == None: #Checking if customer didn't buy SSD, which cuts off option to not buy HDD
                while hddPurchase not in ['1', '2']:
                    hddPurchase = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
                if hddPurchase == '1':
                    customTotalPrice += 106.33
         
                elif hddPurchase == '2':
                    customTotalPrice += 134.33
  
                    
            if ssdPurchase != None: #Now checks if customer BOUGHT ssd which allows option to not buy HDD
                while hddPurchase not in ['1', '2', 'X', 'x']:
                    hddPurchase = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
                if hddPurchase == '1':
                    customTotalPrice += 106.33
       
                elif hddPurchase == '2':
                    customTotalPrice += 134.33
     
                else:
                    customTotalPrice += 0


            #Graphics card is optional so we allow X/x as a possibity.
            print("\nFinally, let's pick your graphics card (or X to not get a graphics card).")
            for graphicsCard in GRAPHICS_CARD:
                print(graphicsCard[0], ":", graphicsCard[1] + ",", "$" +  str(graphicsCard[2]))
            graphicsCardPurchase = input ("Choose the number that corresponds with the part you want: ")
            while graphicsCardPurchase not in ["1", "x", "X"]:
                graphicsCardPurchase = input ("Choose the number that corresponds with the part you want: ")
            if graphicsCardPurchase == "1":
                customTotalPrice += 539.99
    
            else: 
                customTotalPrice += 0
      

            #Using the append function we add the customTotalPrice to set itemPrice.

            itemPrice.append(customTotalPrice)

            #Spitting out the total price for custom build

            print("\nYou have selected all of the required parts! Your total for this PC is $ %0.2f\n" % (customTotalPrice))
        




        elif mainpage == "2":
            #Defining preBuilt price
            preBuiltTotalPrice = 0

            print("\nGreat! Let's pick a pre-built PC!")
            print("\nWhich prebuilt would you like to order?")
            
            #We don't need to import prebuilts again 
            #For prebuilt exact same process as custom code just one option
            for preBuilt in PREBUILTS:
                print(preBuilt[0], ":", preBuilt[1] + ",", "$" + str(preBuilt[2]))
            preBuiltPurchase = input("Choose the number that corresponds with the part you want: ")
            while preBuiltPurchase not in ["1", "2", "3"]:
                preBuiltPurchase = input("Choose the number that corresponds with the part you want: ")
            if preBuiltPurchase == "1":
                preBuiltTotalPrice += 3699.99
            elif preBuiltPurchase == '2':
                preBuiltTotalPrice += 2839.99
            else:
                preBuiltTotalPrice += 1099.99
            
            #We add the price of what customer selected to the set of itemPrice
            itemPrice.append(preBuiltTotalPrice)
            
            #Spitting out the total price for prebuilt

            print("\nYour total price for this prebuilt is $%0.2f\n" % (preBuiltTotalPrice))
    


        elif mainpage == "3":

            #Now we are printing all variables in the set {itemPrice}
            #Then we end the function
            print(f"{itemPrice}\n")
            break


pickItems()
