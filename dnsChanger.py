#!/usr/bin/env python3

import os
import subprocess
import re

#DNS Server list
dnsServers = {'OpenDNS-1':'208.67.222.222', 'OpenDNS-2':'208.67.220.220',
              'Google-1':'8.8.8.8', 'Google-2':'8.8.4.4',
              'CloudFlare-1':'1.1.1.1', 'CloudFlare-2':'1.0.0.1'}

#show network adapters [setup purposes only]
def Show_nAdapters():
    viewNetworkAdpts = "netsh interface ipv4 show interfaces"
    os.system(viewNetworkAdpts)

#show current DNS Servers
def ShowCurrent_DNS_Servers():
    cmdOutput = subprocess.check_output(["ipconfig", "/all"])

    print("\nCurrent DNS Servers:")

    for key, value in dnsServers.items():
        if value in str(cmdOutput):
            print(key+": "+value)
    print("\n")

#Getting speed of DNS Servers
def get_DNS_Speed():
    pingOutput=""
    print("DNS LIST: ")
    #GoogleDNS check
    try:
        pingOutput = subprocess.check_output(["ping.exe","8.8.8.8","-n","2"])
        pattrn = r'([Aa]verage[ =\d]*ms)'
        result = re.search(pattrn, str(pingOutput))
        print("[8.8.8.8] GoogleDNS-1: " + result[1])
    except:
        print("[8.8.8.8] GoogleDNS-1: Connection Error!")
    try:
        pingOutput = subprocess.check_output(["ping.exe","8.8.4.4","-n","2"])
        pattrn = r'([Aa]verage[ =\d]*ms)'
        result = re.search(pattrn, str(pingOutput))
        print("[8.8.4.4] GoogleDNS-2: " + result[1])
    except:
        print("[8.8.4.4] GoogleDNS-2: Connection Error!")

    #OpenDNS check
    try:
        pingOutput = subprocess.check_output(["ping.exe","208.67.222.222","-n","2"])
        pattrn = r'([Aa]verage[ =\d]*ms)'
        result = re.search(pattrn, str(pingOutput))
        print("[208.67.222.222] OpenDNS-1: " + result[1])
    except:
        print("[208.67.222.222] OpenDNS-1: Connection Error!")
    try:
        pingOutput = subprocess.check_output(["ping.exe","208.67.220.220","-n","2"])
        pattrn = r'([Aa]verage[ =\d]*ms)'
        result = re.search(pattrn, str(pingOutput))
        print("[208.67.220.220] OpenDNS-2: " + result[1])
    except:
        print("[208.67.220.220] OpenDNS-2: Connection Error!")

    #CloudFlareDNS check
    try:
        pingOutput = subprocess.check_output(["ping.exe","1.1.1.1","-n","2"])
        pattrn = r'([Aa]verage[ =\d]*ms)'
        result = re.search(pattrn, str(pingOutput))
        print("[1.1.1.1] CloudFlare-1: " + result[1])
    except:
        print("[1.1.1.1] CloudFlare-1: Connection Error!")
    try:
        pingOutput = subprocess.check_output(["ping.exe","1.0.0.1","-n","2"])
        pattrn = r'([Aa]verage[ =\d]*ms)'
        result = re.search(pattrn, str(pingOutput))
        print("[1.0.0.1] CloudFlare-2: " + result[1])
    except:
        print("[1.0.0.1] CloudFlare-2: Connection Error!")

#Change DNS Funciton
def MDns():
    print("\nWARNING!! WRONG INPUT WILL CLOSE THE APPLICATION!! TOO LAZY TO MAKE INPUT ERROR MANAGEMENT!!")

    try:
        daDNS = input("Enter Primary DNS: ")
        daInput = re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", daDNS)
        os.system('netsh interface ip set dnsservers \"PLDT Fiber\" static '+str(daInput[0])+' primary no')

        daDNS = input("Enter Secondary DNS: ")
        daInput = re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", daDNS)
        os.system('netsh interface ip add dnsservers \"PLDT Fiber\" '+str(daInput[0])+' index=2 no')
    except:
        print("Wrong Input Try Again!")
        MDns()
    ShowCurrent_DNS_Servers()
    os.system("Pause")

#Main function
def MainF():
    os.system('cls')
    print("Simple DNS Changer! [By: Linz] \n")
    get_DNS_Speed()
    ShowCurrent_DNS_Servers()
    print("1 : Change DNS \n2 : Exit")
    choice = input("Choice: ")
    if choice[0]=="1":
        MDns()
    else:
        os.system('Exit')

#Running script!
MainF()

#Make sure you're running as admin while running this script