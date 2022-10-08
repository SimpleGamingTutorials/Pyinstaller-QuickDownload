import os
import time

print("Make sure to activate the environment befre running the script")
Question = input("Have you runned the environment first? ")
if Question == ("yes"):
    print("=========================")
    print("Running script")
    time.sleep(2.4)
    print("Running Automation script")
    time.sleep(0.4)
    print("Running  pyinstaller installation")
    os.system("pip install pyinstaller")
    print("=========================")
elif Question == ("no"):   
    print("Moving On ==>")
    pass

print("Do you want to upgrade your pip version?  ")
Question2 = input("Upgrade Version: (y/n) ")
if Question2 == ("y"):
    print("Upgrading ...")
    time.sleep(0.4)
    print("========================")
    os.system("pip install --upgrade pip")
    print("=========================")
    print("Done ...")
elif Question2 == ("n"):
    print("Exiting  ...")
    exit()
