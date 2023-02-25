#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import time
import pygame
import wave
import sys
def wait():
    while pygame.mixer.get_busy():
        time.sleep(0.2)
def gettimeID():
    retstring = "314546463"
    retstr = str(time.time() - 1676700000)
    retstring+=retstr[0]
    for i in range(5):
        retstring+=str(hex(0x3f + int(retstr[i+1]))).replace("0x","")
    return retstring

def StringToCode(string):
    retstring = ""
    for i in range(0,len(string)):
        if i == 0:
            res = bytes(string[i],"utf-8")
            b = [0,0,0]
            for i in range(0,3):
               b[i] = res[i]

            b[1]+=15
            b[2]+=15
            ret = ""
            for i in range(0,3):
                ret+=str(hex(b[i]))
            retstring+=ret.replace("0x","")
        elif i == 1:
            res = bytes(string[i],"utf-8")
            b = [0,0,0]
            for i in range(0,3):
               b[i] = res[i]

            b[0]+=15
            b[1]+=3
            b[2]+=15
            ret = ""
            for i in range(0,3):
                ret+=str(hex(b[i]))
            retstring+=ret.replace("0x","")
        else:
            res = bytes(string[i],"utf-8")
            b = [0,0,0]
            for i in range(0,3):
               b[i] = res[i]
            b[0]+=15
            b[1]+=15
            b[2]+=15
            ret = ""
            for i in range(0,3):
                ret+=str(hex(b[i]))
            retstring+=ret.replace("0x","")
    return retstring+"f28f91"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}



input1 = sys.argv[1]
url = "https://ai-api.baimianxiao.cn/download/e5b5bdf89fc1/"+StringToCode(input1)+"/0.6/0.6/1.2/"+gettimeID()+".wav"
print(url)
response = requests.get(url,headers = headers)
with open("a.wav","wb") as f:
    f.write(response.content)
