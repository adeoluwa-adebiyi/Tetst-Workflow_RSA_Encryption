#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:14:38 2021

@author: hbueno2
"""

import os
import json
INPUTS = json.loads(os.getenv("FUNCTOR_INPUT","{}"))
def modInverse(a, m):
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 
                  109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 
                  173, 179, 181, 191, 193, 197, 199]
    primeNum=0
    for x in range(1, m):
        if(x==primeList[primeNum]):
            primeNum+=1
            if (((a%m) * (x%m)) % m == 1):
                return x
            elif (((a%m) * (-x%m)) % m == 1):
                return -x
    return 1

 
def split(word):
    return [char for char in word]


    
def getNM(p,q):
    n_num=p*q
    m_num=(p-1)*(q-1)
    return n_num, m_num

def getDY(e,m):
    d_num=modInverse(e,m)
    y_num=(1-d_num*e)/m
    return d_num, y_num

def getCipher(letter, e_num, n_num):  ## public(e,n) private(d,n)
    nums=list(range(0,26))
    alpha = split('abcdefghijklmnopqrstuvwxyz')
    
    res = {alpha[i]: nums[i] for i in range(len(alpha))}
    res2 ={nums[i]: alpha[i] for i in range(len(alpha))}
    
    return res2[ pow(res[letter],e_num)%n_num ]

    
def textRSA(word, num1, num2):    ## public(e,n) private(d,n)
    w_lst=split(word)
    txt_lst=[]
    for i in w_lst:
        txt_lst.append(getCipher(i, num1, num2))
    return txt_lst

def main():
    
    # p=17
    # q=11
    p=INPUTS["p"]
    q=INPUTS["q"]
    print("P =",p, ", Q =",q)
    n,m = getNM(p,q)
    print("N =",n, ", M =",m)
    # m=20
    e=37
    d=getDY(e, m)
    print("E =",e,", D=",d[0], ", Y=", d[1])
    print("------------------")
    print("RSA Cipher/Decryption text for \'hi\':")
    print(textRSA('hi',13,33))
    print(textRSA('nr',17,33))
    
if __name__ == "__main__":
    main()





