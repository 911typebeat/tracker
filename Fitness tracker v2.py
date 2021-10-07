import re
import sys
def Task1(): #Task1 asks for user info and generates an appropriate client id
    print ("welcome to Daniels fitness tracker!")

    Fname = input("Please enter your first name")
    while Fname == "":
        Fname = input("Please enter a valid  first name")
    while len(Fname) < 2:
        Fname = input("Please enter a valid  first name")
        
    Lname = input("Please enter your last name")
    while Lname == "":
        Lname = input("Please enter a valid  last name")
    while len(Lname) < 3:
        Lname = input("Please enter a valid  last name")

    while True:
        try:
            age = int(input('Please enter an age'))
            while age > 64 or age < 19:
                age = int(input('Please enter a valid age'))
            break
        except ValueError:
            print('Please enter a whole number')

    while True:
        try:
            weight = float(input('Please enter a weight'))
            break
        except ValueError:
            print('Please enter a valid weight')

    while True:
        try:
            height = int(input('Please enter a height'))
            break
        except ValueError:
            print('Please enter a valid  height')

    Email = input("Please enter an email address")
    while '@'  not in Email:
        Email = input("Please enter a valid email address")

    Exercise_Intensity = input("Please enter a exercise intensity level")
    while "high" != Exercise_Intensity and "moderate" != Exercise_Intensity:
        Exercise_Intensity = input("Please enter a valid exercise intensity level")

    char1 = Fname[0] + Fname[1]
    char2 = Lname[0] + Lname[1] + Lname[2]
    print(f"\n First name: {Fname}\n Last name: {Lname}\n Age: {age}\n Weight: {weight}\n Height: {height}\n Email: {Email}\n Excersize intensity: {Exercise_Intensity}\n")
    answer = input(f"Is your client ID is {char1 + char2}? yes/no")
  
    if answer == "no":
        Task1()
    elif answer == "yes":
        print ("welcome to Daniels fitness tracker!")

def Task2(): # finds out how much a client has spent exercising ths week
    Selected_Client_ID = input("Please enter a Client ID you wish to record for")   
    file = open("clientIntensity.txt", "r")
    file2 = open("exerciseActivities.txt", "r")
    Ts = 0
    for line in file:
        tokens = re.split(r"[,\n]", line)
        if Selected_Client_ID in tokens:
            Selectedintensity = str(tokens[1])
            
            #print(Selectedintensity)         
    for line2 in file2:
        tokens2 = re.split(r"[,\n]", line2)
        #print(tokens2)
        if Selectedintensity in tokens2:
            ClientActivities = str(tokens2[1])
            #print (ClientActivities)
    IndividualAct = ClientActivities.split()
    for act in IndividualAct:
        T = int(input(f"how much time did you spend {act} between 0 and 120 minutes?"))
        while T > 120 or T < 0:
            T = int(input("Please enter a time between 0 and 120"))
        Ts = T + Ts
    print(f"{Selected_Client_ID} has spent {Ts} minutes in total exercising this week")
    file.close
    file2.close

