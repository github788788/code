exec(open('util.py').read())
"""
import json
import time,xlrd,os,sys,csv,pyautogui,time,datetime,xlwt
#import py7zr
import xlsxwriter,subprocess,shutil,math,requests
import pandas as pd

import os,time,pyautogui


def sw(l,w):
	#sw(fil,1)
	os.startfile(l)
	time.sleep(w)

def wri(to_write,wait):
	pyautogui.write(to_write)
	time.sleep(wait)
def key(ray):
	#pop = []
	for a,val in enumerate(ray):
		#try:
		but = []
		print ("val[1]",val[1])
		for b in range(0,val[1]):
			but.append(val[0])
		print (but)
		but3([[but],val[2],val[3]])

def but3(inp):
	#but3(["esc","tab"],0,0)
	ray = inp[0]
	between_wait = inp[1]
	end_wait = inp[2]	

	for a in range(0,len(ray)):
		pyautogui.press(ray[a])
		time.sleep(between_wait)
	time.sleep(end_wait)
	"""



def sta(inp):	
	time.sleep(10)
	sw("con2.lnk",3)
	wri("cd cod",1)
	key([["enter",1,0,2]])
	wri("python aut.py",2)
	key([["enter",1,0,4]])
	wri("ope",2)
	key([["enter",1,0,2]])
	wri("ope2",2)
	key([["enter",1,0,1]])
	key([["enter",1,0,1]])	
inp = []
sta(inp)