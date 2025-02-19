##################################################################################
# Project Code name - Cora                                                       #
#                                                                                #
# License - MIT                                                                  #
# This program is opensource, meaning, free to use, edit, and distribute.        #
# Brought to you by  (clu3bot on github)                                         #
# Project start date - November 5th 2021                                         #
# Public Beta release date -                                                     #
#                                                                                #
# No Responsibily Disclaimer:                                                    #
#                                                                                #
# Cora is a proof of concept tool to make easy of use of various tasks related   #
# to network security, bluetooth security, and hardware.                         # 
# This program is in beta and bugs should be anticipated.                        #
# Brennan McCown (clu3bot) and affiliates take no responsibily for any damage    #
# caused by this program. Including, but not limited to:                         #
# Damage to computer devices (i), Personal Computers(ii).                        #
#                                                                                #
#                                                                                #
# Any use of this program (iii) is intended for educational purposes only.       #
# The  foundation, employees/partners of clu3bot, github Contributors,           #
# and other third parties included, will not be held                             #
# accoutable or responsible for any misuse of this program (iii).                #
# The end user of this program (iii) is responsible for understanding            #
# and acknowledging his/her local laws as well as regulations regarding          #
# all FCC (Federal Communications Commission) laws and regulations.              #
#                                                                                #
# In regards to errors and omissions, Brennan McCown takes on no obligation      #
# to ensure this program (iii) from operating as intended or without error.      #
# This software is provided 'as is'.                                             #
#                                                                                #
# ** i.) Any electronic device the does or does no connect the internet.         #
# ** ii.) Any electronic device used for personal or business.                   #
# ** iii.) Cora framework and all programs and files included within.            #
#                                                                                #
# Do not remove this header.                                                     #
# Cora Version 1.0 Beta, Brennan McCown (clu3bot) 2021                           #
#                                                                                #
##################################################################################


from select import select
from statistics import mode
import sys
import random as rd
import os
import time
import threading as thd
import subprocess as sp
import signal
import os.path
import platform
import argparse as ag


#vars for script
class nvar:
    version="1.0 Beta"
    user="clu3bot"
    date="2021"
    project="cora"

#colar vars
class color:
    lightblue='\033[1;34m' #light blue
    lightred='\033[1;31m' #light red
    lightgreen='\033[1;32m' #lightgreen
    red='\033[0;31m' #red
    yellow='\033[1;33m' #yellow
    none='\033[0m' #no color
    purple='\033[1;35m' #purple
    cyan='\033[0;36m' #cyan
    green='\033[0;32m' #green

#clears terminal when called
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#handles exit when ctrl c is press
def handleexit():
    def signal_handler(signal, frame):
        clear()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

handleexit()

def permissions():  #checks for root permissions
    clear()
    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        print(color.lightred + "You need to run this script with sudo or as root.")
        time.sleep(0.3)
        quit()

def getos():
    osys=platform.system()
    if osys != "Linux":
        print(color.lightred + "This program only runs on Linux operating systems.")
        time.sleep(2)
        quit()

def getmode():
    global mode
    mode = sp.getoutput("sudo bash scrp/checkmode.sh")


def checkmonitor():
    cm = sp.getoutput("sudo bash scrp/checkmode.sh")

    global checkmode
    if cm == "Monitor":
        checkmode = 1
    elif cm == "Managed":
        checkmode = 0
    else:
        print ("Error")


#################################################hardware menu###################################################

hardware_menu_actions  = {}  

def hardware_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Hardware Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[1] Flash Bin Files to Development Boards")
    print ("[2] Burn ISO File to Live USB")  
    print ("[3] View Hardware Info\n")
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    hardware_exec_menu(choice)

    return

#decides which option to call
def hardware_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        hardware_menu_actions['main_menu']()
    else:
        try:
            hardware_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            hardware_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def hardwareoption0():
    print ("option 0")
    time.sleep(2)
    hardware_menu()

def hardwareoption1():
    print ("wifi option 1")
    time.sleep(2)    
    hardware_menu()

def hardwareoption2():
    print ("option 2")
    time.sleep(2)    
    hardware_menu()

def hardwareoption3():
    print ("option 3")
    time.sleep(2)
    hardware_menu()

#binds the options to numbers
hardware_menu_actions = {
    'main_menu': hardware_menu,
    '0': hardwareoption0,
    '1': hardwareoption1,    
    '2': hardwareoption2,
    '3': hardwareoption3,
    'b': back,
    'x': exit,
}

#################################################payload menu###################################################

payload_menu_actions  = {}  

