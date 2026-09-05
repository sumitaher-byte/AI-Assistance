def log(txt):
    file = open(r"D:\Work\Projects\AI Assistance\AI Assistance\log.txt" , "a")
    file.write(txt+"\n")
    file.close()


log("Program started...")


import datetime
import platform
import webbrowser
import os
import json
log("Importing Done...")


with open(r"D:\Work\Projects\AI Assistance\AI Assistance\config.json" , "r") as file:
    data = file.read()
data = json.loads(data)
log("Read data from config...")

print("==========\n  JARVIS  \n==========")
print("Hello " ,data["user_name"], "Sir, Jarvis is here.")
log("Greeted user...")


while True:
    user = input("User:-")
    if user.lower() in ("hi","hello"):
        print("Hello", data["user_name"], "Sir")
        log("Greted user...")

    elif user.lower() == "date":
        print(datetime.date.today())
        log("date task ...")
    elif user.lower() == "time":
        print(datetime.datetime.now().strftime("%I:%M %p"))
        log("time task ...")
    elif user.lower() == "day":
        print(datetime.datetime.now().strftime("%A"))
        log("day task...")


    elif user.lower() == "calculate":
        oprator = input("Enter oprator:-")
        n1 = float(input('Enter No.1:-'))
        n2 = float(input('Enter No.2:-'))
        if oprator == "+":
            print(n1 + n2)
        elif oprator == "-":
            print(n1 - n2)
        elif oprator == "*":
            print(n1 * n2)
        elif oprator == '/':
            print(n1 / n2)
        else:
            print("Something Went Wrong")
        log("Calculation Done...")

    
    
    elif user.lower() == "open youtube":
        print("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
        log("Open Youtube ...")
    elif user.lower() == "open calculator":
        print("Opening Calsi")
        os.system("start calculator:")
        log("open calculator...")
    elif user.lower() == "open game":
        os.startfile("D:\Games\steam unlocked\Games\The.Farmer.Was.Replaced.v2026.04.21\The.Farmer.Was.Replaced.v2026.04.21\TheFarmerWasReplaced.exe")
        log("Open Game...")


    elif user.lower() == "info":
        print('os_name = ',platform.system())
        print('os_version = ',platform.version())
        print("os_release = ",platform.release())
        print("machine = ",platform.machine())
        print("processor = ",platform.processor())
        log("Printed System Info...")


    elif user.lower() == "help":
        print("Commands\nhi, hello  #greetings\ndate  #print date\ntime   #print time\nday     #print day\nhelp   #print guide\nexit, quit, end    #end the program")
        print("info    #gives info about device\ncalculate    #opens callculator\poprators are ("+","-","*","/")")
        log("Printed halp menu...")

    elif user.lower() in ("exit", "quit", "end"):
        log("program ended...")
        break
        

    else:
        print("Sorry Sir, I am under devlopment. Don't have ans for this.")
        log("no data for ans...")
    