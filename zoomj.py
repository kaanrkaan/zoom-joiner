#Zoom Join Tool version 1.0
#Author: K2K
#classname, weekday, time(13.30-1.40), url
import webbrowser as wb 
import datetime
import time
import sys
import os
try:
    temp = open("classes.txt","r")
except:
    file = open("classes.txt","x")
def getTime():
    r = [
        datetime.datetime.today().weekday(),
        datetime.datetime.now().strftime("%H"),
        datetime.datetime.now().strftime("%M")
    ]
    return r
def getClasses():
    f = open("classes.txt","r")
    classes = []
    for x in f:
        temp = x.split(",")
        classes.append(temp)
    return classes
def addClass(classes):
    classList = classes.split(";")
    for x in classList:
        with open("classes.txt", "a") as file:
            file.write("\n")
            file.write(x)
def remClass():
    classes = getClasses()
    print("Please write the name of the class you want to remove.")
    for x in classes:
        print(x[0])
    classname = input()
    temp_idx = "r"
    for i in range(len(classes)):
        if (classes[i][0] == classname):
            temp_idx = i
    if(temp_idx != "r"):
        classes.pop(temp_idx)
        for x in classes:
            with open("classes.txt", "a") as file:
                file.write(x)
                file.write("\n")
    else:
        print("Wrong input value!")
    
def currentClass():
    currentTime = getTime()
    classes = getClasses()
    currentClass = ""
    for x in classes:
        classStartTime = x[2].split("-")[0]
        classEndTime = x[2].split("-")[1]
        classStartHour = int(classStartTime.split(".")[0])
        classStartMin = int(classStartTime.split(".")[1])
        classEndHour = int(classEndTime.split(".")[0])
        classEndMin = int(classEndTime.split(".")[1])
        if(classStartHour <= int(currentTime[1]) <= classEndHour):
            if(int(currentTime[1]) == classEndHour):
                if (int(currentTime[2]) >= classEndMin):
                    break
                else:
                    currentClass = x
            else:
                if(int(currentTime[1]) == classStartHour):
                    if(int(currentTime[2]) > classStartMin):
                        currentClass = x
                    else:
                        break
                else:
                    currentClass = x
    return currentClass
def joinClass(classInfo):
    print("Joining the class:",classInfo[0])
    wb.get().open(classInfo[3], new=2)
def openSettings():
    while True:
        print("*Settings")
        print("a: add class")
        print("r: remove class")
        print("aj: enable autojoin")
        print("e: exit from the settings")
        key = input()
        if(key == "a"):
            print("Please format the input as; class_name,weekday(monday:0-sunday:6),time(starttime(hh.mm)-endtime(hh.mm)),url;otherclass")
            print("Note: please note that there shouldnt be any spaces between commas")
            temp = input()
            addClass(temp)
        elif(key == "r"):
            print()
        elif(key == "aj"):
            print()
        elif(key =="e"):
            break
print("**************************************************")
print("Welcome to Zoom Joiner App")
print("Developer: K2K")
print("**************************************************")

key = "a"
firstmessage = 0
while True:
    temp = currentClass()
    if(temp != "" and firstmessage != 1):
        print("You have",temp[0],"session right now wanna join ?")
        print("y: Yes")
        print("n: No")
        qAnswer = input()
        if(qAnswer == "y"):
            firstmessage = 1
            joinClass(temp)
        else:
            firstmessage = 1
    print("j: join session")
    print("s: settings")
    print("e: exit")
    key = input()
    if(key == "j"):
        if(temp != ""):
            joinClass(temp)
        else:
            print("You have not any classes at the moment :|")
    elif(key =="s"):
        openSettings()
    elif(key == "e"):
        sys.exit()
    else:
        print("Wrong input! Please enter again.")