def payload_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Payload and Exploit Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[0] Search for a tool.\n")
    print ("[1] WiFi Tools"+"               [8] Spoof Mac Adress")
    print ("[2] Bluetooth Tools"+"          [9] Enable Monitor Mode")  
    print ("[3] Prefabricated Scans"+"      [10] Disable Monitor Mode")
    print ("[4] Payload Tools"+"            [11] Select a Target Network")
    print ("[5] Hardware Tools"+"           [12] Show Public IP")
    print ("[6] Cryptography Tools"+"       [b] back")
    print ("[7] Misc Tools"+"               [x] exit")
    print ("\n")
    choice = input("\n>>  ")
    payload_exec_menu(choice)

    return

#decides which option to call
def payload_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        payload_menu_actions['main_menu']()
    else:
        try:
            payload_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            payload_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def payloadoption0():
    print ("option 0")
    time.sleep(2)
    payload_menu()

def payloadoption1():
    print ("wifi option 1")
    time.sleep(2)    
    payload_menu()

def payloadoption2():
    print ("option 2")
    time.sleep(2)    
    payload_menu()

def payloadoption3():
    print ("option 3")
    time.sleep(2)
    payload_menu()

def payloadoption4():
    print ("option 4")
    time.sleep(2)
    payload_menu()

def payloadoption5():
    print ("option 5")
    time.sleep(2)    
    payload_menu()

def payloadoption6():
    print ("option 6")
    time.sleep(2)    
    payload_menu()

def payloadoption7():
    print ("option 7")
    time.sleep(2)
    payload_menu()

def payloadoption8():
    print ("option 8")
    time.sleep(2)
    payload_menu()

def payloadoption9():
    print ("option 9")
    time.sleep(2)
    payload_menu()

def payloadoption10():
    print ("option 10")
    time.sleep(2)
    payload_menu()

def payloadoption11():
    print ("option 11")
    time.sleep(2)
    payload_menu()

def payloadoption12():
    print ("option 12")
    time.sleep(2)
    payload_menu()

def payloadoption13():
    print ("option 13")
    time.sleep(2)
    payload_menu()

#binds the options to numbers
payload_menu_actions = {
    'main_menu': payload_menu,
    '0': payloadoption0,
    '1': payloadoption1,    
    '2': payloadoption2,
    '3': payloadoption3,
    '4': payloadoption4,
    '5': payloadoption5,
    '6': payloadoption6,
    '7': payloadoption7,
    '8': payloadoption8, 
    '9': payloadoption9,
    '10': payloadoption10,
    '11': payloadoption11, 
    '12': payloadoption12,
    '13': payloadoption13,
    'b': back,
    'x': exit,
}

#################################################misc menu###################################################

misc_menu_actions  = {}  

def misc_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Misc Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[0] Search for a tool.\n")
    print ("[1] WiFi Tools"+"               [8] Spoof Mac Adress")
    print ("[2] Bluetooth Tools"+"          [9] Enable Monitor Mode")  
    print ("[3] Prefabricated Scans"+"      [10] Disable Monitor Mode")
    print ("[4] Payload Tools"+"            [11] Select a Target Network")
    print ("[5] Hardware Tools"+"           [12] Show Public IP") 
    print ("[6] Cryptography Tools"+"       [b] back")
    print ("[7] Misc Tools"+"               [x] exit")
    print ("\n")
    choice = input("\n>>  ")
    misc_exec_menu(choice)

    return

#decides which option to call
def misc_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        misc_menu_actions['main_menu']()
    else:
        try:
            misc_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            misc_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def miscoption0():
    print ("option 0")
    time.sleep(2)
    misc_menu()

def miscoption1():
    print ("wifi option 1")
    time.sleep(2)    
    misc_menu()

def miscoption2():
    print ("option 2")
    time.sleep(2)    
    misc_menu()

def miscoption3():
    print ("option 3")
    time.sleep(2)
    misc_menu()

def miscoption4():
    print ("option 4")
    time.sleep(2)
    misc_menu()

def miscoption5():
    print ("option 5")
    time.sleep(2)    
    misc_menu()

def miscoption6():
    print ("option 6")
    time.sleep(2)    
    misc_menu()

def miscoption7():
    print ("option 7")
    time.sleep(2)
    misc_menu()

def miscoption8():
    print ("option 8")
    time.sleep(2)
    misc_menu()

def miscoption9():
    print ("option 9")
    time.sleep(2)
    misc_menu()

def miscoption10():
    print ("option 10")
    time.sleep(2)
    misc_menu()

