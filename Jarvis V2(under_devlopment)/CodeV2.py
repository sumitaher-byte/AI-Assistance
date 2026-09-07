#File Adress
json_file = r"D:\Work\Projects\AI Assistance\AI Assistance\Jarvis V2(under_devlopment)\config.json"
log_file = r"D:\Work\Projects\AI Assistance\AI Assistance\Jarvis V2(under_devlopment)\log.txt"



#Imports
import datetime
import platform
import webbrowser
import os
import json


#clear data in log file
def clear_log_file():
    with open(log_file,"w") as file:
        file.write("file clear...\n")
    


#Adding logs to log_file
def log(txt):
    with open(log_file,"a") as file:
        file.write(txt + "\n")


def router(user):
    if user in command:
        command[user]["handler"]()
    else:
        unknown_command()


def unknown_command():
    print("Command Doesn't exist")



def greeting():
    print("Hello", data["user_name"], "Sir")
    log("Greted user...")


def date():
    print(datetime.date.today())
    log("date task ...")


def time():
    print(datetime.datetime.now().strftime("%I:%M %p"))
    log("time task ...")


def day():
    print(datetime.datetime.now().strftime("%A"))
    log("day task...")


    #Inbuilt Simple Calculator
def calculator():
    operator = input("Enter oprator:-").strip()

    while True:
        try:
            n1 = float(input('Enter No.1.').strip())
            break
        except ValueError:
            print("No is not Valid")

    while True:
        try:
            n2 = float(input('Enter No.2:-').strip())
            break
        except ValueError:
            print("No is not Valid")

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
def open_link():
    link = input("Entre link:-")
    print("Opening ", link)
    webbrowser.open(link)
    log(("Open link..."))


def open_application():
    name = input("Entre app name:-")
    print("Opening", name)
    os.system("start " + name + ":")
    log("open app ...")


def open_file():
    file_addr = str(input("Entre file addr:-"))
    os.startfile(file_addr)
    log("Open file...")


    #print system info
def info():
    print('os_name = ',platform.system())
    print('os_version = ',platform.version())
    print("os_release = ",platform.release())
    print("machine = ",platform.machine())
    print("processor = ",platform.processor())
    log("Printed System Info...")


    #detail operating sommands and manual
def help():
    for key , sub_dic in command.items():
        print(key , " - " , sub_dic["description"])      
    log("Printed halp menu...")


def end_program():
    print("Bye Sir")
    exit()




command = {
    "hi": {
        "handler": greeting,
        "description": "Greet the user"
    },
    "hello": {
        "handler": greeting,
        "description": "Greet the user"
    },
    "date": {
        "handler": date,
        "description": "Show today's date"
    },
    "time": {
        "handler": time,
        "description": "Show the current time"
    },
    "day": {
        "handler": day,
        "description": "Show today's day"
    },
    "calculate": {
        "handler": calculator,
        "description": "Open the calculator"
    },
    "open link": {
        "handler": open_link,
        "description": "Open a web link"
    },
    "open app": {
        "handler": open_application,
        "description": "Open an application"
    },
    "open file": {
        "handler": open_file,
        "description": "Open a file"
    },
    "info": {
        "handler": info,
        "description": "Show system information"
    },
    "help": {
        "handler": help,
        "description": "Show available commands"
    },
    "exit": {
        "handler": end_program,
        "description": "Exit Jarvis"
    }
}


clear_log_file()


log("Program Started")


#Reads Json file for config
with open(json_file , "r") as file:
    data = file.read()
data = json.loads(data)
log("Readed data from config...")


#Print hading and great User
print("==========\n  JARVIS  \n==========")
print("Hello " ,data["user_name"], "Sir, Jarvis is here.")
log("Greeted user...")




while True:
    user = input("User:-").strip().lower()
    router(user)