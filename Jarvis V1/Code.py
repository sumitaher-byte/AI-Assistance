#File address
json_file = r"D:\Work\Projects\AI Assistance\AI Assistance\Jarvis V1\config.json"
log_file = r"D:\Work\Projects\AI Assistance\AI Assistance\Jarvis V1\log.txt"
game = r"D:\Games\steam unlocked\Games\The.Farmer.Was.Replaced.v2026.04.21\The.Farmer.Was.Replaced.v2026.04.21\TheFarmerWasReplaced.exe"

#Imports
import datetime
import platform
import webbrowser
import os
import json


#Adding logs to log_file
def log(txt):
    with open(log_file,"a") as file:
        file.write(txt + "\n")


log("Program started...")


#Reads Json file for config
with open(json_file , "r") as file:
    data = file.read()
data = json.loads(data)
log("Read data from config...")


#Print hading and great User
print("==========\n  JARVIS  \n==========")
print("Hello " ,data["user_name"], "Sir, Jarvis is here.")
log("Greeted user...")


#Take user input
while True:
    user = input("User:-").strip()


    #Replay to hi hallo
    if user.lower() in ("hi","hello"):
        print("Hello", data["user_name"], "Sir")
        log("Greted user...")

    #Date Time Day
    elif user.lower() == "date":
        print(datetime.date.today())
        log("date task ...")
    elif user.lower() == "time":
        print(datetime.datetime.now().strftime("%I:%M %p"))
        log("time task ...")
    elif user.lower() == "day":
        print(datetime.datetime.now().strftime("%A"))
        log("day task...")


    #Inbuilt Simple Calculator
    elif user.lower() == "calculate":
        operator = input("Enter oprator:-").strip()

        while True:
            try:
                n1 = float(input('Enter No.1:-').strip())
                break
            except ValueError:
                print("No is not Valid")

        while True:
            try:
                n2 = float(input('Enter No.2:-').strip())
                break
            except ValueError:
                print("Entre Valid No.:-")

        if operator == "+":
            print(n1 + n2)
        elif operator == "-":
            print(n1 - n2)
        elif operator == "*":
            print(n1 * n2)
        elif operator == '/':
            if n2 == 0:
                print("Cant take 0 as denominator")
            else:
                print(n1 / n2)

        else:
            print("Something Went Wrong")
        log("Calculation Done...")

    

    #opens app and files
    elif user.lower() == "open youtube":
        print("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
        log("Open Youtube ...")
    elif user.lower() == "open calculator":
        print("Opening Calsi")
        os.system("start calculator:")
        log("open calculator...")
    elif user.lower() == "open game":
        os.startfile(game)
        log("Open Game...")


    #print system info
    elif user.lower() == "info":
        print('os_name = ',platform.system())
        print('os_version = ',platform.version())
        print("os_release = ",platform.release())
        print("machine = ",platform.machine())
        print("processor = ",platform.processor())
        log("Printed System Info...")


    #detail operating sommands and manual
    elif user.lower() == "help":
        print("Commands\nhi, hello  #greetings\ndate  #print date\ntime   #print time\nday     #print day\nhelp   #print guide\nexit, quit, end    #end the program")
        print("info    #gives info about device\ncalculate    #opens callculator\noprators are ("+","-","*","/")")
        log("Printed halp menu...")


    #Exit 
    elif user.lower() in ("exit", "quit", "end"):
        log("program ended...")
        break
        

    #error handling
    else:
        print("Sorry Sir, I am under devlopment. Don't have ans for this.")
        log("no data for ans...")