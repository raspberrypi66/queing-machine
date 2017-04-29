# -*- coding: utf-8 -*-

import pygame
import sys
import time
import paho.mqtt.client as mqtt
from subprocess import Popen

def drawRow(rowNo,value):
 global srf
 row=int(rowNo);
 pygame.draw.rect(srf, (60,60,60), [400, 60+(60*row), 150, 50])
 pygame.draw.rect(srf, (0,100,60), [550, 60+(60*row), 150, 50])
 srf.blit(f.render(str(row+1),True,(255,0,0)),(450,60+(60*row)))
 srf.blit(f.render(str(value),True,(255,0,0)),(600,60+(60*row)))
 pygame.display.update()

def updateRow(topic,value):
 print"update"
 global srf
 row=topic[12:]
 row=int(row)-1;
 pygame.draw.rect(srf, (60,60,60), [400, 60+(60*row), 150, 50])
 pygame.draw.rect(srf, (0,100,60), [550, 60+(60*row), 150, 50])
 srf.blit(f.render(str(row+1),True,(255,0,0)),(450,60+(60*row)))
 srf.blit(f.render(str(value),True,(255,0,0)),(600,60+(60*row)))
 Popen("python tts.py "+str(value)+" "+topic[12:], shell=True )
 pygame.display.update()

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
mqttc.connect("localhost",1883,60)
mqttc.subscribe("/queue/call/#", 0)
mqttc.loop_start()

pygame.font.init()
srf = pygame.display.set_mode((800,480))
srf.fill((150,150,150))

f = pygame.font.Font("Loma.ttf",32)

srf.blit(f.render("Counter",True,(255,0,0)),(420,10))
srf.blit(f.render("Number",True,(255,0,0)),(570,10))

for i in range(0,5):
 drawRow(i,"")

pygame.mouse.set_visible(0)
pygame.display.flip()
pygame.display.toggle_fullscreen()

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
