'''
Created on Apr 25, 2014

@author: Kevin
'''
import random 

LowerCase = "abcdefghijklmnopqrstuvwxyz" 
UpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
Numbers = "0123456789" 

Set = LowerCase + UpperCase + Numbers 
def genPwd(): 
    Password = "" 
    for N in range(0,6): 
        Password = Password + random.choice(Set) 
    return Password 

for N in range(1,21): 
    print "%d. %s" % (N, genPwd()) 