def miscoption11():
    print ("option 11")
    time.sleep(2)
    misc_menu()

def miscoption12():
    print ("option 12")
    time.sleep(2)
    misc_menu()

def miscoption13():
    print ("option 13")
    time.sleep(2)
    misc_menu()

#binds the options to numbers
misc_menu_actions = {
    'main_menu': misc_menu,
    '0': miscoption0,
    '1': miscoption1,    
    '2': miscoption2,
    '3': miscoption3,
    '4': miscoption4,
    '5': miscoption5,
    '6': miscoption6,
    '7': miscoption7,
    '8': miscoption8, 
    '9': miscoption9,
    '10': miscoption10,
    '11': miscoption11, 
    '12': miscoption12,
    '13': miscoption13,
    'b': back,
    'x': exit,
}

#################################################crypto menu###################################################

crypto_menu_actions  = {}  

def crypto_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Cryptography Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[1] Base64 Encode/Decode"+"               [8] ")
    print ("[2] Rot Cypher Encode/Decode"+"          [9] ")  
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    crypto_exec_menu(choice)

    return

#decides which option to call
def crypto_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        crypto_menu_actions['main_menu']()
    else:
        try:
            crypto_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            crypto_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu

def cryptooption1():
    os.system("python3 etc/crypto/base-64.py")
    crypto_menu()

def cryptooption2():
    os.system("python3 etc/crypto/rot-cypher.py")
    crypto_menu()

def cryptooption3():
    print ("option 3")
    time.sleep(2)
    crypto_menu()

def cryptooption4():
    print ("option 4")
    time.sleep(2)
    crypto_menu()

def cryptooption5():
    print ("option 5")
    time.sleep(2)    
    crypto_menu()

def cryptooption6():
    print ("option 6")
    time.sleep(2)    
    crypto_menu()

def cryptooption7():
    print ("option 7")
    time.sleep(2)
    crypto_menu()

def cryptooption8():
    print ("option 8")
    time.sleep(2)
    crypto_menu()

def cryptooption9():
    print ("option 9")
    time.sleep(2)
    crypto_menu()

def cryptooption10():
    print ("option 10")
    time.sleep(2)
    crypto_menu()

def cryptooption11():
    print ("option 11")
    time.sleep(2)
    crypto_menu()

def cryptooption12():
    print ("option 12")
    time.sleep(2)
    crypto_menu()

def cryptooption13():
    print ("option 13")
    time.sleep(2)
    crypto_menu()

#binds the options to numbers
crypto_menu_actions = {
    'main_menu': crypto_menu,
    '1': cryptooption1,    
    '2': cryptooption2,
    '3': cryptooption3,
    '4': cryptooption4,
    '5': cryptooption5,
    '6': cryptooption6,
    '7': cryptooption7,
    '8': cryptooption8, 
    '9': cryptooption9,
    '10': cryptooption10,
    '11': cryptooption11, 
    '12': cryptooption12,
    '13': cryptooption13,
    'b': back,
    'x': exit,
}

##################################################scan menu###################################################

scan_menu_actions  = {}  

def scan_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Prefabricated Scan Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[1] ARP Scan")
    print ("[2] NMAP Scan")  
    print ("[3] Verbose NMAP Scan")
    print ("[4] Bluetooth AP Scan")
    print ("[5] Wireless AP Dump")
    print ("[6] Gobuster Scan"+"       [b] back")
    print ("                           [x] exit")
    print ("\n")
    choice = input("\n>>  ")
    scan_exec_menu(choice)

    return

#decides which option to call
def scan_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        scan_menu_actions['main_menu']()
    else:
        try:
            scan_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            scan_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def scanoption0():
    print ("option 0")
    time.sleep(2)
    scan_menu()

def scanoption1():
    print ("wifi option 1")
    time.sleep(2)    
    scan_menu()

def scanoption2():
    print ("option 2")
    time.sleep(2)    
    scan_menu()

def scanoption3():
    print ("option 3")
    time.sleep(2)
    scan_menu()

def scanoption4():
    print ("option 4")
    time.sleep(2)
    scan_menu()

def scanoption5():
    print ("option 5")
    time.sleep(2)    
    scan_menu()

def scanoption6():
    print ("option 6")
    time.sleep(2)    
    scan_menu()


#binds the options to numbers
scan_menu_actions = {
    'main_menu': scan_menu,
    '0': scanoption0,
    '1': scanoption1,    
    '2': scanoption2,
    '3': scanoption3,
    '4': scanoption4,
    '5': scanoption5,
    '6': scanoption6,
    'b': back,
    'x': exit,
}

