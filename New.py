#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2023, 12, 12)
#expirydate = datetime.date(2023, 12, 12)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum
    def lawde_time_pe_khel(n):
        check=0
        for digit in (n):
            if(int(digit)==0):
                check=check+1
        return check
    clear()
    y=1
    newperiod=period
    banner='figlet AMUSEBOX'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @RXCE_HACKER")
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        samjha_maadarchod=lawde_time_pe_khel(last2)
        if(newperiod%2==0):
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1," : 🔴, RED")
            else:
                print(newperiod+1,"  : 🟢, GREEN")
        else:
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"   : 🔴, RED")
            else:
                print(newperiod+1,"   : 🟢, GREEN")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @RXCE_HACKER")
            #print(numbers)
             
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=11, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=13, minute=25, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (now>First and now<Firstend):
            period=220
            hero()
    elif(now>Second and now<Secondend):
            period=280
            hero()
    elif(now>Third and now<Thirdend):
            period=340
            hero()
    elif(now>Final and now<Finalend):
            period=400
            hero()
    else:
        banner='figlet RXCE'
        system(banner)
        print("Hi!! Thanks for buying the hack")
        #print("Hi! thanks for trying our DEMO")
        print("----------Your play time-----------")
        print("29th Dec 2023, 11:00 AM- 11:30 AM")
        print("29th Dec 2023, 02:00 PM- 02:30 PM")
        print("29th Dec 2023, 05:00 PM- 05:30 PM")
        print("29th Dec 2023, 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @HACK_RXCE ")



else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    code="FREEDGSED"
    banner='figlet RXCE'
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@RXCE_HACKER for activating")
    print(" Recharge Amount :        Total limit " )
    print(" 1.     1000 INR -------  1 Day (30 Games")
    print(" 2.     5000 INR -------  7 Days(210 Games")
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
    print("Beware of fraudsters!!!")
    while(True):
        print("Contact Me on Telegram")
        print("If you send to any other name , then IT IS SCAMMM")
        print("--------*--------*----------*---------")
        print("send payment only To Me")
        print("payhere--- UPI : ")
        print("UPI1 : Contact me on telegram")
        print("UPI2 : Contact me on telegram")
        print("If you have already paid to above UPI")
        print("Please Enter your 12 Digit \n UPI reference number ")
        print("or please Enter Correct activation code for 8:30 PM ")
        bhai=input(": ")
        if(bhai==code):
            clear()
            print("----------Your play time-----------")
            print("10th Dec 2023, 02:30 PM- 03:00 PM")
            print("10th Dec 2023, 05:30 PM- 06:00 PM")
            print("10th Dec 2023, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=350
            hero()
            #period("Sorry too many people(>20) using hack in same time ")
            #sys.exit(" \n \n \n Contact on Telegram @RXCE_HACKER")
        elif(bhai==nextday or bhai==nexday1):
            clear()
            banner='figlet RXCE'
            system(banner)
            print("----------Your play time-----------")
            print("11th Dec 2023, 04:00 PM- 04:30 PM")
            print("11th Dec 2023, 06:00 PM- 06:30 PM")
            print("11th Dec 2023, 08:00 PM- 08:30 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=400
            #hero()
            period("Sorry too many people(>20) using hack in same time ")
            sys.exit(" \n \n \n Contact on Telegram @HACK_RXCE")
            
            
        else:
            clear()
            banner='figlet RXCE'
            system(banner)
            print("Incorrect Activation Code :")
     
