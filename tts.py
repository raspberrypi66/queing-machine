#!/usr/bin/python

import sys, getopt
import pygame
import time
import math

_number ={ '0':'blank','1':'one','2':'two','3':'three', '4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
_base={'1':'blank','2':'ten','3':'hundred','4':'thousand','5':'tenthousand'}
_div=[10000,1000,100,10,0]

def num2word(n):
 digit_count = len(n)
 j=digit_count
 for i in range(0,digit_count):
   x=n[i:i+1]
   if(j==2):
    if(x=='1'):
     tts.append("blank")
    elif(x=='2'):
     tts.append("2sp")
    else:
     tts.append(_number[x])
   elif(j==1 and  x=='1'):
    if(n[i-1:i]=='0' or n[i-1:i]==''):
     tts.append(_number[x])
    else:
     tts.append("1sp")
   else:
    tts.append(_number[x])
   if(x!='0'):
    tts.append(_base[str(j)])
   j-=1

def speak(q,c):
 global tts
 tts=["call"]
 num2word(q)
 tts.append("at")
 num2word(c)
 tts.append("end")
 print "Speak..."
 pygame.mixer.init()
 for s in tts :
  pygame.mixer.music.load("/home/pi/queing-machine/voices/"+s+".mp3")
  pygame.mixer.music.play(0,-1)
  while pygame.mixer.music.get_busy():
   time.sleep(0.1)

def main():
 queue_no=sys.argv[1]
 counter_no=sys.argv[2]
 speak(queue_no,counter_no)
	
if __name__ == "__main__":
 main()