##################################################bluetooth menu###################################################

bluetooth_menu_actions  = {}  

def bluetooth_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Bluetooth Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[1] Bluetooth Dos"+"               [3] View Bluetooth Mac")
    print ("[2] Spoof Bluetooth Mac")  
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    wifi_exec_menu(choice)

    return

#decides which option to call
def bluetooth_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        bluetooth_menu_actions['main_menu']()
    else:
        try:
            bluetooth_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            bluetooth_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    bluetooth_menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu

def btoption1():
    print ("wifi option 1")
    time.sleep(2)    
    bluetooth_menu()

def btoption2():
    print ("option 2")
    time.sleep(2)    
    bluetooth_menu()

def btoption3():
    print ("option 3")
    time.sleep(2)
    bluetooth_menu()


#binds the options to numbers
bluetooth_menu_actions = {
    'main_menu': bluetooth_menu,
    '1': btoption1,    
    '2': btoption2,
    '3': btoption3,
    'b': back,
    'x': exit,
}


#beacon spam fix a few things since this code was moved from another directory

def beaconmonitor():
    response = input("Would you like to enable Monitor Mode? (Y/N)")

    lowresponse = response.lower()
    if lowresponse == 'y':
        clear()
        os.system("sudo airmon-ng start "+interface)
        beaconspam()

    elif lowresponse == 'n':
        clear()
        print ("This part of the program requires Monitor Mode")
        userinp = input ("Press Y to enable monitor or Press X to return to Main Menu..")
        lowuserinp = userinp.lower()
        if lowuserinp == "y":
            os.system("sudo airmon-ng start "+interface)
        elif lowuserinp == "x":
            clear()
            print ("Returning to Main Menu..")
            main_menu()
        else:
            clear()
            print ("Invalid Option..")
            beaconmonitor()
    else:
        clear()
        print ("Invalid Option..")
        beaconmonitor()

def beaconcheckmode():
    checkmonitor()
    if checkmode == 1:
        time.sleep(0)
    elif checkmode == 0:
        beaconmonitor()
    else:
        print("An error has occured")

def beaconrandomnames():
    clear()
    beaconcheckmode()
    print ("Starting..")
    time.sleep(0.5)
    print (color.lightgreen+"[Beacon Spam Active]"+color.none)
    os.system("sudo mdk3 "+interface+" b -s 500")

def beaconnamesfile():
    clear()
    beaconcheckmode()
    print ("File must be located in "+color.lightred+" /cora/scrp/wifitools/ess"+color.none)
    if os.path.isfile("scrp/wifitools/tmp/file.txt"):
        clear()
        defaultfile = sp.getoutput("cat scrp/wifitools/tmp/file.txt")
        ask = input("File "+defaultfile+" is currently set as your default names file, is this the file you would like to use? (Y/N)")
        asklower = ask.lower()
        if asklower == "y":
            time.sleep(1)
        elif asklower == "n":
            clear()
            print ("File must be located in "+color.lightred+" /cora/scrp/wifitools/ess"+color.none)
            file = input ("What is the name of the file Including file extention. Example "+color.lightgreen+"file.txt"+color.none+": ")
        else:
            clear()
            print ("File must be located in "+color.lightred+" /cora/scrp/wifitools/ess"+color.none)
            file = input ("What is the name of the file Including file extention. Example "+color.lightgreen+"file.txt"+color.none+": ")

    if os.path.isfile("/ess/"+file):
        question = input ("Would you like to set this File as your Default File? (Y/N)")

        lowquestion = question.lower()
        if lowquestion == "y":
            os.system("echo "+file+" > scrp/wifitools/tmp/file.txt")
        elif lowquestion == "n":
            time.sleep(1)
        else:
            print("Invalid Option..")
    else:
        clear()
        print("File could not located in "+color.lightred+"/cora/scrp/wifitools/ess"+color.none)
        time.sleep(4)
        beaconnamesfile()       


def beaconspam():
    beaconcheckmode()
    print ("Beacon Flood Options:\n\n")
    print ("[1] Use Random Names")
    print ("[2] Use a Names File")
    i = input ("\n\nChoose an Option: ")

    if i == "1":
        beaconrandomnames()
    elif i == "2":
        beaconnamesfile()
    else:
        print ("Invalid Option")


#authdos

def authdos():
    time.sleep(1)

#arpscan

def arpscan():
    os.system("rm -rf scrp/wifitools/tmp/int.txt")
    os.system("echo "+interface+" > scrp/wifitools/tmp/int.txt")
    os.system("sudo bash scrp/wifitools/arpscan.sh")

