from random import randrange
from cv2 import sort
import numpy as np
import math

def GeneratRandom(limit):
    rande = randrange(start=100,stop=limit)
    return rande

def GetDistanceCM(distance):
    list1 = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87,
             80, 75, 70, 67, 62, 59, 57]
    list2 = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70,
             75, 80, 85, 90, 95, 100]
    coeff = np.polyfit(list1,list2,2)
    a, b, c = coeff
    # return int(a*(distance**2) + b*distance + c)  # ploynomial equation
    return int(4500.7*(distance)**-0.948)           # power equation

def Starting():
    name = input("Player Name: ")
    return name
def StorePlayer(name, score):
    file = open("Players.txt","a")
    file.write(f"{name} : {score}\n")

def GetMaxScore():
    file = open("Players.txt","r")   
    scores = []
    for line in file:
        index = line.rfind(" ")
        scores.append(int(line[index+1:]))
    sortedscores = sorted(scores)
    print(f"Max Score is: {sortedscores[-1]}")    
