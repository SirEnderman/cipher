import math
import random
import json

welcome = input("""Hello there! What would you like to do today?
1. Generate your very own CIPHER keys (generate)
2. View your CIPHER keys (view)
3. Encrypt a message using your CIPHER keys (encrypt)
4. Decrypt a message using your CIPHER keys (decrypt)
5. Log actions (log)
:""")


#-------------------------------------------------------KEY GENERATION-----------------------------------------------------------

if welcome == "generate" or welcome == "1":
    print("Generating your CIPHER keys!")
    firstkey = random.randrange(15,100)
    secondkey = random.randrange(101,179)
    
    privatekey1 = firstkey + secondkey + firstkey * secondkey / firstkey 
    privatekey2 = privatekey1 / firstkey * secondkey/ firstkey
    privatekey3 = privatekey2 * 17 + privatekey1 - firstkey
    privatekey4 = privatekey3 + 32 + privatekey1 * math.pow(firstkey,2)
    privatekey5 = 3 + firstkey / privatekey1 * secondkey
    privatekey6 = privatekey5/privatekey1 + 43 + privatekey2
    privatekey7 = privatekey6 * privatekey2 + 43 * firstkey + secondkey
    privatekey8 = privatekey7 * 2 / privatekey3 - secondkey
    privatekey9 = privatekey8 * privatekey2 + 4 * secondkey / firstkey
    privatekey10 = privatekey9 + 1 / privatekey2 * secondkey
    privatekey11 = privatekey10 - 50 * 12 /privatekey7 + 12
    privatekey12 = privatekey11 + privatekey1 - 100 + privatekey5 * 2
    privatekey13 = privatekey12 + privatekey4 * privatekey2 + 61
    privatekey14 = privatekey13 + privatekey6 - 12 * privatekey9 - 23
    privatekey15 = privatekey14 + 12 - math.pow(firstkey,2)
    privatekey16 = privatekey15 + firstkey * 2 - 34 - secondkey
    privatekey17 = privatekey16 / 32 * privatekey2 + 1
    privatekey18 = privatekey17 - privatekey13 * firstkey + 5
    privatekey19 = privatekey18 + privatekey10 * 2
    privatekey = privatekey19 + firstkey + secondkey + 694204204

    keys = {}
    keys["firstpubkey"] = firstkey
    keys["secondpubkey"] = secondkey
    keys["privkey"] = privatekey
    
#prints the cipher public and private keys

    print("")
    print("--------------------------------------------------------")
    print("All right, your public CIPHER keys are", firstkey,  "and", secondkey)
    print("")

    print("--------------------------------------------------------")
    print("Your private CIPHER key is",privatekey)
    print("")
    print("--------------------------------------------------------")
    print("Don't give your private CIPHER key to anyone, even your friends!")
    print("")

#stores the generated keys in keys.json

    with open('keys.json', 'w') as f:
        json.dump(keys, f) 
    print("--------------------------------------------------------")
    print("Keys saved to 'keys.json' sucessfully!")

    logs = open("logs.txt", "w")
    firstkey1 = str(firstkey)
    secondkey1 = str(secondkey)
    privatekey1 = str(privatekey)

    #saving to logs.txt

    logs.write("User Generated new CIPHER keys")
    logs.write(firstkey1)
    logs.write(secondkey1)
    logs.write(privatekey1)
    logs.close()

#--------------------------------------------------------KEY VIEWING-------------------------------------------------------------

if welcome == "view" or welcome == "2":

    f = open('keys.json')
    keys1 = json.load(f)
    keylist1 = keys1.values()
    keylist = list(keylist1)
    firstkey = keylist[0]
    secondkey = keylist[1]
    privatekey = keylist[2]

    print("Your public CIPHER keys are", firstkey ,"and", secondkey)
    print("Your private CIPHER key is", privatekey)

    #saving action to logs.txt

    logs = open("logs.txt", "w")
    firstkey1 = str(firstkey)
    secondkey1 = str(secondkey)
    privatekey1 = str(privatekey)
    
    logs.write("User Generated new CIPHER keys")
    logs.write(firstkey1)
    logs.write(secondkey1)
    logs.write(privatekey1)
    logs.close()

#---------------------------------------------------------ENCRYPTION-------------------------------------------------------------

if welcome == "encrypt" or welcome == "3":

    selectencrypt = input("""Choose an option
1. Input Public CIPHER keys
2. Use Public CIPHER keys saved on system
:""")

#--------------------------------------------------------PART B------------------------------------------------------------------

    if selectencrypt == "2":
        
        f = open('keys.json')
        keys1 = json.load(f)
        keylist1 = keys1.values()
        keylist = list(keylist1)
        firstkey = keylist[0]
        secondkey = keylist[1]
        privatekey = keylist[2]

        message = input(""" So you wanna encrypt? Type your message below
:""")

        g = 3
        numbers = []
    
        for letter in message:
            number = ord(letter) - 96 + g
            g = g + 2
            encryptednumber = number + privatekey + g
            numbers.append(encryptednumber)

        print("The encrypted message is", numbers)

        #storing message in logs.txt
    
        logs = open("logs.txt", "w")
        lognumbers = str(numbers)
        logs.write("User Encrypted")
        logs.write(lognumbers)
        logs.close()