#################################################wifi options#################################################


def beaconspamcall():
    beaconspam()

def authdoscall():
    authdos()

def rougeapcall():
    os.system("sudo bash scrp/wifitools/rougeap.sh")

def deauthcall():
    os.system("sudo bash scrp/wifitools/deauth.sh")

def tkipcall():
    os.system("sudo bash scrp/wifitools/tkip.sh")

def apdumpcall():
    os.system("sudo bash scrp/wifitools/apdump.sh")

def arpscancall():
    arpscan()



##################################################wifi menu###################################################

wifi_menu_actions  = {}  

def wifi_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Wifi Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[1] Beacon/AP Spam")
    print ("[2] Auth Dos Attack")  
    print ("[3] Rouge AP")
    print ("[4] Deauth Airplay Attack")
    print ("[5] TKIP Attack")
    print ("[6] AP Dump (See All nearby APs and Macs)"+"            ["+color.lightred+"b"+color.none+"] back")
    print ("[7] ARP Scan"+"                                         ["+color.lightred+"x"+color.none+"] exit")
    print ("\n")
    choice = input("\n>>  ")
    wifi_exec_menu(choice)

    return

#decides which option to call
def wifi_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        wifi_menu_actions['main_menu']()
    else:
        try:
            wifi_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            wifi_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu

def wifioption1():
    beaconspamcall()

def wifioption2():
    authdoscall()

def wifioption3():
    rougeapcall()

def wifioption4():
    deauthcall()

def wifioption5():
    tkipcall()

def wifioption6():
    apdumpcall()

def wifioption7():
    arpscancall()


#binds the options to numbers
wifi_menu_actions = {
    'main_menu': wifi_menu,
    '1': wifioption1,    
    '2': wifioption2,
    '3': wifioption3,
    '4': wifioption4,
    '5': wifioption5,
    '6': wifioption6,
    '7': wifioption7,
    'b': back,
    'x': exit,
}

#function to call system info script
def sysinfo():
    clear()
    os.system("sudo bash scrp/sysinfo.sh")
    input ("Press any key to return to Main Menu..")
    main_menu()

#funtion to find the public ip of the user

def publicip():
    os.system("curl ipinfo.io/ip > /tmp/ip.txt")
    var = sp.getoutput("cat /tmp/ip.txt")
    os.system("rm -rf /tmp/ip.txt")
    clear()
    print("Your public IP address is:"+color.green+var+color.none)
    input("\nPress any key to return to main menu..")
    main_menu()

#deselects a network
def deselectint():
    print ("deselect net")


#check if a computer only has ethernet

def checkether():
    if interface == 'eth0':
        print ("eth0")
    elif interface == 'eth1':
        print ("eth1")
    elif interface == 'eth2':
        print ("eth2")
    elif interface == 'eth3':
        print ("eth3")
    else:
        time.sleep(2)
 
#change class to a function and return the value of getinterface to the parent function. change everything that currently says the class and use the function. 

def getinterface():
    global interface
    if os.path.isfile("scrp/iface.sh"):
        print (os.environ["int"])
        main_menu()
    else:
        interface = "No Interface Selected"
        time.sleep(0.1)


#fixing error where networkselect.sh cant grab ifac int so the solution is to export iface int from here to a file and grab the file on shell and define a nw variable there

def handlenamechange():
    flag = 'mon'
    if flag in interface :
        namechange = interface
    else:
        interface = interface+flag

def exportint():
    os.system("echo "+interface+" > scrp/tmp/int.txt")
    time.sleep(2)

#show the interface mode
def showinterface():
    clear()
    print ("Currently Selected Interface:"+color.green+ interface+color.none)
    print ("\n\n[1] Main Menu\n")
    yn = input ("Select an Option: ")
    if yn == '1':
        main_menu()
    else:
        clear()
        print ("Invalid Option")
        time.sleep(1)
        showinterface()
    
#function to call script for selecting a network and setting network name to a var
def selectint():
    os.system("sudo bash scrp/iface.sh")
    getinterface()

#function to get the monitor mode and set to a variable

def getmonitormode():
    #either figure out or call a script
    os.system("echo get monitor mode")

#select a target network
def getmode():
    time.sleep(2)

def selectnet():
    clear()

    exportint()
    os.system("sudo bash scrp/networkselect.sh")
    time.sleep(2)
    main_menu()

def deselectnet():
    clear()
    print ("deselect net")
    time.sleep(2)

def shownet():
    clear()
    print("show net")
    time.sleep(2)

#functions for monitor mode

