#!/usr/bin/python
import sys,traceback
import os
import json

print "Enter the file path"
file1=raw_input()
print "Enter the second file path"
file2=raw_input()
if file1=='' and file2=='':
	print "No file paths provided ....... Exited!"
	sys.exit(0)

if file1=='' and file2!='':
	file1,file2=file2,file1
	
#Read the file and write to local temporary file


if file1!='':
	target1 = open('temp1.txt', 'w')
	target1.truncate()
	with open(file1,'r') as f1:
		for line in f1:
			target1.write(line)
	target1.close()
	

	LINE_LIST=[]
	d1={}
	with open('temp1.txt','r') as f1:  
		for line in f1:
			LINE_LIST.append(line)
		for i in range(0,len(LINE_LIST)):
			key=LINE_LIST[i].rstrip().split(' ')[1]
			if key not in d1:
				d1.setdefault(key,[])
			value=LINE_LIST[i].rstrip().split(' ')[2]
			d1[key].append(value)
	keylist = d1.keys()
	keylist.sort()
	print len(d1)
	print key
	print d1[key]
	print len(d1[key])


	target = open('output1.json', 'w')
	target.truncate()
	target.write('{')
	target.write("\n")
	target.write('"name":"apache",')
	target.write("\n")
	target.write('"children":[')
	target.write("\n")
	target.truncate()
	cnt_d=0
	for k in keylist:
		cnt_d += 1
		word_d=k.replace('.','*')
		#word_d=wrd.replace('.','*')
		m=d1[k]
		l='{"name":"'+word_d+'('+str(len(m))+')",'
		#n_l='apache.'+word_d+'('+str(len(m))+').'
		target.write(l)
		target.write("\n")
		target.write('"children":[')
		target.write("\n")
		word_v=''
		cnt=0
		for j in m:
			cnt += 1
			word_v=j
			wvr=word_v.replace('.','*')
			if cnt != len(m):
				target.write('{"name":"'+wvr+'","size":100},')
				target.write("\n")
			else:
				target.write('{"name":"'+wvr+'","size":100}')
				target.write("\n")
				target.write(']')
				target.write("\n")
		if cnt_d != len(d1):
			target.write('},')
			target.write("\n")
		else:
			target.write('}')
			target.write("\n")
	target.write("]")
	target.write("\n")
	target.write("}")
	###Now for the good part --- open the browser
	os.spawnl(os.P_NOWAIT, r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe', r'FireFox', '-new-tab', 'file:///C:/Users/VADHI/Desktop/Software-Architecture/output1.html')	
	
		
	
	
	
	
if file2!='':
	target2 = open('temp2.txt', 'w')
	target2.truncate()
	with open(file2,'r') as f2:
		for line in f2:
			target2.write(line)
	target2.close()
	

	LINE_LIST=[]
	d1={}
	with open('temp2.txt','r') as f1:  
		for line in f1:
			LINE_LIST.append(line)
		for i in range(0,len(LINE_LIST)):
			key=LINE_LIST[i].rstrip().split(' ')[1]
			if key not in d1:
				d1.setdefault(key,[])
			value=LINE_LIST[i].rstrip().split(' ')[2]
			d1[key].append(value)
	keylist = d1.keys()
	keylist.sort()
	print len(d1)
	print key
	print d1[key]
	print len(d1[key])


	target = open('output2.json', 'w')
	target.truncate()
	target.write('{')
	target.write("\n")
	target.write('"name":"apache",')
	target.write("\n")
	target.write('"children":[')
	target.write("\n")
	target.truncate()
	cnt_d=0
	for k in keylist:
		cnt_d += 1
		word_d=k.replace('.','*')
		#word_d=wrd.replace('.','*')
		m=d1[k]
		l='{"name":"'+word_d+'('+str(len(m))+')",'
		#n_l='apache.'+word_d+'('+str(len(m))+').'
		target.write(l)
		target.write("\n")
		target.write('"children":[')
		target.write("\n")
		word_v=''
		cnt=0
		for j in m:
			cnt += 1
			word_v=j
			wvr=word_v.replace('.','*')
			if cnt != len(m):
				target.write('{"name":"'+wvr+'","size":100},')
				target.write("\n")
			else:
				target.write('{"name":"'+wvr+'","size":100}')
				target.write("\n")
				target.write(']')
				target.write("\n")
		if cnt_d != len(d1):
			target.write('},')
			target.write("\n")
		else:
			target.write('}')
			target.write("\n")
	target.write("]")
	target.write("\n")
	target.write("}")
	os.spawnl(os.P_NOWAIT, r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe', r'FireFox', '-new-tab', 'file:///C:/Users/VADHI/Desktop/Software-Architecture/output2.html')	
	