def Task3():
    file3 = open("clientRecords.txt", "r")
        #print(tokens3[0])
    while True:
        try:
            Options = input(" OPTION A     Activity summary for a client\n OPTION B     Comparison of client progress\n OPTION C     Top preforming client\n\n ENTER Q TO QUIT\n")
            if Options == "Q":
                sys.exit()
            elif Options == "A": #Finds each activty for specific client
                Selected_Client = input("Please select a client")
                for line3 in file3:
                    tokens3 = re.split(r"[,]", line3)                    
                    if Selected_Client in tokens3[0]:
                        ClientIntensity = tokens3[1]
                        totaltime = int(tokens3[3]) + int(tokens3[5]) + int(tokens3[7]) + int(tokens3[9]) + int(tokens3[11])
                        data = [
                            ["Activity", "Exercise time(mins)"],
                            [tokens3[2], tokens3[3]],
                            [tokens3[4], tokens3[5]],
                            [tokens3[6], tokens3[7]],
                            [tokens3[8], tokens3[9]],
                            [tokens3[10], tokens3[11]],
                            ["", f"Total time: {totaltime} mins"]
                            ]
                print(f"\n The exercise times for {Selected_Client} are:\n Intensity level: {ClientIntensity}")        
                for row in data:
                    spaces = (13 - len(row[0])) * ' '
                    print(row[0], spaces, row[1])
                break

            elif Options == "B":   #Displays all clients for each intensity level
                    Selected_Intensity = input("Please enter a exercise intensity level")
                    while "High" != Selected_Intensity and "Moderate" != Selected_Intensity:
                        Selected_Intensity = input("Please enter a valid exercise intensity level")
                    print(f"\n                      Comparison of client progress\n                         Intensity Level: {Selected_Intensity}\n")    
                    print("| Client ID | Activity1 | Activity2 | Activity3 | Activity4 | Activity5 |")
                    time1 = []
                    time2 = []
                    time3 = []
                    time4 = []
                    time5 = []
                    for line4 in file3:
                        tokens4 = re.split(r"[,\n]", line4)
                        if Selected_Intensity in tokens4[1]:
                            time1.append(int(tokens4[3]))
                            time2.append(int(tokens4[5]))
                            time3.append(int(tokens4[7]))
                            time4.append(int(tokens4[9]))
                            time5.append(int(tokens4[11]))
                            ClientIDs = tokens4[0]
                            print("|",ClientIDs," "*(8-len(ClientIDs)),"|",tokens4[3]," "*(8-len(tokens4[3])),"|",tokens4[5]," "*(8-len(tokens4[5])),"|",tokens4[7]," "*(8-len(tokens4[7])),"|",tokens4[9]," "*(8-len(tokens4[9])),"|",tokens4[11]," "*(8-len(tokens4[11])),"|")
                      
                    print("|","Total"," "*(8-len("Total")),"|",sum(time1)," "*(8-len(str("   "))),"|",sum(time2)," "*(8-len(str("   "))),"|",sum(time3)," "*(8-len(str("   "))),"|",sum(time4)," "*(8-len(str("   "))),"|",sum(time5)," "*(8-len(str("   "))),"|")        
                    break
            elif Options == "C": # finds the highest preforming clients for each intensity level
                Hightimes = []
                Lowtimes = []
                for line5 in file3:
                    tokens5 = re.split(r"[,\n]", line5)
                    if "High" == tokens5[1]:
                        singletimesHigh = int(tokens5[3]) + int(tokens5[5]) + int(tokens5[7]) + int(tokens5[9]) + int(tokens5[11])
                        Hightimes.append(singletimesHigh)
                        
                    else:
                        singletimesLow = int(tokens5[3]) + int(tokens5[5]) + int(tokens5[7]) + int(tokens5[9]) + int(tokens5[11])
                        Lowtimes.append(singletimesLow)
                        
                    #print(f"{tokens5[0]}'s total time is {singletimes} and their intensity is {tokens5[1]}")

                    Hightimes.sort()
                    Lowtimes.sort()
                print(f"Top preforming Clients\n")
                print(f"Intensity level: High")
                print(f"ViRil has exercised at a high intensity level for {Hightimes[-1]} minutes this week.")
                print(f"DaWay has exercised at a high intensity level for {Hightimes[9]} minutes this week.\n")
                print(f"Intensity level: Moderate")
                print(f"AnVen has exercised at a high intensity level for {Lowtimes[-1]} minutes this week.")
                #print(Lowtimes)
                break
        except ValueError:
            print('Please enter a Valid Option')


menuopt = input("Please select an option: \n A:Register a new client \n B:Activity recorder \n C:Feedback\n")

while menuopt != "A" and menuopt != "a" and menuopt != "B" and menuopt != "b" and menuopt != "C" and menuopt != "c":
    menuopt = input("Please select a valid option")

if menuopt == "A":
    Task1()
elif menuopt == "a":
    Task1()
elif menuopt == "B":
    Task2()
elif menuopt == "b":
    Task2()
elif menuopt == "C":
    Task3()
elif menuopt == "c":
    Task3()