def checkvar():
    if interface == 'No Interface Selected':
        print ("Cannot continue no interface selected..")
        time.sleep(1)
        print ("Returning to Main Menu..")
        time.sleep(2)
        main_menu()
    else:
        time.sleep(0.1) 

######fix####

def monitoron():
    checkvar()
    nc = getinterface()
    os.system("sudo ifconfig "+nc+" up")
    os.system("sudo airmon-ng start "+nc)
    handlenamechange()
    main_menu()

    #left off trying to find a way to update the interface variable in order to change interface variable from update after one of these options is chosen

def monitoroff():
    checkvar()
    nc = handlenamechange()
    os.system("sudo ifconfig "+nc+"up")
    os.system("sudo airmon-ng stop "+nc)
    main_menu()

#functions for spoofing mac#

def randommac():
    os.system("bash scrp/ifaceformac.sh")
    maciface = sp.getoutput("cat scrp/tmp/varformac.txt")

    os.system("macchanger -r "+maciface)

def choosemac():
    os.system("bash scrp/ifaceformac.sh")
    maciface = sp.getoutput("cat scrp/tmp/varformac.txt")

    usermac = input("Type a new mac adress: ")
    os.system("macchanger -m "+usermac+" "+maciface)
    
def resetmac():
    os.system("echo reset mac")

#menu for spoof mac
spoofmenu_actions  = {}  

def spoof_menu():

    handleexit()
    var = sp.getoutput("cat tmp/var.txt")
    clear()
    print ("Mac Adress Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/chimerafoundation/befw\n\n")   ##fix 
    print ("[0] Set Mac Address to a random Mac\n")
    print ("[1] Choose your own Mac address"+"               [2] Reset Mac address to original\n")
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    spoofexec_menu(choice)

    return

#decides which option to call
def spoofexec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        spoofmenu_actions['main_menu']()
    else:
        try:
            spoofmenu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            spoofmenu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def spoofmacoption0():
    print ("random mac")
    time.sleep(2)
    main_menu()

def spoofmacoption1():
    print ("choose mac")
    time.sleep(2)    
    wifi_menu()

def spoofmacoption2():
    print ("reset to original mac")
    time.sleep(2)    
    bluetooth_menu()

spoofmenu_actions = {
    'main_menu': spoof_menu,
    '0': spoofmacoption0,
    '1': spoofmacoption1,    
    '2': spoofmacoption2,
    'b': back,
    'x': exit,
}

#dev term
def devtermcoraman():
    print("Commands: \n")
    print("interface - Shows Interface")
    print("clear - Clears Terminal")
    print("man - Displays Manual")

def devterm():
    term = input (color.green+"system@cora"+color.none+": ")
    termlow = term.lower()

    if termlow == "interface":
        print (interface)
        devterm()
    elif termlow == "interface -tmp":
        if os.path.isfile("scrp/wifitools/tmp/int.txt"):
            z = sp.getoutput("cat scrp/wifitools/tmp/int.txt")
            print(z)
            devterm()
        else:
            print("Interface has not been defined")
            devterm()
    elif termlow == "back":
        main_menu()
    elif termlow == "clear":
        clear()
        devterm()
    elif termlow == "man":
        devtermcoraman()
        devterm()
    else:
        os.system(termlow)
        devterm()


####################################################search funtion#########################################################

#tool keyword flag data

class exceptedformacspoof:
    wordlist = ['macaddress', 'macspoof', 'spoofmac', 'mac', 'mac address', 'mac spoof', 'spoof mac', 'spoof mac address', 'macspoof', 'spoofmac', 'change mac', 'change mac address', 'change macaddress', 'mac changer', 'mac address changer', 'macchanger']

class exceptedformonitor:
    worldlist = ['monitor', 'monitor mode', 'monitormode', 'disable monitor mode', 'disable monitor', 'disablemonitor', 'disablemonitormode', 'network mode', 'managed mode', 'managed mode', 'interface', 'interface mode', 'wireless mode', 'wifi mode', 'airmon-ng']

class exceptedfornetworkselect:
    wordlist = ['target network', 'select network', 'select a network', 'network select', 'selection for network', 'target a network', 'network target', 'wifi target', 'target wifi', 'network selection']

class exceptedforintselect:
    wordlist = ['monitor mode', 'managed mode', 'mode', 'network mode', 'wifi mode', 'wireless mode', 'monitor', 'managed', 'airmon-ng']

class exceptedforip: 
    wordlist = ['ip', 'find ip', 'search ip', 'public ip', 'show ip', 'show public ip', 'showip', 'publicip']

