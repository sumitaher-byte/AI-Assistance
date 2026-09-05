
import datetime
import platform

print("==========\n  JARVIS  \n==========")
print("Hello Sir, Jarvis is here.")


while True:
    user = input("User:-")
    if user.lower() in ("hi","hello"):
        print("Hello Sir")
    elif user.lower() == "date":
        print(datetime.date.today())
    elif user.lower() == "time":
        print(datetime.datetime.now().strftime("%I:%M %p"))
    elif user.lower() == "day":
        print(datetime.datetime.now().strftime("%A"))
    elif user.lower() in ("calculate"):
        oprator = input("Enter oprator:-")
        n1 = input('Enter No.1:-')
        n2 = input('Enter No.2:-')
        if 
    elif user.lower() == "info":
        print('os_name = ',platform.system())
        print('os_version = ',platform.version())
        print("os_release = ",platform.release())
        print("machine = ",platform.machine())
        print("processor = ",platform.processor())
    elif user.lower() == "help":
        print("Commands\nhi, hello  #greetings\ndate  #print date\ntime   #print time\nday     #print day\nhelp   #print guide\nexit, quit, end    #end the program")
        print("info    #gives info about device")
    elif user.lower() in ("exit", "quit", "end"):
        break
    else:
        print("Sorry Sir, I am under devlopment. Don't have ans for this.")
    