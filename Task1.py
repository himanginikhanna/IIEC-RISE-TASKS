import os
import pyttsx3 


pyttsx3.speak("Hello there , What is Your Name?.\n")
Name = input("Enter Your Name")
pyttsx3.speak("Hello {}".format(Name))
pyttsx3.speak("I am  Your Personal Desktop Assistant. I am here to assist you. Which Application You want me to launch for you?")
pyttsx3.speak("Here is the List of Applications from your system :")

print("**************APPLICATION MENU***************")
print(" \t\t App Store \n\t\t iTunes \n\t\t Safari \n\t\t Messages \n\t\t Facetime \n\t\t Mail \n\t\t Contacts \n\t\t Notes \n\t\t Keynote \n\t\t Numbers  \n\t\t Pages \n\t\t Calculator \n\t\t Whatsapp \n\t\t Terminal \n\t\t Siri \n\t\t Skype \n\t\t Teamviewer \n\t\t Pycharm \n\t\t Discord \n\t\t Visual Studio Code \n\t\t Photo Booth \n\t\t System Preferences")
print("*********************************************")

print("To Launch The Application write Application Name")
print("To Exit write Quit or Exit.")

while True:
    app_name = input("Enter Application Name")
    if(("App Store" in app_name) or ("App Store" in app_name) or ("Appstore" in app_name) or ("AppStore" in app_name)):
        pyttsx3.speak("Launching App store")
        os.system("open -a App\ Store")

    elif(("iTunes" in app_name) or ("itunes" in app_name)):
        pyttsx3.speak("Launching iTunes")
        os.system("open -a iTunes")

    elif(("safari" in app_name) or ("Safari" in app_name)):
        pyttsx3.speak("Launching Safari")
        os.system("open -a safari")

    elif(("messages" in app_name) or ("Messages" in app_name)):
        pyttsx3.speak("Launching Messages")
        os.system("open -a Messages")

    elif(("Facetime" in app_name) or ("facetime" in app_name)):
        pyttsx3.speak("Launching Facetime")
        os.system("open -a Facetime")
    
    elif(("Mail" in app_name) or ("mail" in app_name)):
        pyttsx3.speak("Launching Mails")
        os.system("open -a mail")
    
    elif(("Contacts" in app_name) or ("contacts" in app_name)):
        pyttsx3.speak("Launching Contacts")
        os.system("open -a contacts")

    elif(("Notes" in app_name) or ("notes" in app_name)):
        pyttsx3.speak("Launching Notes")
        os.system("open -a notes")

    elif(("Keynote" in app_name) or ("keynote" in app_name)):
        pyttsx3.speak("Launching Keynote")
        os.system("open -a keynote")

    elif(("Numbers" in app_name) or ("numbers" in app_name)):
        pyttsx3.speak("Launching Number")
        os.system("open -a numbers")
    
    elif(("Pages" in app_name) or ("pages" in app_name)):
        pyttsx3.speak("Launching Pages")
        os.system("open -a pages")

    elif(("Calculator" in app_name) or ("Calculator" in app_name)):
        pyttsx3.speak("Launching Calculator")
        os.system("open -a Calculator")

    elif(("Whtsapp" in app_name) or ("whatsapp" in app_name)):
        pyttsx3.speak("Launching Whatsapp")
        os.system("open -a whatsapp")

    elif(("Terminal" in app_name) or ("terminal" in app_name)):
        pyttsx3.speak("Launching Messages")
        os.system("open -a terminal")

    elif(("Siri" in app_name) or ("siri" in app_name)):
        pyttsx3.speak("Launching Siri")
        os.system("open -a siri")

    elif(("Skype" in app_name) or ("skype" in app_name)):
        pyttsx3.speak("Launching Skype")
        os.system("open -a Skype")

    elif(("Teamviewer" in app_name) or ("teamviewer" in app_name)):
        pyttsx3.speak("Launching Teamviewer")
        os.system("open -a Teamviewer")

    elif(("PyCharm" in app_name) or ("pycharm" in app_name)):
        pyttsx3.speak("Launching PyCharm CE")
        os.system("open -a PyCharm\ CE")

    elif(("Discord" in app_name) or ("discord" in app_name)):
        pyttsx3.speak("Launching Discord")
        os.system("open -a Discord")
    
    elif(("Visual Studio Code" in app_name) or ("visual studio code" in app_name)):
        pyttsx3.speak("Launching Visual Studio Code")
        os.system("open -a visual\ studio\ code")

    elif(("Photo Booth" in app_name) or ("photo booth" in app_name) or 
    ("photobooth" in app_name) or ("PhotoBooth " in app_name)):
        pyttsx3.speak("Launching Photo Booth")
        os.system("open -a Photo\ Booth")

    elif(("System Preferences" in app_name) or ("system preferences" in app_name)):
        pyttsx3.speak("Launching System Preferences")
        os.system("open -a System\ Preferences")

    elif (("exit" in app_name) or ("quit" in app_name) or ("Exit" in app_name) or ("Quit" in app_name)):
        break
    
    else:
        pyttsx3.speak("Application Cannot be Launched \n")

pyttsx3.speak("GOODBYE")

    

    