class exceptedforsysteminfo: 
    wordlist = ['system', 'system info', 'info system', 'sys', 'sys info', 'sysinfo', 'systeminfo', 'infosystem', 'show sys info', 'show system info', 'system information', 'specs', 'spec', 'system specs']

class exceptedforbase64:
    wordlist = ['base 64', 'base64', 'base64 encode', 'base', 'base 64 encode', 'base 64 decode', 'base64 decode', 'base64 encryption', 'encrypt base64']

class exceptedforrot:
    wordlist = ['rot cypher', 'rot', 'rot encryption', 'rot-13', 'rot-17', 'rotcypher', 'rot 13', 'rot-17', 'rot-13 cypher', 'rot 13 cypher']

class exceptedforcypher:
    wordlist = ['cypher', 'crypto', 'cryptography', 'encryption', 'cyphers', 'encryptions', 'encode', 'decode']

class exceptedforwifi:
    wordlist = ['mdk3', 'arpscan', 'arp', 'arp scan', 'beacon flood', 'deauth', 'deauther', 'mdk4', 'beacon', 'dos', 'ddos', 'wifi attacks', 'wifiattacks', 'ap spam', 'ap crash', 'rouge ap', 'mitm', 'airplay', 'aircrack', 'tkip', 'tkip attack', 'airplay attack', 'ap dump', 'airodump', 'aircrack-ng', 'airodump-ng', 'nearby ap', 'ap', 'arp', 'arp scan', 'mdk3']

class exceptedformdk3: 
    wordlist = ['mdk3']

class exceptedforbluetooth:
    wordlist = ['bluetooth', 'spoof bluetooth', 'bluez', 'bluetooth dos', 'jam bluetooth', 'bluetooth jam', 'bluebooth jammer']

class exceptedfordevterm:
    wordlist = ['dev']


#options

def dev():
    clear()
    print("Type "+color.red+"back"+color.none+" to return to main menu.")
    devterm()

def mdk3():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] mdk3")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        wifi_menu()
    else:
        clear()
        print("invalid option")
        macspoof()

def wifi():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Wifi Options Menu")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        wifi_menu()
    else:
        clear()
        print("invalid option")
        macspoof()

def macspoof():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Spoof Mac Address")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        spoof_menu()
    else:
        clear()
        print("invalid option")
        macspoof()

def monitormode():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Turn Monitor Mode on")
    print ("[2] Turn Monitor Mode off")
    print ("[3] Show Current Interface")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        monitoron()
    elif yn == '2' :
        monitoroff()
    elif yn == '3' :
        showinterface()
    else:
        clear()
        print("invalid option")
        monitormode()

def netselection():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Select a Network to Target")
    print ("[2] Deselct a Network")
    print ("[3] Show Currently Selected Network")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        selectnet()
    elif yn == '2' :
        deselectnet()
    elif yn == '3' :
        shownet()
    else:
        clear()
        print("invalid option")
        netselection()
    
def pubip():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Show Public Ip")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        publicip()
    else:
        clear()
        print("invalid option")
        pubip()

def systeminfo():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Show System info")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        sysinfo()
    else:
        clear()
        print("invalid option")
        systeminfo()

def base64encode():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Base 64 Encode/Decode")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        cryptooption1()
    else:
        clear()
        print("invalid option")
        systeminfo()

def rotcypher():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Rot Cypher Encode/Decode")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        cryptooption2()
    else:
        clear()
        print("invalid option")
        systeminfo()

def cyphermenu():
    print ("Found "+color.lightgreen+searchvalue+color.none+" In: ")
    print ("[1] Cryptography Menu")
    print ("\n\n\n[b] Search Again")
    print ("[x] Main Menu")
    yesno = input("Select an Option: ")
    yn = yesno.lower()
    if yn == 'x':
        main_menu()
    elif yn == 'b' :
        searchvar()
    elif yn == '1' :
        crypto_menu()
    else:
        clear()
        print("invalid option")
        systeminfo()

#instand responses

def instantresponseip():
    publicip()
# search queries with instant responses

class instantrespondforip :
    flag = ['public ip', 'public ip address']

