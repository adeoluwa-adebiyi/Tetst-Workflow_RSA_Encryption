#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:14:38 2021

@author: hbueno2
"""
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return 1

# # Driver Code
# a = 7
# m = 20
# # Function call
# modInverse(a, m)
 
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
  
    p=3
    q=11
    print("P =",p, ", Q =",q)
    n,m = getNM(p,q)
    print("N =",p, ", M =",q)
    e=13
    d=getDY(e, m)
    print("E =",e,", D=",d[0], ", Y=", d[1])
    print("------------------")
    print("RSA Cipher/Decryption text for \'hi\':")
    print(textRSA('hi',13,33))
    print(textRSA('nr',17,33))
    
if __name__ == "__main__":
    main()