#--------------------------------------------------------PART A---------------------------------------------------------------------

    if selectencrypt == "1":
        
        firstkey = int(input("Enter your first key:"))
        secondkey = int(input("Enter your second key:"))


        privatekey1 = firstkey + secondkey + firstkey * secondkey / firstkey 
        privatekey2 = privatekey1 / firstkey * secondkey/ firstkey
        privatekey3 = privatekey2 * 17 + privatekey1 - firstkey
        privatekey4 = privatekey3 + 32 + privatekey1 * math.pow(firstkey,2)
        privatekey5 = 3 + firstkey / privatekey1 * secondkey
        privatekey6 = privatekey5/privatekey1 + 43 + privatekey2
        privatekey7 = privatekey6 * privatekey2 + 43 * firstkey + secondkey
        privatekey8 = privatekey7 * 2 / privatekey3 - secondkey
        privatekey9 = privatekey8 * privatekey2 + 4 * secondkey / firstkey
        privatekey10 = privatekey9 + 1 / privatekey2 * secondkey
        privatekey11 = privatekey10 - 50 * 12 /privatekey7 + 12
        privatekey12 = privatekey11 + privatekey1 - 100 + privatekey5 * 2
        privatekey13 = privatekey12 + privatekey4 * privatekey2 + 61
        privatekey14 = privatekey13 + privatekey6 - 12 * privatekey9 - 23
        privatekey15 = privatekey14 + 12 - math.pow(firstkey,2)
        privatekey16 = privatekey15 + firstkey * 2 - 34 - secondkey
        privatekey17 = privatekey16 / 32 * privatekey2 + 1
        privatekey18 = privatekey17 - privatekey13 * firstkey + 5
        privatekey19 = privatekey18 + privatekey10 * 2
        privatekey20 = privatekey19 / 2 - 54678
        privatekey = privatekey20 + firstkey + secondkey - 54  

        message = input(""" So you wanna encrypt? Type your message below
:""")

        g = 3
        numbers = []
    
        for letter in message:
            number = ord(letter) - 96 + g
            g = g + 2
            encryptednumber = number + privatekey + g  
            numbers.append(encryptednumber)

        print("The encrypted message is", numbers)


        #storing message in logs.txt
    
        logs = open("logs.txt", "w")
        lognumbers = str(numbers)
        logs.write("User Encrypted")
        logs.write(lognumbers)
        logs.close()
        
#-------------------------------------------------------REENCRYPT--------------------------------------------------------------- 

    redecrypt = input("Do you want to decrypt this message?:")
    
    if redecrypt == "yes" or redecrypt == "true":

        g = 3
        decrypted = []
        
        for code in numbers:

            g = g + 2
            numbers = code - privatekey - g
            g = g - 2
            letter = numbers + 96 - g
            g = g + 2
            letterx = int(letter)
            letter2 = chr(letterx)
            decrypted.append(letter2)
            

        print("The Decrypted message is", decrypted)

#saving activity in logs.txt
        
        logs = open("logs.txt", "w")
        lognumbers = str(decrypted)
        logs.write("User Decrypted")
        logs.write(lognumbers)
        logs.close()
        
            

#---------------------------------------------------------DECRYPTION-------------------------------------------------------------

if welcome == "decrypt" or welcome == "4":

    f = open('keys.json')
    keys1 = json.load(f)
    keylist1 = keys1.values()
    keylist = list(keylist1)
    privatekey = keylist[2]
    numbers = []
    
    n = int(input("How many letters is your encrypted message?:"))
    n2 = ("Type your numbers below, one by one")

    for i in range(0, n):
        listinput = float(input("Enter the number here:"))
        numbers.append(listinput)

        g = 3
        decrypted = []
        
        for code in numbers:

            g = g + 2
            numbers = code - privatekey - g
            g = g - 2
            letter = numbers + 96 - g
            g = g + 2
            letterx = int(letter)
            letter2 = chr(letterx)
            decrypted.append(letter2)
            

    print("The Decrypted message is", decrypted)

        #saving activity in logs.txt
        
    logs = open("logs.txt", "w")
    lognumbers = str(decrypted)
    logs.write("User Decrypted")
    logs.write(lognumbers)
    logs.close()

#-------------------------------------------------------------LOGS----------------------------------------------------------

if welcome == "logs" or welcome == "5":
    logchoice = input(""" Choose an option
1. View last action
2. Clear log file
:""")

    if logchoice == "1":
        logs = open("logs.txt", "r")
        logs.close

    if logchoice == "2":
        file = open("logs.txt","r+")
        file.truncate(0)
        file.close()
        print("Logs cleared successfully!")



        

        
        
                      

    

        





    

    