#search funtion
def searchtool(searchvalue):
    clear()
    sv = searchvalue.lower()
    if sv in instantrespondforip.flag :
        instantresponseip()
    elif sv in exceptedformacspoof.wordlist :
        macspoof()
    elif sv in exceptedformonitor.worldlist :
        monitormode()
    elif sv in exceptedfornetworkselect.wordlist :
        netselection()
    elif sv in exceptedforip.wordlist :
        pubip()
    elif sv in exceptedforsysteminfo.wordlist :
        systeminfo()
    elif sv in exceptedforbase64.wordlist :
        base64encode()
    elif sv in exceptedforcypher.wordlist :
        cyphermenu()
    elif sv in exceptedforrot.wordlist :
        rotcypher()
    elif sv in exceptedformdk3.wordlist :
        mdk3()
    elif sv in exceptedforwifi.wordlist :
        wifi()
    elif sv in exceptedfordevterm.wordlist:
        dev()
    else:
        print("The tool you have searched for "+color.red+sv+color.none+" was unable to be found. Try being more concise (Common names of tools.)")
        time.sleep(4.5)
        searchvar()
    
def searchvar():
    clear()
    global searchvalue
    searchvalue = input("Search for a tool: ")
    searchtool(searchvalue)
    return

######################################################main menu#############################################################


#defines the main menu
menu_actions  = {}  

def main_menu():

    handleexit()
    clear()
    print (r""" 
    ████████                              
  ███░░░░░███                             
 ███     ░░░   ██████  ████████   ██████  
░███          ███░░███░░███░░███ ░░░░░███ 
░███         ░███ ░███ ░███ ░░░   ███████ 
░░███     ███░███ ░███ ░███      ███░░███ 
 ░░█████████ ░░██████  █████    ░░████████
  ░░░░░░░░░   ░░░░░░  ░░░░░      ░░░░░░░░ 
  """)
    print ("By "+nvar.user+", "+nvar.date+ "       Version: "+color.green+ nvar.version+color.none+"     Interface: "+color.green+interface+color.none)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/cora\n\n")   ##fix 
    print ("[0] Search for a tool.\n")
    print ("[1] WiFi Tools"+"               [8] Spoof Mac Adress")
    print ("[2] Bluetooth Tools"+"          [9] Enable Monitor Mode")  
    print ("[3] Prefabricated Scans"+"      [10] Disable Monitor Mode")
    print ("[4] Payload Tools"+"            [11] Select a Wireless Interface")
    print ("                             [12] Select a Target Network")
    print ("[5] Hardware Tools"+"           [13] Show Public IP")
    print ("[6] Cryptography Tools"+"       [14] Show System Info")
    print ("[7] Misc Tools"+"               ["+color.lightred+"x"+color.none+"] exit")
    print ("                             ["+color.lightred+"u"+color.none+"] check for updates")
    print ("\n")
    choice = input("\n>>  ")
    exec_menu(choice)

    return

#decides which option to call
def exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def option0():
    time.sleep(2)
    searchvar()

def option1():
    time.sleep(2)    
    wifi_menu()

def option2():
    time.sleep(2)    
    bluetooth_menu()

def option3():
    time.sleep(2)
    scan_menu()

def option4():
    time.sleep(2)
    payload_menu()

def option5():
    time.sleep(2)    
    hardware_menu()

def option6():
    time.sleep(2)    
    crypto_menu()

def option7():
    time.sleep(2)
    misc_menu()

def option8():
    time.sleep(2)
    spoof_menu()

def option9():
    time.sleep(2)
    monitoron()

def option10():
    time.sleep(2)
    monitoroff()

def option11():
    time.sleep(2)
    selectint()

def option12():
    time.sleep(2)
    selectnet()

def option13():
    time.sleep(2)
    publicip()

def option14():
    time.sleep(2)
    sysinfo()

def update():
    os.system("sudo bash updates.pl")
#binds the options to numbers
menu_actions = {
    'main_menu': main_menu,
    '0': option0,
    '1': option1,    
    '2': option2,
    '3': option3,
    '4': option4,
    '5': option5,
    '6': option6,
    '7': option7,
    '8': option8, 
    '9': option9,
    '10': option10,
    '11': option11, 
    '12': option12,
    '13': option13,
    '14': option14,
    'b': back,
    'x': exit,
    'u': update,
}

###########################################################################################################

def check_install():
    check = sp.getoutput("cat etc/done_flag.txt")
    if check == 'done':
        time.sleep(1)
    else:
        print(color.red+"Run install.py")
        exit()

#possible problem because selectint isnt returned

#what is done on startup
def onstartup():
    clear()
    check_install()
    selectint()
    initialload = "loading "
    print (initialload + nvar.project)
    time.sleep(0.5)
    if interface is None:
        selectint()
    else:
        time.sleep(0.5)
    if os.path.isfile("install.sh"):
        print ("please run the install.sh file in the "+nvar.project+"/ directory")
    else:
        time.sleep(0.5)
        main_menu()
onstartup()
