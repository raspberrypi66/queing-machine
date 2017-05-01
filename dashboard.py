#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import time
import paho.mqtt.client as mqtt
from subprocess import Popen
from tts import speak

#speak("1","100")
def drawRow(rowNo,value):
 #value="0"
 global srf
 global maxX
 global maxY
 row=int(rowNo);
 pygame.draw.rect(srf, (60,60,60), [maxX-580, 150+(90*row), 280, 80])
 pygame.draw.rect(srf, (0,100,60), [maxX-300, 150+(90*row), 280, 80])
 srf.blit(f.render(str(row+1),True,(255,0,0)),(maxX-450,140+(90*row)))
 srf.blit(f.render(str(value),True,(255,0,0)),(maxX-180,140+(90*row)))
 pygame.display.update()

def updateRow(topic,value):
 print"update"
 global srf
 row=topic[12:]
 row=int(row)-1;
 pygame.draw.rect(srf, (60,60,60), [maxX-580, 150+(90*row), 280, 80])
 pygame.draw.rect(srf, (0,100,60), [maxX-300, 150+(90*row), 280, 80])
 srf.blit(f.render(str(row+1),True,(255,0,0)),(maxX-450,140+(90*row)))
 srf.blit(f.render(str(value),True,(255,0,0)),(maxX-180,140+(90*row)))
 pygame.display.update()
 speak(str(value),topic[12:])

def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    updateRow(msg.topic,msg.payload)

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_log(mosq, obj, level, string):
    print(string)

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

mqttc=mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
#mqttc.connect("localhost",1883,60)
#mqttc.subscribe("/queue/call/#", 0)
#mqttc.loop_start()

pygame.font.init()
maxX=1800
maxY=1024
srf = pygame.display.set_mode((maxX,maxY))
srf.fill((150,150,150))
path="/home/pi/queing-machine/"
bg=pygame.image.load(path+"/bg.jpg")
#image position
srf.blit(bg,(120,150))

f = pygame.font.Font(path+"Loma.ttf",64)

srf.blit(f.render("Counter",True,(255,0,0)),(maxX-550,40))
srf.blit(f.render("Number",True,(255,0,0)),(maxX-270,40))

for i in range(0,5):
 drawRow(i,"")

pygame.mouse.set_visible(0)
pygame.display.flip()
pygame.display.toggle_fullscreen()
mqttc.connect("localhost",1883,60)
mqttc.subscribe("/queue/call/#", 0)
mqttc.loop_start()

counter=0
while True:
    counter+=1
    time.sleep(1)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
